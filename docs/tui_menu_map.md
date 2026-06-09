# TUI Menu Map

Full interactive menu hierarchy for `cmd_interactive()`. Update this file after any structural TUI change.

```
cmd_interactive()  (line 8119)             ← entry point, parallel status fetch
  │                                          prompt: [1-n], u=update all, s=settings, f=files, r=reload, q=quit
  ├── u  _batch_update()  (8071)             confirm → update flagged containers sequentially
  │
  ├── f  _interactive_file_manager()  (7416)
  │     ├── 1  _backup_config()              pack config.json + optional credentials.json into timestamped .tar.gz[.rbpe]
  │     ├── 2  _restore_config()             decrypt + validate + extract; live-reloads config if overwriting active paths
  │     └── 3  file browser                  _browse_path loop; _file_action_menu on file selection
  │
  ├── [1-n] container → _action_menu()  (6547)
  │     │                                    prompt: [u/s/v/x/i/c], 0 back, q quit
  │     │
  │     ├── u  _updates_menu()  (6063)
  │     │     ├── 1  Engine.update()
  │     │     ├── 2  _interactive_snapshot_list(rollback_mode=True)   → _execute_rollback() → Engine.rollback()
  │     │     ├── 3  Engine.compose_update()
  │     │     ├── 4  _interactive_version_select()                    → Engine.update(tag=...)
  │     │     └── 5  RegistryClient.has_update()                      (display only)
  │     │
  │     ├── s  _snapshots_menu()  (6117)
  │     │     ├── l  _interactive_snapshot_list(rollback_mode=False)  (browse only)
  │     │     ├── n  Engine.snapshot()                                (new snapshot now)
  │     │     ├── p  sm._rotate()                                     (prune; confirm prompt)
  │     │     ├── d  set or clear snapshot dir override               (_browse_path; set/clear/cancel sub-prompt when override set)
  │     │     ├── k  set or clear per-container snapshot limit        (prompt; set/clear/cancel sub-prompt when override set)
  │     │     ├── m  _interactive_container_chmod()  (5825)
  │     │     └── f  browse snapshot folder                           (_browse_path at container snapshot dir; _file_action_menu on file select)
  │     │
  │     ├── v  _interactive_volumes_menu()  (5102)
  │     │     ├── [1-n] mount → _interactive_mount_action()  (4792)
  │     │     │         ├── 1    Skip / Unskip
  │     │     │         ├── 2    Whitelist add / remove / start
  │     │     │         ├── 3    Set custom save path  (or Change if already set)
  │     │     │         ├── 4*   Clear save path  (* only shown when a custom path is set)
  │     │     │         ├── 4/5  Backup this mount now  (number shifts when clear-path present)
  │     │     │         ├── 5/6  Restore this mount from archive
  │     │     │         ├── 6/7  Enable / Disable encryption for this mount
  │     │     │         └── last Browse archive folder  (_browse_path at per-mount archive dir; _file_action_menu on file select)
  │     │     ├── e → _interactive_volume_encryption_menu()  (5008)   (1-N toggle, a=all, n=none)
  │     │     ├── x → _interactive_exclude_patterns()  (4732)
  │     │     ├── d → set or clear default volume save path           (_browse_path; set/clear/cancel sub-prompt when path set)
  │     │     ├── t → toggle volume backup enabled/disabled for this container
  │     │     ├── r → reset all volume backup rules                   (confirm prompt)
  │     │     ├── b → backup all volumes now                          (Engine._backup_volumes, no image pull/recreate)
  │     │     └── f → browse archive folder                           (_browse_path at volume archive base dir; _file_action_menu on file select)
  │     │
  │     ├── x  _container_control_menu()  (6258)
  │     │     ├── r  docker.stop() + docker.start()                   (restart)
  │     │     ├── p  docker.pause() / docker.unpause()                (label flips based on current health)
  │     │     ├── s  docker.stop()
  │     │     ├── a  docker.start()
  │     │     ├── f  force recreate                                   (stop → rm → run from current spec via to_spec(pin_digest=False); no pull; confirm)
  │     │     └── k  docker.kill()                                    (SIGKILL; confirmation prompt)
  │     │
  │     ├── i  _info_menu()  (6366)
  │     │     ├── d  container details                                (formatted inspect summary: ID, status/uptime, image, digest, restart policy, mem/CPU limits, networks, ports, mounts; read-only)
  │     │     ├── l  docker.logs()                                    (last 100 lines, display only)
  │     │     └── t  docker.stats()                                   (one-shot: CPU%, mem, net I/O, block I/O, PIDs; press-Enter gate)
  │     │
  │     └── c  _container_config_menu()  (5945)
  │           ├── e   toggle encrypt_containers  (this container)
  │           ├── k*  _interactive_password_menu()  (6639)            (* only shown when encryption on)
  │           ├── g   _interactive_registries_menu()  (5302)
  │           ├── p   set or clear pinned tag                         (set/clear/cancel sub-prompt when pinned)
  │           ├── b   _backup_toggles_menu()  (6485)
  │           │         ├── 1  toggle pause_for_backup  (this container)
  │           │         ├── 2  toggle env_backup_disabled  (this container)
  │           │         └── 3  toggle image_export_disabled  (this container)
  │           ├── a   toggle auto_rollback_disabled  (this container)
  │           ├── j   _interactive_cron_menu()  (5718)
  │           │         ├── [1-n] job → _interactive_cron_job_menu()
  │           │         │               ├── 1  toggle enabled/disabled + _cron_apply
  │           │         │               ├── 2  change schedule  (prompt + validate) + _cron_apply
  │           │         │               └── 3  delete job  (confirm, strip crontab, remove from config)
  │           │         └── a   _interactive_cron_add()
  │           └── d   Detach / Re-attach from update_zen             (detach: returns immediately)
  │
  └── [s] settings → _interactive_settings()  (8003)
        │                                       prompt: [s/v/a/e/j/d/c/m], 0 back, q quit
        │
        ├── s  _settings_snapshots_menu()  (7704)
        │     ├── 1  global snapshot directory                        (_browse_path → config.snapshot_dir)
        │     ├── 2  global rotation limit                            (prompt → config.max_snapshots)
        │     ├── 3  snapshot permissions                             (_interactive_global_chmod  (7463) + optional sweep)
        │     └── 4  toggle image_export_enabled
        │
        ├── v  _settings_volumes_menu()  (7761)
        │     ├── 1  toggle volume_backup_enabled
        │     └── 2  toggle pause_for_backup  (global)
        │
        ├── a  toggle auto_rollback  (global; immediate, no submenu)
        │
        ├── e  _interactive_encryption_menu()  (6813)
        │     ├── 1  _interactive_saved_passwords_menu()  (6725)      — list/add/delete/purge
        │     ├── 2  mode selector  (session / always / saved)
        │     ├── 3  per-container status  (read-only)
        │     ├── 4* legacy: disable global encryption                (* only when enabled=True v1)
        │     └── 5* legacy: rotate global password                   (* only when enabled=True v1)
        │
        ├── j  _interactive_cron_overview()  (5785)                   (global read-only job summary + apply)
        │
        ├── d  _settings_display_menu()  (7797)
        │     ├── 1  _interactive_column_menu()  (7628)               (N of 21 optional columns shown)
        │     └── 2  toggle pagination_enabled
        │
        ├── c  _settings_config_files_menu()  (7841)
        │     ├── 1  switch config file                               (load existing or create new; returns immediately on switch)
        │     ├── 2  view recent log                                  (last 50 lines, display only)
        │     └── 3  set log file path                                (_browse_path(mode='dir'))
        │
        └── m  _settings_maintenance_menu()  (7914)
              ├── 1  cleanup orphans                                  (_collect_orphans() scan; [y/N] delete prompt)
              └── 2  detached containers                              (N detached → re-attach)
```
