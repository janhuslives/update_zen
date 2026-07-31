# Priority Fix: Uncaught OSError (EIO) crashes interactive menu — FIXED

Root cause turned out to be a wedged virtiofs share on the VM host; a VM
restart resolved the environmental trigger. The code-level fix below was
still applied since the underlying crash — any transient filesystem I/O
error taking down the whole interactive menu — can recur for unrelated
reasons (network share blip, disk hiccup, etc.) and shouldn't be fatal.

## Symptom

Selecting a container in `cmd_interactive` crashes the whole TUI with an
unhandled traceback instead of showing an error:

```
File "update_zen.py", line 6892, in _action_menu
    snaps = len(sm.list(name))
File "update_zen.py", line 1298, in list
    if not container_dir.exists():
OSError: [Errno 5] Input/output error: '/mnt/media/backups/docker/gluetun'
```

## Root cause

`SnapshotManager.list()` (`update_zen.py:1296-1299`) calls
`container_dir.exists()`. Normally `Path.exists()` swallows
`FileNotFoundError` and returns `False`, but `Errno 5 (EIO)` is a real
filesystem I/O failure, not "path missing" — pathlib lets it propagate
uncaught.

Confirmed environmental cause on the affected host: `/mnt/media` is a
`virtiofs` mount (VM host-passthrough, `media on /mnt/media type virtiofs
(rw,relatime,_netdev,x-systemd.automount,x-systemd.idle-timeout=600)`).
`df -h` shows the mount as healthy overall (2.7T size, 10% used), but the
specific subpath `/mnt/media/backups/docker/gluetun` throws EIO on `ls -la`
— i.e. the mount itself is up, but something under it (likely the
virtiofs host-side share, or an idle-timeout disconnect/reconnect
mid-session, since `x-systemd.idle-timeout=600` is set) left that path
in a broken state. `dmesg` couldn't be checked (`Operation not
permitted` — needs sudo/root or `CAP_SYSLOG`).

## Fix implemented

`SnapshotManager.list()` (`update_zen.py:1296`) now wraps the
`container_dir.exists()` check and `container_dir.glob("*.tar.gz")` call
in `try/except OSError`, logging a clear warning (`"snapshot dir
unreachable for <container>: <path> — <error>"`) and returning `[]`
instead of letting the exception propagate.

Fixed at the source rather than at each call site: `sm.list()` is called
from ~19 locations across the file (`_action_menu`, `cmd_interactive`,
`_rotate`, `cmd_doctor`, various snapshot/rollback menus, etc.). Patching
the single centralized function protects all of them at once, consistent
with `_probe_snapshot_dir`'s existing pattern of treating a filesystem
problem as a clean, reported failure rather than a crash — this extends
that same treatment to the *read* path, not just pre-write checks.

## Follow-up (host side) — UPDATE: guest-side remount does NOT fix it

Tested `sudo umount -l /mnt/media && sudo mount /mnt/media` (lazy
unmount + fresh automount) followed by both unprivileged and `sudo
ls -la` on the path — **still `Input/output error` after the remount,
even as root.** This rules out:
- A stale mount-table entry on the guest (a fresh mount still fails)
- A permissions problem (root fails identically to the unprivileged user)

`sudo dmesg | grep -iE 'virtiofs|error|i/o'` showed nothing relevant:
only boot-time virtiofs init lines (`virtio_fs_setup_dax: No cache
capability` at ~3.8s uptime, informational — DAX just isn't enabled,
not an error) and unrelated noise (PCI hotplug warnings from boot, an
old unrelated `mysqld` segfault ~27 days ago). **The guest kernel is
not logging any virtiofs protocol/transport error for this failing
access** — meaning the EIO is most likely being generated on the
**host side** (virtiofsd) and returned as a clean error response, not
a guest-side transport fault.

**Conclusion: this needs to be investigated from the VM host, not the
guest.** From inside the Ubuntu guest there is no further diagnostic
step available — a full remount was already proven insufficient.
Next steps require host access:
1. Check virtiofsd's status/logs on the host for this specific shared
   directory (`backups/docker/gluetun`) — look for the host process
   serving `/mnt/media`'s virtiofs tag (`media`).
2. Check the *host* filesystem directly at the path backing
   `/mnt/media/backups/docker/gluetun` for corruption, bad permissions,
   an open/locked file handle, or a filesystem-level error (`dmesg`,
   `smartctl`, or equivalent on the host, not the guest).
3. If virtiofsd itself is wedged for this share, restarting the
   virtiofsd process/VM device (not just the guest's mount) is likely
   required — a guest-side umount/mount only tears down the guest's
   client state, not the host daemon's.
4. Confirm whether other subpaths under `/mnt/media/backups/docker/`
   (i.e. other containers' snapshot dirs) are also affected, or if
   this is isolated to `gluetun` — that will indicate whether it's a
   single corrupted directory entry vs. a broader share-level problem.
