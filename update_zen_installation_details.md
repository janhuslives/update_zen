# Update Zen Installation Guide

## Installation Guide for First-Time Users

### Quick Start (5 minutes)

**Prerequisites:**
- Docker CLI installed and working (`docker ps` should list containers)
- Python 3.x available on your system
- sudo access (password will be prompted once during install)

**Installation steps:**

```bash
# 1. Download the script (or copy to your server)
wget https://... -O update_zen.py
# or: scp update_zen.py user@server:~/update_zen.py

# 2. Run the install command as your normal user
python3 update_zen.py install
# You'll be prompted for your sudo password once

# 3. Verify it worked
update_zen status
```

After install, just type `update_zen` — no `python3`, no `sudo`, no password prompts. Config file is auto-created at `~/.update_zen/config.json` on first run.

---

## Installation Architecture (For Developers)

### Overview

The `install` command creates two files to enable passwordless, short-form usage:

1. **Wrapper script** at `/usr/local/bin/update_zen` — a thin bash shell that auto-elevates via `sudo`
2. **Sudoers rule** at `/etc/sudoers.d/update_zen` — grants NOPASSWD privilege for the invoking user

The two-file design ensures the tool can be called as `update_zen <args>` (from anywhere, no python invocation) and auto-elevates to root (where Docker socket access requires privilege).

### The Wrapper Script

```bash
#!/bin/bash
[ "$(id -u)" -ne 0 ] && exec sudo /usr/local/bin/update_zen "$@"
exec /usr/bin/python3 /opt/update_zen/update_zen.py "$@"
```

Two lines. The first checks if the process is already root — if not, it re-execs itself via `sudo` (targeting the wrapper, not the Python script directly). If already root, it falls through to the second line and runs the Python script with the `python3` binary and script path captured at install time (`sys.executable` and `Path(__file__).resolve()`). The script itself is not privileged; the privilege comes from the sudoers rule.

### The Sudoers Rule

Created at `/etc/sudoers.d/update_zen`:

```
your_user ALL=(ALL) NOPASSWD: /usr/local/bin/update_zen
```

- `your_user` is the invoking user (read from `SUDO_USER` environment variable)
- `NOPASSWD` allows sudo without a password prompt
- The target is the **wrapper binary**, not `python3` — sudo matches on what it's asked to run, which is the wrapper re-execing itself

### Why "Must be run as a normal user"

The sudoers rule is written for the user stored in `SUDO_USER`. If you run `python3 update_zen.py install` while already root (via `sudo su`), `SUDO_USER` is empty or unset, and the sudoers rule is skipped entirely — the install still completes and the wrapper is written, but without the NOPASSWD rule.

Running as a normal user ensures `SUDO_USER` is set correctly and the rule is written for the human user who will later invoke `update_zen` from the shell. If `SUDO_USER` is absent, `cmd_install` logs a warning (`"NOPASSWD rule not added — run install as a regular user..."`) and skips writing the sudoers file — the wrapper is still created, but subsequent `update_zen` invocations will prompt for a sudo password.

### Auto-elevation in the Python script

The `main()` function also calls `os.execvp("sudo", ...)` internally. When the wrapper elevates via sudo, this second elevation is a no-op because the process is already root. This dual-elevation design allows the script to work both ways:
- `update_zen update nginx` (via wrapper, sudo elevates)
- `python3 update_zen.py update nginx` (direct invocation, internal sudo elevates)

### File Placement

- Wrapper: `/usr/local/bin/update_zen` — on PATH, executable by all users
- Sudoers: `/etc/sudoers.d/update_zen` — read by sudo at privilege escalation time
- Main script: wherever it lived when `install` was run — the wrapper hard-codes `Path(__file__).resolve()` at install time, so it points to that path (e.g. `/opt/update_zen/update_zen.py`). The script is **not** copied to `/usr/local/bin/`.

Config, snapshots, and logs live in `~/.update_zen/` under the invoking user's home, resolved via `SUDO_USER` at runtime.

### Error Handling

The `install` command has minimal error handling. After writing the wrapper and sudoers rule it attempts:

```bash
apt-get install -y python3-cryptography
```

If `apt-get` is not found or returns a non-zero exit code, a warning is logged and install continues — encryption simply won't be available until the package is installed manually. There is no pre-flight permission check, no Python validation, and no rollback if the wrapper or sudoers write fails.
