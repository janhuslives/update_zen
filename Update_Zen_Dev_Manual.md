# Update Zen — Developer Manual

A CLI tool for monitoring Docker container image updates, executing controlled
updates, and maintaining a rolling window of container configuration snapshots
to enable fast rollback. Written in pure Python standard library — no pip
installs, no daemons, no external dependencies beyond Docker itself.

---

## Table of Contents

1. [Design Philosophy](#1-design-philosophy)
2. [Disk Layout](#2-disk-layout)
3. [Source File Layout](#3-source-file-layout)
4. [Architecture Overview](#4-architecture-overview)
5. [Class Reference](#5-class-reference)
   - [Config](#51-config)
   - [DockerClient](#52-dockerclient)
   - [ContainerSpec](#53-containerspec)
   - [SnapshotManager](#54-snapshotmanager)
   - [RegistryClient](#55-registryclient)
   - [HealthChecker](#56-healthchecker)
   - [Engine](#57-engine)
6. [CLI Commands](#6-cli-commands)
7. [Data Flow](#7-data-flow)
8. [Error Handling](#8-error-handling)
9. [Volume Data Backup and Restore](#9-volume-data-backup-and-restore)
10. [Key Design Decisions](#10-key-design-decisions)
11. [Cloud Sync & Disaster Recovery](#11-cloud-sync--disaster-recovery)

---

## 1. Design Philosophy

**Single file, stdlib only.** The entire tool is `update_zen.py`. No virtual
environments, no package managers, no compiled extensions. Copy one file to a
server and it runs.

**Short-lived CLI invocations only.** Every run is a one-shot command that
completes and exits. There is no daemon, no polling loop, no background process.
The built-in `cron` command manages named recipe entries in the user's crontab
(`nightly_update`, `weekly_check`, etc.) — but each triggered run is still a
short-lived CLI call. There is no long-running background worker.

**Explicit over implicit.** Updates are never applied automatically. The user
decides when to update and when to roll back. The tool provides the information
and executes the decision; it does not make autonomous changes.

**No shell injection surface.** All `subprocess` calls use list arguments with
`shell=False`. Container names, image refs, and env var values containing
spaces or special characters are passed as list elements, never concatenated
into a string that gets evaluated by a shell.

**Typed errors, not silent failures.** Docker CLI failures raise `DockerError`.
Registry failures raise `RegistryError`. Callers receive a typed exception with
the stderr message attached, not a silent non-zero exit code.

---

## 2. Disk Layout

```
~/.update_zen/                          # 0700 — private app directory
│
├── config.json                           # owner-only settings                        (0600)
├── credentials.json                      # saved encryption passwords; never sync     (0600)
│
├── snapshots/
│   ├── nginx/
│   │   ├── 2026-05-12T14-30-22.tar.gz         # main bundle (newest; new format)
│   │   │     members:
│   │   │       2026-05-12T14-30-22.json        #   raw docker inspect output
│   │   │       2026-05-12T14-30-22_compose.yaml  # (if compose-managed)
│   │   │       2026-05-12T14-30-22_env.env     #   (if env overrides exist)
│   │   │       2026-05-12T14-30-22_image.tar   #   (if image export enabled)
│   │   │       _volumes.json                   #   per-mount backup index
│   │   ├── 2026-05-12T14-30-22_config.tar.gz  # per-mount volume archive
│   │   ├── 2026-05-12T14-30-22_data.tar.gz    # per-mount volume archive
│   │   ├── 2026-05-10T09-15-00.tar.gz         # older bundle
│   │   ├── 2026-05-10T09-15-00_config.tar.gz
│   │   ├── 2026-05-08T18-00-00.tar.gz         # oldest kept (max 3 by default)
│   │   └── 2026-05-08T18-00-00_config.tar.gz
│   │
│   ├── sabnzbd/
│   │   └── ...
│   └── ...
│
└── update_zen.log                      # append-only, human-readable               (0600)
```

Each snapshot is a single `{snapshot_id}.tar.gz` main bundle containing the
raw inspect JSON, optional compose file, optional env overrides, optional
pre-update image layers, and a `_volumes.json` index of all backed-up and
skipped mounts. Per-mount volume data is stored in separate
`{snapshot_id}_{mount}.tar.gz` files alongside the bundle — one file per
successfully backed-up mount, named via `_sanitize_mount_name(container_path)`.

**Old-format snapshots** (loose `.json` + sidecar files) are no longer
supported. Use `update_zen convert-snapshots` to migrate any remaining
old-format snapshots to `.tar.gz` bundles.

Filenames use hyphens instead of colons in the timestamp
(`%Y-%m-%dT%H-%M-%S`) for Windows filesystem compatibility during development.

---

## 3. Source File Layout

```
update_zen.py
│
├── # module-level constants
├── _VERSION
├── _SPLASH_SISYPHUS          27-line braille art; embedded directly (no external file)
├── _SPLASH_TITLE             11-line block-letter title; embedded directly
├── _TIPS                     list of helpful tips; one chosen randomly at startup via random.choice()
│
├── # === PATHS ===
├── _get_invoking_home()           resolves original user home under sudo
├── _to_portable_path()            serialize Path → "~/..." if under home
├── _from_portable_path()          deserialize "~/..." → absolute Path
├── _is_local_path()               True if path is under the invoking user's home
├── _portablize_volume_backup()    serialize volume_backup path values as ~/... for config.json
├── _unportablize_volume_backup()  expand ~/... values back to absolute paths on load
├── _ensure_dirs()                 creates ~/.update_zen/ on startup
├── _active_log_file               module-level Path; LOG_FILE at import, updated in main()
│
├── # === CONFIG ===
├── _load_credentials()       load saved_passwords from credentials.json; returns {} if absent
├── _save_credentials()       write saved_passwords to credentials.json with 0600 permissions
├── class Config
│
├── # === LOGGING ===
├── log()                     appends timestamped line to _active_log_file + stdout
│
├── # === CRON ===
├── _CRON_USER                invoking user string for crontab -u
├── _CRON_RECIPES             13 recipe templates: nightly_update, weekly_update,
│                             daily_check, weekly_check; hourly/daily/weekly/monthly_snapshot;
│                             hourly/daily/weekly/monthly_volume_backup; mount_volume_backup
├── _crontab_read()           crontab -u {user} -l; returns "" on no crontab
├── _crontab_write()          pipe content to crontab -u {user} -
├── _cron_block()             build three-line BEGIN/command/END marker block
├── _crontab_remove()         strip a named marker block from a crontab string
├── _crontab_inject()         remove then append (idempotent)
├── _crontab_is_applied()     marker presence check for drift detection
├── _cron_validate_schedule() 5-field cron regex sanity check
├── _cron_apply()             sync config.cron_jobs → crontab; returns list of changes
├── _cron_status()            return per-job dicts with applied field
├── _cron_job_marker()        crontab marker key for a job; recipe name, or recipe:{mount} for per-mount jobs
│
├── # === DOCKER CLIENT ===
├── class DockerError
├── class DockerClient
│     ├── _run()              subprocess wrapper
│     ├── inspect()           container inspect + image augmentation
│     ├── health()            current health/status string
│     ├── pull()              streamed image pull
│     ├── tag_image()         docker tag
│     ├── start()             docker start
│     ├── stop()              docker stop
│     ├── logs()              merged stdout+stderr docker logs (stderr=STDOUT); tail=100 default
│     ├── remove()            docker rm
│     ├── connect_network()   docker network connect
│     ├── _build_run_cmd()    builds docker run arg list
│     └── run()               docker run + connect extra networks
│
├── # === SNAPSHOT MANAGER ===
├── _sanitize_mount_name()    sanitize container path to a safe filename segment
├── _get_named_volumes()      filter Mounts[] for non-anonymous named volumes
├── _get_active_image_ref()   resolve active registry override or fall back to inspect image
├── _derive_version_meta()    extract version+digest from inspect_data → {"version": "...", "digest": "sha256:..."}
├── @dataclass Snapshot       fields: path, timestamp, image_ref, digest, version, volumes
├── @dataclass ContainerSpec
├── class SnapshotManager
│     ├── save()              write .json to staging dir, return (path, staging_dir)
│     ├── save_version()      write {snapshot_id}_version.json to staging dir
│     ├── finalize()          bundle staging dir → .tar.gz (compresslevel=1), delete staging, _rotate
│     ├── _rotate()           prune beyond max_snapshots_for()
│     ├── list()              Snapshot list newest-first; populates version from OCI label or tag
│     ├── load()              read and parse a snapshot from .tar.gz bundle
│     ├── load_version()      read version sidecar from snapshot bundle; returns {} on miss
│     ├── load_volumes()      lazy volume index loader; reads _volumes.json member from bundle
│     └── to_spec()           inspect dict → ContainerSpec
│
├── # === REGISTRY CLIENT ===
├── class RegistryError
├── class RegistryClient
│     ├── _parse_image_ref()  split ref into (registry, repo, tag)
│     ├── _get_credentials()  read ~/.docker/config.json
│     ├── _get_token()        fetch Bearer token from WWW-Authenticate realm
│     ├── _head()             HEAD request → Docker-Content-Digest
│     ├── _get_json()         GET request → parsed JSON
│     ├── get_remote_digest() registry manifest HEAD
│     ├── get_local_digest()  first entry of RepoDigests
│     ├── list_tags()         /v2/<repo>/tags/list → sorted list
│     ├── list_versions()     (tag, date) pairs newest-first
│     ├── _fetch_hub_dates()  Docker Hub REST API tag dates
│     ├── _fetch_github_dates() GitHub Releases API tag dates
│     ├── _replace_tag()      rewrite tag portion of an image ref
│     ├── _version_key()      sort key for semantic version strings
│     └── has_update()        compare remote vs local digest; pin-aware (local vs pin, then pin vs latest)
│
├── # === HEALTH CHECKER ===
├── _diagnose_bind_address()  reads /proc/net/tcp inside container after failure
├── class HealthChecker
│     └── wait_healthy()      polls every 5s up to timeout
│
├── # === ENGINE ===
├── class Engine
│     ├── _get_stack_siblings()     detect gateway + dependent siblings
│     ├── _wait_siblings_running()  poll siblings until running or timeout
│     ├── _backup_volumes()         archive bind mounts + named volumes; pause-aware; writes _volumes.json
│     ├── _save_meta()              write compose + env members into staging dir
│     ├── _save_image()             docker save pre-update image into staging dir
│     ├── _restore_volumes()        restore per-mount archives; ensures named Docker volumes exist
│     ├── rollback()                full rollback sequence; prints was→now summary on success
│     ├── update()                  full update sequence; prints was→now summary on success
│     ├── snapshot()                standalone snapshot without pull/recreate; used by cmd_snapshot() and TUI
│     ├── _resolve_compose_dir()    rewrite Portainer-internal /data paths
│     ├── _compose_run()            run docker compose sub-command
│     └── compose_update()          compose pull + up --force-recreate
│
├── # === COMMANDS ===
├── _get_running_containers()
├── _wrap()                   word-wrap at natural break points
├── _print_table()            fixed-width table with optional column wrapping
├── cmd_check()
├── cmd_status()
├── cmd_doctor()
├── _TAG_WORKERS / _STATUS_WORKERS  parallel worker counts
├── _identify_current_tag()   OCI label or parallel digest comparison
├── cmd_tags()
├── cmd_update()
├── cmd_rollback()
├── cmd_snapshot()            one-shot snapshot without pull/recreate; CLI entry point for Engine.snapshot()
├── cmd_list_snaps()
├── cmd_restore_volume()      standalone per-mount restore from snapshot archive
├── _rules_summary()          one-line summary of volume backup rules
├── _volumes_list_all()       table of all containers with mount/rule counts
├── _volumes_show_one()       per-mount backup status for one container
├── cmd_volumes()
├── cmd_volumes_set()
├── cmd_volumes_backup()      standalone volume backup without container update; --mount PATH for single mount
├── _fmt_uptime()             format StartedAt timestamp as elapsed time (45s / 12m / 3h 20m / 4d 6h)
├── _fetch_one_status()       one container's row for the interactive table; 14-element tuple
├── _browse_path()            interactive filesystem navigator; inline m=new folder, p=dir permissions
├── _prompt_missing_volume()  interactive prompt when a volume archive is missing
├── _show_skipped_volumes_dialogue()           table of backup-time exclusions + restore-volume hint
├── _show_unrestored_named_volumes_dialogue()  warning for named volumes without archives after rollback
├── _execute_rollback()       shared rollback execution: compose notice + Engine.rollback + dialogues
├── _interactive_snapshot_list()  unified snapshot browser (browse + rollback-pick modes)
├── _interactive_exclude_patterns()      exclude pattern list editor
├── _interactive_mount_action()          per-mount contextual sub-menu
├── _interactive_volume_encryption_menu()  per-mount encryption toggle (a=all, n=none, 1-N=toggle)
├── _interactive_volumes_menu()          mount list + dispatch; p→d (set/clear path unified), d→t (toggle backup), v→b (backup all)
├── _interactive_registries_menu()       registry source list — view, select, add, remove
├── _pick_version_tag()       tag list + selection helper; shared by version-select and container config
├── _interactive_version_select()    registry version picker with update/pin action sub-menu
├── _interactive_cron_add()          add a scheduled job for a container
├── _interactive_cron_job_menu()     per-job screen: toggle enabled, reschedule, delete
├── _interactive_cron_menu()         per-container job list + live drift detection
├── _interactive_cron_overview()     global read-only cron job summary
├── _interactive_container_chmod()   per-container snapshot permission profile picker + bulk retroactive apply
├── _container_config_menu()  per-container config sub-menu (registries, pin, auto-rollback, schedule, detach,
│                             backup toggles); snapshot and volume sections moved to dedicated submenus
├── _updates_menu()           update/rollback/compose/version-select/check submenu (u from action menu)
├── _snapshots_menu()         browse/new/prune/dir-override/limit/permissions/folder submenu (s from action menu)
├── _container_control_menu() restart/pause-unpause/stop/start/force-recreate/kill submenu (x from action menu)
├── _info_menu()              details/logs/stats submenu (i from action menu)
├── _backup_toggles_menu()    pause-for-backup/env-backup/image-export per-container toggles (b from configure)
├── _action_menu()            6-key category dispatcher (u/s/v/x/i/c) → submenus above; was flat 17-option menu
├── _interactive_global_chmod()      global permission profile picker; optional retroactive sweep across all containers
├── _HOME_COLUMNS             23-entry ordered column registry for the home screen table
├── _interactive_column_menu()  toggle individual column visibility
├── _settings_snapshots_menu()    global snapshot dir, rotation limit, permission profiles, image export
├── _settings_volumes_menu()      global volume backup toggle, pause-for-backup toggle
├── _settings_display_menu()      column visibility picker, pagination toggle
├── _settings_config_files_menu() switch config file, view log, change log path
├── _settings_maintenance_menu()  orphan cleanup, detached containers
├── _interactive_settings()   8-key domain dispatcher (s/v/a/e/j/d/c/m) → submenus above; was flat 17-option menu
├── _batch_update()           update all flagged containers; confirmation + sequential execution
├── cmd_interactive()         entry point: parallel status fetch + dispatch; 'u' for batch update
├── cmd_config()
├── cmd_pin()
├── cmd_unpin()
├── cmd_image_export()
├── cmd_cleanup()             find and remove orphaned staging dirs and .tmp encryption artifacts
├── cmd_convert_snapshots()   migrate old-format .json snapshots to .tar.gz bundles; --dry-run
├── cmd_cron()                7 subcommands: status, apply, recipes, add, remove, enable, disable
├── _rekey_bundle()           rekey text members of a .tar.gz bundle in-place; binary members passed through
├── _rekey_volume_archive()   decrypt + re-encrypt a per-mount RBPE archive via paired temp files with finally cleanup
├── cmd_encrypt()
└── cmd_install()

└── # === CLI ===
    main()                    argparse setup + auto-elevation + interactive dispatch
```

---

## 4. Architecture Overview

```
CLI args
   │
   ▼
main()
   │
   ├── (no args) ───────────────────────► cmd_interactive()
   │                                         parallel status fetch (10 workers)
   │                                         per-container action menu
   │                                         interactive rollback / version picker
   │                                         interactive volume config
   │                                         settings menu
   │
   ├── check / status / tags ───────────► RegistryClient
   │                                         get_remote_digest()
   │                                         get_local_digest()
   │                                         has_update()
   │                                         list_tags()
   │                                         list_versions()
   │
   ├── update / rollback ───────────────► Engine
   │                                         │
   │                                         ├── DockerClient
   │                                         │     inspect / pull / tag_image
   │                                         │     start / stop / remove / run
   │                                         │     connect_network / health
   │                                         │
   │                                         ├── SnapshotManager
   │                                         │     save / load / to_spec
   │                                         │     list / _rotate
   │                                         │
   │                                         ├── HealthChecker
   │                                         │     wait_healthy()
   │                                         │
   │                                         ├── _backup_volumes()
   │                                         └── _restore_volumes()
   │
   ├── volumes / volumes show / volumes set ► SnapshotManager + DockerClient
   ├── list-snaps ──────────────────────► SnapshotManager.list()
   ├── config ──────────────────────────► subprocess.run(editor) + validate loop
   └── install ─────────────────────────► writes wrapper + sudoers rule

                          ~/.update_zen/ ◄─── all classes read/write here
                            config.json
                            snapshots/  (.tar.gz bundles)
                            update_zen.log
```

All classes except `Engine` are stateless and do one job. `Engine` is the only
class that knows the full update or rollback sequence.

---

## 5. Class Reference

### 5.1 Config

**File path:** `~/.update_zen/config.json`

Holds user preferences. Written once on first run with defaults. Users can edit
the JSON directly. New fields added to the dataclass are automatically migrated
into existing config files on the next run.

**Fields:**

| Field | Type | Default | Description |
|---|---|---|---|
| `snapshot_dir` | Path | `~/.update_zen/snapshots` | Where snapshot files are stored |
| `log_file` | Path | `~/.update_zen/update_zen.log` | Append-only log file. Writes go to `_active_log_file`, a module-level variable initialized to the default at import time and updated to this value after `Config.load()` returns in `main()`. Home-relative paths are stored as `~/...` in config.json. |
| `max_snapshots` | int | 3 | Maximum snapshot pairs retained per container |
| `max_snapshots_overrides` | dict | `{}` | Per-container snapshot limit overrides. Keys are container names, values are ints. `Config.max_snapshots_for(container)` checks this before falling back to global `max_snapshots`. |
| `health_timeout_sec` | int | 300 | Seconds to wait for a container to reach healthy state |
| `exclude` | list[str] | [] | Container names never touched by `check`, `status`, or batch updates. Presented as "Detach from update_zen" in the TUI. Detached containers are not polled for updates. Re-attach via settings → `m` → `2`. |
| `volume_backup` | dict | {} | Per-container mount filtering rules (see Section 9) |
| `volume_backup_enabled` | bool | `True` | Global toggle — when `False`, all volume backup is skipped regardless of per-container rules |
| `auto_rollback` | bool | `True` | Global toggle — when `False`, failed health checks leave the container in place for inspection |
| `auto_rollback_disabled` | list[str] | `[]` | Per-container override list; containers named here skip auto-rollback even when the global toggle is `True` |
| `restart_stack_siblings` | bool | `False` | Enable two-phase sibling restart for Compose stacks (gateway-first) |
| `gateway_wait_sec` | int | 60 | Seconds to wait for a gateway container to become healthy before starting dependent siblings |
| `sibling_wait_sec` | int | 30 | Seconds to wait for non-gateway sibling containers after the gateway is up |
| `pinned_tags` | dict | `{}` | Container → tag string; `Engine.update()` deploys this tag instead of the container's current image tag |
| `registry_alternatives` | dict | `{}` | Container → `{refs, active}` — per-container registry source list; see `_get_active_image_ref()` |
| `image_export_enabled` | bool | `True` | Global toggle — when True, saves image layers to `_image.tar` before each update |
| `image_export_disabled` | list[str] | `[]` | Containers excluded from image export even when the global toggle is True |
| `snapshot_dir_overrides` | dict | `{}` | Container → path string; overrides global `snapshot_dir` for all snapshot and volume archive I/O for that container |
| `pause_for_backup` | bool | `True` | Global toggle — when True, containers are paused during volume backup for consistency |
| `pause_for_backup_disabled` | list[str] | `[]` | Containers that skip the pause step even when the global toggle is True |
| `cron_jobs` | dict | `{}` | Per-container scheduled job lists. Each entry is a list of `{recipe, schedule, enabled}` dicts. `config.json` is the source of truth; the crontab is derived state synced via `_cron_apply()`. |
| `pagination_enabled` | bool | `True` | When True, the container list in `cmd_interactive()` is paginated by terminal height; when False, shows all at once. Toggle in settings → `d` → `2`. |
| `container_versions` | dict | `{}` | Maps container name → `{"version": "...", "digest": "sha256:..."}`. Updated after every update/rollback/snapshot. Primary fallback for "was" version display in summaries. Auto-migrated into configs. Not user-editable. |
| `hidden_columns` | list | 12 default IDs | List of column IDs hidden on the home screen table. Defaults to `_DEFAULT_HIDDEN_COLUMNS` (12 IDs), leaving 9 of 21 optional columns visible. When absent or empty in `config.json`, defaults are applied automatically — empty and absent are treated the same. Managed via settings → `d` → `1`. |
| `snapshot_dir_mode` | int | `0o700` (448 in JSON) | Permission mode applied to newly created snapshot and volume archive **directories**. Stored as a decimal integer. Defaults match the pre-existing hardcoded value — no behaviour change on upgrade. |
| `snapshot_file_mode` | int | `0o600` (384 in JSON) | Permission mode applied to newly created snapshot bundle and volume archive **files**. |
| `snapshot_permission_overrides` | dict | `{}` | Container → `{"dir_mode": <int>, "file_mode": <int>}`. Per-container permission profile overrides. Set when a profile is applied via the container config menu (`m` key); cleared by the Clear override option. `Config.snapshot_dir/file_mode_for(container)` checks this before falling back to the global fields. |
| `encryption` | dict | `{mode, encrypt_containers, encrypt_volumes, saved_passwords}` | Encryption settings. `mode` is one of `"session"`, `"always"`, or `"saved"` (see password storage below). `encrypt_containers` is a list of container names to encrypt. `encrypt_volumes` is a per-container dict mapping container names to lists of container paths. `saved_passwords` is always `{}` in `config.json` — real passwords live in `credentials.json`. |

**Methods:**

```python
Config.load() -> Config
```
Class method. Reads `config.json` if it exists; falls back to defaults for any
missing key. On first run, creates and writes the file with all defaults. On
subsequent runs, if any expected keys are absent from the file (i.e. the schema
has been extended since the file was written), saves the file with the new
fields added. This makes schema migration automatic — users never need to
manually add new fields.

```python
Config.save() -> None
```
Serializes current state to `config.json` as indented JSON. Always writes
`"saved_passwords": {}` regardless of what is in memory — real passwords never
reach `config.json`. Sets `config.json` permissions to `0644`.

#### Password storage model

Encryption passwords are stored separately from all other config to allow
`config.json` to be cloud-synced or committed to a private repo safely.

| Mode | Where password lives | Use case |
|---|---|---|
| `session` | In-process memory only. Prompts once per process, never written anywhere. | Interactive one-off use |
| `saved` | `~/.update_zen/credentials.json` (0600). Loaded into memory at startup. | Automated cron runs |
| `always` | Not stored anywhere. Prompts on every operation. | Maximum security; impractical for cron |

**`credentials.json` format:**
```json
{
  "saved_passwords": {
    "sonarr": "mypassword",
    "radarr::config": "anotherpassword"
  }
}
```

Keys are either a container name (`"sonarr"`) or `"container::mount"` for
per-mount volume encryption.

**Invariant:** `config.json` always contains `"saved_passwords": {}`. Code that
reads `config.get_saved_password()` sees the runtime-merged result (credentials
loaded from `credentials.json` at startup). Code that writes passwords calls
`Config.set_saved_password()`, which routes to `_save_credentials()`. There is
no code path that writes real passwords into `Config.save()`.

**Auto-migration:** If an existing `config.json` contains passwords in
`saved_passwords` (pre-Sprint-1 state), `Config.load()` detects this, writes the
passwords to `credentials.json`, rewrites `config.json` clean, and prints
`Info: saved_passwords migrated...` to stderr. This runs once; subsequent loads
find `config.json` already clean.

**Recovery:** If `credentials.json` is lost, the app still works — it prompts for
passwords on next use. Re-enter the correct password and re-save it through the
TUI (`container menu → k → save password`). There is no recovery path for a lost
encryption password itself; the snapshot archives cannot be decrypted without it.
Store encryption passwords in a password manager alongside other infrastructure
credentials.

---

### 5.2 DockerClient

Thin wrapper around `subprocess.run()` calls to the `docker` CLI. Returns
parsed Python objects, not raw strings. All calls use `shell=False` with a list
argument — no string formatting of user-supplied values.

**Exception:** `DockerError(Exception)` — raised on any non-zero docker exit
code. Message includes the stderr output from the failed command. Also raised
(with a clear message) if the `docker` binary is not found on `PATH`.

**Private method:**

```python
DockerClient._run(args: list) -> subprocess.CompletedProcess
```
Prepends `["docker"]` to `args` and runs with `capture_output=True`. Raises
`DockerError` on non-zero exit or missing binary. All read operations use this.
Write operations that need to stream output (i.e. `pull`) call `subprocess.run`
directly without capturing.

**Public methods:**

```python
DockerClient.inspect(container: str) -> dict
```
Runs `docker inspect <container>`. Parses the JSON array and returns `result[0]`
(the single container object). **Also fetches `RepoDigests` from the image** via
a second `docker image inspect <image_id>` call and injects it into the returned
dict. This is necessary because container inspect does not include `RepoDigests`
natively — it is an image-level field. Without this step, digest comparison and
rollback image pinning would silently fail. Raises `DockerError` if the
container does not exist.

```python
DockerClient.pull(image_ref: str) -> None
```
Runs `docker pull <image_ref>` without capturing output so pull progress is
streamed directly to the user's terminal. `image_ref` may be `name:tag` or
`name@sha256:...`. Raises `DockerError` on failure.

```python
DockerClient.stop(container: str, timeout: int = 10) -> None
```
Runs `docker stop -t <timeout> <container>`. Does not raise if the container is
already stopped (Docker handles this gracefully). Raises `DockerError` on other
failures.

```python
DockerClient.logs(container: str, tail: int = 100) -> str
```
Runs `docker logs --tail <tail> <container>` and returns the combined output as
a string. Unlike `_run()` — which uses `capture_output=True` and separates stdout
from stderr into distinct streams — `logs()` calls `subprocess.run()` directly
with `stderr=subprocess.STDOUT`, merging both streams at the OS level. This
preserves chronological interleaving of lines that a container writes to stdout
and stderr (e.g. a web server logging requests to stdout and errors to stderr).
Raises `DockerError` on non-zero exit. Used by the TUI action menu `l` key.

```python
DockerClient.remove(container: str) -> None
```
Runs `docker rm <container>`. Does not use `-f` — raises `DockerError` if the
container is still running, so callers must stop before removing.

```python
DockerClient.run(spec: ContainerSpec) -> None
```
Builds a `docker run -d` command from a `ContainerSpec` via `_build_run_cmd()`,
executes it, then calls `connect_network()` for any additional networks beyond
the first. Raises `DockerError` if the container fails to start.

```python
DockerClient.health(container: str) -> str
```
Calls `self.inspect()` and reads container state. Returns the `Health.Status`
string (`"healthy"`, `"unhealthy"`, `"starting"`) when a Docker HEALTHCHECK is
defined, otherwise returns the raw `State.Status` string (`"running"`,
`"exited"`, etc.). Used by `HealthChecker.wait_healthy()` and by
`Engine.compose_update()` for the gateway pre-flight check.

```python
DockerClient.tag_image(source: str, target: str) -> None
```
Runs `docker tag <source> <target>`. Called in `Engine.update()` after a
digest-based pull to re-attach the named tag (e.g. `nginx:latest`) to the
newly pulled image so that subsequent `to_spec()` calls see the correct
`Config.Image` value rather than the digest ref.

```python
DockerClient.start(container: str) -> None
```
Runs `docker start <container>`. Used in `Engine.update()` and
`Engine.rollback()` to restart sibling containers that were stopped before
the target container was recreated.

```python
DockerClient.pause(container: str) -> None
```
Runs `docker pause <container>`. Freezes all processes in the container using
the cgroups freezer. A failed pause (e.g. container type does not support
cgroups freeze) is caught and logged in the backup flow — execution continues
with a live backup rather than aborting. Raises `DockerError` on non-zero exit
in other contexts. Used by `Engine.update()` (pause-for-backup) and the TUI
action menu option `9`.

```python
DockerClient.unpause(container: str) -> None
```
Runs `docker unpause <container>`. Resumes all processes in a paused container.
Raises `DockerError` on non-zero exit. Used by `Engine.update()` in the
pause-for-backup `try/finally` block, and by the TUI action menu option `9`.

```python
DockerClient.kill(container: str) -> None
```
Runs `docker kill <container>`. Sends `SIGKILL` immediately — no graceful
shutdown period. Intended for containers that are frozen or unresponsive to
`stop`. Raises `DockerError` on non-zero exit. Used by the TUI action menu
key `k`.

```python
DockerClient.stats(container: str) -> dict
```
Runs `docker stats --no-stream --format '{{json .}}'` and returns the parsed
JSON dict. Available fields: `CPUPerc`, `MemUsage`, `MemPerc`, `NetIO`,
`BlockIO`, `PIDs`. Raises `DockerError` on non-zero exit or if the container
is not in a stats-able state. Used by the TUI action menu key `t`.

```python
DockerClient.connect_network(container: str, network: str) -> None
```
Runs `docker network connect <network> <container>`. Used for containers that
belong to more than one Docker network (since `docker run --network` only
accepts one network).

```python
DockerClient._build_run_cmd(spec: ContainerSpec) -> list
```
Builds the `docker run` argument list from a `ContainerSpec`. Extracted as a
separate method to allow testing command construction without a running Docker
daemon. The full construction order:

```
run -d --name <name>
[-e KEY=value ...]
[-v /host:/container:opts ...]
[-p hostip:hostport:containerport ...]
[--label key=value ...]
[--restart <policy>]
[--network <first_network>]
[--entrypoint <entrypoint[0]>]   (only if spec.entrypoint is non-empty)
<image>
[entrypoint[1:] ...]              (remaining entrypoint args, if any)
[cmd ...]
```

---

### 5.3 ContainerSpec

A `@dataclass` that holds normalized, reconstructed parameters for `docker run`.
Built by `SnapshotManager.to_spec()` from a raw inspect dict. Fields map
directly to `docker run` flags.

```python
@dataclass
class ContainerSpec:
    name:             str          # container name
    image:            str          # name:tag (update) or name@sha256:... (rollback)
    env:              list[str]    # ["KEY=value", ...]
    binds:            list[str]    # ["/host/path:/container/path:ro", ...]
    port_bindings:    list[str]    # ["8080:80/tcp"] or ["1.2.3.4:8080:80/tcp"]
    networks:         list[str]    # all networks; first used in run, rest via connect
    labels:           list[str]    # ["key=value", ...]
    restart:          str          # "unless-stopped", "always", "no", "on-failure:N"
    entrypoint:       list[str]    # [] means use image default
    command:          list[str]    # [] means use image default
    network_mode:     str          # "container:<name>" for shared-namespace stacks; "" otherwise
    # runtime fidelity fields (all default to safe zero/empty/False values)
    privileged:       bool         # --privileged
    devices:          list[str]    # --device /dev/xxx:/dev/xxx
    runtime:          str          # --runtime (suppressed when "runc")
    sysctls:          dict         # --sysctl key=value
    security_opt:     list[str]    # --security-opt
    user:             str          # --user
    working_dir:      str          # --workdir
    ulimits:          list[dict]   # --ulimit type=soft:hard
    shm_size:         int          # --shm-size (bytes; suppressed when 0)
    pid_mode:         str          # --pid
    ipc_mode:         str          # --ipc (suppressed when "private" or "shareable")
    extra_hosts:      list[str]    # --add-host (suppressed when network_mode set)
    dns:              list[str]    # --dns (suppressed when network_mode set)
    dns_search:       list[str]    # --dns-search (suppressed when network_mode set)
    dns_options:      list[str]    # --dns-option (suppressed when network_mode set)
    log_driver:       str          # --log-driver
    log_opts:         dict         # --log-opt key=value
    cpu_shares:       int          # --cpu-shares (suppressed when 0)
    memory:           int          # --memory (suppressed when 0)
    nano_cpus:        int          # --cpus (suppressed when 0)
    hostname:         str          # --hostname (suppressed when network_mode set)
    stop_signal:      str          # --stop-signal (suppressed when "SIGTERM")
    group_add:        list[str]    # --group-add
    init:             bool         # --init
    readonly_rootfs:  bool         # --read-only
```

The `image` field is set differently depending on context:
- `pin_digest=False` (forward update): uses `Config.Image` — e.g. `nginx:latest`
- `pin_digest=True` (rollback): uses `RepoDigests[0]` — e.g. `nginx@sha256:abc...`

When `network_mode` is set (e.g. `"container:gluetun"`), `_build_run_cmd()` passes
`--network container:<name>` instead of using `networks[0]`, and `networks` will be
`[]`. Additionally, `--hostname`, `--add-host`, `--dns`, `--dns-search`, and
`--dns-option` are suppressed — Docker rejects these network-namespace flags when
sharing another container's namespace.

Default-suppression guards prevent emitting flags whose values match Docker's own
defaults (e.g. `--runtime runc`, `--stop-signal SIGTERM`, `--ipc private`,
`--memory 0`). All runtime fidelity fields default to their zero/empty/False values
so existing snapshots that predate these fields are handled correctly.

---

### 5.4 SnapshotManager

Reads and writes snapshot files. Enforces the rolling snapshot limit. Converts
raw inspect data into a structured `ContainerSpec`.

**Constructor:** `SnapshotManager(config: Config)`

```python
SnapshotManager.save(container: str, inspect_data: dict) -> tuple[Path, Path]
```
Creates a `_staging_{timestamp}/` subdirectory inside
`<snapshot_dir_for(container)>/<container>/`, writes the inspect JSON there as
`<snapshot_id>.json`, and returns `(json_path, staging_dir)`. All subsequent
pre-finalization writes (`_save_meta`, `_save_image`, `_backup_volumes`) target
`staging_dir`. Does **not** call `_rotate()` — that moves to `finalize()`.

```python
SnapshotManager.finalize(container: str, snapshot_id: str, staging_dir: Path) -> Path
```
Bundles everything in `staging_dir` into `{snapshot_id}.tar.gz` in the
container's snapshot directory using `compresslevel=1` (meaningfully faster
than the default 9 for large image tars, with modest size penalty). Deletes
`staging_dir`, calls `_rotate()`, and returns the path of the created archive.
Must be called after `_backup_volumes()`.

```python
SnapshotManager._rotate(container: str) -> None
```
Lists existing snapshots for the container (newest first) and deletes any
beyond `config.max_snapshots`. Calls `load_volumes(snapshot)` to get each
snapshot's volume index (needed to find external archive paths), deletes the
main bundle, then globs `{snapshot_id}_*.tar.gz` in the container directory
to delete per-mount archives.

```python
SnapshotManager.list(container: str) -> list[Snapshot]
```
Globs `*.tar.gz` in the container's snapshot directory.
Identifies main archives by matching the bare timestamp regex
`^\d{4}-\d{2}-\d{2}T\d{2}-\d{2}-\d{2}$` against the stem — per-mount volume
archives like `{id}_config.tar.gz` are excluded. Derives snapshot IDs from
`.tar.gz` paths using `path.name.removesuffix(".tar.gz")` (never `path.stem`
— which would return `"...T12-00-00.tar"`, causing the regex to fail silently).
Returns `Snapshot` objects sorted newest first. Returns `[]` if no snapshots
exist.

Each `Snapshot` is a `@dataclass` with:
```python
@dataclass
class Snapshot:
    path:       Path
    timestamp:  datetime
    image_ref:  str     # Config.Image value, e.g. "nginx:latest"
    digest:     str     # RepoDigests[0], e.g. "nginx@sha256:..." (empty if absent)
    version:    str     # org.opencontainers.image.version label, or tag if label absent, or ""
    volumes:    list    # always [] in list(); loaded lazily via load_volumes()
```

```python
SnapshotManager.load_volumes(snapshot: Snapshot) -> dict
```
Lazily loads the volume index for a snapshot. Returns a dict with `"volumes"`
and `"skipped"` arrays. Extracts `_volumes.json` from inside the `.tar.gz`
bundle. Returns `{"volumes": [], "skipped": []}` if no index exists.

```python
SnapshotManager.load(snapshot: Snapshot) -> dict
```
Reads and JSON-parses the snapshot's inspect data. Extracts the
`{snapshot_id}.json` member from the `.tar.gz` bundle and returns the raw
inspect dict.

```python
SnapshotManager.to_spec(inspect_data: dict, pin_digest: bool = True) -> ContainerSpec
```
The densest method in the project. Extracts every `ContainerSpec` field from a
raw inspect dict. The `inspect → ContainerSpec` field mapping:

| Inspect path | ContainerSpec field | Notes |
|---|---|---|
| `Name.lstrip("/")` | `name` | |
| `Config.Image` | `image` | when `pin_digest=False` |
| `RepoDigests[0]` | `image` | when `pin_digest=True` |
| `Config.Env` | `env` | already a list of `"KEY=val"` strings |
| `HostConfig.Binds` | `binds` | already a list of bind strings |
| `HostConfig.PortBindings` | `port_bindings` | reshaped (see below) |
| `NetworkSettings.Networks` keys | `networks` | |
| `Config.Labels` | `labels` | reshaped from `{k: v}` to `["k=v", ...]` |
| `HostConfig.RestartPolicy` | `restart` | `on-failure:N` for retry counts |
| `Config.Entrypoint` | `entrypoint` | null → `[]` |
| `Config.Cmd` | `command` | null → `[]` |

**Port binding reshape:** `HostConfig.PortBindings` is a nested dict:
```json
{"80/tcp": [{"HostIp": "0.0.0.0", "HostPort": "8080"}]}
```
Reshaped to a flat list. If `HostIp` is non-empty:
`"<ip>:<host_port>:<container_port>"`, otherwise `"<host_port>:<container_port>"`.

---

### 5.5 RegistryClient

Checks whether an image has a newer version available on its registry. Uses
`urllib` only — no third-party HTTP library.

**Exception:** `RegistryError(Exception)` — raised on auth failure, network
error, or missing response headers.

**Class attribute:**
```python
_ACCEPT = (
    "application/vnd.docker.distribution.manifest.list.v2+json, "
    "application/vnd.oci.image.index.v1+json, "
    "application/vnd.docker.distribution.manifest.v2+json, "
    "application/vnd.oci.image.manifest.v1+json"
)
```
Manifest list types are listed first so multi-arch images return the index
digest, which matches what `docker image inspect` stores in `RepoDigests`.

```python
RegistryClient._parse_image_ref(image_ref: str) -> (registry, repo, tag)
```
Parses an image reference into its components:

| Input | registry | repo | tag |
|---|---|---|---|
| `nginx` | `registry-1.docker.io` | `library/nginx` | `latest` |
| `nginx:1.25` | `registry-1.docker.io` | `library/nginx` | `1.25` |
| `user/app:v2` | `registry-1.docker.io` | `user/app` | `v2` |
| `ghcr.io/user/app:main` | `ghcr.io` | `user/app` | `main` |

A `ref` component is treated as a registry hostname if it contains `.`, `:`, or
equals `localhost`. Single-component names are official Docker Hub images and
get the `library/` prefix.

```python
RegistryClient._get_credentials(registry: str) -> (username, password) | (None, None)
```
Reads `~/.docker/config.json` and looks for a stored `auth` entry for the
registry. Returns decoded username and password, or `(None, None)` if not found.
Note: only handles embedded `auth` credentials (base64 encoded). Docker
credential stores (`credsStore`, `credHelpers`) are not currently supported.

```python
RegistryClient._get_token(registry: str, www_auth: str) -> str
```
Parses the `WWW-Authenticate` Bearer header from a 401 response. Extracts
`realm`, `service`, and `scope`. Fetches a Bearer token from the auth endpoint,
sending Basic credentials if available. Returns the token string.

```python
RegistryClient._head(url: str, extra_headers: dict = None) -> str
```
Sends a `HEAD` request to `url` with the multi-type `Accept` header. Returns
the `Docker-Content-Digest` header value. Raises `RegistryError` if the header
is absent.

```python
RegistryClient.get_remote_digest(image_ref: str) -> str
```
Sends `HEAD /v2/<repo>/manifests/<tag>`. On 401, parses the `WWW-Authenticate`
header, fetches a Bearer token, and retries. Returns the `Docker-Content-Digest`
value. Raises `RegistryError` on failure.

```python
RegistryClient.get_local_digest(inspect_data: dict) -> str | None
```
Returns the first entry of `inspect_data["RepoDigests"]`, or `None` if empty.
Because `docker inspect <container>` does not natively include `RepoDigests`,
callers must pass data from `DockerClient.inspect()` which augments the dict
with image-level `RepoDigests` automatically.

```python
RegistryClient.has_update(inspect_data: dict, image_ref_override: str = "") -> bool
```
Compares the remote digest to the local digest. Returns `True` if they differ.
Returns `False` if the image ref is missing or `RepoDigests` is empty (i.e.,
locally-built image with no registry digest). Raises `RegistryError` if the
registry call fails — callers (`cmd_check`, `cmd_status`) catch this and display
`"?"` with a logged warning rather than silently showing `"no"`.

When `image_ref_override` is non-empty, it is used as the image ref instead of
reading `Config.Image` from `inspect_data`. Used by `_fetch_one_status`,
`cmd_check`, `cmd_status`, and `_action_menu` choice 5 to pass the active
registry alternative resolved by `_get_active_image_ref()`.

Comparison strips the image name prefix from the local entry before comparing:
```
local: "nginx@sha256:abc123"  → local_hash: "sha256:abc123"
remote:               "sha256:abc123"
```

```python
RegistryClient.list_tags(image_ref: str) -> list[str]
```
Fetches `/v2/<repo>/tags/list` from the registry (with the same 401 → token
flow as `get_remote_digest`). Returns all tags sorted alphabetically. Used by
`cmd_tags` and as a fallback inside `list_versions` when no date-enriched
source is available.

```python
RegistryClient.list_versions(image_ref: str, limit: int = 15) -> list[tuple]
```
Returns up to `limit` version-like tags as `(tag, date_str)` tuples, sorted
newest first. Tags are filtered to strings that start with a digit or `v`+digit
and are not in `_NON_VERSION_TAGS` (e.g. `latest`, `stable`, `edge`).

For Docker Hub images, calls `_fetch_hub_dates()` to get dates from the Hub
REST API (up to 500 tags). For `ghcr.io` images, calls `_fetch_github_dates()`.
For all other registries, falls back to `list_tags()` and sorts by semantic
version with `_version_key()`, returning `"?"` as the date. Used by the
interactive version picker (`_interactive_version_select`).

```python
RegistryClient._fetch_hub_dates(namespace: str, repo: str) -> dict
```
Paginates the Docker Hub REST API (`hub.docker.com/v2/repositories/...`) up to
5 pages (500 tags), returning `{tag: "YYYY-MM-DD"}`. Returns an empty dict on
any failure so callers degrade gracefully to version-sort-only mode.

```python
RegistryClient._fetch_github_dates(org: str, repo: str) -> dict
```
Fetches the GitHub Releases API (`api.github.com/repos/...`) and returns
`{tag: "YYYY-MM-DD"}`. Strips the leading `v` from release tag names so GitHub
tags (e.g. `v0.15.3`) match Docker image tags (e.g. `0.15.3`) directly.
Returns an empty dict on failure, including GitHub rate-limit 403s.

```python
RegistryClient._replace_tag(image_ref: str, new_tag: str) -> str
```
Static method. Rewrites the tag portion of `image_ref` with `new_tag`. Strips
any `@digest` suffix first. Used in `Engine.update()` for `--tag` substitution
and in `_identify_current_tag()` to build per-tag digest refs for comparison.

---

### 5.6 HealthChecker

Polls a container's state after it is started. Handles the three possible
states: HEALTHCHECK defined and passing, no HEALTHCHECK but running, and failed
or exited.

**Class attribute:** `_POLL_INTERVAL = 5` (seconds between polls)

**Constructor:** `HealthChecker(docker: DockerClient, config: Config)`

```python
HealthChecker.wait_healthy(container: str, timeout_sec: int) -> bool
```
Polls every 5 seconds up to `timeout_sec`. Each poll calls
`DockerClient.health()` which reads container `State` and `State.Health`.

Returns `True` if:
- Container has a HEALTHCHECK and reaches `"healthy"`
- Container has no HEALTHCHECK and `State.Status` is `"running"`

Returns `False` if:
- Status reaches `"unhealthy"`, `"exited"`, or `"dead"`
- `timeout_sec` elapses without reaching a passing state
- `DockerClient.health()` raises `DockerError`

Logs each poll result: `[health <container>] <status> (<N>s elapsed)`.

The sleep duration is clamped to `min(_POLL_INTERVAL, max(remaining, 0.05))`
to avoid a tight spin loop as the deadline approaches.

---

### 5.7 Engine

Orchestrates the full update and rollback sequences. The only class that knows
the end-to-end flow. All other classes are stateless utilities.

**Constructor:** `Engine(config: Config)` — instantiates `DockerClient`,
`SnapshotManager`, `RegistryClient`, and `HealthChecker` internally.

#### Engine._get_stack_siblings()

```python
Engine._get_stack_siblings(container: str, inspect_data: dict) -> tuple[list, list]
```

Returns `(gateway_siblings, dependent_siblings)`. Only runs when
`config.restart_stack_siblings` is True and the container has a
`com.docker.compose.project` label.

Discovers sibling containers by querying `docker ps --filter label=...` for the
same Compose project. Detects the gateway by reading the target's
`HostConfig.NetworkMode` — if it starts with `"container:<name>"`, that name is
the gateway. Returns `([gateway_name], [other_siblings])` when a gateway is found,
or `([], [all_siblings])` when there is no `container:` network mode.

#### Engine._wait_siblings_running()

```python
Engine._wait_siblings_running(siblings: list, prefix: str, timeout_sec: int) -> None
```

Polls all containers in `siblings` every 2 seconds until every one reaches
`"running"` or `"healthy"` state, or `timeout_sec` elapses. Non-fatal: if the
deadline passes, a warning is logged and execution continues. Used after starting
gateway and dependent siblings in both `update()` and `rollback()`.

#### Engine.update()

```python
Engine.update(container: str, auto_rollback: bool = True, tag: str = "") -> bool
```

The full update sequence:

```
1.  docker inspect <container>              → DockerClient.inspect()
    Warn if NetworkMode is "container:<x>" without --compose.

2.  Detect stack siblings                   → _get_stack_siblings()

3.  Save config snapshot                    → SnapshotManager.save()
                                              returns (snap_path, staging_dir)
3b. _save_meta(staging_dir)                 → write _compose.yaml and _env.env into staging
3c. _save_image(staging_dir)                → docker save pre-pull image into staging
3d. Pause container (if pause_for_backup enabled and not in disabled list)
      docker pause <container>              → non-fatal on failure; backup proceeds live
    _backup_volumes(staging_dir, paused)    → per-mount archives + _volumes.json into staging
    docker unpause <container>              → always runs (try/finally)
3e. SnapshotManager.finalize()              → bundle staging → {id}.tar.gz, call _rotate

4.  Pull new image by digest (preferred):
      get_remote_digest(image)              → RegistryClient.get_remote_digest()
      docker pull <base>@<sha256:...>       → DockerClient.pull()
      docker tag <digest_ref> <clean_image> → DockerClient.tag_image()
    On RegistryError: fall back to plain tag pull (docker pull <image:tag>).
    If --tag specified: rewrite image ref before pull.
    if pull fails → abort, original still running, return False

5.  docker stop <container>
        if fails → abort, return False

5b. Stop all siblings (non-fatal per sibling)
        docker stop <sibling> for each sibling

6.  docker rm <container>
        if fails → abort, return False

6b. Two-phase sibling restart:
      Start each gateway sibling            → DockerClient.start()
      _wait_siblings_running(gateway_siblings, gateway_wait_sec)
      Start each dependent sibling          → DockerClient.start()
      _wait_siblings_running(dependent_siblings, sibling_wait_sec)

7.  Build spec from pre-update inspect data → SnapshotManager.to_spec(pin_digest=False)

8.  docker run (from spec)                  → DockerClient.run()
        if fails → rollback unconditionally regardless of auto_rollback flag
                   (container is gone — no other option), return False

9.  Wait for healthy state                  → HealthChecker.wait_healthy()
9a. Healthy → log success, return True
9b. Unhealthy + auto_rollback=True → _diagnose_bind_address(), then rollback(snaps[0])
9b. Unhealthy + auto_rollback=False → log failure, leave container in place
```

Each step is logged with the prefix `[UPDATE <container>]`.

#### Engine.rollback()

```python
Engine.rollback(container: str, snapshot: Snapshot, reason: str = "manual") -> bool
```

The full rollback sequence:

```
1.  Load snapshot JSON                      → SnapshotManager.load(snapshot)
2.  Build spec with pinned digest           → SnapshotManager.to_spec(pin_digest=True)
3.  Detect stack siblings from snapshot     → _get_stack_siblings()

3b. If _image.tar member exists in snapshot bundle:
      docker load -i {snapshot_id}_image.tar  (failure is non-fatal — falls through)

4.  Check if pinned image is already local  → docker image inspect <digest>
        if not local → docker pull <image@sha256:...>
        if pull fails → return False

5.  docker stop <container>                 (non-fatal — may already be stopped)

5b. Stop all siblings (non-fatal per sibling)

6.  docker rm <container>
        on DockerError: docker inspect <container>
          if inspect also fails → container already gone, log "already gone", continue
          if inspect succeeds → genuine blocker, return False

    _restore_volumes(container, snapshot, ext_overrides)
        → ensures named Docker volumes exist, then extracts per-mount archives

6b. Two-phase sibling restart:
      Start each gateway sibling            → DockerClient.start()
      _wait_siblings_running(gateway_siblings, gateway_wait_sec)
      Start each dependent sibling          → DockerClient.start()
      _wait_siblings_running(dependent_siblings, sibling_wait_sec)

7.  docker run (from snapshot spec)         → DockerClient.run()
        if fails → return False

8.  Wait for healthy state                  → HealthChecker.wait_healthy()
9.  Log outcome, return True/False
```

Each step is logged with the prefix `[ROLLBACK <container>]`.

The `reason` parameter is written to the log (`"auto"` vs `"manual"`) to make
log review easier after an incident.

#### Engine.compose_update()

```python
Engine.compose_update(container: str, auto_rollback: bool = True) -> bool
```

Updates a container managed by Docker Compose via `docker compose up --force-recreate`.
Required for stacks where containers share a network namespace (e.g. Gluetun-routed
stacks with `network_mode: service:gluetun`), where individual `stop/rm/run`
would leave dependent containers without a network.

```
1.  docker inspect <container>              → reads Compose labels
    Requires com.docker.compose.project.working_dir and
    com.docker.compose.service labels — aborts if absent.

    Resolve working_dir via _resolve_compose_dir() if it's a Portainer-internal
    /data/compose/<id>/ path.

    Pre-flight gateway check: if container uses container:<name> network mode,
    ensure gateway is running before touching anything. Start it and wait up to
    gateway_wait_sec if not.

2.  Save config snapshot                    → SnapshotManager.save()
    _backup_volumes()                       → archives bind mounts to .tar.gz

3.  docker compose pull <service>
        if fails → abort, original still running, return False

4.  docker compose up -d --no-deps --force-recreate <service>
    Always passes --project-name (from com.docker.compose.project label)
    and --no-deps (to avoid touching the gateway container).
        if fails → auto-rollback if enabled, return False

5.  Wait for healthy state                  → HealthChecker.wait_healthy()
5a. Healthy → log success, return True
5b. Unhealthy + auto_rollback=True → _diagnose_bind_address(), then rollback(snaps[0])
5b. Unhealthy + auto_rollback=False → log failure, leave container in place
```

Each step is logged with the prefix `[UPDATE <container>]`.

#### Engine.snapshot()

```python
Engine.snapshot(container: str) -> bool
```

Takes a full snapshot of a running container without pulling a new image or
recreating it. Runs the same capture sequence as the pre-pull steps of
`update()`:

```
1.  docker inspect <container>              → DockerClient.inspect()
        if fails → log error, return False

2.  SnapshotManager.save()                  → write inspect JSON to staging dir
    _save_meta()                            → write compose + env into staging
    _save_image()                           → docker save image into staging

2b. Version metadata capture
    _derive_version_meta(inspect_data)      → extract {"version": "...", "digest": "sha256:..."}
    SnapshotManager.save_version()          → write {snapshot_id}_version.json to staging
    config.container_versions[container] = derived_meta; config.save()

3.  Pause container (if pause_for_backup enabled and not in disabled list)
      docker pause <container>              → non-fatal on failure; backup proceeds live
    _backup_volumes()                       → per-mount archives + _volumes.json into staging
    docker unpause <container>              → always runs (try/finally)

4.  SnapshotManager.finalize()              → bundle staging → {id}.tar.gz, call _rotate
```

Returns `True` on success, `False` if the initial inspect fails. All subsequent
steps (meta, image, volumes) are non-fatal — failures are logged as warnings and
the snapshot is still finalized. Each step is logged with the prefix
`[SNAPSHOT <container>]`.

Has no CLI subcommand. Exposed in the TUI via the `t` key in
`_container_config_menu`. Useful for taking a manual checkpoint before a
potentially risky config change without triggering a full update.

#### Engine._resolve_compose_dir()

```python
Engine._resolve_compose_dir(working_dir: str, prefix: str) -> str
```

Returns an accessible host path for `working_dir`. If the path already exists
on the host filesystem, it is returned unchanged.

Portainer stores compose files at `/data/compose/<stack_id>/` inside its own
container. The label `com.docker.compose.project.working_dir` reflects this
internal path, which does not exist on the host. This method detects paths
starting with `/data/` that are not accessible, then inspects each name in
`_PORTAINER_NAMES` to find where Portainer's `/data` volume is bind-mounted on
the host (e.g. `/opt/portainer/data`) and rewrites the path accordingly.

Returns the resolved path string, or `""` if resolution fails. Also used to
remap individual config file paths listed in
`com.docker.compose.project.config_files` when they share the same `/data/`
prefix.

#### Engine._compose_run()

```python
Engine._compose_run(cmd: list, cwd: str) -> subprocess.CompletedProcess
```

Static method. Runs a `docker compose` sub-command (passed as a list) in
directory `cwd`. Raises `DockerError` with a clear human-readable message if
the `docker` binary is not found. Does **not** raise on a non-zero exit code —
callers inspect `result.returncode` themselves so they can log an appropriate
message before deciding whether to roll back.

#### Engine._save_meta()

```python
Engine._save_meta(container: str, snapshot_id: str, inspect_data: dict,
                  staging_dir: Path) -> None
```

Writes two optional files into `staging_dir` immediately after
`SnapshotManager.save()` and before the image pull. Both become members of the
main `.tar.gz` bundle when `finalize()` runs.

- `{snapshot_id}_compose.yaml` — the container's compose file, captured via
  `_resolve_compose_dir()` (handles Portainer path rewriting transparently).
  Written only when the container has `com.docker.compose.project.working_dir`
  and the path resolves to an accessible location.
- `{snapshot_id}_env.env` — user-set env overrides, computed by diffing
  `Config.Env` (the merged container env) against the image-baked defaults from
  `docker image inspect <image_id>`. Written only when overrides exist. This
  file is reference-only — the full env in the snapshot JSON is what the
  reconstruction path uses.

Both writes are non-blocking: any failure is logged as a warning and the update
sequence continues.

#### Engine._save_image()

```python
Engine._save_image(container: str, snapshot_id: str, inspect_data: dict,
                   staging_dir: Path) -> None
```

Saves the container's current image to `{snapshot_id}_image.tar` inside
`staging_dir` using `docker save <image_id> -o <path>`. Called immediately
after `_save_meta()`, before the new image is pulled. This preserves the
pre-update image layers on disk (bundled into the main `.tar.gz` by `finalize()`)
so rollback can succeed without network access.

Respects `config.image_export_enabled` (global toggle) and
`config.image_export_disabled` (per-container opt-out list). A failed
`docker save` is logged as a warning and any partially-written tar is deleted
— the failure never blocks the update.

#### Engine._backup_volumes()

```python
Engine._backup_volumes(container: str, snapshot_id: str, inspect_data: dict,
                       staging_dir: Path, paused: bool = False) -> None
```

Archives the container's bind mount host directories and named Docker volumes
to individual per-mount archives. Called from `update()` after `_save_image()`,
while the container is still running (or paused — see below).

Logs one of two lines at the start of each run:
- `"container is paused — backup will be consistent"` when `paused=True`
- `"container is live — backup may be inconsistent"` when `paused=False`

**Bind mounts** — parsed from `HostConfig.Binds`. Any entry whose host path
does not start with `/` is silently skipped (it's a named volume reference
that will be handled by the named-volumes loop below).

**Named volumes** — discovered via `_get_named_volumes(inspect_data)`, which
filters `Mounts[]` for `Type == "volume"` entries and excludes 64-char hex
names (anonymous volumes are ephemeral and misleading to back up).

For each mount (bind or named), the method:
1. Reads per-container filtering rules from `config.volume_backup[container]`
2. Skips if `container_path` is in `skip_mounts`
3. Skips if `include_only_mounts` is set and `container_path` is not in the list
4. Skips if the source path does not exist on disk
5. Skips if the path is a socket or device file
6. Archives to `{snapshot_id}_{mount}.tar.gz` applying `exclude` patterns;
   writes `vol_name` into the index entry for named volumes

Writes `_volumes.json` into `staging_dir` containing `volumes` (archived mounts)
and `skipped` (excluded mounts with reasons) arrays. This file becomes a member
of the main `.tar.gz` bundle when `finalize()` runs.

Per-mount archive location follows the four-level hierarchy: global
`snapshot_dir` → `snapshot_dir_overrides` → container volume `save_path` →
per-mount `mount_paths`. Errors during archiving are caught and logged but do
not abort the update sequence.

#### Engine._restore_volumes()

```python
Engine._restore_volumes(container: str, snapshot: Snapshot,
                        ext_overrides: dict | None) -> None
```

Restores volume data from a snapshot's per-mount archives back to the
filesystem. Called from `rollback()` after the container is removed and before
it is recreated. The `ext_overrides` parameter controls interactivity: `None`
means non-interactive (log missing archives and skip); any dict (including `{}`)
means interactive (call `_prompt_missing_volume()` when an archive is not found).

Calls `sm.load_volumes(snapshot)` to get the index. For each entry in
`volumes`: if `vol_name` is set, ensures the named Docker volume exists
(`docker volume inspect`; creates via `docker volume create` on failure);
then extracts the per-mount archive with `extractall(path="/")`. Uses a
two-path lookup: checks the recorded `archive_dir` first, then falls back to
`snapshot_dir_for(container)` so archives moved to the default location after
the fact are still found.

Per-mount archives were built with absolute `arcname` values (the full source
path), so `extractall(path="/")` restores each file to its original location
without any path manipulation. All extraction failures are non-fatal — logged
and skipped so the config rollback always completes.

---

## 6. CLI Commands

**Global flag: `--config PATH`**

All commands accept `--config PATH` to load a non-default config file. The flag
is parsed by a mini pre-parser before `Config.load()` runs, so it works at any
argument position. `UPDATE_ZEN_CONFIG` (environment variable) is also supported
but unreliable under `sudo` because sudo strips env vars by default — prefer the
flag for scripting and cron.

```
update_zen --config /mnt/nas/update_zen.json update nginx
```

### `update_zen` (no arguments)

Launches interactive mode. Fetches status for all running containers in parallel
(10 workers) and displays a numbered table. The user selects a container by
number, then operates on it from a per-container action menu.

**Home screen table columns**

The table is built from the `_HOME_COLUMNS` registry (23 entries total: 2 always-on
+ 21 optional). Columns are toggled via the Display domain in settings (`s` from home
→ `d` → `1` — `_interactive_column_menu`).
The 9 columns visible by default on a fresh install are:

`#` | `CONTAINER` | `ENC` | `SVD PWD` | `HLTH` | `UPDT` | `IMAGE` | `DATE` | `UPTIME` | `%` | `MOUNTS`

Notable column details:

- **HLTH** — Health/state condensed to a single character: `+` healthy, `*` running,
  `X` unhealthy/dead/removing, `~` starting, `-` exited/created, `|` paused,
  `@` restarting, `?` unknown/error.
- **SVD PWD** — Box indicator (`■`/`□`) showing whether a permanently-saved
  encryption password exists in `credentials.json` for this container.
- **IMAGE** — Shows the pinned tag from `config.pinned_tags` if set; otherwise
  the tag portion of the image reference only (e.g. `v1.24.0`). `:latest` is
  simplified to `latest`. Truncated to 12 chars.
- **UPTIME** — Elapsed time since last start, formatted as `45s` / `12m` /
  `3h 20m` / `4d 6h`. Populated from `docker inspect` `State.StartedAt`;
  zero-time sentinel (`0001-...`) shown as `—`.

The 12 columns hidden by default (accessible via settings → `d` → `1`) are: `VER`,
`SNAPS`, `PIN`, `CRON`, `AUTO RB`, `IMG EXP`, `VOL BAK`, `RESTARTS`, `PORTS`,
`NETWORK`, `COMPOSE`, `SNAPSHOT PATH`.

### `update_zen check [<container> ...]`

Checks one or more containers (or all running containers if none specified) for
available image updates. Skips containers in `config.exclude`.

Output table: `CONTAINER | IMAGE | UPDATE`

`UPDATE` column shows:
- `yes` — remote digest differs from local
- `no` — digests match (up to date)
- `?` — registry check failed (warning logged with reason)

### `update_zen status`

Shows a summary of all running containers (excluding `config.exclude`).

Output table: `CONTAINER | IMAGE | DIGEST | UPDATE | SNAPS | VERSION | DATE`

- `DIGEST` — first 19 chars of `sha256:...` portion of local digest, or `none`
- `UPDATE` — same as `check`
- `SNAPS` — number of saved snapshots for this container
- `VERSION` — `org.opencontainers.image.version` OCI label, falling back to image tag if it contains a digit; `?` if neither is available
- `DATE` — `org.opencontainers.image.created` OCI label truncated to `YYYY-MM-DD`; `?` if absent

### `update_zen doctor`

Validates the current configuration against the local filesystem and reports
health across five areas. Run this after a new install, after migrating from
another machine, or any time something seems misconfigured.

**Output sections:**

- **Credentials** — checks whether `credentials.json` exists, has `0600`
  permissions, and how many passwords are stored. Flags `✗` if `config.json`
  itself contains passwords (pre-migration state).
- **Path Portability** — checks `snapshot_dir`, `log_file`,
  `snapshot_dir_overrides`, and `volume_backup` path fields. Reports `✓` for
  portable `~/...` paths that exist, `!` for absolute NAS paths (expected but
  not portable), and `✗` for any configured path that does not exist on disk.
- **Permissions** — checks `~/.update_zen/` (0700), `config.json` (0644),
  `credentials.json` (0600), `update_zen.log` (0600).
- **Snapshot Directories** — checks the global snapshot dir and any
  per-container override dirs. Shows snapshot counts per container. Reports `✗`
  for missing override dirs (rollback unavailable).
- **Encryption** — for each container in `encrypt_containers`: reports whether
  saved credentials are present or will be prompted at runtime.
- **Legacy Snapshots** — scans all configured snapshot directories for remaining
  old-format `.json` snapshot files. When found, prints a per-container count and
  prompts the user to run `update_zen convert-snapshots`. Does not set exit code
  to 1 — legacy snapshots should be migrated but do not block operation.
- **Orphaned Artifacts** — reports any `_staging_*` directories and `*.tmp`
  encryption leftovers found across all configured snapshot directories. Does not
  set exit code to 1 — orphans are a space leak, not a config error. Run
  `update_zen cleanup` to remove them.

**Exit code:** 0 on a clean config. 1 if any `✗` finding exists (for scripting).

---

### `update_zen tags <container>`

Lists all available image tags for the container's image, sorted alphabetically.
Marks the currently-running tag with `← current`.

Current tag identification uses two strategies in order:
1. Read the `org.opencontainers.image.version` OCI label from the local image — zero registry calls if present.
2. Parallel digest comparison: fetch remote digests for all tags (up to 10 concurrent workers) and compare against the local `RepoDigests` entry; short-circuits on first match.

### `update_zen update <container> [flags]`

Pulls the latest image and recreates the named container using the full
`Engine.update()` sequence. Auto-rollback on health check failure is on by
default.

**Flags:**
- `--no-auto-rollback` — leave the broken container in place for inspection instead of rolling back
- `--compose` — update via `docker compose up --force-recreate` (`Engine.compose_update()`); required for Gluetun-routed stacks; ignores `--tag`
- `--tag <tag>` — pull and deploy a specific image tag instead of the current one; ignored when `--compose` is used

Exits 0 on success, 1 on failure.

### `update_zen rollback <container> [--snap N]`

Recreates a container from a saved snapshot using `Engine.rollback()`.

- `--snap N` (1, 2, or 3) — rolls back immediately to that snapshot (see Bug 4 for the `max_snapshots > 3` limitation)
- Without `--snap` — prints the numbered snapshot list and prompts interactively:

```
Available snapshots for nginx:
  [1]  2026-05-12 14:30  nginx@sha256:abc123...
  [2]  2026-05-10 09:15  nginx@sha256:def456...
Roll back to [1-2]:
```

Exits 0 on success, 1 on failure. `Ctrl+C` or `EOF` prints `"Aborted."` and
exits 1.

### `update_zen snapshot <container>`

Takes a full snapshot of a running container without pulling a new image or
recreating it. Equivalent to the snapshot action in the TUI Snapshots submenu.

Runs the same capture sequence as the pre-update phase of `update_zen update`:

1. `docker inspect <container>` → write inspect JSON to staging dir
2. Capture compose sidecar (`_compose.yaml`) and env overrides (`_env.env`)
   if applicable
3. `docker save` pre-existing image layers to `_image.tar` in staging (if image
   export is enabled for this container)
4. Pause the container (if `pause_for_backup` enabled), run `_backup_volumes()`,
   then unpause unconditionally via `try/finally`
5. `SnapshotManager.finalize()` — bundle staging → `{timestamp}.tar.gz`,
   trigger `_rotate()`

All steps after inspect are non-fatal: a failed image export or volume backup
logs a warning and the snapshot is still finalized. Exits 0 on success, 1 if the
initial inspect fails.

Useful for taking a manual checkpoint before a risky config change without
triggering a full update.

### `update_zen list-snaps <container>`

Lists saved snapshots for a container in numbered order (newest first):
```
  [1]  2026-05-12 14:30  nginx@sha256:abc123...
  [2]  2026-05-10 09:15  nginx@sha256:def456...
```
Prints `"No snapshots for <container>"` if none exist.

### `update_zen restore-volume <container> [snapshot_id]`

Standalone command to restore a single volume mount from a saved snapshot
archive. Unlike `rollback`, this command only restores data — it does not
recreate the container.

- Without `snapshot_id` — presents a numbered snapshot picker, then shows a
  combined table of all mounts from the selected snapshot's volume index
  (both successfully archived mounts and skipped mounts with reasons).
- With `snapshot_id` — skips the snapshot picker.

For each archived mount with a known archive path: offers restore-in-place or
browse to a custom location. For archived mounts whose archive is missing, or
skipped mounts: opens `_browse_path` so the user can locate the file manually.

Warns before overwriting data on a running container. Non-interactive path
lookup checks the recorded `archive_dir` first, then falls back to
`snapshot_dir_for(container)` for archives that have been moved.

### `update_zen image-export <status|enable|disable> [<container>]`

Manages per-container and global image export opt-outs.

- `status` — shows global `image_export_enabled` toggle and the `image_export_disabled` list
- `enable [container]` — with a container name: removes it from `image_export_disabled`; without: sets global `image_export_enabled = True`
- `disable [container]` — with a container name: adds it to `image_export_disabled`; without: sets global `image_export_enabled = False`

### `update_zen cron [<subcommand>]`

Manages scheduled job recipes. `config.json` is the **source of truth**; the
actual crontab is **derived state**. Every write operation updates `config.json`
first, then immediately syncs to the crontab. On a new server, a single
`update_zen cron apply` replays the full desired state into a fresh crontab.

**Design: marker-bracketed crontab entries**

Each managed crontab block is wrapped in `BEGIN`/`END` comment markers that
include the container name and recipe name:

```
# BEGIN update_zen:sonarr:nightly_update
0 3 * * * update_zen update sonarr >> ~/.update_zen/update_zen.log 2>&1
# END update_zen:sonarr:nightly_update
```

`_crontab_inject` calls `_crontab_remove` first, then appends — making all
apply operations idempotent. Output is redirected to `config.log_file` so cron
runs are not lost to the local mail spool.

All `crontab` calls pass `-u $SUDO_USER` (resolved to `_CRON_USER` at module
load from `SUDO_USER` → `USER` → `"root"`), so entries land in the invoking
user's crontab, not root's.

**Per-mount job markers**

The `mount_volume_backup` recipe lets a single container have multiple
per-mount backup jobs in the same crontab. Each job's `BEGIN`/`END` markers
include the mount path so they can coexist without overwriting each other:

```
# BEGIN update_zen:sonarr:mount_volume_backup:config
0 1 * * * update_zen volumes backup sonarr --mount /config >> ... 2>&1
# END update_zen:sonarr:mount_volume_backup:config
```

`_cron_job_marker(job)` generates this key: plain `recipe_name` for all
standard recipes, `recipe_name:{sanitized_mount}` for `mount_volume_backup`.
`_cron_apply`, `_cron_status`, and drift detection all route through this
helper, so per-mount jobs behave identically to regular jobs for `apply`,
`status`, `enable`, and `disable`.

**Available recipes:**

| Recipe | Default schedule | Description |
|---|---|---|
| `nightly_update` | `0 3 * * *` | Pull latest image and recreate the container nightly |
| `weekly_update` | `0 3 * * 0` | Pull latest image and recreate the container (Sundays at 3 am) |
| `daily_check` | `0 8 * * *` | Log whether a newer image is available (daily at 8 am) |
| `weekly_check` | `0 8 * * 1` | Log whether a newer image is available (Mondays at 8 am) |
| `hourly_snapshot` | `0 * * * *` | Standalone snapshot every hour |
| `daily_snapshot` | `0 2 * * *` | Standalone snapshot daily at 2 am |
| `weekly_snapshot` | `0 2 * * 0` | Standalone snapshot Sundays at 2 am |
| `monthly_snapshot` | `0 2 1 * *` | Standalone snapshot 1st of month at 2 am |
| `hourly_volume_backup` | `0 * * * *` | Volume backup every hour |
| `daily_volume_backup` | `0 1 * * *` | Volume backup daily at 1 am |
| `weekly_volume_backup` | `0 1 * * 0` | Volume backup Sundays at 1 am |
| `monthly_volume_backup` | `0 1 1 * *` | Volume backup 1st of month at 1 am |
| `mount_volume_backup` | `0 1 * * *` | Volume backup for a single mount (requires `--mount PATH`) |

**Subcommands:**

`update_zen cron status` (default when no subcommand given)

Prints a table of all configured jobs:

```
CONTAINER   RECIPE           SCHEDULE    ENABLED  APPLIED
sonarr      nightly_update   0 3 * * *   yes      yes
radarr      weekly_check     0 8 * * 1   yes      NO (drift)
```

`APPLIED` is `yes` when the `BEGIN` marker is present in the actual crontab,
`NO (drift)` when the job is enabled in config but the marker is absent. A
`! Drift detected — run 'update_zen cron apply' to fix.` footer is appended
when any drift is found. Drift is surfaced but never silently auto-corrected.

---

`update_zen cron apply [<container>]`

Syncs `config.json` → crontab for all containers, or for one container if
`<container>` is given. Idempotent: reads the current crontab, removes any
managed blocks that should change, appends updated blocks, and writes only if
the content would actually change. Prints each change made or `"Nothing to
apply."` if already in sync.

---

`update_zen cron recipes`

Lists all available recipe templates with their label, description, default
schedule, and command template. Use this to discover recipe names before calling
`cron add`.

---

`update_zen cron add <container> <recipe> [--schedule CRON] [--mount PATH]`

Adds a scheduled job for `<container>` using the named `<recipe>`. Rejects
unknown recipe names (exits 1, lists valid names).

Duplicate handling differs by recipe type:
- **Standard recipes** — one job per recipe per container; use `cron enable` to
  re-activate a disabled job instead of adding a new one.
- **`mount_volume_backup`** — multiple jobs can coexist for the same container,
  one per distinct mount path. The `--mount PATH` flag is **required** for this
  recipe; the command exits 1 without it. Duplicate recipe+mount pairs are
  rejected.

**Flags:**
- `--schedule CRON` — override the recipe's default schedule with a custom
  5-field cron expression (e.g. `"0 4 * * *"`). Validated by
  `_cron_validate_schedule` before saving. If omitted, the recipe's default
  schedule is used.
- `--mount PATH` — container mount path for `mount_volume_backup` (e.g.
  `/config`). Required for that recipe; ignored for all others.

Saves to `config.json`, then calls `_cron_apply` immediately. Exits 1 if the
crontab write fails (config is already saved; run `cron apply` to retry).

---

`update_zen cron remove <container> <recipe>`

Removes the job from both the crontab and `config.json`. Unlike other write
operations, `remove` strips the crontab entry directly (via `_crontab_remove` +
`_crontab_write`) before removing from config — it cannot use `_cron_apply`
because the job is already gone from config at that point. Exits 1 if the named
job is not found for the container.

---

`update_zen cron enable <container> <recipe>`

Sets `enabled: true` in config, saves, and calls `_cron_apply` to inject the
crontab entry. No-ops if the job is already enabled. Exits 1 if the job is not
found (use `cron add` first).

---

`update_zen cron disable <container> <recipe>`

Sets `enabled: false` in config, saves, and calls `_cron_apply` to remove the
crontab entry. The job remains visible in `cron status` with `ENABLED: no`.
No-ops if the job is already disabled.

---

### `update_zen encrypt [<subcommand>]`

Manages snapshot and volume archive encryption. Uses AES-256-GCM with a
per-file random salt and scrypt KDF. Encryption is configured per-container.

**Subcommands:**

`update_zen encrypt status`

Shows which containers are in `encrypt_containers`, whether saved credentials
are present for each, and the current password prompt mode.

---

`update_zen encrypt setup`

Adds a container to `encrypt_containers` and configures the password prompt
mode (`session`, `always`, or `saved`). Optionally saves the password to
`credentials.json` during setup.

---

`update_zen encrypt remove`

Removes a container from `encrypt_containers`. Does not decrypt existing
archives — use `encrypt disable --container` to decrypt before removing.

---

`update_zen encrypt rotate --container <name> [--include-archives] [--mode MODE]`

Changes the encryption password for a container, re-keying all its snapshot
bundles.

For each main `.tar.gz` bundle: text members (`.json`, `.yaml`, `.env`) are
decrypted with the old password and re-encrypted with the new one; binary
members (`_image.tar` etc.) are copied unchanged. A `.rekey_tmp` temporary file
is written alongside the bundle and renamed into place atomically on success.

**Flags:**
- `--include-archives` — also re-key per-mount RBPE volume archives. Without
  this flag, volume archives are left with the old password and a note is
  printed. Use when volume archives are also encrypted.
- `--mode session|every_time` — change the password prompt mode at the same time
  the key rotation completes. Optional.

If the container has a saved password entry in `credentials.json`, it is updated
to the new password automatically on success.

---

`update_zen encrypt disable --container <name>`

Decrypts all snapshot bundles and volume archives for a container, then removes
it from `encrypt_containers` and `encrypt_volumes` and purges its saved password
entry from `credentials.json`.

For each main bundle: text members are decrypted to plaintext; binary members
are copied unchanged. For each per-mount RBPE volume archive: decrypts in-place
via paired temp files with `finally` cleanup. All config changes are saved only
after all files are successfully decrypted.

---

### `update_zen volumes`

Shows a table of all running containers with bind-mount count and a one-line
summary of volume backup rules.

Output table: `CONTAINER | MOUNTS | BACKUP RULES`

### `update_zen volumes show <container>`

Shows each bind mount for a container with its host path, container path, and
current backup status (`backed up`, `skipped`, `skipped (not in whitelist)`,
`disabled`). Also prints exclude patterns and any global or per-container
disabled state.

### `update_zen volumes set <container> [flags]`

Modifies volume backup rules for a container. All flags are additive/removable
within a single invocation.

**Flags:**
- `--skip PATH` — add a container path to `skip_mounts` (repeatable)
- `--unskip PATH` — remove a container path from `skip_mounts`
- `--only PATH` — replace `include_only_mounts` with these paths (repeatable)
- `--no-only` — clear `include_only_mounts` so all mounts are backed up
- `--exclude PATTERN` — add a glob pattern to `exclude` (repeatable)
- `--no-exclude PATTERN` — remove a glob pattern from `exclude`
- `--disable` — disable volume backup for this container
- `--enable` — re-enable volume backup for this container
- `--reset` — remove all backup rules for this container

### `update_zen volumes backup <container> [--mount PATH]`

Backs up a container's volumes without stopping, updating, or snapshotting the
container. Intended for cron-scheduled volume checkpoints and on-demand backups.

Sequence:
1. `docker inspect <container>` — get mount list
2. Pause the container if `pause_for_backup` is enabled (non-fatal: continues
   live on failure)
3. `Engine._backup_volumes()` — archive eligible bind mounts and named volumes to
   per-mount `{timestamp}_{mount}.tar.gz` files in the container's snapshot dir,
   applying the container's `volume_backup` filtering rules
4. Unpause unconditionally via `try/finally`
5. Print `Done: N archived, N skipped.`

Archives are written alongside any existing snapshot bundles and use the same
naming scheme. They are **not** bundled into a main `.tar.gz` and are **not**
tracked by snapshot rotation — they accumulate until removed manually or by
`update_zen cleanup`.

**Flags:**
- `--mount PATH` — back up only this container mount path (by container path,
  e.g. `/config`); all other mounts are skipped. Without this flag, all eligible
  mounts are backed up.

Exits 0 on success, 1 if the initial inspect fails.

### `update_zen config`

Opens `config.json` in an editor with a validate-before-commit loop. Editor
discovery order: `$VISUAL` → `$EDITOR` → `nano` → `vi` (first found via
`shutil.which`).

**Validate-before-commit loop:**

1. Write a temp `.json.bak` backup of the current file (reflects last good state).
2. Open the editor via `subprocess.run` — process returns after the user saves
   and exits.
3. Call `Config.load()` as the validation oracle. On success: delete the backup
   and exit.
4. On failure: print the parse or type error and offer three choices:
   - `r` — re-open the editor (returns to step 2)
   - `b` — restore from the backup (reverts to last good state and exits)
   - `q` — quit without restoring (broken file stays on disk)
5. The temp backup is deleted unconditionally in `finally`.

Non-zero editor exit codes are not treated as errors — `vim` exits non-zero on
`:cq` but the file may still be valid; the validator decides, not the exit code.

The config path follows the `--config` flag, then `UPDATE_ZEN_CONFIG` env var,
then `~/.update_zen/config.json`.

### `update_zen cleanup [--yes] [--container NAME]`

Finds and removes orphaned artifacts left by interrupted operations across all
configured snapshot directories.

**What it finds:**

- **Staging directories** (`_staging_{timestamp}/` inside container snapshot dirs)
  — created by `SnapshotManager.save()` and normally bundled and deleted by
  `finalize()`. If the process is killed mid-update, the staging dir remains; for
  updates with image export enabled it may hold several GB.
- **Encryption temp files** (`*.tmp` inside container snapshot dirs) — created
  during volume archive encryption; the original `.tar.gz` is renamed to
  `.archive.tar.tmp` and encrypted to the original path. If interrupted, the
  `.tmp` remains and the destination may be absent or partial.

**Dry run (default):** prints a table of orphaned items with container, type,
size, and path, then exits. No deletion occurs.

```
Orphaned artifacts — 2 items, 4.3 GB total:

CONTAINER   TYPE     SIZE     PATH
sonarr      staging  4.2 GB   /mnt/nas/sonarr/_staging_2026-06-01T03-14-22
radarr      tmp      87.4 MB  /mnt/nas/radarr/2026-06-01T04-00-01_data.tar.tmp

Run with --yes to delete.
```

**Flags:**
- `--yes` — show the table, then prompt `[y/N]` before deleting. Partial
  failures are logged individually and do not abort the run.
- `--container NAME` — scope the scan to one container's directories only.

Also accessible from the Maintenance submenu in interactive settings, which shows
a live `clean` or `N orphaned artifacts found` summary line and allows inline
deletion with the same `[y/N]` prompt.

### `update_zen convert-snapshots [--container NAME] [--dry-run]`

Migrates old-format snapshots (loose `.json` + sidecar files) to new-format
`.tar.gz` bundles. Run this if any `.json` snapshots remain from a version
predating the archive simplification.

**Conversion sequence per snapshot:**

1. Create `_staging_{snapshot_id}/` inside the container snapshot dir
2. Copy the inspect `.json` as raw bytes into staging
3. Translate `_ext.json` (old volume index schema) → `_volumes.json` (current
   schema) during staging — all other fields are preserved
4. Copy all other sidecars (`_compose.yaml`, `_env.env`, `_image.tar`,
   `_version.json`) as raw bytes — no decrypt/re-encrypt cycle, so any RBPE
   encryption is preserved transparently
5. Delete the original `.json` and all its sidecars **before** calling
   `sm.finalize()` — deletion-first prevents `sm.list()` from counting both
   formats simultaneously and triggering incorrect rotation
6. `sm.finalize()` — bundle staging → `{snapshot_id}.tar.gz`, trigger `_rotate()`

**Flags:**
- `--container NAME` — limit the scan to one container; without it, all
  containers across all configured snapshot directories are processed
- `--dry-run` — print what would be converted without touching any files

Exits 0. Prints `"No legacy .json snapshots found."` (with container scope note
if `--container` was used) when nothing needs conversion.

`update_zen doctor` detects any remaining `.json` snapshots and prompts to
run this command when found.

### `update_zen install`

Writes `/usr/local/bin/update_zen` as a bash wrapper that auto-elevates to
root, then adds a NOPASSWD sudoers rule at `/etc/sudoers.d/update_zen` for
the invoking user. After install, `update_zen` can be typed without `python3`
or a sudo password prompt. Must be run as a normal user (not directly as root)
for the NOPASSWD rule to be attributed correctly.

### Interactive Mode: File Manager (`f` key)

Pressing `f` from the main container list opens `_interactive_file_manager`, a
three-option menu for managing config files and navigating the filesystem.

**Option 1 — Backup config**

Calls `_backup_config`. If `credentials.json` exists, the user is asked whether
to include it before the destination picker. The archive is a timestamped
`.tar.gz` (e.g. `config_backup_2026-06-04T14-22-07.tar.gz`). An optional RBPE
v2 encryption step produces a `.tar.gz.rbpe` sidecar and deletes the plain tar.
Both the plain and encrypted paths are written `0600`.

Including credentials is useful for a full machine restore. Omitting them
produces a portable archive safe for cloud sync or version control.

**Option 2 — Restore config backup**

Calls `_restore_config`. Browses for a `.tar.gz` or `.tar.gz.rbpe` file. RBPE
files are decrypted to a temporary path (`tempfile.mkstemp`) with a `try/finally`
guarantee of cleanup. The archive is inspected for `config.json` membership
before extraction — the user cannot accidentally extract an unrelated tar. The
user chooses to overwrite the live config paths or extract to a different folder.
Only known members (`config.json`, `credentials.json`) are written. When
overwriting live, `Config.load()` is called and the refreshed object is returned
to `cmd_interactive` immediately.

**Option 3 — File browser**

Opens a `_browse_path` loop starting at `/`. Selecting a file opens
`_file_action_menu(path)`, a looping sub-menu with three actions:

- **Delete** — confirms, unlinks the file, exits sub-menu
- **Move / rename** — browses for destination dir, optional rename, confirms,
  `shutil.move`
- **Change permissions** — four presets (`0600`/`0644`/`0755`/`0400`) or custom
  octal; loops so further changes can be made

The browser stays open after each action. Returning from `_file_action_menu`
reopens `_browse_path` at the parent of the selected file rather than at the
original menu root — the browser position is preserved. Press `0` in the file
action menu to return to the browser; press `q` in the browser to exit the file
manager.

**Inline browser keys (available everywhere)**

Three keys are available inside `_browse_path` from every call site — not just the
file manager, but also snapshot folder browsing, archive folder browsing, and all
path-picker dialogs in the TUI:

- `m` — creates a subdirectory in the current location (prompts for name,
  validates, `mkdir(0o700)`, navigates in)
- `p` — sets permissions on the current directory (four directory presets:
  `0700`/`0750`/`0755`/`0777`, plus custom octal; directory-appropriate modes
  only — file-mode presets like `0600` are excluded)
- `d` — deletes the directory currently being browsed; prints a content summary
  (`N files, M subfolders` or `empty folder`) before asking; requires typing the
  full word `yes` as a friction guard against accidental recursive deletes; blocks
  deletion of `/`; uses `shutil.rmtree` (handles non-empty directories); on
  success navigates to parent, on `OSError` stays in place

**Other `f` key entry points**

The file browser is also reachable from two other menus without going through the
file manager:

- **Action menu `f`** — opens `_browse_path` pre-positioned at the container's
  snapshot directory; `_file_action_menu` on file selection.
- **Volumes menu `f`** — opens `_browse_path` pre-positioned at the container's
  volume archive base directory (respects `save_path` override).
- **Mount action menu last option** — opens `_browse_path` at the per-mount
  archive directory (respects `mount_paths`, then `save_path`, then snapshot dir).

Browse position preservation applies at all three call sites above and in the
file manager: returning from `_file_action_menu` always resumes at the parent of
the file that was selected, not back at the original root.

---

### Interactive Mode: Container Action Menu

Selecting a container from the home screen opens the per-container action menu.
The menu is **two-level**: first choose a category key, then choose an action
within that category. Press `0` from any submenu to return to the category menu;
press `0` from the category menu to return to the container list.

**Category dispatcher (`u/s/v/x/i/c`):**

| Key | Category | Submenu function |
|---|---|---|
| `u` | Updates & Rollback | `_updates_menu()` |
| `s` | Snapshots | `_snapshots_menu()` |
| `v` | Volumes | `_interactive_volumes_menu()` |
| `x` | Container Control | `_container_control_menu()` |
| `i` | Info | `_info_menu()` |
| `c` | Configure | `_container_config_menu()` |

---

**`u` — Updates & Rollback** (`_updates_menu`)

| Key | Action |
|---|---|
| `1` | `Engine.update()` — full pull + recreate with health check and auto-rollback |
| `2` | `_interactive_snapshot_list(rollback_mode=True)` → `Engine.rollback()` |
| `3` | `Engine.compose_update()` — required for Gluetun-routed stacks |
| `4` | `_interactive_version_select()` — pick and deploy a specific tag |
| `5` | `RegistryClient.has_update()` — display-only update check |

---

**`s` — Snapshots** (`_snapshots_menu`)

| Key | Action |
|---|---|
| `l` | `_interactive_snapshot_list(rollback_mode=False)` — browse snapshots |
| `n` | `Engine.snapshot()` — take a new snapshot now without pulling or recreating |
| `p` | `sm._rotate()` — prune beyond limit immediately (confirm prompt) |
| `d` | Set or clear snapshot dir override for this container (`_browse_path`) |
| `k` | Set or clear per-container `max_snapshots` limit override |
| `m` | `_interactive_container_chmod()` — pick or clear a permission profile |
| `f` | Open `_browse_path` at this container's snapshot directory |

---

**`v` — Volumes** (`_interactive_volumes_menu`)

Opens the per-container mount list. Per-mount actions are accessible by selecting
a mount number. Top-level keys:

| Key | Action |
|---|---|
| `e` | `_interactive_volume_encryption_menu()` — `1-N` toggle per mount, `a=all`, `n=none` |
| `x` | `_interactive_exclude_patterns()` — edit glob exclude patterns |
| `d` | Set or clear default volume save path (`_browse_path`) |
| `t` | Toggle volume backup enabled/disabled for this container |
| `r` | Reset all volume backup rules (confirm prompt) |
| `b` | Backup all volumes now (no image pull or container recreate) |
| `f` | Browse archive folder (`_browse_path` at volume archive base dir) |

---

**`x` — Container Control** (`_container_control_menu`)

Direct container state operations. All prompt for confirmation.

| Key | Action |
|---|---|
| `r` | Restart — `docker stop` + `docker start` |
| `p` | Pause / Unpause — label renders the correct action based on current state |
| `s` | Stop — `docker stop` |
| `a` | Start — `docker start` |
| `f` | Force recreate — stop → remove → `to_spec(pin_digest=False)` → `docker run`; no image pull |
| `k` | Kill — `docker kill` (`SIGKILL`); for containers frozen or unresponsive to `stop` |

---

**`i` — Info** (`_info_menu`)

| Key | Action |
|---|---|
| `d` | Container details — formatted inspect summary: ID, status/uptime, image, digest, restart policy, mem/CPU limits, networks, ports, mounts |
| `l` | Logs — `docker.logs()`, merged stdout+stderr, last 100 lines |
| `t` | Stats — `docker.stats()` one-shot: CPU %, memory, net I/O, block I/O, PIDs |

---

**`c` — Configure** (`_container_config_menu`)

| Key | Action |
|---|---|
| `e` | Toggle `encrypt_containers` for this container |
| `k`* | `_interactive_password_menu()` — manage saved password (* only shown when encryption is on) |
| `g` | `_interactive_registries_menu()` — view, add, select, remove registry sources |
| `p` | Set or clear pinned tag |
| `b` | `_backup_toggles_menu()` — pause-for-backup, env backup, image export (per-container) |
| `a` | Toggle `auto_rollback_disabled` for this container |
| `j` | `_interactive_cron_menu()` — add/edit/delete scheduled jobs for this container |
| `d` | Detach / Re-attach from update_zen |

---

### Interactive Mode: Settings Menu

Press `s` from the home screen to open the settings menu. Like the action menu,
settings is **two-level**: first choose a domain key, then act within that domain.
Press `0` from any submenu to return to the domain menu; press `0` from the
domain menu to return to the home screen.

**Domain dispatcher (`s/v/a/e/j/d/c/m`):**

| Key | Domain | Submenu function |
|---|---|---|
| `s` | Snapshots | `_settings_snapshots_menu()` |
| `v` | Volumes | `_settings_volumes_menu()` |
| `a` | Auto-rollback | immediate toggle — no submenu |
| `e` | Encryption | `_interactive_encryption_menu()` |
| `j` | Jobs | `_interactive_cron_overview()` |
| `d` | Display | `_settings_display_menu()` |
| `c` | Config files | `_settings_config_files_menu()` |
| `m` | Maintenance | `_settings_maintenance_menu()` |

---

**`s` — Snapshots** (`_settings_snapshots_menu`)

| Option | Action |
|---|---|
| `1` | Global snapshot directory (`_browse_path` → `config.snapshot_dir`) |
| `2` | Global rotation limit (prompt → `config.max_snapshots`) |
| `3` | Snapshot permissions (`_interactive_global_chmod` + optional retroactive sweep) |
| `4` | Toggle `image_export_enabled` globally |

---

**`v` — Volumes** (`_settings_volumes_menu`)

| Option | Action |
|---|---|
| `1` | Toggle `volume_backup_enabled` globally |
| `2` | Toggle `pause_for_backup` globally |

---

**`a` — Auto-rollback**

Immediate toggle of the global `auto_rollback` config field — no submenu. Per-container
overrides are managed in the container's Configure menu (`c` → `a`).

---

**`e` — Encryption** (`_interactive_encryption_menu`)

| Option | Action |
|---|---|
| `1` | `_interactive_saved_passwords_menu()` — list, add, delete, purge saved passwords |
| `2` | Password mode selector (`session` / `always` / `saved`) |
| `3` | Per-container encryption status (read-only) |

---

**`j` — Jobs** (`_interactive_cron_overview`)

Global read-only summary of all scheduled cron jobs across all containers, with
live drift detection. To add or edit jobs for a specific container, navigate to
that container → `c` → `j`.

---

**`d` — Display** (`_settings_display_menu`)

| Option | Action |
|---|---|
| `1` | `_interactive_column_menu()` — toggle individual column visibility (21 optional columns, including `SNAPSHOT PATH`) |
| `2` | Toggle `pagination_enabled` |

There is no separate fast-toggle for individual columns — the column visibility
picker is the single surface for all optional columns.

---

**`c` — Config files** (`_settings_config_files_menu`)

| Option | Action |
|---|---|
| `1` | Switch to a different config file (live reload; returns immediately on switch) |
| `2` | View recent log (last 50 lines, display only) |
| `3` | Set log file path (`_browse_path(mode='dir')`) |

---

**`m` — Maintenance** (`_settings_maintenance_menu`)

| Option | Action |
|---|---|
| `1` | Cleanup orphans — scan for `_staging_*` dirs and `*.tmp` encryption leftovers; `[y/N]` delete prompt |
| `2` | Detached containers — list all containers in `config.exclude`; re-attach from here |

---

### Interactive Mode: Navigation Conventions

These key bindings are consistent across all TUI menus:

| Key | Consistent meaning | Notes |
|---|---|---|
| `0` | Go back one level | submenu → category/domain menu → home screen |
| `e` | Encryption | volumes menu, configure menu, settings |
| `j` | Jobs / schedule | configure menu, settings |
| `f` | Browse files/folder | action menu, volumes menu; pre-positions at relevant directory |
| `d` | Directory (snapshot/volumes context) or Details (info context) | unambiguous by context |

`q` exits the TUI from any menu.

---

### Interactive Mode: Container Detachment

The `config.exclude` list is presented to users as "Detach from update_zen"
throughout the TUI and in the action menu. This reflects the semantic intent
more clearly: detached containers are not monitored or touched by the tool.

Detached containers:
- Do not appear in `status` or `check` CLI output
- Do not appear in the interactive TUI home screen
- Are not available for batch updates
- Are not polled for update availability

Settings → `m` → `2` provides a global view to re-attach any detached container,
without requiring navigation to its individual config menu. The container config
key `d` (in `_container_config_menu()`) allows detaching/re-attaching from a
specific container.

---

## 7. Data Flow

### Update flow

```
update_zen update nginx
        │
        ▼
Engine.update("nginx")
  1. DockerClient.inspect("nginx")
        → docker inspect nginx
        → docker image inspect <image_id>   ← injects RepoDigests
        → returns merged dict
     Capture pre-update version info for completion summary:
        _was_tag     ← tag from Config.Image; "" when image is digest-pinned (@sha256:)
        _was_version ← _was_tag if non-empty and non-"latest", else OCI version label
        _was_hash    ← first 12 hex chars of RepoDigests[0] sha256 (empty if absent)

  2. SnapshotManager.save("nginx", data)
        → creates _staging_2026-05-12T14-30-22/ in snapshot dir
        → writes 2026-05-12T14-30-22.json into staging
        → returns (json_path, staging_dir)

     _save_meta("nginx", "2026-05-12T14-30-22", data, staging_dir)
        → writes _compose.yaml into staging (if compose-managed and path resolves)
        → writes _env.env into staging (if user-set env overrides exist)

     _save_image("nginx", "2026-05-12T14-30-22", data, staging_dir)
        → docker save <image_id> -o staging/2026-05-12T14-30-22_image.tar
        → skipped if image_export_disabled for "nginx" or global toggle is False

     docker pause nginx  (if pause_for_backup enabled)
     _backup_volumes("nginx", "2026-05-12T14-30-22", data, staging_dir, paused=True)
        → applies config.volume_backup["nginx"] filtering rules
        → archives bind mounts and named volumes to per-mount .tar.gz files
        → writes _volumes.json index into staging
     docker unpause nginx  (always, even on backup failure)

     SnapshotManager.finalize("nginx", "2026-05-12T14-30-22", staging_dir)
        → bundles staging/ → 2026-05-12T14-30-22.tar.gz (compresslevel=1)
        → deletes staging/
        → _rotate() — prunes oldest snapshot if > max_snapshots

  3. Pull new image by digest (preferred path):
        RegistryClient.get_remote_digest("nginx:latest")
        → HEAD https://registry-1.docker.io/v2/library/nginx/manifests/latest
        → returns "sha256:abc123..."

        DockerClient.pull("nginx@sha256:abc123...")
        → docker pull nginx@sha256:abc123...   (streamed to terminal)

        DockerClient.tag_image("nginx@sha256:abc123...", "nginx:latest")
        → docker tag nginx@sha256:abc123... nginx:latest
        → ensures Config.Image is the clean tag, not the digest ref

        On RegistryError: falls back to docker pull nginx:latest

  4. DockerClient.stop("nginx")
  5. (stop siblings if restart_stack_siblings enabled)
  6. DockerClient.remove("nginx")
     (start gateway siblings, wait; start dependent siblings, wait)

  7. SnapshotManager.to_spec(data, pin_digest=False)
        → ContainerSpec(name="nginx", image="nginx:latest", ...)

  8. DockerClient.run(spec)
        → docker run -d --name nginx -e ... -v ... -p ... nginx:latest
        → docker network connect <extra_net> nginx   (if multiple networks)

  9. HealthChecker.wait_healthy("nginx", 300)
        → polls docker inspect every 5s
        → returns True (healthy/running) or False (unhealthy/timeout)

  9a. Success → DockerClient.inspect("nginx") again (wrapped in try/except)
        Extract _new_version, _new_tag, _new_hash using the same logic as step 1.
        _derive_version_meta(inspect_data) → {"version": "...", "digest": "sha256:..."}
        config.container_versions[container] = _snap_meta
        config.save()
        Print stdout summary:

        Updated nginx
          was: X  →  now: Y              (versions differ)
          tag: X  →  Y                  (same version, different non-latest tag)
          version: X  (same — image re-pulled)  (same version, same tag)
          sha256: ...abc123  →  ...def456     (both hashes present, differ)
          sha256: ...abc123  (digest unchanged)  (both hashes present, same)

        sha256 line omitted when either hash is empty (locally-built image or
        inspect failed). Return True.

  9b. Failure → _diagnose_bind_address(); if auto_rollback: Engine.rollback("nginx",
        snaps[0], reason="auto"); return False.
```

### Rollback flow

```
update_zen rollback nginx --snap 1
        │
        ▼
Engine.rollback("nginx", snaps[0], reason="manual")
  0. Capture current container version for post-rollback summary:
        DockerClient.inspect("nginx") → extract _cur_version, _cur_tag, _cur_hash
        Wrapped in try/except DockerError — container may already be gone (e.g.
        the auto-rollback path triggered after a failed docker run in update()).
        All three fields set to "" on failure; summary still prints the "now" side.

  1. SnapshotManager.load(snap)
        → reads and parses .json file
     Extract snapshot version info for summary (same logic as update() step 1):
        _snap_version, _snap_tag, _snap_hash from the snapshot's inspect JSON
  1a. SnapshotManager.load_version(snap)
        → load version metadata from snapshot bundle; fallback from config.container_versions if not available

  2. SnapshotManager.to_spec(data, pin_digest=True)
        → ContainerSpec(name="nginx", image="nginx@sha256:abc123...", ...)

  2b. If _image.tar member exists in snapshot bundle:
        docker load -i 2026-05-12T14-30-22_image.tar
        → failure is non-fatal; falls through to step 3

  3. DockerClient._run(["image", "inspect", "nginx@sha256:abc123..."])
        → if DockerError: DockerClient.pull("nginx@sha256:abc123...")

  4. DockerClient.stop("nginx")   (non-fatal)
  5. DockerClient.remove("nginx")
        → on DockerError: inspect to confirm gone; if already gone, continue

     _restore_volumes("nginx", snapshot, ext_overrides={})
        → reads _volumes.json from snapshot bundle
        → for named volumes: docker volume inspect / create as needed
        → extracts each per-mount archive via extractall(path="/")
        → missing archive: logs warning (non-interactive) or prompts (interactive)
        → always non-fatal — rollback continues regardless

  6. DockerClient.run(spec)
        → docker run -d --name nginx ... nginx@sha256:abc123...

  7. HealthChecker.wait_healthy("nginx", 300)

  8. Success → log rollback successful
     _derive_version_meta(inspect_data) → {"version": "...", "digest": "sha256:..."}
     config.container_versions[container] = _snap_meta
     config.save()
     Print stdout summary:

        Rolled back nginx
          was: X  →  now: Y              (versions differ)
          tag: X  →  Y                  (same version, different non-latest tag)
          version: X  (restoring same version)  (same version, same tag)
          sha256: ...abc123  →  ...def456     (both hashes present, differ)
          sha256: ...abc123  (digest unchanged)  (both hashes present, same)

        "was" fields are "?" when _cur_* is empty (container was already gone).
        sha256 line omitted when either hash is empty. Return True.
     Failure → log failed — container did not reach healthy state; return False.
```

---

## 8. Error Handling

| Failure point | Behavior |
|---|---|
| `docker` binary not found | `DockerError` raised immediately with "is Docker installed?" message |
| Container not found for inspect | `DockerError` propagates to caller with Docker's stderr |
| Registry unreachable during `check`/`status` | `RegistryError` caught in command layer; row shows `"?"`, warning logged |
| `docker pull` fails | `Engine.update()` logs error, returns False; original container still running |
| Container stop/remove fails during update | Logged; update aborted; original container may still be running |
| Container start fails after remove | Container is gone; rollback triggered unconditionally regardless of `auto_rollback` setting |
| Health check fails after update | Auto-rollback if enabled; otherwise container left for inspection |
| Rollback also fails | Logs critical error; does not loop or retry |
| Snapshot file corrupt | `SnapshotManager.list()` skips the file, logs warning; other snapshots unaffected |
| Image not found locally for rollback | Re-pulls by digest before recreating |
| `RepoDigests` empty (locally-built image) | `has_update()` returns `False`; no error (can't compare without a registry digest) |
| Volume backup fails | Error logged; update sequence continues; `.tar.gz` may be absent or incomplete |
| Volume restore archive missing | Warning logged; rollback continues with config restore only |
| Volume restore extraction fails | Error logged; rollback continues — container recreated without data restore |

The tool never retries automatically. On failure it reports state clearly and
exits non-zero. The user decides whether to retry.

---

## 9. Volume Data Backup and Restore

Volume backup and restore supports both **bind mounts** (host directories
mapped into containers) and **named Docker volumes** (`-v name:/path`). Both
types are handled transparently by the same archive machinery. Implementation
uses Python's `tarfile` module only — no external tool required.

### 9.1 Storage layout

Volume data is stored alongside the main snapshot bundle, correlated by the
same timestamp stem. Each successfully backed-up mount gets its own archive:

```
~/.update_zen/snapshots/nginx/
  2026-05-12T14-30-22.tar.gz         ← main bundle (inspect JSON + _volumes.json + ...)
  2026-05-12T14-30-22_config.tar.gz  ← per-mount archive for /config
  2026-05-12T14-30-22_data.tar.gz    ← per-mount archive for /data
```

The main bundle contains `_volumes.json` — an index of all mounts with their
archive names, locations, and reasons for skipping. The per-mount archives are
referenced from this index. All files for a snapshot are pruned together by
`_rotate()`.

### 9.2 Filtering rules

Volume backup can be configured per container in `config.volume_backup`. The
key is the container name; the value is a rules object.

```json
"volume_backup": {
  "plex": {
    "skip_mounts": ["/media", "/transcode"]
  },
  "nextcloud": {
    "include_only_mounts": ["/config"]
  },
  "sonarr": {
    "exclude": ["**/cache/**", "**/*.log"]
  }
}
```

**`skip_mounts`** — skip entire mounts by their container path. Use for large
media libraries or other data that does not need to be rolled back.

**`include_only_mounts`** — whitelist: only archive mounts whose container path
appears in this list. Everything else is skipped. Use when a container has one
config mount and multiple large data mounts.

**`include_only_mounts` and `skip_mounts` are mutually exclusive per container.**
Use one or the other, not both.

**`exclude`** — `fnmatch` glob patterns applied to individual file paths within
the mounts being archived. Use for cache directories or log files inside an
otherwise small mount.

Rules use **container paths** (not host paths) as identifiers. Container paths
are stable even if the underlying host path changes location.

### 9.3 What is always skipped

Regardless of rules, the following are never archived:

- Paths that do not exist on disk
- Unix sockets (e.g. `/var/run/docker.sock`)
- Device files and other special filesystem entries

These are detected via `Path.is_dir() / Path.is_file()` — anything that returns
`False` for both is skipped.

### 9.4 Restore behavior

`_restore_volumes()` reads the `_volumes.json` index from the snapshot bundle
and restores each archived mount independently. Archives are built with absolute `arcname` values (the full
source path), so `extractall(path="/")` restores each file to its original
location without any path manipulation.

For named Docker volumes, `_restore_volumes()` first ensures the volume exists:
runs `docker volume inspect <vol_name>` and calls `docker volume create
<vol_name>` on failure. If volume creation fails, that mount is skipped and the
restore continues.

If no archive exists for a given mount (the snapshot predates backup being
enabled, or the mount was excluded by rules), `_restore_volumes()` either
logs a warning and skips (non-interactive) or calls `_prompt_missing_volume()`
to let the user locate the archive manually (interactive / TUI). Volume restore
failures are always non-fatal — the container is recreated regardless.

---

## 10. Key Design Decisions

### Container inspect is augmented with image RepoDigests

`docker inspect <container>` does not include `RepoDigests` — that is an
image-level field. `DockerClient.inspect()` performs a second
`docker image inspect <image_id>` call and injects the result into the returned
dict. This keeps the rest of the codebase simple: callers always receive a
complete dict that includes `RepoDigests`, and `RegistryClient` and
`SnapshotManager` never need to make separate image inspect calls.

### Manifest list Accept headers listed first

The `_ACCEPT` string in `RegistryClient` lists manifest list types
(`manifest.list.v2`, `oci.image.index`) before single-manifest types. This
causes Docker Hub and other multi-arch registries to return the index digest
rather than the platform-specific manifest digest. Docker's `RepoDigests` stores
the index digest (the one that was resolved when the image was pulled), so
listing index types first ensures the remote and local digests are of the same
type and compare correctly.

### `has_update` raises RegistryError rather than returning False on failure

Early versions of `has_update` caught `RegistryError` internally and returned
`False`. This caused all registry errors (auth failure, network issue, missing
header) to be silently reported as "up to date." The current implementation lets
`RegistryError` propagate; callers (`cmd_check`, `cmd_status`) catch it, log a
visible warning, and show `"?"` in the update column.

### `pin_digest=True` for rollback, `pin_digest=False` for forward update

`SnapshotManager.to_spec()` takes a `pin_digest` flag that controls the `image`
field of the returned `ContainerSpec`. For rollback (`pin_digest=True`), the
image field is `name@sha256:...` — the exact bytes that were running at snapshot
time, regardless of what `:latest` points to now. For forward update
(`pin_digest=False`), the image field is `name:tag` so Docker resolves it to
whatever is current on the registry.

### `docker run` is built as a list, never a string

`_build_run_cmd()` builds a list of strings and passes it to `subprocess.run`
with `shell=False`. Container names, image refs, env var values, and volume
paths that contain spaces or shell metacharacters are passed as list elements
and never interpreted by a shell. This eliminates an entire class of injection
vulnerabilities.

### Stop is non-fatal in rollback

In `Engine.rollback()`, the `DockerClient.stop()` call is wrapped in a
try/except that swallows `DockerError`. The container may already be stopped
(e.g. it crashed, or rollback was triggered by a failed auto-update). Making
stop non-fatal means rollback proceeds correctly in all these cases.

### Auto-rollback after a failed start is unconditional

If `docker run` fails during `Engine.update()` (not the health check — the
actual start), the container is already removed and cannot be recovered except
by rollback. In this case `Engine.rollback()` is called unconditionally,
regardless of the `auto_rollback` flag. The `auto_rollback` flag only controls
the behavior after a *successful* start that then fails the health check.

### Volume restore is non-fatal

`_restore_volumes()` never aborts the rollback sequence, even on complete
failure. A missing archive (snapshot predates backup being enabled) or an
extraction error results in a logged warning and the rollback continues. This
ensures a config rollback always completes — restoring the container to a known
good configuration — even if the data restore cannot. The user can address data
issues manually from a known-good container state.

### Config schema migration is automatic

`Config.load()` compares the set of keys in the existing `config.json` against
the set of fields defined in the dataclass. If any fields are missing (because
the schema was extended after the file was written), the file is saved again
with the new fields added at their default values. Users never need to manually
edit config files when the schema changes.

### Sockets and device files are skipped during backup

Bind mounts sometimes include Unix sockets (e.g. `/var/run/docker.sock` mounted
into monitoring containers). Archiving a socket with `tarfile` creates a useless
entry and restoring it would be incorrect. The backup loop checks
`Path.is_dir() or Path.is_file()` before calling `tar.add()` and skips anything
that fails both checks.

### Version history is stored in three places for redundancy and fallback

The version+digest record (`{"version": "...", "digest": "sha256:..."}`) is
captured by `_derive_version_meta()` after every update, rollback, or standalone
snapshot and stored in:

1. **config.json** (`container_versions` dict) — primary storage, survives
   snapshot rotation, used as the main fallback for "was version" display in
   update/rollback summaries
2. **Snapshot bundle** (`{snapshot_id}_version.json` member inside `.tar.gz`) —
   informational sidecar, embedded in the archive for historical context
3. **Volume archives** (`_meta.json` member in each per-mount `.tar.gz`) —
   contextual metadata, tied to the mount's backup for reference

The fallback chain when displaying "was version" in summaries is: live inspect →
config → snapshot → "?".

This ensures updates/rollbacks show meaningful version transitions even when
containers use `:latest` tags without OCI labels. The config storage survives
snapshot rotation, so version history persists across the rolling snapshot window.

### "Detach" is the user-facing term; "exclude" is the internal field name

The `config.exclude` list is presented to users as "Detach from update_zen"
throughout the TUI:
- Container config menu key `d`: "Detach from update_zen" (or "Re-attach..."
  if already detached)
- Settings → `m` → `2`: "Detached containers: N detached"

This reflects the semantic intent more clearly: detached containers are not
monitored or touched by the tool. Detached containers:
- Do not appear in `status` or `check` CLI output
- Do not appear in the interactive TUI home screen
- Are not available for batch updates
- Are not polled for update availability

Settings → `m` → `2` provides a global view to re-attach any container, without
requiring navigation to its individual config menu.

### Interactive pagination is toggleable, controlled by a config field

`pagination_enabled` defaults to True. When enabled, `cmd_interactive()` splits
the container list into pages based on terminal height (`_term_lines // 4`) and
shows a "press any key for next" prompt between pages. When disabled, the full
table is displayed and the user scrolls as needed.

The toggle is managed via settings → `d` → `2` and survives session restarts in
`config.json`.

This provides flexibility: users on small terminals benefit from pagination,
while users with large screens or moderate container counts prefer a single
scrollable view.

**Page size calculation:** `max(5, _term_lines // 4)` — ensures at least 5 rows
per page even on very small terminals, and adapts to actual screen height.

### Home screen table uses a registry-driven column visibility system

The home screen container table is built dynamically from `_HOME_COLUMNS`, an
ordered list of 23 column descriptors. Each entry has an `id`, `header`, and
`always` flag. The two `always: True` columns (`#` and `CONTAINER`) cannot be
hidden. The other 21 are optional and stored in `hidden_columns`.

**Why a registry instead of per-field booleans:** a one-off boolean per
column doesn't scale. Adding 11 more optional columns would have required 11
config booleans and 11 settings options. The registry approach handles any
number of columns with a single config list and a single settings option.

**`hidden_columns` empty = show defaults, not show all:** when `hidden_columns`
is absent or empty in `config.json`, `Config.load` applies `_DEFAULT_HIDDEN_COLUMNS`
(12 IDs) rather than treating empty as "show everything". This is intentional —
showing all 21 optional columns on a fresh install is overwhelming. Empty and
absent are treated identically; only a non-empty list is taken as user intent.

**`_fetch_one_status` tuple extension:** the column system needed uptime,
restarts, ports, network, and compose project data. Rather than adding new
`docker inspect` calls, these five fields were extracted from the existing
inspect dict that `_fetch_one_status` already fetched. The return tuple was
extended from 9 to 14 elements. All 6 destructuring sites use `*_` extended
unpacking (`name, health, ..., mounts, *_ = status`) so adding tail elements
is a one-character change per site.

### Snapshot file permissions are configurable via named profiles

Prior to commit `4314813`, all snapshot and volume archive files were created
with hardcoded `0700` (dirs) / `0600` (files) modes. These modes are now
configurable through named **permission profiles**:

| Profile | Dirs | Files | Use case |
|---|---|---|---|
| Secure | `0700` | `0600` | Owner only — default; matches pre-existing behaviour |
| Group | `0750` | `0640` | Owner + group read; useful when snapshot dirs are on a shared NAS |
| Shared | `0755` | `0644` | World-readable |
| Custom | user-entered | user-entered | Any valid octal, dirs and files specified separately |

Three surfaces expose this:

- **Settings → `s` → `3`** (`_interactive_global_chmod`) — picks a global profile,
  writes `snapshot_dir_mode`/`snapshot_file_mode` to config, and optionally
  applies the mode retroactively to all existing snapshot files. When
  per-container overrides exist, the sweep can be scoped to skip those
  containers.

- **Container config menu `m` key** (`_interactive_container_chmod`) — applies a
  profile to one container's snapshot directories and saves the choice to
  `snapshot_permission_overrides[container]`. The menu header tags the active
  source as `[global default]` or `[container override]` on each visit.

All write-time chmod calls in `SnapshotManager` and `Engine._backup_volumes` /
`Engine._save_image` route through `Config.snapshot_dir_mode_for(container)` and
`Config.snapshot_file_mode_for(container)` — the two resolution points that check
per-container overrides first, then fall back to the global config fields.
Config backup files, `config.json`, `credentials.json`, and the log file remain
hardcoded at `0600` and are not affected by profile changes.

### Interactive menu input handling separates table display from prompt loop

The main `cmd_interactive()` loop was refactored to decouple the full-table
fetch-and-display from the input prompt. This separation achieves two goals:

1. **Avoid redrawing on invalid input:** When the user presses Enter with no
   input or enters invalid text, the prompt reappears without redrawing the
   entire table. Only valid commands or state changes trigger a full refetch
   and redisplay.

2. **Fix the `_should_refetch` flag lifecycle:** The flag was previously being
   reset at the top of the main loop before being read, making it impossible
   for any operation (reload, detach, re-attach) to actually trigger a refetch.
   The flag is now initialized before the loop and reset only after a successful
   fetch, preserving its state across iterations.

**Architecture:**
```
Outer loop (main while True):
  - Fetch data (if first iteration or _should_refetch)
  - Display table
  - Reset _should_refetch
  
  Inner loop (input while True):
    - Prompt for input
    - If invalid → continue inner loop (no redraw)
    - If valid → handle command, break inner loop
  
  If command requires state change → set _should_refetch
  Back to outer loop
```

---

## 11. Cloud Sync & Disaster Recovery

### 11.1 Cloud sync setup

`config.json` is stored at `0600` (owner-read/write only). `saved_passwords` is
always `{}` on disk — real passwords live only in `credentials.json`, which stays
local and is never synced.

To sync `config.json`, your sync tool must run as the same user who owns the file,
or you must copy it manually. Do not relax the file permissions to accommodate a
sync daemon running as a different user.

```
1. Run: update_zen doctor
   Confirm "config.json passwords: ✓ empty (correctly separated)".
   If passwords are still in config.json, run any update_zen command once
   to trigger the auto-migration, then re-run doctor.

2. Copy or sync ~/.update_zen/config.json using a tool that runs as your user
   (rsync, scp, rclone run as yourself, a private git repo, etc.)
   Do NOT sync credentials.json — it stays local only.

3. Optional: set UPDATE_ZEN_CONFIG=/path/to/synced/config.json
   in /etc/environment or your shell profile to point at the synced copy directly.
```

### 11.2 Machine migration

```
1. On the new machine: install update_zen, mount NAS at the same paths.

2. Copy config.json from cloud or backup.
   Place at ~/.update_zen/config.json
   (or wherever UPDATE_ZEN_CONFIG points).

3. Run: update_zen doctor
   Review the output. Missing paths show ✗. Absolute NAS paths show ! (expected).
   Edit config.json directly to fix any paths that changed on the new machine
   (e.g. NAS mount point moved from /mnt/media to /mnt/nas).

4. For each container with saved snapshots:
     update_zen rollback <container>
   Enter encryption passwords when prompted. Retrieve from your password manager.
   Re-save passwords through the TUI if you want them stored for cron runs.

5. Run: update_zen cron apply
   Restores all scheduled jobs from config.json into the new machine's crontab.
```

### 11.3 Encryption password recovery

**If you lose your encryption password:**
There is no recovery path. Encryption is AES-256-GCM with a per-file random
salt and an scrypt KDF. Without the correct password, snapshot archives cannot
be decrypted. Store encryption passwords in a password manager alongside other
infrastructure credentials.

**If you lose credentials.json:**
The app still works — it will prompt for passwords on next use. Re-enter the
correct password and re-save it through the TUI (`container menu → k → save
password`). The saved password is written to a new `credentials.json` with
`0600` permissions.

**If you lose both config.json and credentials.json:**
You can still roll back manually: locate the snapshot `.tar.gz` bundle, extract
the `{snapshot_id}.json` member, and use the raw inspect data to manually
recreate the container. This is an advanced recovery path; under normal
circumstances, keeping `config.json` in cloud sync prevents this scenario.
