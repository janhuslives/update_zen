# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

**Note on terminology:** When the user refers to "dev manual," they are referring to `Update_Zen_Dev_Manual.md`, not this file. This file (`CLAUDE.md`) contains code guidance and architecture documentation for Claude. The separate dev manual is a user-facing reference document.

---

## What this is

Update Zen is a single-file CLI tool (`update_zen.py`) for managing Docker container updates with snapshot-based rollback. **No pip installs, no virtual environments, no build step.** The only dependency is the `docker` CLI binary.

---

## Git discipline

Never create a commit or push to the remote unless the user explicitly instructs
it in that message. Completing a task, finishing an implementation step, or
writing a file does not constitute permission to commit or push.

The only automatic exception is the **Victory Lap** ritual (see below), which is
triggered exclusively by the phrase "Victory Lap!" or a close grammatical variation.
Phrases like "implement X", "fix Y", or "sprint Z" are implementation requests only
— they end when the code is written, with no commit or push.

**If you are about to run `git commit` or `git push` and the user's message did not
contain an explicit commit/push instruction or "Victory Lap", stop and do not run it.**

When in doubt, do not commit.

---

## "Victory Lap!"

When the user says "Victory Lap!" (or a close grammatical variation — "take a
victory lap", "victory lap time", etc.), it means:

1. **Commit and push** the current changes with an appropriate commit message.
2. **Write a dev journal** in `dev_journals/` explaining everything changed in
   that commit. Name the file `<7-char-hash>_<topic>.md` using the hash of the
   commit just created. Match the format of existing journals: **Background**,
   **Design** or **Root Cause**, **Implementation**, **Files Changed** table.
   The most recent journal in `dev_journals/` is the best formatting template.
3. **Commit and push** the new journal file as a second commit.

---

## Running it

```bash
# Run directly
python3 update_zen.py <command>

# After install (creates /usr/local/bin/update_zen + NOPASSWD sudoers rule)
python3 update_zen.py install   # run once as normal user — prompts for sudo password

# The script auto-elevates to root on every invocation via os.execvp("sudo", ...)
# after install, subsequent runs require no password

# Config lives at ~/.update_zen/config.json
update_zen config               # opens config in $EDITOR / nano / vi
```

## Architecture

Everything lives in `update_zen.py`. Key classes in file order: `Config`, `DockerClient`, `EncryptionManager`, `SnapshotManager`, `RegistryClient`, `HealthChecker`, `Engine`, then `cmd_*()` functions and `main()`. See the function index below for navigation.

`Engine` is the only stateful orchestrator. All other classes are stateless utilities that do one job.

`EncryptionManager` is instantiated stateless (`EncryptionManager(config)`). v2 API passes `password` directly to `encrypt_bytes`/`decrypt_bytes`/`encrypt_file`/`decrypt_file` — no upfront unlock needed. v1 shims (`setup()`, `unlock()`, `_key`) remain for the legacy global encryption menu only. `_get_password(config, container, mount=None)` is the single resolution point: saved → session cache → prompt.

---

## Critical non-obvious details

### `config.json` never contains real passwords

`Config.save()` always writes `"saved_passwords": {}`. Real passwords live only
in `credentials.json`, which is loaded and merged into the in-memory config in
`Config.load()`. Code that reads `config.get_saved_password()` sees the merged
result. Code that writes passwords calls `Config.set_saved_password()`, which
routes to `_save_credentials()`. There is no code path that writes real passwords
into `Config.save()`.

`CREDENTIALS_FILE = BASE_DIR / "credentials.json"` is always relative to
`BASE_DIR` (`~/.update_zen/`). It is never affected by `UPDATE_ZEN_CONFIG`
— credentials stay local even when config.json is synced to cloud storage or a
custom path.

### `DockerClient.inspect()` augments the dict

`docker inspect <container>` does not include `RepoDigests` — that is an image-level field. `inspect()` performs a **second** `docker image inspect <image_id>` call and injects `RepoDigests` into the returned dict. Every downstream caller (RegistryClient, SnapshotManager) relies on this augmentation being present. Do not bypass `DockerClient.inspect()` for container data.

### `_INVOKING_HOME` and `SUDO_USER`

The script always runs as root (auto-elevation in `main()`). All paths — config, snapshots, log, docker credentials — resolve through `_INVOKING_HOME`, which checks `SUDO_USER` to find the original user's home directory (`/home/<user>/...` not `/root/...`). This is set once at module load time. `RegistryClient._get_credentials()` uses `_INVOKING_HOME` for the same reason.

### `pin_digest` controls update vs rollback image pinning

`SnapshotManager.to_spec(inspect_data, pin_digest)`:
- `pin_digest=False` → `image = Config.Image` (e.g. `nginx:latest`) — used for forward updates
- `pin_digest=True` → `image = RepoDigests[0]` (e.g. `nginx@sha256:abc...`) — used for rollback, pins exact bytes

### `container:` network mode requires special handling

Containers using `network_mode: service:gluetun` (Gluetun VPN stacks) have `HostConfig.NetworkMode = "container:<id>"` and an **empty** `NetworkSettings.Networks`. `inspect()` resolves the container ID to a name (stable across recreations). `to_spec()` checks for the `container:` prefix and stores it in `ContainerSpec.network_mode`, leaving `networks = []`. `_build_run_cmd()` passes `--network container:<name>` when this field is set.

When `restart_stack_siblings` is enabled, `_get_stack_siblings()` returns `(gateway_siblings, dependent_siblings)`. The gateway must be started and healthy before dependents are started — see the two-phase boot logic in `Engine.update()` and `Engine.rollback()`.

`_build_run_cmd()` suppresses `--hostname`, `--add-host`, `--dns`, `--dns-search`, and `--dns-option` when `spec.network_mode` is set — Docker rejects these network-namespace flags when sharing another container's namespace.

### `--compose` path resolves Portainer's internal paths

Portainer stores compose files at `/data/compose/<stack_id>/` **inside** its own container. The label `com.docker.compose.project.working_dir` reflects this internal path, which does not exist on the host. `Engine._resolve_compose_dir()` inspects the Portainer container to find where its `/data` volume is bind-mounted (e.g. `/opt/portainer/data`) and rewrites the path. Every `docker compose` invocation also passes `--project-name` (from the container's `com.docker.compose.project` label) and `--no-deps` to avoid recreating gateway containers.

### `RegistryClient` digest comparison strips the image name prefix

Local digest from `RepoDigests[0]`: `"nginx@sha256:abc123"` — remote digest from registry: `"sha256:abc123"`. Comparison strips everything before and including `@` from the local value.

### Snapshot format: `.tar.gz` bundle

Every snapshot is a single `{snapshot_id}.tar.gz` main bundle. Old-format loose
`.json` snapshots are no longer read — use `update_zen convert-snapshots` to
migrate any that remain.

**Main bundle** (`{snapshot_id}.tar.gz`):
- `{snapshot_id}.json` — raw inspect JSON (member inside archive)
- `{snapshot_id}_compose.yaml` — compose file (member; only when container has `com.docker.compose.project.working_dir` and the path resolves)
- `{snapshot_id}_env.env` — user-set env overrides (member; only when overrides exist; reference-only — full env in JSON is what reconstruct uses)
- `{snapshot_id}_image.tar` — output of `docker save` (member; only when image export is enabled)
- `_volumes.json` — per-mount volume index with `volumes` (archived) and `skipped` (excluded) arrays

`finalize()` bundles a `_staging_{timestamp}/` directory into the archive at `compresslevel=1`, deletes staging, and calls `_rotate()`. A failed write of any member is a logged warning and never blocks the update.

**Per-mount volume archives** (separate files, outside the bundle):
- `{snapshot_id}_{mount}.tar.gz` — one per successfully backed-up mount. Mount names come from `_sanitize_mount_name(container_path)`. Location follows the four-level hierarchy: global `snapshot_dir` → per-container `snapshot_dir_overrides` → container volume `save_path` → per-mount `mount_paths`.

`_rotate()` calls `load_volumes()` to get each snapshot's archive paths, then globs `{snapshot_id}_*.tar.gz` in the container directory to delete per-mount archives.

### `path.name.removesuffix(".tar.gz")` — never use `path.stem` for snapshot IDs

`Path.stem` only strips the last extension. For `2026-05-15T16-08-16.tar.gz`, `path.stem` returns `"2026-05-15T16-08-16.tar"` — the timestamp regex `^\d{4}-\d{2}-\d{2}T\d{2}-\d{2}-\d{2}$` never matches. Everywhere a snapshot ID must be derived from a `.tar.gz` path, use `path.name.removesuffix(".tar.gz")`.

### Named volume backup

Named Docker volumes (`-v myvolume:/path`) appear in `Mounts[]` with `Type == "volume"` but NOT in `HostConfig.Binds`. `_get_named_volumes(inspect_data)` filters `Mounts` for these entries and excludes 64-char hex names (anonymous volumes are ephemeral — backing them up is misleading). The bind loop in `_backup_volumes` skips any `HostConfig.Binds` entry whose host path doesn't start with `/` (it's a named volume reference, not a real path) to avoid creating a false duplicate skipped entry alongside the one correctly handled by the named-volumes loop.

### Auto-rollback after failed `docker run` is unconditional

If `docker run` fails in `Engine.update()` (not the health check — the actual container start), the container is already removed. Rollback is triggered **regardless** of the `auto_rollback` flag. The flag only governs the behavior after a successful start that fails the health check.

### Pre-flight snapshot dir writability check

`Engine.update()` and `Engine.snapshot()` both call `_probe_snapshot_dir(snap_dir)` as their very first step — before inspect, before password prompts, before any container is touched. The helper writes and deletes a `.write_probe` file; if the write fails (e.g. NAS offline, full disk, wrong permissions) it returns the OSError string and the caller logs the error and returns `False` immediately. This prevents a snapshot directory problem from being discovered mid-update after the container has already been stopped. `cmd_doctor` also probes the global snapshot dir and all per-container overrides.

---

## Config fields

See `docs/config_reference.md` for full documentation of each config field, their CLI flags, TUI locations, and non-obvious behaviors.

---

## Adding new commands

1. Write a `cmd_<name>(args: argparse.Namespace) -> None` function in the `# === COMMANDS ===` section
2. Register it in `main()` following the existing `sub.add_parser` / `set_defaults(func=cmd_<name>)` pattern
3. `args.config` is always available (set in `main()` before dispatch)

---

## Dev journals

After every substantive commit, write a dev journal in `dev_journals/` named `<7-char-hash>_<topic>.md`. Follow the format of existing journals: **Background**, **Root Cause** or **Design**, **Implementation**, **Files Changed** table. The journal for the immediately preceding commit is the best formatting template.

---

## Function index

Line numbers drift with edits — update after any structural change. Use these to jump directly with the Read tool rather than grepping.

### Engine core
| Function | Line | Purpose |
|---|---|---|
| `Engine.update` | 2508 | Full update sequence; resolves snap_pw + _pw_fn closure for per-entity encryption |
| `Engine.rollback` | 2341 | Full rollback sequence; resolves snap_pw, passes to sm.load |
| `Engine.snapshot` | 2763 | Standalone snapshot without pull/recreate: inspect → save → meta → image → pause/backup/unpause → finalize |
| `Engine._backup_volumes` | 1933 | Archive bind mounts + named volumes to per-mount `.tar.gz` files; pause-aware; injects `_meta.json` into each archive when version_meta is provided |
| `Engine._restore_volumes` | 2266 | Restore volume archives; prompts when `ext_overrides` is not None |
| `Engine._get_stack_siblings` | 1884 | Detect Compose gateway/sibling containers |
| `Engine._save_meta` | 2171 | Capture compose sidecar + env overrides into staging dir |
| `Engine._save_image` | 2236 | docker save pre-update image to `_image.tar` in staging |

### Snapshot / config
| Function | Line | Purpose |
|---|---|---|
| `_probe_snapshot_dir` | 984 | Write-probe check; returns OSError string or None; aborts update/snapshot early if unwritable |
| `_derive_version_meta` | 1004 | Extract version + digest from inspect_data; returns `{"version": "...", "digest": "sha256:..."}` |
| `_sanitize_mount_name` | 996 | Sanitize container path to a safe filename segment |
| `_get_named_volumes` | 1016 | Filter `Mounts` for non-anonymous named volumes |
| `_get_active_image_ref` | 1033 | Resolve active registry override or fall back to inspect image |
| `Config.snapshot_dir_for` | 258 | Return per-container snapshot dir override or global `snapshot_dir` |
| `Config.max_snapshots_for` | 262 | Return per-container snapshot limit override or global `max_snapshots` |
| `Config.is_encryption_enabled` | 273 | True if container is in `encrypt_containers` list |
| `Config.is_volume_encrypted` | 276 | True if mount is in `encrypt_volumes[container]` or list contains `"all"` |
| `Config.snapshot_dir_mode_for` | 265 | Return per-container snapshot dir mode override or global `snapshot_dir_mode` |
| `Config.snapshot_file_mode_for` | 269 | Return per-container snapshot file mode override or global `snapshot_file_mode` |
| `Config.get_saved_password` | 282 | Return saved password for container or container::mount key |
| `Config.set_saved_password` | 290 | Write password to `saved_passwords` and save config |
| `Config.purge_saved_passwords` | 300 | Remove saved passwords for one container or all; returns count |
| `Config.load` | 318 | Read config.json, merge credentials.json, auto-migrate passwords + new fields |
| `Config.save` | 401 | Write config.json with `saved_passwords: {}` (never writes real passwords) |
| `SnapshotManager.save` | 1199 | Write inspect JSON to staging dir, return `(path, staging_dir)` |
| `SnapshotManager.save_version` | 1470 | Write `{snapshot_id}_version.json` to staging dir |
| `SnapshotManager.finalize` | 1216 | Bundle staging dir into `.tar.gz`, delete staging, call `_rotate` |
| `SnapshotManager._rotate` | 1229 | Prune old snapshots; calls `load_volumes()` for archive paths, globs `{snapshot_id}_*.tar.gz` for per-mount archives |
| `SnapshotManager.list` | 1253 | Return `Snapshot` list newest-first; globs `*.tar.gz` only; populates `version` from OCI label or tag |
| `SnapshotManager.load` | 1289 | Load inspect JSON from snapshot `.tar.gz` bundle |
| `SnapshotManager.load_version` | 1474 | Read version sidecar from bundle; returns `{}` on miss |
| `SnapshotManager.load_volumes` | 1326 | Load volume index; extracts `_volumes.json` member from bundle |
| `SnapshotManager.to_spec` | 1341 | inspect dict → ContainerSpec |

`Snapshot` fields (populated by `list()`; `volumes` always `[]` until `load_volumes()` is called):
```python
path:       Path       # .tar.gz path
timestamp:  datetime
image_ref:  str        # Config.Image value, e.g. "nginx:latest"
digest:     str        # RepoDigests[0], e.g. "nginx@sha256:..." (empty if absent)
version:    str        # org.opencontainers.image.version label, or tag if label absent, or ""
volumes:    list       # loaded lazily via load_volumes()
```

A richer version record is available via `sm.load_version(snapshot)` → `{"version": "...", "digest": "sha256:..."}` from the `{snapshot_id}_version.json` sidecar. Returns `{}` for old snapshots predating commit `4adca3b`.

---

## Interactive menu hierarchy

See `docs/tui_menu_map.md` for the full TUI menu tree. Read it when extending or restructuring any menu.

---

## Key utility APIs

### `_browse_path(start, mode='dir', filter_ext='') -> Path | None`
Interactive filesystem navigator. `mode='dir'`: user navigates and confirms a directory with `[0]`; returns the confirmed `Path`. `mode='file'`: selecting a file returns it. `filter_ext` (e.g. `'.gz'`) limits which files are listed. Returns `None` on `[q]` cancel or `KeyboardInterrupt`.

Three inline keys are available in all modes from every call site:
- `m` — prompts for a name (rejects empty, `/`, `.`, `..`), creates a subdirectory at `0o700`, and navigates into it.
- `p` — shows the current directory's mode, then offers four directory-appropriate presets (`0700`/`0750`/`0755`/`0777`) or custom octal input. File presets are omitted — they lack the execute bit directories need for traversal.
- `d` — deletes the current directory; prints content summary, requires typing `yes`, blocks `/`, uses `shutil.rmtree`; navigates to parent on success.

### `_print_table(headers, rows, max_widths=None)`
`rows` is `list[tuple[str, ...]]`. Multi-line cells use `"\n"` as separator. `max_widths` is `dict[col_index, int]` — cells pre-wrapped by `_wrap()`. Headers support `"\n"` for multi-line names; single-line headers are prefixed with `"\n"` so they sit on line 1.

---

## Common patterns

### Config write (volume_backup)
Always use this pattern when modifying per-container backup rules. It ensures empty rule dicts are never written as `{}` to the JSON.

```python
rules = dict(config.volume_backup.get(container, {}))
# ... modify rules ...
if rules:
    config.volume_backup[container] = rules
else:
    config.volume_backup.pop(container, None)
config.save()
```

### Interactive menu loop
All TUI menus follow this structure. Re-read state at the top of each iteration so changes made inside sub-functions are reflected immediately on redraw.

```python
while True:
    # re-read state from config here (fresh each iteration)
    # print display
    # print options
    try:
        raw = input("prompt: ").strip().lower()
    except (EOFError, KeyboardInterrupt):
        print()
        return
    if raw == "0":
        return
    elif raw == "x":
        ...
    else:
        print("Invalid choice.")
```

### Nested input prompt (inside a menu loop)
When a menu option needs a second prompt, wrap it in its own try/except. Use `continue` (not `return`) on interrupt so the menu redraws rather than exits.

```python
try:
    val = input("Enter value: ").strip()
except (EOFError, KeyboardInterrupt):
    print()
    continue
```
