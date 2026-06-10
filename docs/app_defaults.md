# Update Zen — App Defaults Reference

What Update Zen does out of the box with zero configuration, from install to first update.

---

## Snapshot location

`~/.update_zen/snapshots/<container_name>/`

One subdirectory per container. All files owned by the invoking user.

---

## What gets captured per update

### Main bundle — `{timestamp}.tar.gz`

| Member | Always? | Notes |
|---|---|---|
| `{timestamp}.json` | Yes | Full `docker inspect` output |
| `{timestamp}_image.tar` | Yes | Pre-update image via `docker save` |
| `{timestamp}_compose.yaml` | Conditional | Only when compose labels are present and the file resolves |
| `{timestamp}_env.env` | Conditional | Only when env overrides exist beyond image defaults |
| `_volumes.json` | Yes | Index of volume archives: what was written and what was skipped |

### Per-mount volume archives — `{timestamp}_{mount_name}.tar.gz`

One file per mount, written alongside the main bundle:

- All bind mounts where the host path exists (`/host/path:/container/path`)
- All named volumes (non-anonymous — 64-char hex names are skipped)
- Sockets and device files are skipped automatically
- Container is briefly **paused** during backup for consistency, then unpaused

If the container has no bind mounts or named volumes, volume backup is skipped entirely and logged.

---

## Retention

**3 snapshots** kept per container. The oldest is deleted automatically when a 4th is created.

---

## Permissions

| Item | Default |
|---|---|
| Snapshot directories | `0700` (owner only) |
| Snapshot files | `0600` (owner only) |

---

## What's off by default

- Encryption — snapshots are plaintext
- Per-container directory overrides — all containers use the same snapshot dir
- Per-container retention overrides — all containers keep the same number of snapshots
- Compose-mode rollback — available only when a compose sidecar was captured

---

## Other defaults

| Setting | Default | Notes |
|---|---|---|
| `image_export_enabled` | `true` | Pre-update image saved via `docker save` |
| `volume_backup_enabled` | `true` | Global volume backup on |
| `pause_for_backup` | `true` | Container paused during volume archival |
| `auto_rollback` | `true` | Rolls back automatically if health check fails |
| `health_timeout_sec` | `300` | 5 minutes to pass health check before rollback |
| `max_snapshots` | `3` | Snapshots retained per container |
| `snapshot_dir_mode` | `0700` | Directory permissions |
| `snapshot_file_mode` | `0600` | File permissions |
