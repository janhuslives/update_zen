# Config Field Reference

Full documentation for every `config.json` field. Update this file when adding or changing config fields.

---

## `volume_backup`

```json
"volume_backup": {
  "sonarr": {
    "save_path": "/mnt/nas/sonarr",
    "skip_mounts": ["/config/logs"],
    "include_only_mounts": null,
    "exclude": ["*.log", "cache/**"],
    "mount_paths": {
      "/app/data": "/mnt/nas/sonarr-data"
    }
  }
}
```

Archive path resolution uses a four-level hierarchy (each level falls back to the one above):
1. **Global** — `config.snapshot_dir`
2. **Per-container snapshot dir** — `config.snapshot_dir_overrides[container]`
3. **Container volume save_path** — `volume_backup[container]["save_path"]` — overrides levels 1–2 for per-mount archives only
4. **Mount** — `volume_backup[container]["mount_paths"][cp]` — overrides all above

All levels resolve to `{base}/{container}/{snapshot_id}_{mount}.tar.gz`. The helper `_resolve_archive_path(config, container, snapshot_id)` implements levels 1–3 for legacy combined-archive lookups; mount-level paths are handled inline in `_backup_volumes`.

- `save_path` — container-level archive base; CLI: `--save-path DIR` / `--no-save-path`
- `skip_mounts` — blacklist by container path
- `include_only_mounts` — whitelist; `null` = back up all; `[]` = back up nothing (distinct from null — check with `if include_only is not None`)
- `exclude` — `fnmatch` patterns applied inside each archive
- `mount_paths` — per-mount custom archive dirs; location recorded in `_volumes.json` inside the main bundle

Rules managed via `update_zen volumes set <container> [flags]` — see `cmd_volumes_set()`.

---

## `pinned_tags`

Dict mapping container name → tag string.

- `Engine.update()` deploys this tag instead of the container's current image tag. Explicit `--tag` overrides the pin but does not clear it.
- Ignored for compose updates.
- `has_update()` with a pin compares the pinned tag's remote digest against `:latest`.
- CLI: `update_zen pin <container> [tag]` / `update_zen unpin <container>`; TUI: action menu `p`, option 9.

---

## `registry_alternatives`

```json
"registry_alternatives": {
  "homepage": {
    "refs": ["ghcr.io/gethomepage/homepage:v1.12.2", "gethomepage/homepage:v1.12.2"],
    "active": "ghcr.io/gethomepage/homepage:v1.12.2"
  }
}
```

Full image references stored (not just registry hostnames) because repo paths differ across registries. `_get_active_image_ref(config, container, inspect_data)` is the single resolution point — falls back to inspect image when no entry. Ignored for compose updates. TUI: action menu `r` → `_interactive_registries_menu()`.

---

## `image_export_enabled` / `image_export_disabled`

- `image_export_enabled: bool = True` — global toggle. When True, `Engine._save_image()` runs `docker save` pre-pull. On rollback, `docker load` fires before the local-image check (enables offline restore).
- `image_export_disabled: list = []` — per-container opt-outs.
- Failed `docker save` is a logged warning only, never blocks the update. Failed `docker load` falls through to registry pull.
- CLI: `update_zen image-export status / enable [container] / disable [container]`; TUI: settings 5 (global), action menu `i` (per-container).

---

## `env_backup_disabled`

`env_backup_disabled: list = []` — per-container opt-outs for env override capture. Containers here skip the env diff in `Engine._save_meta()`. The env file is reference-only — rollback uses the full env in the JSON snapshot, so disabling has no effect on rollback correctness. TUI: action menu `f`; header shows `[no-env]` badge when disabled.

---

## `snapshot_dir_overrides`

Dict mapping container name → path string. `Config.snapshot_dir_for(container)` returns this path instead of the global `snapshot_dir`. All snapshot I/O and volume archive fallback paths route through `snapshot_dir_for()`. Also redirects volume archives unless an explicit `save_path` or `mount_paths` entry takes precedence. TUI: `_container_config_menu` keys `s` (set) and `x` (clear).

---

## `max_snapshots_overrides`

Dict mapping container name → int. `Config.max_snapshots_for(container)` returns this value when present, falling back to global `max_snapshots`. Applied by `SnapshotManager._rotate()`. TUI: `_container_config_menu` keys `n` (set) and `z` (clear); header shows `[keep:N]` badge when active.

---

## `pause_for_backup` / `pause_for_backup_disabled`

- `pause_for_backup: bool = True` — global toggle. `docker pause` fires immediately before `_backup_volumes`, `docker unpause` in `try/finally` after.
- `pause_for_backup_disabled: list = []` — per-container opt-outs.
- A failed `docker pause` is caught and logged — execution continues with a live backup.
- `_backup_volumes` logs: `"container is paused — backup will be consistent"` or `"container is live — backup may be inconsistent"`.
- TUI: settings 6 (global); `_container_config_menu` key `b` (per-container).

---

## `cron_jobs`

```json
"cron_jobs": {
  "sonarr": [
    { "recipe": "nightly_update", "schedule": "0 3 * * *", "enabled": true }
  ]
}
```

`config.json` is the source of truth; crontab is derived state. One container can hold multiple jobs; duplicate recipe+container pairs are rejected. `enabled: false` keeps the job visible but removes its crontab entry.

Each managed block is wrapped in markers:
```
# BEGIN update_zen:sonarr:nightly_update
0 3 * * * update_zen update sonarr >> ~/.update_zen/update_zen.log 2>&1
# END update_zen:sonarr:nightly_update
```

Available recipes: `nightly_update`, `weekly_update`, `daily_check`, `weekly_check`.

- All `crontab` calls pass `-u $SUDO_USER` — entries land in the invoking user's crontab, not root's.
- `_cron_apply(config, container=None)` syncs config → crontab; idempotent; only writes when content would change.
- `_cron_validate_container_name(name)` enforces `[a-zA-Z0-9][a-zA-Z0-9_.-]*` as a backstop against shell metacharacters.
- Drift (marker missing from crontab despite `enabled: true`) is surfaced in `cron status` and the TUI cron menu.
- CLI: `update_zen cron status / apply / recipes / add / remove / enable / disable`
- TUI: `_container_config_menu` key `j`; settings 11 → `_interactive_cron_overview`.

---

## `pagination_enabled`

`pagination_enabled: bool = True` — When True, container list is paginated based on terminal height with a "press any key for next" prompt. When False, entire list shown at once. The startup "press any key to continue" prompt is always shown regardless. TUI: settings 12.

---

## `container_versions`

`container_versions: dict = {}` — maps container name → `{"version": "...", "digest": "sha256:..."}`. Updated after every successful update, rollback, or snapshot. Primary fallback for "was" version display when inspect returns empty or `:latest`. Populated by `_derive_version_meta(inspect_data)`. Auto-migrated on next save. Not user-editable.

---

## `hidden_columns`

List of column IDs suppressed on the home screen table. Defaults to `_DEFAULT_HIDDEN_COLUMNS` (12 IDs), leaving 9 of 21 optional columns visible.

- Empty and absent treated identically — defaults applied in both cases in `Config.load`.
- Backward compat: if `show_snapshot_path` was `False` and `"snapshot_path"` not yet in `hidden_columns`, it is appended automatically on first load.
- TUI: settings 17 → `_interactive_column_menu`; settings 16 = fast-toggle shortcut for `"snapshot_path"`.

---

## `snapshot_dir_mode` / `snapshot_file_mode`

- `snapshot_dir_mode: int = 0o700` — mode for newly created snapshot/volume-archive directories.
- `snapshot_file_mode: int = 0o600` — mode for newly created snapshot bundles and volume archive files.
- Stored as decimal integers in JSON (`448` = `0o700`).
- `Config.snapshot_dir_mode_for(container)` and `Config.snapshot_file_mode_for(container)` check `snapshot_permission_overrides[container]` first, then fall back to globals.
- Config backup files, `config.json`, `credentials.json`, and the log file remain hardcoded at `0o600`.
- TUI: settings 15 (global + optional retroactive sweep); `_container_config_menu` key `m` (per-container).

---

## `snapshot_permission_overrides`

`snapshot_permission_overrides: dict = {}` — maps container name → `{"dir_mode": <int>, "file_mode": <int>}`. Set automatically when the user applies a permission profile via `_container_config_menu` key `m`. Cleared by "Clear override" in that menu. When the global retroactive sweep is scoped to "skip containers with overrides", containers with entries here are excluded.
