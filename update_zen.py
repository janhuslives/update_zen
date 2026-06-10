#!/usr/bin/env python3
_VERSION = "2026-05-19a"

_TIPS = [
    "Use 'u' in the container list to batch update multiple containers at once.",
    "You are loved.",
    "No one knows the struggles you've been through to be where you are today.",
    "Be kind, for everyone you meet is fighting a hard battle.",
    "You can restore individual volumes from past snapshots without rolling back the entire container.",
    "Set a pinned version with 'p' to deploy a specific release instead of latest.",
    "The war is not meant to be won, it is meant to be continuous.",
    "Derek Dwilson created this app and made it free. Pay it forward somehow.",
    "Pause-for-backup is on by default — containers are briefly paused during volume backup for consistency.",
    "Use snapshot overrides to store backups in different locations per container.",
    "Check encryption status in Settings → Encryption to protect your snapshots.",
    "Use 'Select version...' in a container's Updates menu to pick and deploy any available registry tag.",
    "Cron jobs can automate updates and status checks on a schedule you define.",
    "If a container fails to start after an update, rollback happens automatically. The auto-rollback setting governs health-check failures.",
    "With the measure you use - it will be measured to you.",
    "So long as men die, liberty will never perish.",
    "Named volumes are automatically backed up alongside bind mounts.",
]

_SPLASH_SISYPHUS = """\
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⡠⠤⠤⢄⡀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡤⠆⠀⡀⡀⠀⠀⠈⠁⠀⠀⠈⠤⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠖⠃⠀⠄⠂⠆⠀⠀⠀⠀⠐⠂⠒⠐⠀⢁⠐⢢⡀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠮⣀⠖⡥⠤⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠒⠚⢉⠄⢡⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣤⣶⡖⡶⠖⣢⢄⠀⠀⠀⠀⠀⡰⣁⠾⠀⢊⠁⠠⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠈⠁⢁⢸⢹⣸⠂⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣄⣰⣧⡳⣾⢟⣿⢏⠕⠃⠀⢤⡬⠄⠀⠀⠀⢠⣴⢑⠤⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⡀⠐⠂⢊⣘⣘⡸⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⢔⣁⣤⡾⡧⣴⠿⠯⠋⠋⠀⠀⠀⠀⠠⠬⡼⠀⠀⢀⣮⠫⠀⡂⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠠⠄⠄⠤⠤⠠⣥⠧⡲⡇⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠖⠋⣹⠝⡫⢕⠫⢊⡤⢊⡕⠋⢃⠀⠀⠀⠀⢀⣀⠤⠊⠁⢀⡠⢼⢽⠉⡤⠤⠄⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⠐⡂⣢⣻⡧⣑⢼⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠆⢀⣴⣈⢠⣀⢮⠓⠈⡠⠊⠀⠀⠀⠀⠉⠒⡾⠉⢁⡠⠄⠒⠊⠀⠀⡏⡧⠤⢐⢂⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠤⢨⠰⠥⡬⠘⣢⠉⠀⠀⢀⣀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠤⠒⠙⡽⠃⡠⢛⠍⠊⠁⢠⠒⠀⠀⠀⠀⠀⠀⡰⠚⠈⠉⠁⠀⠀⠀⢀⣀⡀⢾⠘⠐⠺⠤⠀⣀⡂⠈⠘⠀⡀⣘⢘⣂⡴⣘⣚⢺⢒⣖⡖⠁⣀⡰⠾⠋⠀
                    ⠀⠀⠀⠀⠀⠀⠘⠀⠀⢀⠐⠀⢠⣥⠋⢀⠔⠋⠁⠀⠀⠀⠀⠀⢠⣎⣀⡀⠠⠤⠴⠒⠒⠋⠉⠀⠀⠘⣤⠀⠻⡖⡒⢒⠀⠀⢄⠀⠁⠡⠠⢭⢤⠃⣿⣺⢾⡫⡐⠋⠁⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠒⡂⣁⣀⠴⢹⠀⢀⠂⠀⠀⠀⠀⠀⠀⠀⡰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠰⣖⡖⠐⠮⠌⡁⡓⡗⡖⣺⣴⣶⢶⢾⠛⠉⠊⠉⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠐⠉⡀⠊⡀⠀⠔⠂⣀⠜⠀⠀⠀⠀⠀⠀⢀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠱⠀⠽⠃⠖⠛⡻⣽⠿⡋⠉⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠁⡰⣡⡄⠶⠞⠋⠀⠀⠀⠀⠀⢀⣴⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⠟⠉⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠁⠉⠀⠀⠀⠀⠀⠀⠀⠀⢀⣞⠁⣠⣤⣤⡴⠶⠆⠘⢻⡿⠆⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣴⠶⡟⠏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⠉⠀⠁⠀⠀⠀⠀⠀⢀⡜⠁⠀⠀⠀⠀⠀⠀⢀⡠⠴⠿⠙⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡘⠀⠀⠀⠀⠀⠀⠀⠀⣀⠚⠀⠀⠀⠀⢀⣀⣠⡒⠙⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠞⠁⠀⠀⠀⠀⠀⠀⠀⡰⠃⠀⠀⢀⢤⠺⠉⠓⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠋⠀⠀⠀⠀⠀⠀⠀⠀⣼⡯⠿⠙⠙⠑⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠜⠀⠀⠀⠀⠀⢀⠠⢤⠚⠫⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠉⠀⠀⠀⢀⣠⡞⡋⠔⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠴⠁⠀⠀⣠⣎⢋⠵⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⡌⣒⡲⡶⠺⠑⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⢀⣄⠽⠣⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⢀⡠⣴⠭⠐⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⣤⠔⠈⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""

_SPLASH_TITLE = """\
                    ████  ████  █████                        █████
                   ▒▒███ ▒▒███ ▒▒███                        ▒▒███
 ████████   ██████  ▒███  ▒███  ▒███████   ██████    ██████  ▒███ █████           ████████  ████████   ██████
▒▒███▒▒███ ███▒▒███ ▒███  ▒███  ▒███▒▒███ ▒▒▒▒▒███  ███▒▒███ ▒███▒▒███           ▒▒███▒▒███▒▒███▒▒███ ███▒▒███
 ▒███ ▒▒▒ ▒███ ▒███ ▒███  ▒███  ▒███ ▒███  ███████ ▒███ ▒▒▒  ▒██████▒             ▒███ ▒███ ▒███ ▒▒▒ ▒███ ▒███
 ▒███     ▒███ ▒███ ▒███  ▒███  ▒███ ▒███ ███▒▒███ ▒███  ███ ▒███▒▒███            ▒███ ▒███ ▒███     ▒███ ▒███
 █████    ▒▒██████  █████ █████ ████████ ▒▒████████▒▒██████  ████ █████ █████████ ▒███████  █████    ▒▒██████
▒▒▒▒▒      ▒▒▒▒▒▒  ▒▒▒▒▒ ▒▒▒▒▒ ▒▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒  ▒▒▒▒ ▒▒▒▒▒ ▒▒▒▒▒▒▒▒▒  ▒███▒▒▒  ▒▒▒▒▒      ▒▒▒▒▒▒
                                                                                  ▒███
                                                                                  █████
                                                                                 ▒▒▒▒▒"""

import argparse
import base64
import concurrent.futures
import fnmatch
import hashlib
import io
import json
import os
import random
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
import termios
import time
import tty
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

# === PATHS ===

def _get_invoking_home() -> Path:
    # When run via sudo, use the original user's home so config, snapshots, and
    # Docker credentials are resolved from their directory rather than /root.
    sudo_user = os.environ.get("SUDO_USER")
    if sudo_user:
        try:
            import pwd
            return Path(pwd.getpwnam(sudo_user).pw_dir)
        except KeyError:
            pass
    return Path.home()


_INVOKING_HOME = _get_invoking_home()
_INVOKING_UID = int(os.environ.get("SUDO_UID", os.getuid()))
_INVOKING_GID = int(os.environ.get("SUDO_GID", os.getgid()))
BASE_DIR = _INVOKING_HOME / ".update_zen"
SNAPSHOT_DIR = BASE_DIR / "snapshots"
LOG_FILE = BASE_DIR / "update_zen.log"
_active_log_file: Path = LOG_FILE  # updated to config.log_file after Config.load()
_env_config = os.environ.get("UPDATE_ZEN_CONFIG")
CONFIG_FILE = Path(_env_config) if _env_config else BASE_DIR / "config.json"
CREDENTIALS_FILE = BASE_DIR / "credentials.json"
CRON_CONFIG_DIR = BASE_DIR / "cron_configs"


def _to_portable_path(p: Path) -> str:
    """Serialize a path as ~/... when it lives under the invoking user's home."""
    try:
        return "~/" + str(p.relative_to(_INVOKING_HOME))
    except ValueError:
        return str(p)


def _from_portable_path(s: str) -> Path:
    """Expand ~/... using the invoking user's home; leave absolute paths unchanged."""
    if s.startswith("~/"):
        return _INVOKING_HOME / s[2:]
    return Path(s)


def _is_local_path(p: Path) -> bool:
    """True if path is under the invoking user's home directory."""
    try:
        p.relative_to(_INVOKING_HOME)
        return True
    except ValueError:
        return False


def _portablize_volume_backup(vb: dict) -> dict:
    """Return a copy of volume_backup with path values serialized as ~/... where possible."""
    result = {}
    for container, rules in vb.items():
        r = dict(rules)
        if r.get("save_path"):
            r["save_path"] = _to_portable_path(Path(r["save_path"]))
        if r.get("mount_paths"):
            r["mount_paths"] = {
                cp: _to_portable_path(Path(hp))
                for cp, hp in r["mount_paths"].items()
            }
        result[container] = r
    return result


def _unportablize_volume_backup(vb: dict) -> dict:
    """Return a copy of volume_backup with ~/... values expanded to absolute paths."""
    result = {}
    for container, rules in vb.items():
        r = dict(rules)
        if r.get("save_path"):
            r["save_path"] = str(_from_portable_path(r["save_path"]))
        if r.get("mount_paths"):
            r["mount_paths"] = {
                cp: str(_from_portable_path(hp))
                for cp, hp in r["mount_paths"].items()
            }
        result[container] = r
    return result


def _ensure_dirs(config_path: "Path | None" = None) -> None:
    BASE_DIR.mkdir(exist_ok=True)
    SNAPSHOT_DIR.mkdir(exist_ok=True)
    CRON_CONFIG_DIR.mkdir(exist_ok=True)
    CONFIG_FILE.parent.mkdir(parents=True, exist_ok=True)
    dirs = [BASE_DIR, SNAPSHOT_DIR, CRON_CONFIG_DIR, CONFIG_FILE.parent]
    if config_path is not None and config_path.parent != CONFIG_FILE.parent:
        config_path.parent.mkdir(parents=True, exist_ok=True)
        dirs.append(config_path.parent)
    for d in dirs:
        d.chmod(0o700)
        os.chown(d, _INVOKING_UID, _INVOKING_GID)


def _load_credentials(base_dir: Path = None) -> dict:
    """Load saved_passwords from credentials.json. Returns {} if file absent."""
    path = (base_dir or BASE_DIR) / "credentials.json"
    if not path.exists():
        return {}
    try:
        raw = path.read_bytes()
        enc = EncryptionManager(None)
        if enc.is_encrypted(raw):
            if _master_password is None:
                return {}
            raw = enc.decrypt_bytes(raw, _master_password)
        data = json.loads(raw)
        return data.get("saved_passwords", {})
    except Exception:
        return {}


def _save_credentials(saved_passwords: dict, base_dir: Path = None) -> None:
    """Write saved_passwords to credentials.json with 0600 permissions."""
    path = (base_dir or BASE_DIR) / "credentials.json"
    raw = (json.dumps({"saved_passwords": saved_passwords}, indent=2) + "\n").encode()
    if _master_password is not None:
        raw = EncryptionManager(None).encrypt_bytes(raw, _master_password)
    with open(path, "wb") as f:
        f.write(raw)
    path.chmod(0o600)
    os.chown(path, _INVOKING_UID, _INVOKING_GID)


# === CONFIG ===

_DEFAULT_HIDDEN_COLUMNS = [
    "ver", "snaps", "pin", "cron", "auto_rb", "img_exp",
    "vol_bak", "restarts", "ports", "network", "compose", "snap_path",
]



@dataclass
class Config:
    snapshot_dir: Path = field(default_factory=lambda: SNAPSHOT_DIR)
    log_file: Path = field(default_factory=lambda: LOG_FILE)
    max_snapshots: int = 3
    max_snapshots_overrides: dict = field(default_factory=dict)
    health_timeout_sec: int = 300
    exclude: list = field(default_factory=list)
    volume_backup: dict = field(default_factory=dict)
    volume_backup_enabled: bool = True
    auto_rollback: bool = True
    auto_rollback_disabled: list = field(default_factory=list)
    pinned_tags: dict = field(default_factory=dict)
    restart_stack_siblings: bool = False
    gateway_wait_sec: int = 60
    sibling_wait_sec: int = 30
    image_export_enabled: bool = True
    image_export_disabled: list = field(default_factory=list)
    env_backup_disabled: list = field(default_factory=list)
    registry_alternatives: dict = field(default_factory=dict)
    pause_for_backup: bool = True
    pause_for_backup_disabled: list = field(default_factory=list)
    snapshot_dir_overrides: dict = field(default_factory=dict)
    encryption: dict = field(default_factory=lambda: {
        "mode": "session",
        "encrypt_containers": [],
        "encrypt_volumes": {},
        "saved_passwords": {},
    })
    cron_jobs: dict = field(default_factory=dict)
    pagination_enabled: bool = True
    hidden_columns: list = field(default_factory=lambda: list(_DEFAULT_HIDDEN_COLUMNS))
    container_versions: dict = field(default_factory=dict)
    snapshot_dir_mode: int = 0o700
    snapshot_file_mode: int = 0o600
    snapshot_permission_overrides: dict = field(default_factory=dict)
    # Not serialized — tracks where this config was loaded from so save()
    # always writes back to the same file, even when a custom path is used.
    _path: Path = field(default_factory=lambda: CONFIG_FILE, init=False, repr=False)

    def snapshot_dir_for(self, container: str) -> Path:
        override = self.snapshot_dir_overrides.get(container)
        return Path(override) if override else self.snapshot_dir

    def max_snapshots_for(self, container: str) -> int:
        return self.max_snapshots_overrides.get(container, self.max_snapshots)

    def snapshot_dir_mode_for(self, container: str) -> int:
        override = self.snapshot_permission_overrides.get(container, {})
        return override.get("dir_mode", self.snapshot_dir_mode)

    def snapshot_file_mode_for(self, container: str) -> int:
        override = self.snapshot_permission_overrides.get(container, {})
        return override.get("file_mode", self.snapshot_file_mode)

    def is_encryption_enabled(self, container: str) -> bool:
        return container in self.encryption.get("encrypt_containers", [])

    def is_volume_encrypted(self, container: str, mount: str) -> bool:
        mounts = self.encryption.get("encrypt_volumes", {}).get(container)
        if not mounts:
            return False
        return "all" in mounts or mount in mounts

    def get_saved_password(self, container: str, mount: str | None = None) -> "str | None":
        saved = self.encryption.get("saved_passwords", {})
        if mount is not None:
            pw = saved.get(f"{container}::{mount}")
            if pw is not None:
                return pw
        return saved.get(container)

    def set_saved_password(self, container: str, password: str,
                           mount: str | None = None) -> None:
        if "saved_passwords" not in self.encryption:
            self.encryption["saved_passwords"] = {}
        key = f"{container}::{mount}" if mount is not None else container
        self.encryption["saved_passwords"][key] = password
        # Write credentials separately; config.json never receives real passwords.
        _save_credentials(self.encryption["saved_passwords"], self._path.parent)
        self.save()

    def purge_saved_passwords(self, container: str | None = None) -> int:
        saved = self.encryption.get("saved_passwords", {})
        if container is None:
            count = len(saved)
            self.encryption["saved_passwords"] = {}
            _session_cache.clear()
        else:
            keys = [k for k in saved if k == container or k.startswith(f"{container}::")]
            count = len(keys)
            for k in keys:
                del saved[k]
                _session_cache.pop(k, None)
        if count:
            _save_credentials(self.encryption["saved_passwords"], self._path.parent)
            self.save()
        return count

    @classmethod
    def load(cls, path: "Path | None" = None) -> "Config":
        if path is None:
            path = CONFIG_FILE
        if not path.exists():
            cfg = cls()
            cfg._path = path
            cfg.save()
            return cfg
        raw = path.read_bytes()
        _enc = EncryptionManager(None)
        if _enc.is_encrypted(raw):
            if _master_password is None:
                raise RuntimeError(
                    f"config.json at {path} is encrypted but no master password is set"
                )
            try:
                raw = _enc.decrypt_bytes(raw, _master_password)
            except Exception as e:
                raise RuntimeError(f"Failed to decrypt config.json: {e}") from e
        data = json.loads(raw)
        defaults = cls()
        cfg = cls(
            snapshot_dir=_from_portable_path(data.get("snapshot_dir", str(defaults.snapshot_dir))),
            log_file=_from_portable_path(data.get("log_file", str(defaults.log_file))),
            max_snapshots=int(data.get("max_snapshots", defaults.max_snapshots)),
            max_snapshots_overrides=dict(data.get("max_snapshots_overrides",
                                                   defaults.max_snapshots_overrides)),
            health_timeout_sec=int(data.get("health_timeout_sec", defaults.health_timeout_sec)),
            exclude=list(data.get("exclude", defaults.exclude)),
            volume_backup=_unportablize_volume_backup(
                dict(data.get("volume_backup", defaults.volume_backup))
            ),
            volume_backup_enabled=bool(data.get("volume_backup_enabled",
                                                 defaults.volume_backup_enabled)),
            auto_rollback=bool(data.get("auto_rollback", defaults.auto_rollback)),
            auto_rollback_disabled=list(data.get("auto_rollback_disabled",
                                                  defaults.auto_rollback_disabled)),
            pinned_tags=dict(data.get("pinned_tags", defaults.pinned_tags)),
            restart_stack_siblings=bool(data.get("restart_stack_siblings",
                                                  defaults.restart_stack_siblings)),
            gateway_wait_sec=int(data.get("gateway_wait_sec", defaults.gateway_wait_sec)),
            sibling_wait_sec=int(data.get("sibling_wait_sec", defaults.sibling_wait_sec)),
            image_export_enabled=bool(data.get("image_export_enabled",
                                               defaults.image_export_enabled)),
            image_export_disabled=list(data.get("image_export_disabled",
                                                defaults.image_export_disabled)),
            env_backup_disabled=list(data.get("env_backup_disabled",
                                              defaults.env_backup_disabled)),
            registry_alternatives=dict(data.get("registry_alternatives",
                                                 defaults.registry_alternatives)),
            snapshot_dir_overrides={
                k: str(_from_portable_path(v))
                for k, v in data.get("snapshot_dir_overrides",
                                     defaults.snapshot_dir_overrides).items()
            },
            pause_for_backup=bool(data.get("pause_for_backup", defaults.pause_for_backup)),
            pause_for_backup_disabled=list(data.get("pause_for_backup_disabled",
                                                     defaults.pause_for_backup_disabled)),
            encryption={**defaults.encryption, **data.get("encryption", {})},
            cron_jobs=dict(data.get("cron_jobs", defaults.cron_jobs)),
            pagination_enabled=bool(data.get("pagination_enabled", defaults.pagination_enabled)),
            hidden_columns=(list(data["hidden_columns"]) if data.get("hidden_columns")
                            else list(_DEFAULT_HIDDEN_COLUMNS)),
            container_versions=dict(data.get("container_versions", defaults.container_versions)),
            snapshot_dir_mode=int(data.get("snapshot_dir_mode", defaults.snapshot_dir_mode)),
            snapshot_file_mode=int(data.get("snapshot_file_mode", defaults.snapshot_file_mode)),
            snapshot_permission_overrides=dict(data.get("snapshot_permission_overrides",
                                                         defaults.snapshot_permission_overrides)),
        )
        # Write back if any keys are missing so new fields migrate automatically.
        _expected = {"snapshot_dir", "log_file", "max_snapshots", "max_snapshots_overrides",
                     "health_timeout_sec", "exclude", "volume_backup",
                     "volume_backup_enabled", "auto_rollback", "auto_rollback_disabled",
                     "pinned_tags", "restart_stack_siblings",
                     "gateway_wait_sec", "sibling_wait_sec",
                     "image_export_enabled", "image_export_disabled",
                     "env_backup_disabled",
                     "registry_alternatives", "snapshot_dir_overrides",
                     "pause_for_backup", "pause_for_backup_disabled",
                     "encryption", "cron_jobs", "pagination_enabled",
                     "hidden_columns", "container_versions",
                     "snapshot_dir_mode", "snapshot_file_mode", "snapshot_permission_overrides"}
        cfg._path = path
        if not _expected.issubset(data.keys()):
            cfg.save()
        # Merge saved passwords from credentials.json into in-memory config.
        # This makes the rest of the app work unchanged — it still reads passwords
        # from config.encryption["saved_passwords"] at runtime.
        cred_passwords = _load_credentials(path.parent)
        if cred_passwords:
            cfg.encryption["saved_passwords"] = cred_passwords
        return cfg

    def save(self) -> None:
        raw = (json.dumps(
            {
                "snapshot_dir": _to_portable_path(self.snapshot_dir),
                "log_file": _to_portable_path(self.log_file),
                "max_snapshots": self.max_snapshots,
                "max_snapshots_overrides": self.max_snapshots_overrides,
                "health_timeout_sec": self.health_timeout_sec,
                "exclude": self.exclude,
                "volume_backup": _portablize_volume_backup(self.volume_backup),
                "volume_backup_enabled": self.volume_backup_enabled,
                "auto_rollback": self.auto_rollback,
                "auto_rollback_disabled": self.auto_rollback_disabled,
                "pinned_tags": self.pinned_tags,
                "restart_stack_siblings": self.restart_stack_siblings,
                "gateway_wait_sec": self.gateway_wait_sec,
                "sibling_wait_sec": self.sibling_wait_sec,
                "image_export_enabled": self.image_export_enabled,
                "image_export_disabled": self.image_export_disabled,
                "env_backup_disabled": self.env_backup_disabled,
                "registry_alternatives": self.registry_alternatives,
                "snapshot_dir_overrides": {
                    k: _to_portable_path(Path(v))
                    for k, v in self.snapshot_dir_overrides.items()
                },
                "pause_for_backup": self.pause_for_backup,
                "pause_for_backup_disabled": self.pause_for_backup_disabled,
                "encryption": {
                    **self.encryption,
                    "saved_passwords": {},  # never write real passwords to config.json
                },
                "cron_jobs": self.cron_jobs,
                "pagination_enabled": self.pagination_enabled,
                "hidden_columns": self.hidden_columns,
                "container_versions": self.container_versions,
                "snapshot_dir_mode": self.snapshot_dir_mode,
                "snapshot_file_mode": self.snapshot_file_mode,
                "snapshot_permission_overrides": self.snapshot_permission_overrides,
            },
            indent=2,
        ) + "\n").encode()
        if _master_password is not None:
            raw = EncryptionManager(None).encrypt_bytes(raw, _master_password)
        with open(self._path, "wb") as f:
            f.write(raw)
        try:
            self._path.chmod(0o600)
            os.chown(self._path, _INVOKING_UID, _INVOKING_GID)
        except OSError:
            pass


# === LOGGING ===

def log(msg: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {msg}"
    print(line)
    log_path = _active_log_file
    is_new = not log_path.exists()
    with open(log_path, "a") as f:
        f.write(line + "\n")
    if is_new:
        try:
            log_path.chmod(0o600)
            os.chown(log_path, _INVOKING_UID, _INVOKING_GID)
        except OSError:
            pass


# === CRON ===

_CRON_USER: str = os.environ.get("SUDO_USER") or os.environ.get("USER") or "root"

_CRON_RECIPES: dict = {
    "nightly_update": {
        "label":            "Nightly update",
        "description":      "Pull the latest image and recreate the container nightly.",
        "default_schedule": "0 3 * * *",
        "command":          "update_zen update {container}",
    },
    "weekly_update": {
        "label":            "Weekly update",
        "description":      "Pull the latest image and recreate the container (Sundays at 3am).",
        "default_schedule": "0 3 * * 0",
        "command":          "update_zen update {container}",
    },
    "daily_check": {
        "label":            "Daily update check",
        "description":      "Log whether a newer image is available.",
        "default_schedule": "0 8 * * *",
        "command":          "update_zen check {container}",
    },
    "weekly_check": {
        "label":            "Weekly update check",
        "description":      "Log whether a newer image is available (Mondays at 8am).",
        "default_schedule": "0 8 * * 1",
        "command":          "update_zen check {container}",
    },
    "hourly_snapshot": {
        "label":            "Hourly snapshot",
        "description":      "Take a full snapshot of the container every hour.",
        "default_schedule": "0 * * * *",
        "command":          "update_zen snapshot {container}",
    },
    "daily_snapshot": {
        "label":            "Daily snapshot",
        "description":      "Take a full snapshot of the container daily (2am).",
        "default_schedule": "0 2 * * *",
        "command":          "update_zen snapshot {container}",
    },
    "weekly_snapshot": {
        "label":            "Weekly snapshot",
        "description":      "Take a full snapshot of the container weekly (Sundays at 2am).",
        "default_schedule": "0 2 * * 0",
        "command":          "update_zen snapshot {container}",
    },
    "monthly_snapshot": {
        "label":            "Monthly snapshot",
        "description":      "Take a full snapshot of the container on the 1st of each month.",
        "default_schedule": "0 2 1 * *",
        "command":          "update_zen snapshot {container}",
    },
    "hourly_volume_backup": {
        "label":            "Hourly volume backup",
        "description":      "Back up all container volumes every hour.",
        "default_schedule": "0 * * * *",
        "command":          "update_zen volumes backup {container}",
    },
    "daily_volume_backup": {
        "label":            "Daily volume backup",
        "description":      "Back up all container volumes daily (1am).",
        "default_schedule": "0 1 * * *",
        "command":          "update_zen volumes backup {container}",
    },
    "weekly_volume_backup": {
        "label":            "Weekly volume backup",
        "description":      "Back up all container volumes weekly (Sundays at 1am).",
        "default_schedule": "0 1 * * 0",
        "command":          "update_zen volumes backup {container}",
    },
    "monthly_volume_backup": {
        "label":            "Monthly volume backup",
        "description":      "Back up all container volumes on the 1st of each month.",
        "default_schedule": "0 1 1 * *",
        "command":          "update_zen volumes backup {container}",
    },
    "mount_volume_backup": {
        "label":            "Volume backup — single mount",
        "description":      "Back up one specific container mount on a schedule.",
        "default_schedule": "0 1 * * *",
        "command":          "update_zen volumes backup {container} --mount {mount}",
        "requires_mount":   True,
    },
}


def _cron_job_marker(job: dict) -> str:
    """Unique crontab marker key for a job (used in BEGIN/END comment lines).
    For mount_volume_backup, encodes the mount so multiple mounts coexist."""
    recipe = job.get("recipe", "")
    mount  = job.get("mount", "")
    if mount:
        return f"{recipe}:{_sanitize_mount_name(mount)}"
    return recipe


def _crontab_read() -> str:
    result = subprocess.run(
        ["crontab", "-u", _CRON_USER, "-l"],
        capture_output=True, text=True,
    )
    if result.returncode == 0:
        return result.stdout
    if result.returncode == 1 and "no crontab for" in result.stderr:
        return ""
    raise RuntimeError(result.stderr.strip() or f"exit {result.returncode}")


def _crontab_write(content: str) -> None:
    result = subprocess.run(
        ["crontab", "-u", _CRON_USER, "-"],
        input=content, text=True, capture_output=True,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or f"exit {result.returncode}")


def _cron_block(container: str, recipe: str, schedule: str,
                command: str, log_file: "Path",
                job: "dict | None" = None) -> str:
    if not _cron_validate_container_name(container):
        raise ValueError(f"Unsafe container name for cron: {container!r}")
    mount = (job or {}).get("mount", "")
    cron_config = (job or {}).get("cron_config")
    cmd = command.format(container=container, mount=mount)
    if cron_config:
        cfg_path = str(_from_portable_path(cron_config) / "config.json")
        cmd = "update_zen --config " + cfg_path + " " + cmd[len("update_zen "):]
    return (
        f"# BEGIN update_zen:{container}:{recipe}\n"
        f"{schedule} {cmd} >> {log_file} 2>&1\n"
        f"# END update_zen:{container}:{recipe}\n"
    )


def _crontab_remove(content: str, container: str, recipe: str) -> str:
    begin = f"# BEGIN update_zen:{container}:{recipe}"
    end   = f"# END update_zen:{container}:{recipe}"
    lines = content.splitlines(keepends=True)
    out: list = []
    skip = False
    for line in lines:
        stripped = line.rstrip("\r\n")
        if stripped == begin:
            if out and not out[-1].strip():
                out.pop()
            skip = True
        if skip:
            if stripped == end:
                skip = False
            continue
        out.append(line)
    return "".join(out)


def _crontab_inject(content: str, container: str, recipe: str,
                    schedule: str, command: str, log_file: "Path",
                    job: "dict | None" = None) -> str:
    content = _crontab_remove(content, container, recipe)
    if content and not content.endswith("\n"):
        content += "\n"
    if content.strip():
        content += "\n"
    content += _cron_block(container, recipe, schedule, command, log_file, job)
    return content


def _crontab_is_applied(content: str, container: str, recipe: str) -> bool:
    return f"# BEGIN update_zen:{container}:{recipe}" in content


def _cron_validate_container_name(name: str) -> bool:
    return bool(re.fullmatch(r"[a-zA-Z0-9][a-zA-Z0-9_.\-]*", name))


def _cron_validate_schedule(schedule: str) -> bool:
    parts = schedule.split()
    if len(parts) != 5:
        return False
    return all(re.fullmatch(r"[\d\*,\-\/]+", p) for p in parts)


def _cron_apply(config: "Config", container: "str | None" = None) -> list:
    try:
        original = _crontab_read()
    except RuntimeError as e:
        raise RuntimeError(f"Could not read crontab: {e}") from e

    content = original
    changes: list = []
    targets = [container] if container else list(config.cron_jobs.keys())
    for ctr in targets:
        if not _cron_validate_container_name(ctr):
            changes.append(f"  skipped  {ctr}  (unsafe container name — remove from config)")
            continue
        for job in config.cron_jobs.get(ctr, []):
            recipe   = job.get("recipe", "")
            schedule = job.get("schedule", "")
            enabled  = job.get("enabled", False)
            rec = _CRON_RECIPES.get(recipe)
            if rec is None:
                changes.append(f"  skipped  {ctr}:{recipe}  (unknown recipe)")
                continue
            marker = _cron_job_marker(job)
            if enabled:
                content = _crontab_inject(content, ctr, marker, schedule,
                                          rec["command"], config.log_file, job=job)
                changes.append(f"  applied  {ctr}:{marker}")
            else:
                content = _crontab_remove(content, ctr, marker)
                changes.append(f"  removed  {ctr}:{marker}")

    if content != original:
        try:
            _crontab_write(content)
        except RuntimeError as e:
            raise RuntimeError(f"Could not write crontab: {e}") from e

    return changes


def _cron_status(config: "Config") -> list:
    try:
        content = _crontab_read()
    except RuntimeError:
        content = ""
    rows: list = []
    for container, jobs in config.cron_jobs.items():
        for job in jobs:
            schedule = job.get("schedule", "")
            enabled  = job.get("enabled", False)
            marker   = _cron_job_marker(job)
            rows.append({
                "container": container,
                "recipe":    marker,
                "schedule":  schedule,
                "enabled":   enabled,
                "applied":   _crontab_is_applied(content, container, marker),
            })
    return rows


# === DOCKER CLIENT ===

class DockerError(Exception):
    pass


class DockerClient:

    @staticmethod
    def _run(args: list) -> subprocess.CompletedProcess:
        try:
            result = subprocess.run(
                ["docker"] + args,
                capture_output=True,
                text=True,
            )
        except FileNotFoundError:
            raise DockerError("docker executable not found — is Docker installed?")
        if result.returncode != 0:
            raise DockerError(
                result.stderr.strip() or f"docker {args[0]} exited {result.returncode}"
            )
        return result

    def inspect(self, container: str) -> dict:
        result = self._run(["inspect", container])
        data = json.loads(result.stdout)[0]
        # Container inspect does not include RepoDigests — fetch it from the
        # image so digest comparison and rollback pinning work correctly.
        image_id = data.get("Image", "")
        if image_id:
            try:
                img_result = self._run(["image", "inspect", image_id])
                img_data = json.loads(img_result.stdout)[0]
                data["RepoDigests"] = img_data.get("RepoDigests") or []
                labels = (img_data.get("Config") or {}).get("Labels") or {}
                data["ImageVersion"] = labels.get("org.opencontainers.image.version", "")
                raw_created = (labels.get("org.opencontainers.image.created")
                               or img_data.get("Created") or "")
                # Truncate to YYYY-MM-DD; treat epoch zero as absent.
                data["ImageCreated"] = (raw_created[:10]
                                        if len(raw_created) >= 10 and not raw_created.startswith("0001")
                                        else "")
            except DockerError:
                data["RepoDigests"] = []
                data["ImageVersion"] = ""
                data["ImageCreated"] = ""
        # When NetworkMode is "container:<id>", resolve the ID to a name so the
        # spec can be reconstructed by name after the referenced container is
        # recreated (its ID changes on every recreation).
        network_mode = (data.get("HostConfig") or {}).get("NetworkMode", "")
        if network_mode.startswith("container:"):
            cid = network_mode.split(":", 1)[1]
            try:
                nm_result = self._run(["inspect", "--format", "{{.Name}}", cid])
                resolved = nm_result.stdout.strip().lstrip("/")
                if resolved:
                    data["HostConfig"]["NetworkMode"] = f"container:{resolved}"
            except DockerError:
                pass  # leave as-is; ID-based mode is still better than nothing
        return data

    def health(self, container: str) -> str:
        data = self.inspect(container)
        state = data.get("State", {})
        status = state.get("Status", "unknown")
        health_obj = state.get("Health")
        if health_obj is None:
            # No HEALTHCHECK defined — report the raw container state
            return status
        health_status = health_obj.get("Status", "")
        if health_status in ("healthy", "unhealthy", "starting"):
            return health_status
        return status

    def pull(self, image_ref: str) -> None:
        # Stream pull progress directly to the terminal — don't capture.
        try:
            result = subprocess.run(["docker", "pull", image_ref], check=False)
        except FileNotFoundError:
            raise DockerError("docker executable not found — is Docker installed?")
        if result.returncode != 0:
            raise DockerError(f"docker pull failed for {image_ref}")

    def tag_image(self, source: str, target: str) -> None:
        self._run(["tag", source, target])

    def start(self, container: str) -> None:
        self._run(["start", container])

    def stop(self, container: str, timeout: int = 10) -> None:
        self._run(["stop", "-t", str(timeout), container])

    def pause(self, container: str) -> None:
        self._run(["pause", container])

    def unpause(self, container: str) -> None:
        self._run(["unpause", container])

    def kill(self, container: str) -> None:
        self._run(["kill", container])

    def stats(self, container: str) -> dict:
        result = self._run(["stats", "--no-stream", "--format", "{{json .}}", container])
        return json.loads(result.stdout.strip())

    def logs(self, container: str, tail: int = 100) -> str:
        try:
            result = subprocess.run(
                ["docker", "logs", "--tail", str(tail), container],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
            )
        except FileNotFoundError:
            raise DockerError("docker executable not found — is Docker installed?")
        if result.returncode != 0:
            raise DockerError(result.stdout.strip() or f"docker logs exited {result.returncode}")
        return result.stdout

    def remove(self, container: str) -> None:
        # docker rm without -f raises naturally if the container is still running.
        self._run(["rm", container])

    def connect_network(self, container: str, network: str) -> None:
        self._run(["network", "connect", network, container])

    def _build_run_cmd(self, spec: "ContainerSpec") -> list:
        cmd = ["run", "-d", "--name", spec.name]
        for e in spec.env:
            cmd += ["-e", e]
        for b in spec.binds:
            cmd += ["-v", b]
        for p in spec.port_bindings:
            cmd += ["-p", p]
        for label in spec.labels:
            cmd += ["--label", label]
        if spec.restart:
            cmd += ["--restart", spec.restart]
        for cap in spec.cap_add:
            cmd += ["--cap-add", cap]
        for cap in spec.cap_drop:
            cmd += ["--cap-drop", cap]
        # network_mode takes priority (e.g. "container:gluetun" for shared-namespace
        # stacks).  Otherwise use the first regular network; extras added after start.
        if spec.network_mode:
            cmd += ["--network", spec.network_mode]
        elif spec.networks:
            cmd += ["--network", spec.networks[0]]
        if spec.privileged:
            cmd.append("--privileged")
        for device in spec.devices:
            cmd += ["--device", device]
        if spec.runtime and spec.runtime != "runc":
            cmd += ["--runtime", spec.runtime]
        for k, v in spec.sysctls.items():
            cmd += ["--sysctl", f"{k}={v}"]
        for opt in spec.security_opt:
            cmd += ["--security-opt", opt]
        if spec.user:
            cmd += ["--user", spec.user]
        if spec.working_dir:
            cmd += ["--workdir", spec.working_dir]
        for ul in spec.ulimits:
            name = ul.get("Name", "")
            soft = ul.get("Soft", 0)
            hard = ul.get("Hard", 0)
            if name:
                val = f"{soft}" if soft == hard else f"{soft}:{hard}"
                cmd += ["--ulimit", f"{name}={val}"]
        if spec.shm_size:
            cmd += ["--shm-size", str(spec.shm_size)]
        if spec.pid_mode:
            cmd += ["--pid", spec.pid_mode]
        if spec.ipc_mode and spec.ipc_mode != "private":
            cmd += ["--ipc", spec.ipc_mode]
        # --hostname, --add-host, and all --dns* flags are network-namespace
        # settings that Docker rejects when --network container:<name> is used.
        if not spec.network_mode:
            if spec.hostname:
                cmd += ["--hostname", spec.hostname]
            for host in spec.extra_hosts:
                cmd += ["--add-host", host]
            for d in spec.dns:
                cmd += ["--dns", d]
            for s in spec.dns_search:
                cmd += ["--dns-search", s]
            for o in spec.dns_options:
                cmd += ["--dns-option", o]
        if spec.log_driver and spec.log_driver != "json-file":
            cmd += ["--log-driver", spec.log_driver]
        for k, v in spec.log_opts.items():
            cmd += ["--log-opt", f"{k}={v}"]
        if spec.cpu_shares:
            cmd += ["--cpu-shares", str(spec.cpu_shares)]
        if spec.memory:
            cmd += ["--memory", str(spec.memory)]
        if spec.nano_cpus:
            cmd += ["--cpus", f"{spec.nano_cpus / 1e9:g}"]
        if spec.stop_signal and spec.stop_signal != "SIGTERM":
            cmd += ["--stop-signal", spec.stop_signal]
        for g in spec.group_add:
            cmd += ["--group-add", g]
        if spec.init:
            cmd.append("--init")
        if spec.readonly_rootfs:
            cmd.append("--read-only")
        extra_entry_args = []
        if spec.entrypoint:
            cmd += ["--entrypoint", spec.entrypoint[0]]
            extra_entry_args = spec.entrypoint[1:]
        cmd.append(spec.image)
        cmd += extra_entry_args + list(spec.command)
        return cmd

    def run(self, spec: "ContainerSpec") -> None:
        self._run(self._build_run_cmd(spec))
        for network in spec.networks[1:]:
            self.connect_network(spec.name, network)


# === SNAPSHOT MANAGER ===

@dataclass
class Snapshot:
    path: Path
    timestamp: datetime
    image_ref: str   # Config.Image value, e.g. "nginx:latest"
    digest: str      # RepoDigests entry, e.g. "nginx@sha256:..." (empty if absent)
    version: str = ""  # org.opencontainers.image.version label, or tag portion of image_ref
    volumes: list = field(default_factory=list)


@dataclass
class ContainerSpec:
    name: str
    image: str        # name:tag for forward updates; name@sha256:... for rollbacks
    env: list
    binds: list
    port_bindings: list
    networks: list
    labels: list
    restart: str
    entrypoint: list
    command: list
    network_mode: str = ""  # "container:<name>" when sharing another container's network namespace
    cap_add: list = field(default_factory=list)
    cap_drop: list = field(default_factory=list)
    privileged: bool = False
    devices: list = field(default_factory=list)      # ["host:container[:perms]", ...]
    runtime: str = ""
    sysctls: dict = field(default_factory=dict)
    security_opt: list = field(default_factory=list)
    user: str = ""
    working_dir: str = ""
    ulimits: list = field(default_factory=list)      # [{"Name":..,"Soft":..,"Hard":..}, ...]
    shm_size: int = 0
    pid_mode: str = ""
    ipc_mode: str = ""
    extra_hosts: list = field(default_factory=list)
    dns: list = field(default_factory=list)
    dns_search: list = field(default_factory=list)
    dns_options: list = field(default_factory=list)
    log_driver: str = ""
    log_opts: dict = field(default_factory=dict)
    cpu_shares: int = 0
    memory: int = 0
    nano_cpus: int = 0
    hostname: str = ""
    stop_signal: str = ""
    group_add: list = field(default_factory=list)
    init: bool = False
    readonly_rootfs: bool = False


def _probe_snapshot_dir(path: Path) -> "str | None":
    """Write and delete a probe file to verify path is writable. Returns error string or None."""
    try:
        path.mkdir(parents=True, exist_ok=True)
        probe = path / ".write_probe"
        probe.write_text("")
        probe.unlink()
        return None
    except OSError as e:
        return str(e)


def _sanitize_mount_name(container_path: str) -> str:
    s = container_path.lstrip("/")
    s = s.replace("/", "_")
    s = re.sub(r"[^a-zA-Z0-9_\-]", "_", s)
    s = re.sub(r"_+", "_", s)
    return s


def _derive_version_meta(inspect_data: dict) -> dict:
    """Extract version and digest from inspect data. Returns dict with 'version' and 'digest' keys."""
    labels = inspect_data.get("Config", {}).get("Labels") or {}
    image = inspect_data.get("Config", {}).get("Image", "")
    tag = "" if "@sha256:" in image else image.rsplit(":", 1)[-1]
    version = (tag if tag and tag != "latest"
               else labels.get("org.opencontainers.image.version", "") or tag)
    digests = inspect_data.get("RepoDigests") or []
    digest = digests[0].split("@sha256:", 1)[-1] if digests and "@sha256:" in digests[0] else ""
    return {"version": version, "digest": f"sha256:{digest}" if digest else ""}


def _get_named_volumes(inspect_data: dict) -> list[dict]:
    """Return named, non-anonymous volumes from a container inspect dict."""
    result = []
    for m in inspect_data.get("Mounts", []):
        if m.get("Type") != "volume":
            continue
        name = m.get("Name", "")
        if re.match(r"^[0-9a-f]{64}$", name):
            continue
        result.append({
            "Name": name,
            "Source": m.get("Source", ""),
            "Destination": m.get("Destination", ""),
        })
    return result


def _get_nonlocal_volumes(inspect_data: dict) -> list[dict]:
    """Return named, non-anonymous volumes that have no local host path (non-local driver)."""
    result = []
    for m in inspect_data.get("Mounts", []):
        if m.get("Type") != "volume":
            continue
        name = m.get("Name", "")
        if re.match(r"^[0-9a-f]{64}$", name):
            continue
        if not m.get("Source", ""):
            result.append({
                "Name": name,
                "Driver": m.get("Driver", ""),
                "Destination": m.get("Destination", ""),
            })
    return result


def _get_active_image_ref(config: "Config", container: str, inspect_data: dict) -> str:
    alts = config.registry_alternatives.get(container, {})
    active = alts.get("active", "")
    refs = alts.get("refs", [])
    if active and active in refs:
        return active
    return inspect_data.get("Config", {}).get("Image", "")


def _collect_container_snapshot_dirs(config: "Config", container: str) -> list:
    """Return all existing snapshot/archive directories for a container across all path levels."""
    seen: set = set()
    result = []
    candidates = [config.snapshot_dir_for(container) / container]
    rules = config.volume_backup.get(container, {})
    if rules.get("save_path"):
        candidates.append(Path(rules["save_path"]) / container)
    for mp in rules.get("mount_paths", {}).values():
        candidates.append(Path(mp) / container)
    for d in candidates:
        if d not in seen and d.exists():
            seen.add(d)
            result.append(d)
    return result


def _bulk_chmod_tree(root: Path, dir_mode: int, file_mode: int) -> tuple:
    """Apply dir_mode to every directory and file_mode to every file under root (inclusive).
    Returns (dirs_changed, files_changed). Per-entry OSErrors are logged and skipped."""
    dirs_n = files_n = 0
    for dirpath, _dirnames, filenames in os.walk(root):
        try:
            os.chmod(dirpath, dir_mode)
            dirs_n += 1
        except OSError as e:
            log(f"[chmod_tree] {dirpath}: {e}")
        for fname in filenames:
            fpath = Path(dirpath) / fname
            try:
                os.chmod(fpath, file_mode)
                files_n += 1
            except OSError as e:
                log(f"[chmod_tree] {fpath}: {e}")
    return dirs_n, files_n


_PERMISSION_PROFILES = [
    ("Secure", 0o700, 0o600, "owner only"),
    ("Group",  0o750, 0o640, "owner + group read"),
    ("Shared", 0o755, 0o644, "world readable"),
]


def _permission_profile_label(dir_mode: int, file_mode: int) -> str:
    """Return the named profile matching (dir_mode, file_mode), or 'Custom 0NNN/0NNN'."""
    for label, dm, fm, _ in _PERMISSION_PROFILES:
        if dm == dir_mode and fm == file_mode:
            return label
    return f"Custom {dir_mode:04o}/{file_mode:04o}"


# === ENCRYPTION ===

def _derive_key_from_salt(password: str, salt: bytes) -> bytes:
    return hashlib.scrypt(password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)


class EncryptionManager:

    def __init__(self, config: Config) -> None:
        pass

    def encrypt_bytes(self, data: bytes, password: str) -> bytes:
        from cryptography.hazmat.primitives.ciphers.aead import AESGCM
        salt = os.urandom(16)
        key = _derive_key_from_salt(password, salt)
        nonce = os.urandom(12)
        ct = AESGCM(key).encrypt(nonce, data, None)
        return json.dumps({
            "enc": "v2",
            "salt": base64.b64encode(salt).decode(),
            "nonce": base64.b64encode(nonce).decode(),
            "ct": base64.b64encode(ct).decode(),
        }).encode()

    def decrypt_bytes(self, blob: bytes, password: str) -> bytes:
        from cryptography.hazmat.primitives.ciphers.aead import AESGCM
        envelope = json.loads(blob)
        key = _derive_key_from_salt(password, base64.b64decode(envelope["salt"]))
        nonce = base64.b64decode(envelope["nonce"])
        ct = base64.b64decode(envelope["ct"])
        return AESGCM(key).decrypt(nonce, ct, None)

    def is_encrypted(self, data) -> bool:
        if isinstance(data, dict):
            return data.get("enc") == "v2"
        if isinstance(data, bytes):
            try:
                parsed = json.loads(data)
                return isinstance(parsed, dict) and parsed.get("enc") == "v2"
            except (json.JSONDecodeError, UnicodeDecodeError):
                return False
        return False

    def encrypt_file(self, src: Path, dst: Path, password: str) -> None:
        from cryptography.hazmat.primitives.ciphers.aead import AESGCM
        salt = os.urandom(16)
        key = _derive_key_from_salt(password, salt)
        nonce = os.urandom(12)
        aesgcm = AESGCM(key)
        with open(src, "rb") as fin, open(dst, "wb") as fout:
            fout.write(b"RBPE\x02")
            fout.write(salt)
            fout.write(nonce)
            chunk_idx = 0
            while True:
                plaintext = fin.read(65536)
                if not plaintext:
                    break
                aad = chunk_idx.to_bytes(8, "big")
                ct = aesgcm.encrypt(nonce, plaintext, aad)
                fout.write(len(ct).to_bytes(4, "big"))
                fout.write(ct)
                chunk_idx += 1

    def decrypt_file(self, src: Path, dst: Path, password: str) -> None:
        from cryptography.hazmat.primitives.ciphers.aead import AESGCM
        with open(src, "rb") as fin, open(dst, "wb") as fout:
            magic = fin.read(4)
            if magic != b"RBPE":
                raise ValueError(f"Not an RBPE encrypted file: {src}")
            version = fin.read(1)
            if version == b"\x02":
                salt = fin.read(16)
                nonce = fin.read(12)
                key = _derive_key_from_salt(password, salt)
            else:
                raise ValueError(f"Unsupported RBPE version {version!r}: {src}")
            aesgcm = AESGCM(key)
            chunk_idx = 0
            while True:
                length_bytes = fin.read(4)
                if not length_bytes:
                    break
                length = int.from_bytes(length_bytes, "big")
                ct = fin.read(length)
                aad = chunk_idx.to_bytes(8, "big")
                plaintext = aesgcm.decrypt(nonce, ct, aad)
                fout.write(plaintext)
                chunk_idx += 1


def _is_encrypted_file(path: Path) -> bool:
    try:
        with open(path, "rb") as f:
            return f.read(4) == b"RBPE"
    except OSError:
        return False



class SnapshotManager:

    def __init__(self, config: Config) -> None:
        self.config = config

    def save(self, container: str, inspect_data: dict,
             password: str | None = None) -> tuple:
        container_dir = self.config.snapshot_dir_for(container) / container
        container_dir.mkdir(parents=True, exist_ok=True)
        container_dir.chmod(self.config.snapshot_dir_mode_for(container))
        os.chown(container_dir, _INVOKING_UID, _INVOKING_GID)
        timestamp = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
        staging_dir = container_dir / f"_staging_{timestamp}"
        staging_dir.mkdir()
        staging_dir.chmod(self.config.snapshot_dir_mode_for(container))
        path = staging_dir / f"{timestamp}.json"
        data = json.dumps(inspect_data, indent=2).encode() + b"\n"
        if password is not None:
            data = EncryptionManager(self.config).encrypt_bytes(data, password)
        path.write_bytes(data)
        return path, staging_dir

    def finalize(self, container: str, snapshot_id: str, staging_dir: Path) -> Path:
        container_dir = self.config.snapshot_dir_for(container) / container
        archive_path = container_dir / f"{snapshot_id}.tar.gz"
        with tarfile.open(archive_path, "w:gz", compresslevel=1) as tar:
            for f in sorted(staging_dir.iterdir()):
                tar.add(f, arcname=f.name)
        archive_path.chmod(self.config.snapshot_file_mode_for(container))
        for f in staging_dir.iterdir():
            f.unlink()
        staging_dir.rmdir()
        self._rotate(container)
        return archive_path

    def _rotate(self, container: str) -> None:
        snaps = self.list(container)
        prefix = f"[rotate {container}]"
        limit = self.config.max_snapshots_for(container)
        for snap in snaps[limit:]:
            snapshot_id = snap.path.name.removesuffix(".tar.gz")
            container_dir = snap.path.parent
            try:
                vol_data = self.load_volumes(snap)
                for entry in vol_data.get("volumes", []):
                    if entry.get("archive_dir"):
                        ext_archive = (Path(entry["archive_dir"])
                                       / container / entry["archive_name"])
                        if ext_archive.exists():
                            ext_archive.unlink()
                            log(f"{prefix} deleted {ext_archive} — external volume archive for rotated snapshot")
            except Exception:
                pass
            for mount_archive in container_dir.glob(f"{snapshot_id}_*.tar.gz"):
                mount_archive.unlink()
                log(f"{prefix} deleted {mount_archive} — volume archive for rotated snapshot")
            snap.path.unlink()
            log(f"{prefix} deleted {snap.path} — exceeded rotation limit ({limit})")

    def list(self, container: str) -> list:
        container_dir = self.config.snapshot_dir_for(container) / container
        if not container_dir.exists():
            return []
        snaps = []
        _ts_re = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}-\d{2}-\d{2}$")
        _enc = EncryptionManager(self.config)
        for path in container_dir.glob("*.tar.gz"):
            snapshot_id = path.name.removesuffix(".tar.gz")
            if not _ts_re.match(snapshot_id):
                continue
            try:
                ts = datetime.strptime(snapshot_id, "%Y-%m-%dT%H-%M-%S")
                with tarfile.open(path, "r:gz") as tar:
                    member = tar.extractfile(f"{snapshot_id}.json")
                    raw = member.read()
                    if _enc.is_encrypted(raw):
                        pw = _get_password(self.config, container)
                        if pw is None:
                            log(f"Warning: skipping encrypted snapshot {path.name} — no password configured")
                            continue
                        raw = EncryptionManager(self.config).decrypt_bytes(raw, pw)
                    data = json.loads(raw)
                image_ref = data.get("Config", {}).get("Image", "")
                repo_digests = data.get("RepoDigests") or []
                digest = repo_digests[0] if repo_digests else ""
                _labels = data.get("Config", {}).get("Labels") or {}
                version = (_labels.get("org.opencontainers.image.version", "")
                           or (image_ref.rsplit(":", 1)[-1] if ":" in image_ref else ""))
                snaps.append(Snapshot(path=path, timestamp=ts, image_ref=image_ref,
                                      digest=digest, version=version, volumes=[]))
            except Exception:
                log(f"Warning: skipping corrupt snapshot {path.name}")
        snaps.sort(key=lambda s: s.timestamp, reverse=True)
        return snaps

    def load(self, snapshot: Snapshot, password: str | None = None) -> dict:
        container = snapshot.path.parent.name
        _enc = EncryptionManager(self.config)

        def _decrypt(raw: bytes) -> bytes:
            if not _enc.is_encrypted(raw):
                return raw
            pw = password or _get_password(self.config, container)
            if pw is None:
                try:
                    parsed = json.loads(raw)
                    if isinstance(parsed, dict) and parsed.get("enc") == "v2":
                        raise RuntimeError(
                            f"Snapshot {snapshot.path.name} is encrypted but no "
                            "password is configured for this container."
                        )
                except (json.JSONDecodeError, UnicodeDecodeError):
                    pass
                return raw
            try:
                return EncryptionManager(self.config).decrypt_bytes(raw, pw)
            except Exception as e:
                log(f"Decryption failed for {snapshot.path.name}: {e}")
                raise

        snapshot_id = snapshot.path.name.removesuffix(".tar.gz")
        target = f"{snapshot_id}.json"
        raw = None
        with tarfile.open(snapshot.path, "r|gz") as tar:
            for member in tar:
                if member.name == target and member.isfile():
                    raw = tar.extractfile(member).read()
                    break
        if raw is None:
            raise RuntimeError(f"Snapshot bundle {snapshot.path.name} is missing {target}")
        return json.loads(_decrypt(raw))

    def load_volumes(self, snapshot: Snapshot) -> dict:
        empty: dict = {"volumes": [], "skipped": []}
        try:
            with tarfile.open(snapshot.path, "r:gz") as tar:
                try:
                    snapshot_id = snapshot.path.name.removesuffix(".tar.gz")
                    member = tar.extractfile(f"{snapshot_id}_volumes.json")
                    if member is None:
                        return empty
                    return json.loads(member.read())
                except KeyError:
                    return empty
        except Exception:
            return empty

    def to_spec(self, inspect_data: dict, pin_digest: bool = True) -> ContainerSpec:
        cfg = inspect_data.get("Config", {})
        host_cfg = inspect_data.get("HostConfig", {})
        net_settings = inspect_data.get("NetworkSettings", {})

        name = inspect_data["Name"].lstrip("/")

        repo_digests = inspect_data.get("RepoDigests") or []
        if pin_digest and repo_digests:
            image = repo_digests[0]
        else:
            image = cfg.get("Image", "")

        env = cfg.get("Env") or []
        binds = host_cfg.get("Binds") or []

        raw_ports = host_cfg.get("PortBindings") or {}
        port_bindings = []
        for container_port, host_bindings in raw_ports.items():
            for binding in (host_bindings or []):
                host_port = binding.get("HostPort", "")
                host_ip = binding.get("HostIp", "")
                if host_ip:
                    port_bindings.append(f"{host_ip}:{host_port}:{container_port}")
                else:
                    port_bindings.append(f"{host_port}:{container_port}")

        # Containers that share another container's network namespace
        # (e.g. Gluetun-routed stacks) have NetworkMode "container:<name>"
        # and an empty NetworkSettings.Networks.  Preserve the mode so
        # docker run --network container:<name> is reconstructed correctly.
        raw_network_mode = host_cfg.get("NetworkMode", "")
        if raw_network_mode.startswith("container:"):
            spec_network_mode = raw_network_mode
            networks = []
        else:
            spec_network_mode = ""
            networks = list((net_settings.get("Networks") or {}).keys())

        raw_labels = cfg.get("Labels") or {}
        labels = [f"{k}={v}" for k, v in raw_labels.items()]

        restart_policy = host_cfg.get("RestartPolicy") or {}
        restart_name = restart_policy.get("Name") or "no"
        max_retry = restart_policy.get("MaximumRetryCount", 0)
        if restart_name == "on-failure" and max_retry:
            restart = f"on-failure:{max_retry}"
        else:
            restart = restart_name

        entrypoint = cfg.get("Entrypoint") or []
        command = cfg.get("Cmd") or []
        cap_add = host_cfg.get("CapAdd") or []
        cap_drop = host_cfg.get("CapDrop") or []

        privileged = bool(host_cfg.get("Privileged", False))
        devices = []
        for d in (host_cfg.get("Devices") or []):
            hp = d.get("PathOnHost", "")
            cp_dev = d.get("PathInContainer", "")
            perms = d.get("CgroupPermissions", "")
            if hp and cp_dev:
                devices.append(f"{hp}:{cp_dev}:{perms}" if perms else f"{hp}:{cp_dev}")
        runtime = host_cfg.get("Runtime", "") or ""
        sysctls = dict(host_cfg.get("Sysctls") or {})
        security_opt = list(host_cfg.get("SecurityOpt") or [])
        user = cfg.get("User", "") or ""
        working_dir = cfg.get("WorkingDir", "") or ""
        ulimits = list(host_cfg.get("Ulimits") or [])
        shm_size = int(host_cfg.get("ShmSize") or 0)
        pid_mode = host_cfg.get("PidMode", "") or ""
        ipc_mode = host_cfg.get("IpcMode", "") or ""
        extra_hosts = list(host_cfg.get("ExtraHosts") or [])
        dns = list(host_cfg.get("Dns") or [])
        dns_search = list(host_cfg.get("DnsSearch") or [])
        dns_options = list(host_cfg.get("DnsOptions") or [])
        log_config = host_cfg.get("LogConfig") or {}
        log_driver = log_config.get("Type", "") or ""
        log_opts = dict(log_config.get("Config") or {})
        cpu_shares = int(host_cfg.get("CpuShares") or 0)
        memory = int(host_cfg.get("Memory") or 0)
        nano_cpus = int(host_cfg.get("NanoCpus") or 0)
        hostname = cfg.get("Hostname", "") or ""
        stop_signal = cfg.get("StopSignal", "") or ""
        group_add = list(host_cfg.get("GroupAdd") or [])
        init = bool(host_cfg.get("Init", False))
        readonly_rootfs = bool(host_cfg.get("ReadonlyRootfs", False))

        return ContainerSpec(
            name=name,
            image=image,
            env=env,
            binds=binds,
            port_bindings=port_bindings,
            networks=networks,
            labels=labels,
            restart=restart,
            entrypoint=entrypoint,
            command=command,
            network_mode=spec_network_mode,
            cap_add=cap_add,
            cap_drop=cap_drop,
            privileged=privileged,
            devices=devices,
            runtime=runtime,
            sysctls=sysctls,
            security_opt=security_opt,
            user=user,
            working_dir=working_dir,
            ulimits=ulimits,
            shm_size=shm_size,
            pid_mode=pid_mode,
            ipc_mode=ipc_mode,
            extra_hosts=extra_hosts,
            dns=dns,
            dns_search=dns_search,
            dns_options=dns_options,
            log_driver=log_driver,
            log_opts=log_opts,
            cpu_shares=cpu_shares,
            memory=memory,
            nano_cpus=nano_cpus,
            hostname=hostname,
            stop_signal=stop_signal,
            group_add=group_add,
            init=init,
            readonly_rootfs=readonly_rootfs,
        )

    def save_version(self, snapshot_id: str, staging_dir: Path, version_meta: dict) -> None:
        path = staging_dir / f"{snapshot_id}_version.json"
        path.write_text(json.dumps(version_meta))

    def load_version(self, snapshot: Snapshot) -> dict:
        snapshot_id = snapshot.path.name.removesuffix(".tar.gz")
        try:
            with tarfile.open(snapshot.path, "r:gz") as tar:
                m = tar.getmember(f"{snapshot_id}_version.json")
                return json.loads(tar.extractfile(m).read())
        except Exception:
            return {}


# === REGISTRY CLIENT ===

class RegistryError(Exception):
    pass


class RegistryClient:

    # Manifest list types listed first so multi-arch images return the index
    # digest, which matches what docker inspect stores in RepoDigests.
    _ACCEPT = ", ".join([
        "application/vnd.docker.distribution.manifest.list.v2+json",
        "application/vnd.oci.image.index.v1+json",
        "application/vnd.docker.distribution.manifest.v2+json",
        "application/vnd.oci.image.manifest.v1+json",
    ])

    @staticmethod
    def _parse_image_ref(image_ref: str) -> tuple:
        # Drop any digest suffix — we resolve by tag, not digest.
        if "@" in image_ref:
            image_ref = image_ref.split("@")[0]

        # Separate the tag: last colon that comes after the last slash.
        last_slash = image_ref.rfind("/")
        last_colon = image_ref.rfind(":")
        if last_colon > last_slash:
            ref, tag = image_ref[:last_colon], image_ref[last_colon + 1:]
        else:
            ref, tag = image_ref, "latest"

        parts = ref.split("/")
        first = parts[0]
        # A registry hostname contains a dot, a colon (port), or is "localhost".
        if "." in first or ":" in first or first == "localhost":
            registry = first
            repo = "/".join(parts[1:])
        else:
            registry = "registry-1.docker.io"
            # Single-component names are official images: nginx → library/nginx.
            repo = f"library/{parts[0]}" if len(parts) == 1 else "/".join(parts)

        return registry, repo, tag

    @staticmethod
    def _get_credentials(registry: str) -> tuple:
        docker_config = _INVOKING_HOME / ".docker" / "config.json"
        if not docker_config.exists():
            return None, None
        try:
            data = json.loads(docker_config.read_text())
            auths = data.get("auths", {})
            entry = auths.get(registry) or auths.get(f"https://{registry}")
            if not entry or not entry.get("auth"):
                return None, None
            username, password = base64.b64decode(entry["auth"]).decode().split(":", 1)
            return username, password
        except Exception:
            return None, None

    def _get_token(self, registry: str, www_auth: str) -> str:
        params = dict(re.findall(r'(\w+)="([^"]*)"', www_auth))
        realm = params.get("realm", "")
        qs = urllib.parse.urlencode({
            k: params[k] for k in ("service", "scope") if k in params
        })
        req = urllib.request.Request(f"{realm}?{qs}")
        username, password = self._get_credentials(registry)
        if username and password:
            creds = base64.b64encode(f"{username}:{password}".encode()).decode()
            req.add_header("Authorization", f"Basic {creds}")
        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read())
            token = data.get("token") or data.get("access_token", "")
            if not token:
                raise RegistryError(f"empty token from {realm}")
            return token
        except urllib.error.URLError as e:
            raise RegistryError(f"token fetch failed from {realm}: {e.reason}")

    def _head(self, url: str, extra_headers: dict = None) -> str:
        req = urllib.request.Request(url, method="HEAD")
        req.add_header("Accept", self._ACCEPT)
        for k, v in (extra_headers or {}).items():
            req.add_header(k, v)
        with urllib.request.urlopen(req, timeout=10) as resp:
            digest = resp.headers.get("Docker-Content-Digest", "")
            if not digest:
                raise RegistryError(f"no Docker-Content-Digest header from {url}")
            return digest

    def _get_json(self, url: str, extra_headers: dict = None) -> dict:
        req = urllib.request.Request(url)
        for k, v in (extra_headers or {}).items():
            req.add_header(k, v)
        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                body = resp.read()
        except urllib.error.HTTPError:
            raise
        except (urllib.error.URLError, TimeoutError, OSError) as e:
            raise RegistryError(f"request failed for {url}: {e}") from e
        if not body:
            raise RegistryError(f"empty response from {url}")
        try:
            return json.loads(body)
        except json.JSONDecodeError as e:
            raise RegistryError(f"invalid JSON from {url}: {e}") from e

    def get_remote_digest(self, image_ref: str) -> str:
        registry, repo, tag = self._parse_image_ref(image_ref)
        url = f"https://{registry}/v2/{repo}/manifests/{tag}"
        try:
            return self._head(url)
        except urllib.error.HTTPError as e:
            if e.code != 401:
                raise RegistryError(f"registry error for {image_ref}: {e.code} {e.reason}")
            token = self._get_token(registry, e.headers.get("WWW-Authenticate", ""))
            try:
                return self._head(url, {"Authorization": f"Bearer {token}"})
            except urllib.error.HTTPError as e2:
                if e2.code == 404:
                    raise RegistryError(f"tag not found for {image_ref}: {e2.code} {e2.reason}")
                raise RegistryError(f"auth failed for {image_ref}: {e2.code} {e2.reason}")
        except (urllib.error.URLError, TimeoutError, OSError) as e:
            raise RegistryError(f"registry unreachable for {image_ref}: {e}")

    def get_local_digest(self, inspect_data: dict) -> str:
        digests = inspect_data.get("RepoDigests") or []
        return digests[0] if digests else None

    def list_tags(self, image_ref: str) -> list:
        """Return all available tags for the image, sorted alphabetically."""
        registry, repo, _ = self._parse_image_ref(image_ref)
        url = f"https://{registry}/v2/{repo}/tags/list"
        try:
            data = self._get_json(url)
        except urllib.error.HTTPError as e:
            if e.code != 401:
                raise RegistryError(f"registry error for {image_ref}: {e.code} {e.reason}")
            token = self._get_token(registry, e.headers.get("WWW-Authenticate", ""))
            try:
                data = self._get_json(url, {"Authorization": f"Bearer {token}"})
            except urllib.error.HTTPError as e2:
                raise RegistryError(f"auth failed for {image_ref}: {e2.code} {e2.reason}")
        except (urllib.error.URLError, TimeoutError, OSError) as e:
            raise RegistryError(f"registry unreachable for {image_ref}: {e}")
        return sorted(data.get("tags") or [])

    @staticmethod
    def _replace_tag(image_ref: str, new_tag: str) -> str:
        """Return image_ref with its tag replaced by new_tag."""
        if "@" in image_ref:
            image_ref = image_ref.split("@")[0]
        last_slash = image_ref.rfind("/")
        last_colon = image_ref.rfind(":")
        if last_colon > last_slash:
            return image_ref[:last_colon] + ":" + new_tag
        return image_ref + ":" + new_tag

    # Tags that look like version strings but aren't pinnable release versions.
    _NON_VERSION_TAGS = frozenset({
        "latest", "stable", "edge", "nightly", "main", "master",
        "develop", "development", "beta", "alpha", "rc", "release",
        "test", "testing", "canary", "next", "current",
        "prod", "production", "snapshot",
    })

    @staticmethod
    def _version_key(tag: str) -> tuple:
        """Sort key for semantic version strings, handles leading 'v'."""
        parts = re.split(r"[.\-]", tag.lstrip("v"))
        # Wrap each part as (0, int) or (1, str) so numeric and string parts
        # are never compared directly against each other across different tags.
        return tuple((0, int(p)) if p.isdigit() else (1, p) for p in parts)

    def _fetch_hub_dates(self, namespace: str, repo: str) -> dict:
        """Return {tag: 'YYYY-MM-DD'} from the Docker Hub REST API.

        Paginates up to 5 pages (500 tags). Returns empty dict on any failure
        so callers degrade gracefully to version-sort-only mode.
        """
        dates = {}
        url = (f"https://hub.docker.com/v2/repositories/{namespace}/{repo}/tags/"
               f"?page_size=100&ordering=last_updated")
        pages = 0
        while url and pages < 5:
            try:
                data = self._get_json(url)
            except Exception:
                break
            for entry in data.get("results") or []:
                name = entry.get("name", "")
                pushed = entry.get("tag_last_pushed") or ""
                if name and pushed:
                    dates[name] = pushed[:10]
            url = data.get("next") or ""
            pages += 1
        return dates

    def _fetch_github_dates(self, org: str, repo: str) -> dict:
        """Return {tag: 'YYYY-MM-DD'} from the GitHub Releases API.

        Preserves the tag name exactly as GitHub stores it (e.g. 'v1.12.2'),
        because ghcr.io images mirror the GitHub release tag as the Docker tag.
        Returns empty dict on failure, including GitHub rate-limit 403s.
        """
        url = f"https://api.github.com/repos/{org}/{repo}/releases?per_page=100"
        try:
            entries = self._get_json(url, {"Accept": "application/vnd.github+json"})
        except Exception:
            return {}
        dates = {}
        for entry in entries if isinstance(entries, list) else []:
            tag = entry.get("tag_name") or ""
            published = entry.get("published_at") or ""
            if tag and published:
                dates[tag] = published[:10]
        return dates

    def list_versions(self, image_ref: str, limit: int | None = None) -> list:
        """Return version tags for the image, newest first.

        Each entry is (tag, date_str) where date_str is 'YYYY-MM-DD' or '?'
        when no date source is available for the registry. Tags are filtered
        to version-like strings (start with a digit or 'v'+digit, not in
        _NON_VERSION_TAGS). Sorted by date descending when dates are available,
        falling back to semantic version order otherwise. Pass limit to cap results.
        """
        registry, repo, _ = self._parse_image_ref(image_ref)

        # Fetch dates first for registries that support it. The dates APIs
        # return tags ordered by push date (newest first), making them a better
        # source of recent tags than the registry /tags/list endpoint, which
        # paginates alphabetically and would only return the first page.
        if registry == "registry-1.docker.io":
            parts = repo.split("/", 1)
            namespace = parts[0]
            repo_name = parts[1] if len(parts) == 2 else parts[0]
            dates = self._fetch_hub_dates(namespace, repo_name)
        elif registry == "ghcr.io":
            parts = repo.split("/", 1)
            dates = self._fetch_github_dates(parts[0], parts[1]) if len(parts) == 2 else {}
        else:
            dates = {}

        if dates:
            # Use the dates dict as the tag source — it already contains the
            # most recently pushed tags, so no need to call list_tags at all.
            version_tags = [
                t for t in dates
                if t.lstrip("v")[:1].isdigit() and t.lower() not in self._NON_VERSION_TAGS
            ]
            combined = sorted(
                [(t, dates[t]) for t in version_tags],
                key=lambda x: x[1],
                reverse=True,
            )
        else:
            # No date source available — fall back to the registry tag list.
            try:
                all_tags = self.list_tags(image_ref)
            except RegistryError:
                return []
            version_tags = [
                t for t in all_tags
                if t.lstrip("v")[:1].isdigit() and t.lower() not in self._NON_VERSION_TAGS
            ]
            combined = sorted(
                [(t, "?") for t in version_tags],
                key=lambda x: RegistryClient._version_key(x[0]),
                reverse=True,
            )

        return combined if not limit else combined[:limit]

    def has_update(self, inspect_data: dict, pinned_tag: str = "",
                   image_ref_override: str = "") -> bool:
        image_ref = image_ref_override or inspect_data.get("Config", {}).get("Image", "")
        if not image_ref:
            return False

        if pinned_tag:
            pinned_ref = self._replace_tag(image_ref, pinned_tag)
            pinned_digest = self.get_remote_digest(pinned_ref)
            local = self.get_local_digest(inspect_data)
            if local:
                local_hash = local.split("@")[-1]
                if local_hash != pinned_digest:
                    return True
            latest_ref = self._replace_tag(image_ref, "latest")
            latest_digest = self.get_remote_digest(latest_ref)
            return pinned_digest != latest_digest

        local = self.get_local_digest(inspect_data)
        if not local:
            # Locally-built image with no registry digest — can't compare.
            return False
        # Let RegistryError propagate so callers can log a visible warning.
        remote = self.get_remote_digest(image_ref)
        # local is "nginx@sha256:abc", remote is "sha256:abc" — compare hash only.
        local_hash = local.split("@")[-1]
        return remote != local_hash


# === HEALTH CHECKER ===

def _diagnose_bind_address(container: str, docker: "DockerClient") -> None:
    """Log a hint if the container has listening ports bound to a specific
    network interface rather than localhost or 0.0.0.0.

    This catches the pattern where a server update changes the bind address from
    0.0.0.0 to a specific container IP (e.g. via HOSTNAME env var), causing the
    health check probe — which always targets localhost — to get ECONNREFUSED
    even though the server is running and healthy from the app's perspective.
    """
    # Addresses the health check CAN reach via localhost — no action needed.
    _REACHABLE = {
        "0100007F",                            # 127.0.0.1
        "00000000",                            # 0.0.0.0 (IPv4 any)
        "00000000000000000000000001000000",    # ::1
        "00000000000000000000000000000000",    # :: (IPv6 any)
    }
    non_local_ports: list[int] = []
    for tcp_file in ("/proc/net/tcp", "/proc/net/tcp6"):
        try:
            result = docker._run(["exec", container, "cat", tcp_file])
        except DockerError:
            continue
        for line in result.stdout.splitlines()[1:]:  # skip header row
            parts = line.split()
            if len(parts) < 4 or parts[3] != "0A":  # 0A = TCP LISTEN
                continue
            addr_port = parts[1]
            colon = addr_port.rfind(":")
            if colon == -1:
                continue
            addr = addr_port[:colon]
            try:
                port = int(addr_port[colon + 1:], 16)
            except ValueError:
                continue
            if addr not in _REACHABLE:
                non_local_ports.append(port)
    if non_local_ports:
        ports_str = ", ".join(str(p) for p in sorted(set(non_local_ports)))
        log(
            f"[health {container}] HINT: port(s) {ports_str} are listening on a "
            f"specific network interface (not localhost or 0.0.0.0) — the health "
            f"check probe targets localhost and cannot reach them. This often "
            f"happens when a new image version reads HOSTNAME from the environment "
            f"and uses it as the bind address. Fix: add HOSTNAME=0.0.0.0 to the "
            f"container's environment variables."
        )


class HealthChecker:
    _POLL_INTERVAL = 5  # seconds between polls

    def __init__(self, docker: DockerClient, config: Config) -> None:
        self.docker = docker
        self.config = config

    def wait_healthy(self, container: str, timeout_sec: int) -> bool:
        deadline = time.monotonic() + timeout_sec
        while True:
            try:
                status = self.docker.health(container)
            except DockerError as e:
                log(f"[health {container}] error polling: {e}")
                return False

            remaining = deadline - time.monotonic()
            elapsed = int(timeout_sec - remaining)
            log(f"[health {container}] {status} ({elapsed}s elapsed)")

            if status in ("healthy", "running"):
                return True
            if status in ("unhealthy", "exited", "dead"):
                return False

            # "starting" or unknown — keep polling if time remains
            if remaining <= 0:
                log(f"[health {container}] timed out after {timeout_sec}s")
                return False
            time.sleep(min(self._POLL_INTERVAL, max(remaining, 0.05)))


# === ENGINE ===

class Engine:

    def __init__(self, config: Config) -> None:
        self.config = config
        self.docker = DockerClient()
        self.registry = RegistryClient()
        self.sm = SnapshotManager(config)
        self.hc = HealthChecker(self.docker, config)

    def _get_stack_siblings(self, container: str, inspect_data: dict) -> tuple:
        """Return (gateway_siblings, dependent_siblings).

        gateway_siblings is the container whose network namespace the target
        shares (e.g. Gluetun).  It must be started and healthy before any
        dependent sibling can join its network namespace.
        """
        if not self.config.restart_stack_siblings:
            return [], []
        labels = inspect_data.get("Config", {}).get("Labels") or {}
        project = labels.get("com.docker.compose.project")
        if not project:
            return [], []
        try:
            result = self.docker._run([
                "ps", "--filter",
                f"label=com.docker.compose.project={project}",
                "--format", "{{.Names}}",
            ])
            all_siblings = [n.strip() for n in result.stdout.splitlines()
                            if n.strip() and n.strip() != container]
        except DockerError:
            return [], []

        # Detect the gateway: the container referenced in the target's NetworkMode.
        # DockerClient.inspect() already resolved the container ID to a name.
        network_mode = (inspect_data.get("HostConfig") or {}).get("NetworkMode", "")
        gateway_name = network_mode.split(":", 1)[1] if network_mode.startswith("container:") else ""

        if gateway_name and gateway_name in all_siblings:
            return [gateway_name], [s for s in all_siblings if s != gateway_name]
        return [], all_siblings

    def _wait_siblings_running(self, siblings: list, prefix: str, timeout_sec: int) -> None:
        deadline = time.monotonic() + timeout_sec
        while time.monotonic() < deadline:
            statuses = []
            for s in siblings:
                try:
                    statuses.append(self.docker.health(s))
                except DockerError:
                    statuses.append("unknown")
            if all(st in ("running", "healthy") for st in statuses):
                log(f"{prefix} all siblings running")
                return
            time.sleep(2)
        log(f"{prefix} siblings not all ready after {timeout_sec}s "
            "— starting target anyway")

    def _backup_volumes(self, container: str, snapshot_id: str,
                        inspect_data: dict, staging_dir: Path,
                        paused: bool = False,
                        password_fn: "callable | None" = None,
                        version_meta: dict | None = None,
                        target_mount: "str | None" = None) -> None:
        prefix = f"[backup {container}]"
        if not self.config.volume_backup_enabled:
            log(f"{prefix} volume backup disabled globally — skipping")
            return

        binds = inspect_data.get("HostConfig", {}).get("Binds") or []
        named_vols = _get_named_volumes(inspect_data)
        if not binds and not named_vols:
            log(f"{prefix} no bind mounts or named volumes — skipping volume backup")
            return

        rules = self.config.volume_backup.get(container, {})
        if not rules.get("enabled", True):
            log(f"{prefix} volume backup disabled for {container} — skipping")
            return

        if paused:
            log(f"{prefix} container is paused — backup will be consistent")
        else:
            log(f"{prefix} container is live — backup may be inconsistent")
        skip_mounts      = set(rules.get("skip_mounts", []))
        include_only     = rules.get("include_only_mounts")  # None means archive all
        exclude_patterns = rules.get("exclude", [])
        mount_paths      = rules.get("mount_paths", {})  # container_path -> archive_dir base
        container_save_path = rules.get("save_path")

        def _tar_filter(tarinfo):
            for pat in exclude_patterns:
                if fnmatch.fnmatch(tarinfo.name, pat):
                    return None
            return tarinfo

        written = []
        skipped = []

        for bind in binds:
            parts = bind.split(":")
            host_path, container_path = parts[0], parts[1]

            if not host_path.startswith("/"):
                # Named volume reference in Binds (e.g. "myvolume:/path") — handled by named_vols loop
                continue

            if target_mount is not None and container_path != target_mount:
                continue

            if container_path in skip_mounts:
                log(f"{prefix} skipping {container_path} (skip_mounts rule)")
                skipped.append({"container_path": container_path, "host_path": host_path,
                                "vol_name": "", "reason": "skip_mounts rule"})
                continue
            if include_only is not None and container_path not in include_only:
                log(f"{prefix} skipping {container_path} (not in include_only_mounts)")
                skipped.append({"container_path": container_path, "host_path": host_path,
                                "vol_name": "", "reason": "not in include_only_mounts"})
                continue
            p = Path(host_path)
            if not p.exists():
                log(f"{prefix} host path not found, skipping: {host_path}")
                skipped.append({"container_path": container_path, "host_path": host_path,
                                "vol_name": "", "reason": "host path not found"})
                continue
            if not (p.is_dir() or p.is_file()):
                log(f"{prefix} skipping special file (socket/device): {host_path}")
                skipped.append({"container_path": container_path, "host_path": host_path,
                                "vol_name": "", "reason": "special file (socket/device)"})
                continue

            # Resolve archive destination: mount_paths > save_path > snapshot_dir
            if container_path in mount_paths:
                archive_base = Path(mount_paths[container_path])
                archive_dir_val = str(archive_base)
            elif container_save_path:
                archive_base = Path(container_save_path)
                archive_dir_val = str(archive_base)
            else:
                archive_base = self.config.snapshot_dir_for(container)
                archive_dir_val = None

            archive_name = f"{snapshot_id}_{_sanitize_mount_name(container_path)}.tar.gz"
            archive_path = archive_base / container / archive_name

            log(f"{prefix} archiving {host_path} → {archive_name}")
            try:
                archive_path.parent.mkdir(parents=True, exist_ok=True)
                archive_path.parent.chmod(self.config.snapshot_dir_mode_for(container))
                os.chown(archive_path.parent, _INVOKING_UID, _INVOKING_GID)
                with tarfile.open(archive_path, "w:gz") as tar:
                    tar.add(host_path, arcname=host_path,
                            filter=_tar_filter if exclude_patterns else None)
                    if version_meta:
                        import io
                        _meta_bytes = json.dumps({
                            "container": container,
                            "mount": container_path,
                            "snapshot_id": snapshot_id,
                            **version_meta,
                        }).encode()
                        _ti = tarfile.TarInfo(name="_meta.json")
                        _ti.size = len(_meta_bytes)
                        tar.addfile(_ti, io.BytesIO(_meta_bytes))
                if password_fn is not None:
                    pw = password_fn(container_path)
                    if pw is not None:
                        tmp = archive_path.with_suffix(".tmp")
                        archive_path.rename(tmp)
                        try:
                            EncryptionManager(self.config).encrypt_file(tmp, archive_path, pw)
                            tmp.unlink()
                            log(f"{prefix} encrypted {archive_name}")
                        except Exception as e:
                            log(f"{prefix} encrypt failed for {archive_name}: {e} — leaving temp for manual recovery")
                if archive_path.exists():
                    archive_path.chmod(self.config.snapshot_file_mode_for(container))
                written.append({
                    "container_path": container_path,
                    "host_path": host_path,
                    "vol_name": "",
                    "archive_name": archive_name,
                    "archive_dir": archive_dir_val,
                })
            except Exception as e:
                log(f"{prefix} volume backup failed for {container_path}: {e}")
                try:
                    if archive_path.exists():
                        archive_path.unlink()
                except Exception:
                    pass
                skipped.append({"container_path": container_path, "host_path": host_path,
                                "vol_name": "", "reason": "archive failed"})

        for vol in named_vols:
            vol_name      = vol["Name"]
            source        = vol["Source"]
            container_path = vol["Destination"]

            if target_mount is not None and container_path != target_mount:
                continue

            if container_path in skip_mounts:
                log(f"{prefix} skipping named volume {vol_name} at {container_path} (skip_mounts rule)")
                skipped.append({"container_path": container_path, "host_path": source,
                                "vol_name": vol_name, "reason": "skip_mounts rule"})
                continue
            if include_only is not None and container_path not in include_only:
                log(f"{prefix} skipping named volume {vol_name} at {container_path} (not in include_only_mounts)")
                skipped.append({"container_path": container_path, "host_path": source,
                                "vol_name": vol_name, "reason": "not in include_only_mounts"})
                continue
            if not source:
                log(f"{prefix} skipping named volume {vol_name}: non-local driver (no Source path)")
                skipped.append({"container_path": container_path, "host_path": "",
                                "vol_name": vol_name, "reason": "non-local driver"})
                continue
            p = Path(source)
            if not p.exists():
                log(f"{prefix} named volume source not found, skipping: {source}")
                skipped.append({"container_path": container_path, "host_path": source,
                                "vol_name": vol_name, "reason": "source path not found"})
                continue

            # Resolve archive destination: mount_paths > save_path > snapshot_dir
            if container_path in mount_paths:
                archive_base = Path(mount_paths[container_path])
                archive_dir_val = str(archive_base)
            elif container_save_path:
                archive_base = Path(container_save_path)
                archive_dir_val = str(archive_base)
            else:
                archive_base = self.config.snapshot_dir_for(container)
                archive_dir_val = None

            archive_name = f"{snapshot_id}_{_sanitize_mount_name(container_path)}.tar.gz"
            archive_path = archive_base / container / archive_name

            log(f"{prefix} archiving named volume {vol_name} ({source}) → {archive_name}")
            try:
                archive_path.parent.mkdir(parents=True, exist_ok=True)
                archive_path.parent.chmod(self.config.snapshot_dir_mode_for(container))
                os.chown(archive_path.parent, _INVOKING_UID, _INVOKING_GID)
                with tarfile.open(archive_path, "w:gz") as tar:
                    tar.add(source, arcname=source,
                            filter=_tar_filter if exclude_patterns else None)
                    if version_meta:
                        import io
                        _meta_bytes = json.dumps({
                            "container": container,
                            "mount": container_path,
                            "snapshot_id": snapshot_id,
                            **version_meta,
                        }).encode()
                        _ti = tarfile.TarInfo(name="_meta.json")
                        _ti.size = len(_meta_bytes)
                        tar.addfile(_ti, io.BytesIO(_meta_bytes))
                if password_fn is not None:
                    pw = password_fn(container_path)
                    if pw is not None:
                        tmp = archive_path.with_suffix(".tmp")
                        archive_path.rename(tmp)
                        try:
                            EncryptionManager(self.config).encrypt_file(tmp, archive_path, pw)
                            tmp.unlink()
                            log(f"{prefix} encrypted {archive_name}")
                        except Exception as e:
                            log(f"{prefix} encrypt failed for {archive_name}: {e} — leaving temp for manual recovery")
                if archive_path.exists():
                    archive_path.chmod(self.config.snapshot_file_mode_for(container))
                written.append({
                    "container_path": container_path,
                    "host_path": source,
                    "vol_name": vol_name,
                    "archive_name": archive_name,
                    "archive_dir": archive_dir_val,
                })
            except Exception as e:
                log(f"{prefix} volume backup failed for named volume {vol_name}: {e}")
                try:
                    if archive_path.exists():
                        archive_path.unlink()
                except Exception:
                    pass
                skipped.append({"container_path": container_path, "host_path": source,
                                "vol_name": vol_name, "reason": "archive failed"})

        try:
            (staging_dir / f"{snapshot_id}_volumes.json").write_text(
                json.dumps({"volumes": written, "skipped": skipped}, indent=2) + "\n"
            )
            log(f"{prefix} volume index: {len(written)} archived, {len(skipped)} skipped")
        except Exception as e:
            log(f"{prefix} could not write volume index: {e}")

    def _save_meta(self, container: str, snapshot_id: str, inspect_data: dict,
                   staging_dir: Path, password: "str | None" = None) -> None:
        prefix = f"[meta {container}]"

        # Compose file: resolve working dir, then find the compose file inside it.
        labels = inspect_data.get("Config", {}).get("Labels") or {}
        working_dir = labels.get("com.docker.compose.project.working_dir", "")
        config_files_raw = labels.get("com.docker.compose.project.config_files", "")
        if working_dir:
            resolved_dir = self._resolve_compose_dir(working_dir, prefix)
            if resolved_dir:
                compose_file = None
                if config_files_raw:
                    for raw_path in config_files_raw.split(","):
                        candidate = Path(raw_path.strip())
                        if candidate.is_file():
                            compose_file = candidate
                            break
                        # Rewrite Portainer internal path using resolved dir
                        if working_dir and raw_path.strip().startswith(working_dir):
                            rel = raw_path.strip()[len(working_dir):].lstrip("/")
                            candidate = Path(resolved_dir) / rel
                            if candidate.is_file():
                                compose_file = candidate
                                break
                if compose_file is None:
                    for name in ("compose.yaml", "compose.yml",
                                 "docker-compose.yaml", "docker-compose.yml"):
                        candidate = Path(resolved_dir) / name
                        if candidate.is_file():
                            compose_file = candidate
                            break
                if compose_file:
                    try:
                        content = compose_file.read_bytes()
                        if password is not None:
                            content = EncryptionManager(self.config).encrypt_bytes(content, password)
                        (staging_dir / f"{snapshot_id}_compose.yaml").write_bytes(content)
                        log(f"{prefix} captured compose file from {compose_file}")
                    except Exception as e:
                        log(f"{prefix} could not capture compose file: {e}")

        # Env overrides: diff container env against image-baked defaults.
        if container in self.config.env_backup_disabled:
            log(f"{prefix} env backup disabled for {container} — skipping")
            return
        image_id = inspect_data.get("Image", "")
        container_env = list(inspect_data.get("Config", {}).get("Env") or [])
        if image_id and container_env:
            try:
                result = self.docker._run(["image", "inspect", image_id])
                image_data = json.loads(result.stdout)
                if isinstance(image_data, list) and image_data:
                    image_data = image_data[0]
                image_env = set(image_data.get("Config", {}).get("Env") or [])
                overrides = [e for e in container_env if e not in image_env]
                if overrides:
                    content = ("\n".join(overrides) + "\n").encode()
                    if password is not None:
                        content = EncryptionManager(self.config).encrypt_bytes(content, password)
                    (staging_dir / f"{snapshot_id}_env.env").write_bytes(content)
                    log(f"{prefix} recorded {len(overrides)} env override(s)")
            except Exception as e:
                log(f"{prefix} could not compute env overrides: {e}")

    def _save_image(self, container: str, snapshot_id: str, inspect_data: dict,
                    staging_dir: Path) -> None:
        prefix = f"[image {container}]"
        if not self.config.image_export_enabled:
            log(f"{prefix} image export disabled globally — skipping")
            return
        if container in self.config.image_export_disabled:
            log(f"{prefix} image export disabled for {container} — skipping")
            return

        image_id = inspect_data.get("Image", "")
        if not image_id:
            log(f"{prefix} no image ID in inspect data — skipping")
            return

        image_tar = staging_dir / f"{snapshot_id}_image.tar"
        log(f"{prefix} saving image {image_id[:19]}...")
        try:
            self.docker._run(["save", image_id, "-o", str(image_tar)])
            image_tar.chmod(self.config.snapshot_file_mode_for(container))
            size_mb = image_tar.stat().st_size / 1_048_576
            log(f"{prefix} image saved: {image_tar} ({size_mb:.0f} MB)")
        except Exception as e:
            log(f"{prefix} image save failed (skipping): {e}")
            try:
                if image_tar.exists():
                    image_tar.unlink()
            except Exception:
                pass

    def _restore_volumes(self, container: str, snapshot: "Snapshot",
                         ext_overrides: dict | None = None) -> None:
        prefix = f"[restore {container}]"
        vol_data = self.sm.load_volumes(snapshot)
        volumes = vol_data.get("volumes", [])
        if not volumes:
            log(f"{prefix} no volume archives recorded for this snapshot — skipping restore")
            return

        for entry in volumes:
            cp = entry["container_path"]
            archive_name = entry["archive_name"]
            archive_dir = entry.get("archive_dir")

            if ext_overrides is not None and cp in ext_overrides:
                override = ext_overrides[cp]
                if override is None:
                    log(f"{prefix} skipping volume {cp} (user choice)")
                    continue
                vol_path = Path(override)
            else:
                vol_path = None
                if archive_dir:
                    candidate = Path(archive_dir) / container / archive_name
                    if candidate.exists():
                        vol_path = candidate
                if vol_path is None:
                    candidate = self.config.snapshot_dir_for(container) / container / archive_name
                    if candidate.exists():
                        vol_path = candidate

                if vol_path is None:
                    if ext_overrides is not None:
                        located = _prompt_missing_volume(cp, archive_name)
                        if located:
                            vol_path = located
                        else:
                            log(f"{prefix} skipping volume {cp} (user choice)")
                            continue
                    else:
                        log(f"{prefix} volume archive not found for {cp}: {archive_name} — skipping")
                        continue

            vol_name_entry = entry.get("vol_name", "")
            if vol_name_entry:
                try:
                    self.docker._run(["volume", "inspect", vol_name_entry])
                except DockerError:
                    log(f"{prefix} volume {vol_name_entry} not found — creating")
                    try:
                        self.docker._run(["volume", "create", vol_name_entry])
                    except DockerError as e:
                        log(f"{prefix} could not create volume {vol_name_entry}: {e} — skipping restore for {cp}")
                        continue

            log(f"{prefix} restoring volume {cp} from {vol_path.name}")
            try:
                if _is_encrypted_file(vol_path):
                    pw = _get_password(self.config, container, mount=cp)
                    if pw is None:
                        raise RuntimeError(f"Volume archive for {cp} is encrypted but no password is configured")
                    dec_tmp = vol_path.with_suffix(".dec_tmp")
                    EncryptionManager(self.config).decrypt_file(vol_path, dec_tmp, pw)
                    try:
                        with tarfile.open(dec_tmp, "r:gz") as tar:
                            tar.extractall(path="/")
                    finally:
                        dec_tmp.unlink(missing_ok=True)
                else:
                    with tarfile.open(vol_path, "r:gz") as tar:
                        tar.extractall(path="/")
                log(f"{prefix} volume restore complete: {cp}")
            except Exception as e:
                log(f"{prefix} volume restore failed for {cp}: {e}")

    def rollback(self, container: str, snapshot: Snapshot,
                 reason: str = "manual",
                 ext_overrides: dict | None = None) -> bool:
        ts = snapshot.timestamp.strftime("%Y-%m-%d %H:%M")
        prefix = f"[ROLLBACK {container}]"
        log(f"{prefix} restoring snapshot {ts} (reason: {reason})")

        # Capture current container version for post-rollback summary (before we stop it)
        try:
            _cur_data = self.docker.inspect(container)
            _cur_labels = _cur_data.get("Config", {}).get("Labels") or {}
            _cur_image = _cur_data.get("Config", {}).get("Image", "")
            _cur_tag = "" if "@sha256:" in _cur_image else _cur_image.rsplit(":", 1)[-1]
            _cur_version = (_cur_tag if _cur_tag and _cur_tag != "latest"
                            else _cur_labels.get("org.opencontainers.image.version", "") or _cur_tag)
            _cur_digests = _cur_data.get("RepoDigests") or []
            _cur_hash = (_cur_digests[0].split("@sha256:")[-1][:12]
                         if _cur_digests and "@sha256:" in _cur_digests[0] else "")
        except DockerError:
            _cur_version, _cur_tag, _cur_hash = "", "", ""
        # Fallback to saved version from config if live inspect didn't yield one
        if not _cur_version or not _cur_hash:
            _saved = self.config.container_versions.get(container, {})
            if not _cur_version:
                _cur_version = _saved.get("version", "")
            if not _cur_hash:
                _raw = _saved.get("digest", "")
                _cur_hash = _raw.split("@sha256:")[-1][:12] if _raw else ""

        # Step 1+2: load snapshot and build pinned spec
        snap_pw = _get_password(self.config, container)
        inspect_data = self.sm.load(snapshot, password=snap_pw)
        log(f"{prefix} snapshot loaded")

        # Extract snapshot version info from sidecar for post-rollback summary (what we're restoring to)
        _snap_meta = self.sm.load_version(snapshot)
        _snap_version = _snap_meta.get("version", "") or snapshot.version
        _snap_hash = _snap_meta.get("digest", "").split("@sha256:")[-1][:12] if _snap_meta.get("digest") else ""
        _snap_image = inspect_data.get("Config", {}).get("Image", "") if inspect_data else snapshot.image_ref
        _snap_tag = "" if "@sha256:" in _snap_image else _snap_image.rsplit(":", 1)[-1]
        spec = self.sm.to_spec(inspect_data, pin_digest=True)

        # Detect stack siblings from the snapshot's inspect data
        gateway_siblings, dependent_siblings = self._get_stack_siblings(container, inspect_data)
        all_siblings = gateway_siblings + dependent_siblings
        if gateway_siblings:
            log(f"{prefix} network gateway: {', '.join(gateway_siblings)}")
        if dependent_siblings:
            log(f"{prefix} stack siblings: {', '.join(dependent_siblings)}")

        # Step 2b: load image from local archive if available (enables offline restore)
        snap_dir = self.config.snapshot_dir_for(container) / container
        snapshot_id = snapshot.path.name.removesuffix(".tar.gz")
        image_tar = snap_dir / f"{snapshot_id}_image.tar"
        if image_tar.exists():
            log(f"{prefix} loading image from archive {image_tar}")
            try:
                self.docker._run(["load", "-i", str(image_tar)])
                log(f"{prefix} image loaded from archive")
            except DockerError as e:
                log(f"{prefix} image load failed ({e}) — will attempt registry pull")

        # Step 3: pull pinned image only if not already local
        log(f"{prefix} checking for image {spec.image}")
        try:
            self.docker._run(["image", "inspect", spec.image])
            log(f"{prefix} image already local")
        except DockerError:
            log(f"{prefix} pulling {spec.image}")
            try:
                self.docker.pull(spec.image)
            except DockerError as e:
                log(f"{prefix} failed to pull image: {e}")
                return False

        # Step 4: stop target (may already be stopped — not fatal)
        log(f"{prefix} stopping container")
        try:
            self.docker.stop(container)
        except DockerError:
            pass

        # Step 4b: stop siblings
        for sibling in all_siblings:
            log(f"{prefix} stopping sibling {sibling}")
            try:
                self.docker.stop(sibling)
            except DockerError as e:
                log(f"{prefix} could not stop sibling {sibling}: {e}")

        # Step 5: remove target — container may already be gone if this rollback
        # was triggered by a failed docker run (update removes it before the
        # run attempt, so it no longer exists when rollback fires).
        log(f"{prefix} removing container")
        try:
            self.docker.remove(container)
        except DockerError as e:
            try:
                self.docker._run(["inspect", container])
                # inspect succeeded — container exists but can't be removed
                log(f"{prefix} remove failed: {e}")
                return False
            except DockerError:
                log(f"{prefix} container already gone — continuing rollback")

        # Volume restore hook (between remove and recreate)
        self._restore_volumes(container, snapshot, ext_overrides)

        # Step 5b: start gateway first and wait for it, then start dependents
        for sibling in gateway_siblings:
            log(f"{prefix} starting gateway {sibling}")
            try:
                self.docker.start(sibling)
            except DockerError as e:
                log(f"{prefix} could not start gateway {sibling}: {e}")
        if gateway_siblings:
            self._wait_siblings_running(
                gateway_siblings, prefix, self.config.gateway_wait_sec
            )
        for sibling in dependent_siblings:
            log(f"{prefix} starting sibling {sibling}")
            try:
                self.docker.start(sibling)
            except DockerError as e:
                log(f"{prefix} could not start sibling {sibling}: {e}")
        if dependent_siblings:
            self._wait_siblings_running(
                dependent_siblings, prefix, self.config.sibling_wait_sec
            )

        # Step 6: recreate from snapshot spec
        log(f"{prefix} starting container from snapshot")
        try:
            self.docker.run(spec)
        except DockerError as e:
            log(f"{prefix} start failed: {e}")
            return False

        # Step 7: health check
        log(f"{prefix} waiting for healthy state "
            f"(timeout: {self.config.health_timeout_sec}s)")
        healthy = self.hc.wait_healthy(container, self.config.health_timeout_sec)

        # Step 8: log outcome
        if healthy:
            log(f"{prefix} rollback successful")
            print(f"\nRolled back {container}")
            if _cur_version or _snap_version:
                if _cur_version != _snap_version:
                    print(f"  was: {_cur_version or '?'}  →  now: {_snap_version or '?'}")
                elif _cur_tag != _snap_tag and _snap_tag not in ("latest", ""):
                    print(f"  tag: {_cur_tag or '?'}  →  {_snap_tag}")
                else:
                    print(f"  version: {_snap_version or '?'}  (restoring same version)")
            if _cur_hash and _snap_hash:
                if _cur_hash == _snap_hash:
                    print(f"  sha256: ...{_snap_hash}  (digest unchanged)")
                else:
                    print(f"  sha256: ...{_cur_hash}  →  ...{_snap_hash}")
            # Update stored version in config
            if _snap_meta:
                self.config.container_versions[container] = _snap_meta
                self.config.save()
            return True
        log(f"{prefix} rollback failed — container did not reach healthy state")
        return False

    def update(self, container: str, auto_rollback: bool = True, tag: str = "") -> bool:
        prefix = f"[UPDATE {container}]"

        # Pre-flight: verify snapshot dir is writable before touching the container
        snap_dir = self.config.snapshot_dir_for(container) / container
        err = _probe_snapshot_dir(snap_dir)
        if err:
            log(f"{prefix} snapshot dir not writable — aborting: {err}")
            return False

        # Step 1: inspect
        log(f"{prefix} inspecting current container")
        try:
            inspect_data = self.docker.inspect(container)
        except DockerError as e:
            log(f"{prefix} failed to inspect: {e}")
            return False

        # Capture pre-update version info for the completion summary
        _was_labels = inspect_data.get("Config", {}).get("Labels") or {}
        _was_image = inspect_data.get("Config", {}).get("Image", "")
        _was_tag = "" if "@sha256:" in _was_image else _was_image.rsplit(":", 1)[-1]
        _was_version = (_was_tag if _was_tag and _was_tag != "latest"
                        else _was_labels.get("org.opencontainers.image.version", "") or _was_tag)
        _was_digests = inspect_data.get("RepoDigests") or []
        _was_hash = (_was_digests[0].split("@sha256:")[-1][:12]
                     if _was_digests and "@sha256:" in _was_digests[0] else "")

        # Fallback to saved version from config if live inspect didn't yield one
        if not _was_version or not _was_hash:
            _saved = self.config.container_versions.get(container, {})
            if not _was_version:
                _was_version = _saved.get("version", "")
            if not _was_hash:
                _raw = _saved.get("digest", "")
                _was_hash = _raw.split("@sha256:")[-1][:12] if _raw else ""

        # Warn when the container shares another container's network namespace.
        # In this topology (e.g. Gluetun stacks) individual container restarts
        # are fragile — use --compose for a full stack redeploy instead.
        raw_nm = inspect_data.get("HostConfig", {}).get("NetworkMode", "")
        if raw_nm.startswith("container:"):
            log(f"{prefix} WARNING: container uses shared network namespace "
                f"({raw_nm}). Consider using --compose for reliable stack updates.")

        # Step 2: detect stack siblings before touching anything
        gateway_siblings, dependent_siblings = self._get_stack_siblings(container, inspect_data)
        all_siblings = gateway_siblings + dependent_siblings
        if gateway_siblings:
            log(f"{prefix} network gateway: {', '.join(gateway_siblings)}")
        if dependent_siblings:
            log(f"{prefix} stack siblings: {', '.join(dependent_siblings)}")

        # Pre-flight warning: non-local driver volumes cannot be backed up
        nonlocal_vols = _get_nonlocal_volumes(inspect_data)
        if nonlocal_vols:
            log(f"{prefix} WARNING: {len(nonlocal_vols)} volume(s) use a non-local driver "
                "and cannot be backed up")
            print(f"\n  ⚠  Warning: {len(nonlocal_vols)} volume(s) for '{container}' "
                  "cannot be backed up.")
            print("     These volumes use a non-local storage driver with no accessible")
            print("     host path. They will be skipped during backup. If a rollback is")
            print("     needed, data on these volumes will not be restored.")
            print()
            for v in nonlocal_vols:
                driver_str = f"  driver: {v['Driver']}" if v['Driver'] else ""
                print(f"       • {v['Name']}  ({v['Destination']}){driver_str}")
            print()
            try:
                yn = input("  Press Enter to continue, or type 'abort' to cancel: ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                print("\n  Aborted.")
                return False
            if yn == "abort":
                log(f"{prefix} update aborted by user (non-local volume warning)")
                print("  Aborted.")
                return False

        # Pre-flight warning: compose file cannot be resolved
        _labels = inspect_data.get("Config", {}).get("Labels") or {}
        _working_dir = _labels.get("com.docker.compose.project.working_dir", "")
        if _working_dir and not self._resolve_compose_dir(_working_dir, prefix):
            log(f"{prefix} WARNING: compose file could not be resolved — "
                "snapshot will not include a compose sidecar")
            print(f"\n  ⚠  Warning: compose file not found for '{container}'.")
            print("     The container has Docker Compose labels but the compose file")
            print("     cannot be located on disk. This snapshot will not include a")
            print("     compose sidecar. If a rollback is needed, the container will")
            print("     be reconstructed from 'docker run' rather than 'docker compose up'.")
            print()
            try:
                yn = input("  Press Enter to continue, or type 'abort' to cancel: ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                print("\n  Aborted.")
                return False
            if yn == "abort":
                log(f"{prefix} update aborted by user (compose file warning)")
                print("  Aborted.")
                return False

        # Step 3: snapshot then volume backup hook
        log(f"{prefix} saving config snapshot")
        snap_pw = _get_password(self.config, container)
        snap_path, staging_dir = self.sm.save(container, inspect_data, password=snap_pw)
        self._save_meta(container, snap_path.stem, inspect_data, staging_dir, password=snap_pw)
        self._save_image(container, snap_path.stem, inspect_data, staging_dir)
        def _pw_fn(container_path: str) -> "str | None":
            return _get_password(self.config, container, mount=container_path)
        do_pause = (self.config.pause_for_backup
                    and container not in self.config.pause_for_backup_disabled)
        if do_pause:
            log(f"{prefix} pausing container for consistent volume backup")
            try:
                self.docker._run(["pause", container])
            except DockerError as e:
                log(f"{prefix} could not pause container: {e} — proceeding without pause")
                do_pause = False
        _pre_update_meta = _derive_version_meta(inspect_data)
        try:
            self._backup_volumes(container, snap_path.stem, inspect_data, staging_dir,
                                 paused=do_pause, password_fn=_pw_fn, version_meta=_pre_update_meta)
        finally:
            if do_pause:
                try:
                    self.docker._run(["unpause", container])
                    log(f"{prefix} container unpaused")
                except DockerError as e:
                    log(f"{prefix} WARNING: failed to unpause container: {e}")
        # Write version metadata to the snapshot
        _pre_update_meta = _derive_version_meta(inspect_data)
        self.sm.save_version(snap_path.stem, staging_dir, _pre_update_meta)
        self.sm.finalize(container, snap_path.stem, staging_dir)
        log(f"{prefix} snapshot finalized → {snap_path.stem}.tar.gz")

        # Step 4: pull new image (substituting tag if --tag was specified)
        inspect_image = inspect_data.get("Config", {}).get("Image", "")
        image = _get_active_image_ref(self.config, container, inspect_data)
        if image != inspect_image:
            log(f"{prefix} using registry override: {image} (container has {inspect_image})")
        # Resolve tag: explicit --tag > stored pin > (use container's current image tag)
        effective_tag = tag or self.config.pinned_tags.get(container, "")
        if effective_tag and not tag:
            log(f"{prefix} applying pinned tag '{effective_tag}'")
        if effective_tag:
            new_image = RegistryClient._replace_tag(image, effective_tag)
            log(f"{prefix} pinning to tag '{effective_tag}': {image} → {new_image}")
            image = new_image
            inspect_data["Config"]["Image"] = image

        # Pull by digest to bypass Docker's tag-based manifest cache, which can
        # cause `docker pull <tag>` to be a no-op even when the registry has a
        # newer image. On registry failure, fall back to a plain tag pull.
        # Strip any @digest suffix before building the digest ref — Config.Image
        # carries one when the container was last started via rollback (pin_digest=True),
        # and leaving it in produces a malformed "image@sha256@sha256:..." reference.
        # Also update inspect_data so to_spec() starts the container on the new tag,
        # not the stale pinned digest.
        clean_image = image.split("@")[0] if "@" in image else image
        try:
            remote_digest = self.registry.get_remote_digest(image)
            last_slash = clean_image.rfind("/")
            last_colon = clean_image.rfind(":")
            base = clean_image[:last_colon] if last_colon > last_slash else clean_image
            digest_ref = f"{base}@{remote_digest}"
            log(f"{prefix} pulling {digest_ref}")
            try:
                self.docker.pull(digest_ref)
                self.docker.tag_image(digest_ref, clean_image)
                inspect_data["Config"]["Image"] = clean_image
            except DockerError as e:
                log(f"{prefix} pull failed: {e}")
                return False
        except RegistryError as e:
            log(f"{prefix} registry digest lookup failed ({e}), falling back to tag pull")
            log(f"{prefix} pulling {clean_image}")
            try:
                self.docker.pull(clean_image)
                inspect_data["Config"]["Image"] = clean_image
            except DockerError as e2:
                log(f"{prefix} pull failed: {e2}")
                return False

        # Step 5: stop target
        log(f"{prefix} stopping container")
        try:
            self.docker.stop(container)
        except DockerError as e:
            log(f"{prefix} stop failed: {e}")
            return False

        # Step 5b: stop siblings
        for sibling in all_siblings:
            log(f"{prefix} stopping sibling {sibling}")
            try:
                self.docker.stop(sibling)
            except DockerError as e:
                log(f"{prefix} could not stop sibling {sibling}: {e}")

        # Step 6: remove target
        log(f"{prefix} removing container")
        try:
            self.docker.remove(container)
        except DockerError as e:
            log(f"{prefix} remove failed: {e}")
            return False

        # Step 6b: start gateway first and wait for it, then start dependents
        for sibling in gateway_siblings:
            log(f"{prefix} starting gateway {sibling}")
            try:
                self.docker.start(sibling)
            except DockerError as e:
                log(f"{prefix} could not start gateway {sibling}: {e}")
        if gateway_siblings:
            self._wait_siblings_running(
                gateway_siblings, prefix, self.config.gateway_wait_sec
            )
        for sibling in dependent_siblings:
            log(f"{prefix} starting sibling {sibling}")
            try:
                self.docker.start(sibling)
            except DockerError as e:
                log(f"{prefix} could not start sibling {sibling}: {e}")
        if dependent_siblings:
            self._wait_siblings_running(
                dependent_siblings, prefix, self.config.sibling_wait_sec
            )

        # Steps 7+8: build spec from pre-update inspect data and start target
        spec = self.sm.to_spec(inspect_data, pin_digest=False)
        log(f"{prefix} starting updated container")
        try:
            self.docker.run(spec)
        except DockerError as e:
            log(f"{prefix} start failed: {e}")
            # Container is gone — roll back unconditionally from newest snapshot.
            snaps = self.sm.list(container)
            if snaps:
                self.rollback(container, snaps[0], reason="auto")
            else:
                log(f"{prefix} no snapshot to roll back to")
            return False

        # Step 8: health check
        log(f"{prefix} waiting for healthy state "
            f"(timeout: {self.config.health_timeout_sec}s)")
        healthy = self.hc.wait_healthy(container, self.config.health_timeout_sec)

        # Step 9a: success
        if healthy:
            log(f"{prefix} update successful")
            try:
                _new_data = self.docker.inspect(container)
                _new_labels = _new_data.get("Config", {}).get("Labels") or {}
                _new_image = _new_data.get("Config", {}).get("Image", "")
                _new_tag = "" if "@sha256:" in _new_image else _new_image.rsplit(":", 1)[-1]
                _new_version = (_new_tag if _new_tag and _new_tag != "latest"
                                else _new_labels.get("org.opencontainers.image.version", "") or _new_tag)
                _new_digests = _new_data.get("RepoDigests") or []
                _new_hash = (_new_digests[0].split("@sha256:")[-1][:12]
                             if _new_digests and "@sha256:" in _new_digests[0] else "")
            except DockerError:
                _new_version, _new_tag, _new_hash = "", "", ""
            print(f"\nUpdated {container}")
            _display_version = tag or _new_version or _new_tag or "?"
            if _was_version or _display_version:
                if _was_version != _display_version:
                    print(f"  was: {_was_version or '?'}  →  now: {_display_version}")
                elif _was_tag != _new_tag and _new_tag not in ("latest", ""):
                    print(f"  tag: {_was_tag or '?'}  →  {_new_tag}")
                else:
                    print(f"  version: {_display_version}  (same — image re-pulled)")
            if _was_hash and _new_hash:
                if _was_hash == _new_hash:
                    print(f"  sha256: ...{_new_hash}  (digest unchanged)")
                else:
                    print(f"  sha256: ...{_was_hash}  →  ...{_new_hash}")
            # Update stored version in config
            _update_meta = _derive_version_meta(_new_data)
            if not _update_meta["version"]:
                _update_meta["version"] = _display_version
            if not _update_meta["digest"]:
                _update_meta["digest"] = (_new_digests[0] if _new_digests and "@sha256:" in _new_digests[0] else "")
            if _update_meta["version"] or _update_meta["digest"]:
                self.config.container_versions[container] = _update_meta
                self.config.save()
            return True

        # Step 9b: failure
        log(f"{prefix} container failed health check")
        _diagnose_bind_address(container, self.docker)
        if auto_rollback:
            snaps = self.sm.list(container)
            if snaps:
                self.rollback(container, snaps[0], reason="auto")
            else:
                log(f"{prefix} no snapshot available for rollback")
        else:
            log(f"{prefix} auto-rollback disabled — "
                "container left in place for inspection")
        return False

    def snapshot(self, container: str) -> bool:
        prefix = f"[SNAPSHOT {container}]"

        snap_dir = self.config.snapshot_dir_for(container) / container
        err = _probe_snapshot_dir(snap_dir)
        if err:
            log(f"{prefix} snapshot dir not writable — aborting: {err}")
            return False

        log(f"{prefix} inspecting container")
        try:
            inspect_data = self.docker.inspect(container)
        except DockerError as e:
            log(f"{prefix} failed to inspect: {e}")
            return False

        snap_pw = _get_password(self.config, container)
        snap_path, staging_dir = self.sm.save(container, inspect_data, password=snap_pw)
        self._save_meta(container, snap_path.stem, inspect_data, staging_dir, password=snap_pw)
        self._save_image(container, snap_path.stem, inspect_data, staging_dir)

        def _pw_fn(container_path: str) -> "str | None":
            return _get_password(self.config, container, mount=container_path)

        do_pause = (self.config.pause_for_backup
                    and container not in self.config.pause_for_backup_disabled)
        if do_pause:
            log(f"{prefix} pausing container for consistent volume backup")
            try:
                self.docker._run(["pause", container])
            except DockerError as e:
                log(f"{prefix} could not pause container: {e} — proceeding without pause")
                do_pause = False
        _snap_meta = _derive_version_meta(inspect_data)
        try:
            self._backup_volumes(container, snap_path.stem, inspect_data, staging_dir,
                                 paused=do_pause, password_fn=_pw_fn, version_meta=_snap_meta)
        finally:
            if do_pause:
                try:
                    self.docker._run(["unpause", container])
                    log(f"{prefix} container unpaused")
                except DockerError as e:
                    log(f"{prefix} WARNING: failed to unpause container: {e}")
        # Write version metadata to snapshot and config
        if _snap_meta["version"] or _snap_meta["digest"]:
            self.config.container_versions[container] = _snap_meta
            self.config.save()
        self.sm.save_version(snap_path.stem, staging_dir, _snap_meta)
        self.sm.finalize(container, snap_path.stem, staging_dir)
        log(f"{prefix} snapshot complete → {snap_path.stem}.tar.gz")
        return True

    # Known Portainer container names to try when resolving its data volume.
    _PORTAINER_NAMES = [
        "portainer", "portainer-ce",
        "portainer_portainer_1", "portainer-portainer-1",
    ]

    def _resolve_compose_dir(self, working_dir: str, prefix: str) -> str:
        """Return an accessible host path for working_dir.

        Portainer stores compose files at /data/compose/<id>/ *inside* its
        own container.  The label com.docker.compose.project.working_dir
        reflects that internal path, which does not exist on the host.
        Resolve it by inspecting the Portainer container to find where its
        /data volume is bind-mounted on the host.
        """
        if Path(working_dir).is_dir():
            return working_dir

        # Only attempt resolution for paths that look like Portainer internals.
        if not working_dir.startswith("/data/"):
            log(f"{prefix} compose working directory not found: {working_dir}")
            return ""

        log(f"{prefix} {working_dir} not on host — searching for Portainer data volume")
        for pname in self._PORTAINER_NAMES:
            try:
                fmt = "{{range .Mounts}}{{if eq .Destination \"/data\"}}{{.Source}}{{end}}{{end}}"
                result = self.docker._run(["inspect", pname, "--format", fmt])
                data_host = result.stdout.strip()
                if not data_host:
                    continue
                # /data/compose/4  →  <data_host>/compose/4
                resolved = data_host + working_dir[len("/data"):]
                if Path(resolved).is_dir():
                    log(f"{prefix} resolved via {pname}: {resolved}")
                    return resolved
                log(f"{prefix} portainer data at {data_host} but {resolved} not found")
            except DockerError:
                continue

        log(f"{prefix} could not resolve compose directory {working_dir} — "
            "ensure Portainer's data volume is bind-mounted on this host "
            "(e.g. -v /opt/portainer/data:/data) or run the update from "
            "Portainer's 'Update the stack' button directly")
        return ""

    @staticmethod
    def _compose_run(cmd: list, cwd: str) -> subprocess.CompletedProcess:
        """Run a docker compose sub-command, raising DockerError with a clear message."""
        try:
            return subprocess.run(cmd, cwd=cwd, check=False)
        except FileNotFoundError as e:
            fname = str(e.filename or "")
            if "docker" in fname or not fname:
                raise DockerError("docker executable not found — is Docker installed?")
            raise DockerError(f"path not found while running compose: {e.filename}")

    def compose_update(self, container: str, auto_rollback: bool = True,
                       tag: str = "") -> bool:
        """Update via 'docker compose up --force-recreate'.

        Required for stacks where containers share a network namespace (e.g.
        Gluetun-routed stacks with network_mode: service:gluetun).  Replicates
        what Portainer's 'Update the stack, repull image and redeploy' does.
        """
        prefix = f"[UPDATE {container}]"

        # Step 1: inspect to get compose labels
        log(f"{prefix} inspecting current container")
        try:
            inspect_data = self.docker.inspect(container)
        except DockerError as e:
            log(f"{prefix} failed to inspect: {e}")
            return False

        inspect_image = inspect_data.get("Config", {}).get("Image", "")

        labels = inspect_data.get("Config", {}).get("Labels") or {}
        working_dir = labels.get("com.docker.compose.project.working_dir", "")
        config_files_raw = labels.get("com.docker.compose.project.config_files", "")
        service = labels.get("com.docker.compose.service", "")

        if not working_dir or not service:
            log(f"{prefix} --compose requires Compose-managed container "
                "(labels com.docker.compose.project.working_dir and "
                "com.docker.compose.service must be present)")
            return False

        # Resolve Portainer-internal paths to their host equivalents.
        working_dir = self._resolve_compose_dir(working_dir, prefix)
        if not working_dir:
            return False

        log(f"{prefix} compose project dir: {working_dir}, service: {service}")

        # Pre-flight: ensure the gateway container is running before touching anything.
        # With --no-deps, compose won't start the gateway — it must already be up.
        network_mode = (inspect_data.get("HostConfig") or {}).get("NetworkMode", "")
        gateway_name = network_mode.split(":", 1)[1] if network_mode.startswith("container:") else ""
        if gateway_name:
            gateway_status = self.docker.health(gateway_name)
            if gateway_status not in ("running", "healthy"):
                log(f"{prefix} gateway {gateway_name} is {gateway_status} — "
                    "attempting to start it before updating")
                try:
                    self.docker.start(gateway_name)
                except DockerError as e:
                    log(f"{prefix} could not start gateway {gateway_name}: {e}")
                    log(f"{prefix} aborting — start {gateway_name} manually and retry")
                    return False
                log(f"{prefix} waiting for gateway {gateway_name} "
                    f"(timeout: {self.config.gateway_wait_sec}s)")
                if not self.hc.wait_healthy(gateway_name, self.config.gateway_wait_sec):
                    log(f"{prefix} gateway {gateway_name} did not reach healthy state — "
                        "aborting update")
                    return False
                log(f"{prefix} gateway {gateway_name} is ready")

        # Step 2: snapshot + volume backup before touching anything
        log(f"{prefix} saving config snapshot")
        snap_pw = _get_password(self.config, container)
        snap_path, staging_dir = self.sm.save(container, inspect_data, password=snap_pw)
        self._save_meta(container, snap_path.stem, inspect_data, staging_dir, password=snap_pw)
        self._save_image(container, snap_path.stem, inspect_data, staging_dir)
        def _pw_fn(container_path: str) -> "str | None":
            return _get_password(self.config, container, mount=container_path)
        do_pause = (self.config.pause_for_backup
                    and container not in self.config.pause_for_backup_disabled)
        if do_pause:
            log(f"{prefix} pausing container for consistent volume backup")
            try:
                self.docker._run(["pause", container])
            except DockerError as e:
                log(f"{prefix} could not pause container: {e} — proceeding without pause")
                do_pause = False
        _pre_update_meta = _derive_version_meta(inspect_data)
        try:
            self._backup_volumes(container, snap_path.stem, inspect_data, staging_dir,
                                 paused=do_pause, password_fn=_pw_fn,
                                 version_meta=_pre_update_meta)
        finally:
            if do_pause:
                try:
                    self.docker._run(["unpause", container])
                    log(f"{prefix} container unpaused")
                except DockerError as e:
                    log(f"{prefix} WARNING: failed to unpause container: {e}")
        _pre_update_meta = _derive_version_meta(inspect_data)
        self.sm.save_version(snap_path.stem, staging_dir, _pre_update_meta)
        self.sm.finalize(container, snap_path.stem, staging_dir)

        # Build the base compose command (with explicit -f flags if provided).
        # Use the resolved config file paths (same substitution as working_dir).
        # --project-name must match the name Portainer used when creating the stack;
        # without it compose derives the name from the directory ("4"), which won't
        # match the project label on the running containers and causes service lookups
        # like network_mode: service:gluetun to fail with "container missing".
        project_name = labels.get("com.docker.compose.project", "")
        compose_base = ["compose"]
        if project_name:
            compose_base += ["--project-name", project_name]
        orig_data_prefix = labels.get("com.docker.compose.project.working_dir", "")
        for cf in [f.strip() for f in config_files_raw.split(",") if f.strip()]:
            # If the config file path shares Portainer's /data prefix, remap it.
            if orig_data_prefix and cf.startswith(orig_data_prefix):
                cf = working_dir + cf[len(orig_data_prefix):]
            compose_base += ["-f", cf]

        # Apply registry override and/or tag via a minimal compose override file.
        # Compose merges -f files in order, so the last -f wins on conflicts.
        effective_image = _get_active_image_ref(self.config, container, inspect_data)
        effective_tag = tag or self.config.pinned_tags.get(container, "")
        if effective_tag:
            effective_image = RegistryClient._replace_tag(effective_image, effective_tag)
        override_file = None
        if effective_image != inspect_image:
            log(f"{prefix} image override: {inspect_image} → {effective_image}")
            override_content = f"services:\n  {service}:\n    image: {effective_image}\n"
            fd, override_path = tempfile.mkstemp(suffix=".yml", prefix="rbp_override_")
            try:
                os.write(fd, override_content.encode())
            finally:
                os.close(fd)
            compose_base += ["-f", override_path]
            override_file = override_path

        try:
            # Step 3: pull new image via compose
            log(f"{prefix} pulling via docker compose pull {service}")
            try:
                result = self._compose_run(
                    ["docker"] + compose_base + ["pull", service], working_dir
                )
            except DockerError as e:
                log(f"{prefix} {e}")
                return False
            if result.returncode != 0:
                log(f"{prefix} compose pull failed — original container still running")
                return False

            # Step 4: recreate via compose (handles dependency order automatically)
            log(f"{prefix} recreating via docker compose up --force-recreate {service}")
            try:
                result = self._compose_run(
                    ["docker"] + compose_base + ["up", "-d", "--no-deps", "--force-recreate", service],
                    working_dir,
                )
            except DockerError as e:
                log(f"{prefix} {e}")
                return False
            if result.returncode != 0:
                log(f"{prefix} compose up failed")
                if auto_rollback:
                    snaps = self.sm.list(container)
                    if snaps:
                        self.rollback(container, snaps[0], reason="auto")
                    else:
                        log(f"{prefix} no snapshot to roll back to")
                return False

            # Step 5: health check
            log(f"{prefix} waiting for healthy state "
                f"(timeout: {self.config.health_timeout_sec}s)")
            healthy = self.hc.wait_healthy(container, self.config.health_timeout_sec)

            if healthy:
                log(f"{prefix} compose update successful")
                return True

            log(f"{prefix} container failed health check")
            _diagnose_bind_address(container, self.docker)
            if auto_rollback:
                snaps = self.sm.list(container)
                if snaps:
                    self.rollback(container, snaps[0], reason="auto")
                else:
                    log(f"{prefix} no snapshot available for rollback")
            else:
                log(f"{prefix} auto-rollback disabled — "
                    "container left in place for inspection")
            return False
        finally:
            if override_file:
                try:
                    os.unlink(override_file)
                except OSError:
                    pass


# === COMMANDS ===

def _get_running_containers(docker: DockerClient) -> list:
    result = docker._run(["ps", "--format", "{{.Names}}"])
    return [n.strip() for n in result.stdout.splitlines() if n.strip()]


def _wrap(text: str, width: int) -> str:
    """Hard-wrap text to width, preferring to break at / : or space."""
    if len(text) <= width:
        return text
    lines = []
    while len(text) > width:
        cut = width
        for sep in (' ', '/', ':'):
            i = text.rfind(sep, 0, width + 1)
            if i > 0:
                cut = i + 1  # keep separator on the first line
                break
        lines.append(text[:cut])
        text = text[cut:]
    if text:
        lines.append(text)
    return "\n".join(lines)


def _print_table(headers: list, rows: list,
                 max_widths: dict | None = None) -> None:
    def cell_lines(val: object) -> list:
        return str(val).split("\n")

    if max_widths:
        rows = [
            tuple(_wrap(str(c), max_widths[i]) if i in max_widths else c
                  for i, c in enumerate(row))
            for row in rows
        ]

    all_rows = [headers] + list(rows)
    widths = [
        max(max(len(line) for line in cell_lines(r[i])) for r in all_rows)
        for i in range(len(headers))
    ]

    def fmt_line(line_sets: list, line_idx: int) -> str:
        parts = []
        for i, lines in enumerate(line_sets):
            text = lines[line_idx] if line_idx < len(lines) else ""
            parts.append(text.ljust(widths[i]))
        return "  ".join(parts)

    header_line_sets = [cell_lines(h) for h in headers]
    for line_idx in range(max(len(ls) for ls in header_line_sets)):
        print(fmt_line(header_line_sets, line_idx))
    print("  ".join("-" * w for w in widths))
    for row in rows:
        line_sets = [cell_lines(row[i]) for i in range(len(headers))]
        for line_idx in range(max(len(ls) for ls in line_sets)):
            print(fmt_line(line_sets, line_idx))


def _getchar() -> str:
    try:
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            return sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)
    except (termios.error, io.UnsupportedOperation):
        return input()


# Master password for config-file-at-rest encryption. Set once in main() after
# startup prompt; None means config files are stored as plaintext.
_master_password: "str | None" = None

# Per-process password cache. Keys are "container" or "container::/mount".
# Only populated when encryption mode is "session". Never written to disk.
_session_cache: dict[str, str] = {}

# Tracks which entities have already been shown the "save password" tip
# this process. Prevents repeating it for the same entity.
_offered_save: set[str] = set()


def _enc_pw_status(config: "Config", container: str) -> str:
    """Return 'saved', 'session', or 'locked' — password availability for badge/menu."""
    if config.get_saved_password(container) is not None:
        return "saved"
    if container in _session_cache:
        return "session"
    return "locked"


def _verify_enc_password_for(config: Config, container: str, password: str) -> bool:
    """Decrypt one file for this container to verify the password.

    Returns True if an encrypted file was found and decrypted successfully.
    Returns False if no encrypted files exist yet (nothing to verify against).
    Raises cryptography.exceptions.InvalidTag on wrong password.
    """
    from cryptography.exceptions import InvalidTag
    _ts_re = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}-\d{2}-\d{2}$")
    container_dir = config.snapshot_dir_for(container) / container
    if not container_dir.exists():
        return False
    enc = EncryptionManager(config)

    def _try(raw: bytes) -> bool:
        if not enc.is_encrypted(raw):
            return False
        enc.decrypt_bytes(raw, password)
        return True

    bundles = sorted(
        [p for p in container_dir.glob("*.tar.gz")
         if _ts_re.match(p.name.removesuffix(".tar.gz"))],
        key=lambda p: p.stat().st_mtime, reverse=True,
    )
    for bundle in bundles:
        sid = bundle.name.removesuffix(".tar.gz")
        target = f"{sid}.json"
        try:
            with tarfile.open(bundle, "r|gz") as tar:
                for member in tar:
                    if member.name == target:
                        raw = tar.extractfile(member).read()
                        if _try(raw):
                            return True
                        break
        except InvalidTag:
            raise
        except Exception:
            continue

    return False


def _get_password(config: Config, container: str,
                  mount: str | None = None) -> "str | None":
    """Return the encryption password for a container or volume mount.

    Returns None if the entity is not marked for encryption.
    Resolution order: saved_passwords → session cache → prompt.
    After a prompt, caches or offers to save based on config mode.
    """
    if mount is not None:
        if not config.is_volume_encrypted(container, mount):
            return None
    else:
        if not config.is_encryption_enabled(container):
            return None

    cache_key = f"{container}::{mount}" if mount is not None else container
    mode = config.encryption.get("mode", "session")
    label = cache_key

    # 1. Saved password (checked regardless of mode)
    saved = config.get_saved_password(container, mount)
    if saved is not None:
        return saved

    # 2. Session cache (skipped when mode is "always")
    if mode != "always" and cache_key in _session_cache:
        return _session_cache[cache_key]

    # 3. Prompt
    import getpass
    if not sys.stdin.isatty():
        print(
            f"Error: encryption is enabled for {label} but stdin is not a TTY.",
            file=sys.stderr,
        )
        sys.exit(1)
    try:
        password = getpass.getpass(f"Encryption password for {label}: ")
    except (EOFError, KeyboardInterrupt):
        print()
        sys.exit(0)
    if not password:
        print("Password cannot be empty.", file=sys.stderr)
        sys.exit(1)

    # Always session-cache after a prompt (except "always" mode which intentionally re-prompts)
    if mode != "always":
        _session_cache[cache_key] = password

    # Show a one-time hint to save via the dedicated menu instead of prompting mid-operation
    if cache_key not in _offered_save and sys.stdin.isatty():
        _offered_save.add(cache_key)
        print(f"  (tip: open container menu → w to save this password permanently)")

    return password


def _get_password_verified(config: Config, container: str,
                            mount: str | None = None,
                            max_attempts: int = 3) -> "str | None":
    """Like _get_password but verifies by decrypting a real file.

    On wrong password: clears the session cache entry and retries.
    Returns None if the entity is not marked for encryption.
    Exits after max_attempts failures.
    """
    from cryptography.exceptions import InvalidTag
    cache_key = f"{container}::{mount}" if mount is not None else container
    for attempt in range(1, max_attempts + 1):
        password = _get_password(config, container, mount)
        if password is None:
            return None
        try:
            found = _verify_enc_password_for(config, container, password)
            if not found:
                return password  # no files yet — accept at face value
            return password
        except InvalidTag:
            _session_cache.pop(cache_key, None)
            remaining = max_attempts - attempt
            if remaining > 0:
                print(f"Incorrect password. "
                      f"{remaining} attempt{'s' if remaining != 1 else ''} remaining.")
            else:
                print("Too many failed attempts.", file=sys.stderr)
                sys.exit(1)
    sys.exit(1)


def _prompt_master_password_startup(config_path: Path, max_attempts: int = 3) -> str:
    """Prompt for the master password at startup, verifying it against the encrypted config."""
    from cryptography.exceptions import InvalidTag
    import getpass
    enc = EncryptionManager(None)
    raw = config_path.read_bytes()
    for attempt in range(1, max_attempts + 1):
        try:
            pw = getpass.getpass("Master password: ")
        except (EOFError, KeyboardInterrupt):
            print()
            sys.exit(0)
        if not pw:
            print("Password cannot be empty.", file=sys.stderr)
            sys.exit(1)
        try:
            enc.decrypt_bytes(raw, pw)
            return pw
        except InvalidTag:
            remaining = max_attempts - attempt
            if remaining > 0:
                print(f"Incorrect password. {remaining} attempt{'s' if remaining != 1 else ''} remaining.")
            else:
                print("Too many failed attempts.", file=sys.stderr)
                sys.exit(1)
    sys.exit(1)


def cmd_check(args: argparse.Namespace) -> None:
    docker = DockerClient()
    registry = RegistryClient()
    names = list(args.containers) if args.containers else _get_running_containers(docker)
    names = [n for n in names if n not in args.config.exclude]
    if not names:
        print("No containers to check.")
        return
    rows = []
    for name in names:
        try:
            data = docker.inspect(name)
            image = data.get("Config", {}).get("Image", "")
            try:
                pinned_tag = args.config.pinned_tags.get(name, "")
                active_ref = _get_active_image_ref(args.config, name, data)
                update = "yes" if registry.has_update(data, pinned_tag=pinned_tag,
                                                      image_ref_override=active_ref) else "no"
            except RegistryError as e:
                log(f"Warning: registry check failed for {name}: {e}")
                update = "?"
        except DockerError as e:
            image, update = "?", f"error: {e}"
            pinned_tag = args.config.pinned_tags.get(name, "")
        pin = pinned_tag or "—"
        rows.append((name, image, update, pin))
    _print_table(["CONTAINER", "IMAGE", "UPDATE", "PIN"], rows)


def cmd_status(args: argparse.Namespace) -> None:
    docker = DockerClient()
    registry = RegistryClient()
    sm = SnapshotManager(args.config)
    names = _get_running_containers(docker)
    names = [n for n in names if n not in args.config.exclude]
    if not names:
        print("No running containers.")
        return
    rows = []
    for name in names:
        try:
            data = docker.inspect(name)
            image = data.get("Config", {}).get("Image", "")
            local = registry.get_local_digest(data) or ""
            short_digest = local.split("@")[-1][:19] if local else "none"
            try:
                active_ref = _get_active_image_ref(args.config, name, data)
                update = "yes" if registry.has_update(data,
                                                      image_ref_override=active_ref) else "no"
            except RegistryError as e:
                log(f"Warning: registry check failed for {name}: {e}")
                update = "?"
            snaps = str(len(sm.list(name)))
            version = data.get("ImageVersion", "")
            if not version:
                # Fall back to the image tag if it looks like a version number.
                tag = image.rsplit(":", 1)[-1] if ":" in image else ""
                version = tag if tag and any(c.isdigit() for c in tag) else "?"
            date = data.get("ImageCreated", "") or "?"
        except DockerError as e:
            image, short_digest, update, snaps, version, date = "?", "?", "error", "0", "?", "?"
        rows.append((name, image, short_digest, update, snaps, version, date))
    _print_table(["CONTAINER", "IMAGE", "DIGEST", "UPDATE", "SNAPS", "VERSION", "DATE"], rows)


def cmd_doctor(args: argparse.Namespace) -> None:
    """Validate configuration paths, credentials, and permissions."""
    config = args.config
    config_path = config._path
    has_error = False
    sm = SnapshotManager(config)

    try:
        with open(config_path) as f:
            raw = json.load(f)
    except Exception:
        raw = {}

    def _path_status(stored: str, runtime: Path) -> str:
        if not runtime.exists():
            return f"✗  {stored}  (missing)"
        if stored.startswith("~/"):
            return f"✓  {stored}"
        if _is_local_path(runtime):
            return f"!  {stored}  (absolute — save config to make portable)"
        return f"!  {stored}  (absolute — NAS path)"

    # ── Credentials ─────────────────────────────────────────────────────────

    print("\n─── Credentials")
    cred_path = config_path.parent / "credentials.json"
    print(f"  credentials.json:    {cred_path}")
    if cred_path.exists():
        print("    exists:            ✓")
        try:
            mode = cred_path.stat().st_mode & 0o777
            perm_ok = mode == 0o600
            print(f"    permissions:       {'✓' if perm_ok else '!'}  {oct(mode)}"
                  + ("" if perm_ok else "  (expected 0o600)"))
        except OSError:
            print("    permissions:       !  could not check")
        creds = _load_credentials(cred_path.parent)
        names_str = ", ".join(creds.keys()) if creds else "none"
        print(f"    passwords stored:  {len(creds)}  ({names_str})")
    else:
        print("    exists:            -  not found (normal if no passwords saved)")

    raw_enc_pw = raw.get("encryption", {}).get("saved_passwords", {})
    if raw_enc_pw:
        print(f"  config.json passwords:  ✗  {len(raw_enc_pw)} found — run any command to auto-migrate")
        has_error = True
    else:
        print("  config.json passwords:  ✓  empty (correctly separated)")

    # ── Path Portability ─────────────────────────────────────────────────────

    print("\n─── Path Portability")

    sd_stored = raw.get("snapshot_dir", _to_portable_path(config.snapshot_dir))
    print(f"  snapshot_dir:         {_path_status(sd_stored, config.snapshot_dir)}")

    lf_stored = raw.get("log_file", _to_portable_path(config.log_file))
    print(f"  log_file:             {_path_status(lf_stored, config.log_file)}")

    raw_overrides = raw.get("snapshot_dir_overrides", {})
    if raw_overrides:
        print("  snapshot_dir_overrides:")
        for container, stored_val in raw_overrides.items():
            runtime_path = Path(config.snapshot_dir_overrides.get(container, stored_val))
            status = _path_status(stored_val, runtime_path)
            if status.startswith("✗"):
                has_error = True
            print(f"    {container}:  {status}")

    raw_vb = raw.get("volume_backup", {})
    save_paths = {c: r["save_path"] for c, r in raw_vb.items() if r.get("save_path")}
    if save_paths:
        print("  volume_backup save_paths:")
        for container, stored_val in save_paths.items():
            runtime_str = config.volume_backup.get(container, {}).get("save_path", stored_val)
            status = _path_status(stored_val, Path(runtime_str))
            if status.startswith("✗"):
                has_error = True
            print(f"    {container}:  {status}")

    mount_entries = [
        (container, cp, stored_hp,
         config.volume_backup.get(container, {}).get("mount_paths", {}).get(cp, stored_hp))
        for container, raw_rules in raw_vb.items()
        for cp, stored_hp in raw_rules.get("mount_paths", {}).items()
    ]
    if mount_entries:
        print("  volume_backup mount_paths:")
        for container, cp, stored_val, runtime_str in mount_entries:
            status = _path_status(stored_val, Path(runtime_str))
            if status.startswith("✗"):
                has_error = True
            print(f"    {container} {cp}:  {status}")

    # ── Permissions ──────────────────────────────────────────────────────────

    print("\n─── Permissions")
    perm_checks = [
        (BASE_DIR,        0o700, "~/.update_zen/"),
        (config_path,     0o600, "config.json"),
        (cred_path,       0o600, "credentials.json"),
        (config.log_file, 0o600, "update_zen.log"),
    ]
    for path, expected, label in perm_checks:
        if not path.exists():
            print(f"  {label:<22} -  not found")
            continue
        try:
            mode = path.stat().st_mode & 0o777
            perm_ok = mode == expected
            suffix = "" if perm_ok else f"  (expected {oct(expected)})"
            print(f"  {label:<22} {'✓' if perm_ok else '!'}  {oct(mode)}{suffix}")
        except OSError:
            print(f"  {label:<22} !  could not check")

    # ── Snapshot Directories ─────────────────────────────────────────────────

    print("\n─── Snapshot Directories")
    override_containers = set(config.snapshot_dir_overrides.keys())

    snap_dir = config.snapshot_dir
    if snap_dir.exists():
        counts = []
        try:
            for subdir in sorted(snap_dir.iterdir()):
                if subdir.is_dir() and not subdir.name.startswith("_") \
                        and subdir.name not in override_containers:
                    n = len(sm.list(subdir.name))
                    if n:
                        counts.append(f"{subdir.name}: {n}")
        except Exception:
            pass
        counts_str = f"  ({', '.join(counts)})" if counts else ""
        write_err = _probe_snapshot_dir(snap_dir)
        if write_err:
            print(f"  global:  ✗  {snap_dir}  (not writable: {write_err}){counts_str}")
            has_error = True
        else:
            print(f"  global:  ✓  {snap_dir}{counts_str}")
    else:
        print(f"  global:  -  {snap_dir}  (not yet created)")

    for container, override_str in config.snapshot_dir_overrides.items():
        override_path = Path(override_str)
        if override_path.exists():
            try:
                n = len(sm.list(container))
                snap_note = f"  ({n} snapshot{'s' if n != 1 else ''})"
            except Exception:
                snap_note = ""
            write_err = _probe_snapshot_dir(override_path)
            if write_err:
                print(f"  {container}:  ✗  {override_path}  (not writable: {write_err}){snap_note}")
                has_error = True
            else:
                print(f"  {container}:  ✓  {override_path}{snap_note}")
        else:
            print(f"  {container}:  ✗  {override_path}  (missing — rollback unavailable)")
            has_error = True

    # ── Encryption Consistency ───────────────────────────────────────────────

    print("\n─── Encryption")
    encrypt_containers = config.encryption.get("encrypt_containers", [])
    if not encrypt_containers:
        print("  No containers configured for encryption.")
    else:
        for container in encrypt_containers:
            pw = config.get_saved_password(container)
            if pw:
                print(f"  {container}:  encrypted  ✓  credentials present")
            else:
                print(f"  {container}:  encrypted  !  no credentials stored (will prompt at runtime)")

    # ── Legacy Snapshots ─────────────────────────────────────────────────────

    legacy_found = {}
    for cname in _all_snapshot_container_names(config):
        count = sum(1 for s in sm.list(cname) if s.path.suffix == ".json")
        if count:
            legacy_found[cname] = count
    if legacy_found:
        print("\n─── Legacy Snapshots")
        for cname, count in sorted(legacy_found.items()):
            print(f"  ! {cname}: {count} legacy .json snapshot(s)"
                  " — run 'update_zen convert-snapshots' to migrate")

    # ── Orphaned Artifacts ───────────────────────────────────────────────────

    orphans = _collect_orphans(config)
    if orphans:
        total = sum(o["size_bytes"] for o in orphans)
        print("\n─── Orphaned Artifacts")
        print(f"  ! {len(orphans)} orphaned artifact(s) found, {_fmt_bytes(total)} total")
        print("    Run 'update_zen cleanup' to review and remove.")

    print()
    if has_error:
        sys.exit(1)


def cmd_cleanup(args: argparse.Namespace) -> None:
    """Find and remove orphaned staging dirs and .tmp files from interrupted operations."""
    import shutil
    config = args.config
    container = args.container
    do_delete = args.yes

    orphans = _collect_orphans(config, container)

    if not orphans:
        scope = f" for {container}" if container else ""
        print(f"No orphaned artifacts found{scope}.")
        return

    total_bytes = sum(o["size_bytes"] for o in orphans)
    rows = [
        (o["container"], o["type"], _fmt_bytes(o["size_bytes"]), str(o["path"]))
        for o in orphans
    ]
    print(f"\nOrphaned artifacts — {len(orphans)} item{'s' if len(orphans) != 1 else ''}, "
          f"{_fmt_bytes(total_bytes)} total:\n")
    _print_table(["CONTAINER", "TYPE", "SIZE", "PATH"], rows)
    print()

    if not do_delete:
        print("Run with --yes to delete.")
        return

    try:
        raw = input(
            f"Delete {len(orphans)} item{'s' if len(orphans) != 1 else ''}? [y/N] "
        ).strip().lower()
    except (EOFError, KeyboardInterrupt):
        print()
        return
    if raw != "y":
        print("Aborted.")
        return

    deleted = 0
    freed = 0
    for o in orphans:
        p = o["path"]
        try:
            if o["type"] == "staging":
                shutil.rmtree(p)
            else:
                p.unlink()
            log(f"[cleanup] removed {o['type']}: {p}")
            deleted += 1
            freed += o["size_bytes"]
        except OSError as e:
            log(f"[cleanup] failed to remove {p}: {e}")

    print(f"Removed {deleted} item{'s' if deleted != 1 else ''}, freed {_fmt_bytes(freed)}.")


def cmd_convert_snapshots(args: argparse.Namespace) -> None:
    """Migrate legacy .json-format snapshots to .tar.gz bundles."""
    import shutil
    config = args.config
    sm = SnapshotManager(config)
    dry_run = args.dry_run

    containers = [args.container] if args.container else _all_snapshot_container_names(config)
    if not containers:
        print("No snapshot directories found.")
        return

    total_converted = 0
    total_failed = 0

    for container in containers:
        snaps = sm.list(container)
        old_snaps = [s for s in snaps if s.path.suffix == ".json"]
        if not old_snaps:
            continue

        print(f"\n{container}: {len(old_snaps)} legacy snapshot(s) found")

        for snap in old_snaps:
            snapshot_id = snap.path.stem
            container_dir = snap.path.parent
            sidecars = [
                snap.path.with_name(snapshot_id + suf)
                for suf in ("_compose.yaml", "_env.env", "_image.tar", "_ext.json", "_version.json")
                if snap.path.with_name(snapshot_id + suf).exists()
            ]

            if dry_run:
                extras = f"  + {[s.name for s in sidecars]}" if sidecars else ""
                print(f"  would convert: {snap.path.name}{extras}")
                total_converted += 1
                continue

            staging_dir = container_dir / f"_staging_{snapshot_id}"
            try:
                staging_dir.mkdir(exist_ok=True)
                staging_dir.chmod(config.snapshot_dir_mode_for(container))

                # Copy raw JSON bytes — preserves existing encryption state
                (staging_dir / f"{snapshot_id}.json").write_bytes(snap.path.read_bytes())

                for sib in sidecars:
                    suffix = sib.name[len(snapshot_id):]
                    if suffix == "_ext.json":
                        # Translate external_volumes index → new _volumes.json schema
                        try:
                            ext_data = json.loads(sib.read_text())
                            volumes = [
                                {
                                    "container_path": e["container_path"],
                                    "host_path": e.get("host_path", ""),
                                    "archive_name": f"{snapshot_id}.tar.gz",
                                    "archive_dir": e["archive_dir"],
                                }
                                for e in ext_data.get("external_volumes", [])
                            ]
                            (staging_dir / f"{snapshot_id}_volumes.json").write_text(
                                json.dumps({"volumes": volumes, "skipped": []}, indent=2) + "\n"
                            )
                        except Exception as e:
                            log(f"[convert {container}] could not translate _ext.json for "
                                f"{snapshot_id}: {e}")
                    else:
                        # Copy raw bytes — preserves encryption on compose/env sidecars
                        (staging_dir / f"{snapshot_id}{suffix}").write_bytes(sib.read_bytes())

                # Delete originals before finalize so snapshot count stays stable through rotation
                snap.path.unlink()
                for sib in sidecars:
                    sib.unlink()

                sm.finalize(container, snapshot_id, staging_dir)
                print(f"  converted: {snapshot_id}.json → {snapshot_id}.tar.gz")
                log(f"[convert {container}] converted {snapshot_id}")
                total_converted += 1

            except Exception as e:
                print(f"  failed: {snapshot_id}: {e}")
                log(f"[convert {container}] failed: {snapshot_id}: {e}")
                try:
                    if staging_dir.exists():
                        shutil.rmtree(staging_dir)
                except Exception:
                    pass
                total_failed += 1

    if total_converted == 0 and total_failed == 0:
        scope = f" for {args.container}" if args.container else ""
        print(f"No legacy .json snapshots found{scope}.")
        return

    verb = "Would convert" if dry_run else "Converted"
    print(f"\n{verb}: {total_converted}  Failed: {total_failed}")


_TAG_WORKERS = 10     # parallel registry workers for digest-based tag identification
_STATUS_WORKERS = 10  # parallel registry workers for interactive status table


def _identify_current_tag(registry: RegistryClient, docker: DockerClient,
                           data: dict, tags: list) -> str:
    """Return the tag that matches the running image, or '' if undetermined.

    Strategy A — OCI label (zero extra registry calls):
      Read org.opencontainers.image.version from the image's own labels.
      If it matches a tag in the list, return it immediately.

    Strategy B — parallel digest comparison (fallback):
      Fetch remote digests for all tags concurrently (up to _TAG_WORKERS
      workers) and compare against the local image digest.
    """
    # Strategy A: OCI label
    image_id = data.get("Image", "")
    if image_id:
        try:
            result = docker._run(["image", "inspect", image_id])
            img_data = json.loads(result.stdout)[0]
            version_label = (img_data.get("Config", {}).get("Labels") or {}).get(
                "org.opencontainers.image.version", ""
            )
            if version_label and version_label in tags:
                return version_label
        except (DockerError, Exception):
            pass

    # Strategy B: parallel digest comparison
    local_digests = data.get("RepoDigests") or []
    if not local_digests:
        return ""
    local_hash = local_digests[0].split("@")[-1]  # "sha256:abc..."
    image_ref = data.get("Config", {}).get("Image", "")

    print("Identifying current version via digest comparison "
          f"({len(tags)} tags, up to {_TAG_WORKERS} parallel)...")

    def fetch_digest(tag: str):
        ref = RegistryClient._replace_tag(image_ref, tag)
        try:
            return tag, registry.get_remote_digest(ref)
        except RegistryError:
            return tag, None

    with concurrent.futures.ThreadPoolExecutor(max_workers=_TAG_WORKERS) as pool:
        futures = {pool.submit(fetch_digest, tag): tag for tag in tags}
        for future in concurrent.futures.as_completed(futures):
            tag, digest = future.result()
            if digest and digest == local_hash:
                # Cancel remaining work — we found the match
                for f in futures:
                    f.cancel()
                return tag

    return ""


def cmd_tags(args: argparse.Namespace) -> None:
    docker = DockerClient()
    registry = RegistryClient()
    try:
        data = docker.inspect(args.container)
    except DockerError as e:
        print(f"Error: {e}")
        sys.exit(1)
    image_ref = data.get("Config", {}).get("Image", "")
    if not image_ref:
        print(f"Could not determine image for {args.container}")
        sys.exit(1)
    base = RegistryClient._replace_tag(image_ref, "").rstrip(":")
    try:
        tags = registry.list_tags(image_ref)
    except RegistryError as e:
        print(f"Registry error: {e}")
        sys.exit(1)
    if not tags:
        print(f"No tags found for {base}")
        return

    current_tag = _identify_current_tag(registry, docker, data, tags)

    print(f"Available tags for {base}:")
    for tag in tags:
        marker = "  ←  current" if tag == current_tag else ""
        print(f"  {tag}{marker}")


def cmd_update(args: argparse.Namespace) -> None:
    engine = Engine(args.config)
    if args.compose:
        success = engine.compose_update(args.container, auto_rollback=args.auto_rollback,
                                        tag=args.tag or "")
    else:
        success = engine.update(args.container, auto_rollback=args.auto_rollback,
                                tag=args.tag or "")
    if not success:
        sys.exit(1)


def cmd_rollback(args: argparse.Namespace) -> None:
    sm = SnapshotManager(args.config)
    snaps = sm.list(args.container)
    if not snaps:
        print(f"No snapshots for {args.container}")
        sys.exit(1)

    if args.snap is not None:
        idx = args.snap - 1
        if idx >= len(snaps):
            print(f"Snapshot {args.snap} does not exist "
                  f"({len(snaps)} available).")
            sys.exit(1)
        snapshot = snaps[idx]
    else:
        print(f"Available snapshots for {args.container}:")
        for i, snap in enumerate(snaps, 1):
            ts = snap.timestamp.strftime("%Y-%m-%d %H:%M")
            ref = snap.digest or snap.image_ref
            print(f"  [{i}]  {ts}  {ref}")
        n = len(snaps)
        prompt = f"Roll back to [1{f'-{n}' if n > 1 else ''}]: "
        try:
            raw = input(prompt).strip()
        except (EOFError, KeyboardInterrupt):
            print("\nAborted.")
            sys.exit(1)
        if not raw.isdigit() or not (1 <= int(raw) <= n):
            print(f"Invalid choice: enter a number between 1 and {n}.")
            sys.exit(1)
        snapshot = snaps[int(raw) - 1]

    engine = Engine(args.config)
    success = engine.rollback(args.container, snapshot)
    if not success:
        sys.exit(1)


def cmd_list_snaps(args: argparse.Namespace) -> None:
    sm = SnapshotManager(args.config)
    snaps = sm.list(args.container)
    if not snaps:
        print(f"No snapshots for {args.container}")
        return
    for i, snap in enumerate(snaps, 1):
        ts = snap.timestamp.strftime("%Y-%m-%d %H:%M")
        ref = snap.digest or snap.image_ref
        print(f"  [{i}]  {ts}  {ref}")


def cmd_snapshot(args: argparse.Namespace) -> None:
    if not Engine(args.config).snapshot(args.container):
        sys.exit(1)


def cmd_restore_volume(args: argparse.Namespace) -> None:
    config = args.config
    container = args.container
    sm = SnapshotManager(config)
    docker = DockerClient()

    snaps = sm.list(container)
    if not snaps:
        print(f"No snapshots for {container}.")
        sys.exit(1)

    if args.snapshot_id:
        matches = [s for s in snaps
                   if s.path.name.removesuffix(".tar.gz") == args.snapshot_id]
        if not matches:
            print(f"Snapshot not found: {args.snapshot_id}")
            sys.exit(1)
        snap = matches[0]
    else:
        print(f"\nAvailable snapshots for {container}:")
        for i, s in enumerate(snaps, 1):
            ts = s.timestamp.strftime("%Y-%m-%d %H:%M")
            ref = s.digest or s.image_ref
            print(f"  [{i}]  {ts}  {ref}")
        n = len(snaps)
        try:
            raw = input(f"Select snapshot [1-{n}], 0 to cancel: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nCancelled.")
            return
        if raw == "0":
            return
        if not raw.isdigit() or not (1 <= int(raw) <= n):
            print("Invalid choice.")
            sys.exit(1)
        snap = snaps[int(raw) - 1]

    vol_data = sm.load_volumes(snap)
    volumes = vol_data.get("volumes", [])
    skipped = vol_data.get("skipped", [])

    if not volumes and not skipped:
        print("No volume data recorded for this snapshot.")
        return

    entries = []
    for v in volumes:
        archive_dir = v.get("archive_dir")
        loc = (Path(archive_dir) / container / v["archive_name"]
               if archive_dir else config.snapshot_dir_for(container) / container / v["archive_name"])
        status = ("archived (external)" if archive_dir and loc.exists()
                  else "archived (missing)" if not loc.exists()
                  else "archived")
        entries.append(("volume", v, status, loc))
    for s in skipped:
        entries.append(("skipped", s, f"skipped: {s['reason']}", None))

    ts_str = snap.timestamp.strftime("%Y-%m-%d %H:%M")
    print(f"\n  ── Mounts for {container} — {ts_str} {'─' * 10}\n")
    for i, (kind, entry, status, _loc) in enumerate(entries, 1):
        cp = entry["container_path"]
        hp = entry.get("host_path", "")
        print(f"  [{i}]  {cp:<25}  {hp:<40}  {status}")
    print("\n  [0]  Cancel")

    try:
        raw = input("\n  Select mount: ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\nCancelled.")
        return
    if raw == "0":
        return
    if not raw.isdigit() or not (1 <= int(raw) <= len(entries)):
        print("Invalid choice.")
        return

    kind, entry, _status, known_path = entries[int(raw) - 1]
    cp = entry["container_path"]

    if kind == "volume":
        if known_path and known_path.exists():
            print(f"\n  1  Restore from {known_path}")
            print("  2  Browse to a different archive")
            print("  0  Cancel")
            try:
                choice = input("  [1/2/0]: ").strip()
            except (EOFError, KeyboardInterrupt):
                print("\nCancelled.")
                return
            if choice == "0":
                return
            if choice == "1":
                archive = known_path
            elif choice == "2":
                archive = _browse_path(Path("/"), mode="file", filter_ext=".gz")
                if not archive:
                    print("  Cancelled.")
                    return
            else:
                print("  Invalid choice.")
                return
        else:
            print(f"\n  Archive not found at expected location.")
            if known_path:
                print(f"  Expected: {known_path}")
            print("  1  Browse to archive")
            print("  0  Cancel")
            try:
                choice = input("  [1/0]: ").strip()
            except (EOFError, KeyboardInterrupt):
                print("\nCancelled.")
                return
            if choice != "1":
                return
            archive = _browse_path(Path("/"), mode="file", filter_ext=".gz")
            if not archive:
                print("  Cancelled.")
                return
    else:
        print(f"\n  No archive was recorded for {cp} ({entry['reason']}).")
        print("  1  Browse to an archive file")
        print("  0  Cancel")
        try:
            choice = input("  [1/0]: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nCancelled.")
            return
        if choice != "1":
            return
        archive = _browse_path(Path("/"), mode="file", filter_ext=".gz")
        if not archive:
            print("  Cancelled.")
            return

    try:
        result = docker._run(["inspect", "--format", "{{.State.Running}}", container])
        if "true" in result.stdout.lower():
            print(f"\n  Warning: {container} is currently running.")
            print("  Restoring will overwrite live data on disk.")
            try:
                confirm = input("  Continue? [y/N]: ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                print("\nCancelled.")
                return
            if confirm != "y":
                print("  Aborted.")
                return
    except DockerError:
        pass

    print(f"\n  Restoring {cp} from {archive.name}...")
    try:
        with tarfile.open(archive, "r:gz") as tar:
            tar.extractall(path="/")
        log(f"[restore-volume {container}] restored {cp} from {archive}")
        print("  Done.")
    except Exception as e:
        log(f"[restore-volume {container}] restore failed for {cp}: {e}")
        print(f"  Restore failed: {e}")
        sys.exit(1)


def _rules_summary(rules: dict) -> str:
    if not rules:
        return "all"
    if not rules.get("enabled", True):
        return "disabled"
    only = rules.get("include_only_mounts")
    skip = rules.get("skip_mounts", [])
    excl = rules.get("exclude", [])
    parts = []
    if only is not None:
        parts.append("only: " + ", ".join(only))
    elif skip:
        parts.append("skip: " + ", ".join(skip))
    else:
        parts.append("all")
    if excl:
        parts.append("excl: " + ", ".join(excl))
    return "  ".join(parts)


def _volumes_list_all(config: Config, docker: DockerClient) -> None:
    try:
        result = docker._run(["ps", "--format", "{{.Names}}"])
        names = sorted(n.strip() for n in result.stdout.splitlines() if n.strip())
    except DockerError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    if not names:
        print("No running containers.")
        return
    rows = []
    for name in names:
        try:
            data = docker.inspect(name)
            binds = data.get("HostConfig", {}).get("Binds") or []
            named_vols = _get_named_volumes(data)
            rules = config.volume_backup.get(name, {})
            rows.append((name, str(len(binds) + len(named_vols)), _rules_summary(rules)))
        except DockerError:
            rows.append((name, "?", "error"))
    _print_table(["CONTAINER", "MOUNTS", "BACKUP RULES"], rows)


def _volumes_show_one(config: Config, docker: DockerClient, container: str) -> None:
    try:
        data = docker.inspect(container)
    except DockerError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    binds = data.get("HostConfig", {}).get("Binds") or []
    named_vols = _get_named_volumes(data)
    rules = config.volume_backup.get(container, {})
    skip_mounts = set(rules.get("skip_mounts", []))
    include_only = rules.get("include_only_mounts")
    exclude_patterns = rules.get("exclude", [])
    globally_off = not config.volume_backup_enabled
    container_off = not rules.get("enabled", True)
    backup_off = globally_off or container_off

    bind_noun = "bind mount" if len(binds) == 1 else "bind mounts"
    vol_noun  = "named volume" if len(named_vols) == 1 else "named volumes"
    summary_parts = [f"{len(binds)} {bind_noun}"]
    if named_vols:
        summary_parts.append(f"{len(named_vols)} {vol_noun}")
    disabled_label = ""
    if globally_off:
        disabled_label = "  [backup DISABLED globally]"
    elif container_off:
        disabled_label = "  [backup DISABLED]"
    print(f"{container} — {', '.join(summary_parts)}{disabled_label}\n")

    if not binds and not named_vols:
        print("  (no bind mounts or named volumes)")
        return

    def _mount_status(container_path: str) -> str:
        if backup_off:
            return "disabled"
        if include_only is not None:
            return "backed up" if container_path in include_only else "skipped (not in whitelist)"
        if container_path in skip_mounts:
            return "skipped"
        return "backed up"

    if binds:
        rows = []
        for bind in binds:
            parts = bind.split(":")
            host_path, container_path = parts[0], parts[1] if len(parts) > 1 else ""
            rows.append((container_path, host_path, _mount_status(container_path)))
        _print_table(["CONTAINER PATH", "HOST PATH", "STATUS"], rows)
    else:
        print("  (no bind mounts)")

    if named_vols:
        print()
        rows = []
        for vol in named_vols:
            rows.append((vol["Destination"], vol["Name"], _mount_status(vol["Destination"])))
        _print_table(["CONTAINER PATH", "VOLUME NAME", "STATUS"], rows)

    save_path = rules.get("save_path", "")
    print(f"\nContainer save path: {save_path or '(default)'}")
    print(f"Exclude patterns: {', '.join(exclude_patterns) if exclude_patterns else '(none)'}")


def cmd_volumes(args: argparse.Namespace) -> None:
    docker = DockerClient()
    if getattr(args, "volumes_action", None) == "show":
        _volumes_show_one(args.config, docker, args.container)
    else:
        _volumes_list_all(args.config, docker)


def cmd_volumes_set(args: argparse.Namespace) -> None:
    config = args.config
    container = args.container

    if args.reset:
        config.volume_backup.pop(container, None)
        config.save()
        print(f"Cleared all backup rules for {container}.")
        return

    rules = dict(config.volume_backup.get(container, {}))
    changed = False

    if args.disable:
        if rules.get("enabled", True):
            rules["enabled"] = False
            changed = True
    elif args.enable:
        if not rules.get("enabled", True):
            rules.pop("enabled", None)
            changed = True

    if args.skip or args.unskip:
        skip = list(rules.get("skip_mounts", []))
        for path in args.skip:
            if path not in skip:
                skip.append(path)
                changed = True
        for path in args.unskip:
            if path in skip:
                skip.remove(path)
                changed = True
        if skip:
            rules["skip_mounts"] = skip
        else:
            rules.pop("skip_mounts", None)

    if args.clear_only:
        if "include_only_mounts" in rules:
            rules.pop("include_only_mounts")
            changed = True
    elif args.only:
        rules["include_only_mounts"] = list(args.only)
        changed = True

    if args.exclude or args.no_exclude:
        excl = list(rules.get("exclude", []))
        for pat in args.exclude:
            if pat not in excl:
                excl.append(pat)
                changed = True
        for pat in args.no_exclude:
            if pat in excl:
                excl.remove(pat)
                changed = True
        if excl:
            rules["exclude"] = excl
        else:
            rules.pop("exclude", None)

    if args.mount_path or args.no_mount_path:
        mount_paths = dict(rules.get("mount_paths", {}))
        for container_path, archive_dir in args.mount_path:
            if mount_paths.get(container_path) != archive_dir:
                mount_paths[container_path] = archive_dir
                changed = True
        for container_path in args.no_mount_path:
            if container_path in mount_paths:
                mount_paths.pop(container_path)
                changed = True
        if mount_paths:
            rules["mount_paths"] = mount_paths
        else:
            rules.pop("mount_paths", None)

    if getattr(args, "no_save_path", False):
        if "save_path" in rules:
            rules.pop("save_path")
            changed = True
    elif getattr(args, "save_path", None):
        if rules.get("save_path") != args.save_path:
            rules["save_path"] = args.save_path
            changed = True

    encrypt_mounts = getattr(args, "encrypt_vol", []) or []
    no_encrypt_mounts = getattr(args, "no_encrypt_vol", []) or []
    if encrypt_mounts or no_encrypt_mounts:
        enc_cfg = config.encryption
        enc_containers = list(enc_cfg.get("encrypt_containers", []))
        vol_map = dict(enc_cfg.get("encrypt_volumes", {}))
        for mount in encrypt_mounts:
            existing = list(vol_map.get(container, []))
            if mount not in existing:
                existing.append(mount)
                vol_map[container] = existing
                changed = True
            if container not in enc_containers:
                enc_containers.append(container)
                changed = True
        for mount in no_encrypt_mounts:
            existing = list(vol_map.get(container, []))
            if mount in existing:
                existing.remove(mount)
                if existing:
                    vol_map[container] = existing
                else:
                    vol_map.pop(container, None)
                changed = True
        enc_cfg["encrypt_containers"] = enc_containers
        enc_cfg["encrypt_volumes"] = vol_map

    if not changed:
        print(f"No changes made for {container}.")
        return

    if rules:
        config.volume_backup[container] = rules
    else:
        config.volume_backup.pop(container, None)

    config.save()
    summary = _rules_summary(config.volume_backup.get(container, {}))
    enc_note = ""
    if encrypt_mounts or no_encrypt_mounts:
        vol_enc = config.encryption.get("encrypt_volumes", {}).get(container, [])
        if "all" in vol_enc:
            enc_note = "  [encrypt: all volumes]"
        elif vol_enc:
            enc_note = f"  [encrypt: {', '.join(vol_enc)}]"
        else:
            enc_note = "  [encrypt: none]"
    print(f"Updated {container}: {summary}{enc_note}")


def cmd_volumes_backup(args: argparse.Namespace) -> None:
    config = args.config
    container = args.container
    target_mount = args.mount or None

    docker = DockerClient()
    try:
        inspect_data = docker.inspect(container)
    except DockerError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    timestamp = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
    staging = Path(tempfile.mkdtemp(prefix="rbp_vol_"))
    try:
        do_pause = (config.pause_for_backup
                    and container not in config.pause_for_backup_disabled)
        if do_pause:
            try:
                docker._run(["pause", container])
            except DockerError as e:
                print(f"Could not pause {container}: {e} — backing up live")
                do_pause = False
        try:
            def _pw_fn(cp: str) -> "str | None":
                return _get_password(config, container, mount=cp)
            Engine(config)._backup_volumes(container, timestamp, inspect_data,
                                           staging, paused=do_pause,
                                           password_fn=_pw_fn,
                                           target_mount=target_mount)
        finally:
            if do_pause:
                try:
                    docker._run(["unpause", container])
                except DockerError as e:
                    print(f"WARNING: failed to unpause {container}: {e}", file=sys.stderr)
        idx_path = staging / f"{timestamp}_volumes.json"
        if idx_path.exists():
            idx = json.loads(idx_path.read_text())
            n_done = len(idx.get("volumes", []))
            n_skip = len(idx.get("skipped", []))
            print(f"Done: {n_done} archived, {n_skip} skipped.")
        else:
            print("Done (no volume index written).")
    finally:
        shutil.rmtree(str(staging), ignore_errors=True)


def _fmt_uptime(started_at: str) -> str:
    if not started_at or started_at.startswith("0001-"):
        return "—"
    try:
        ts = started_at.replace("Z", "+00:00")
        if "." in ts:
            dot = ts.index(".")
            plus = ts.index("+", dot)
            ts = ts[:dot + 7] + ts[plus:]  # truncate nanoseconds to microseconds
        dt = datetime.fromisoformat(ts)
        delta = datetime.now(tz=dt.tzinfo) - dt
        s = max(0, int(delta.total_seconds()))
        if s < 60:
            return f"{s}s"
        if s < 3600:
            return f"{s // 60}m"
        if s < 86400:
            h, m = s // 3600, (s % 3600) // 60
            return f"{h}h {m}m" if m else f"{h}h"
        d, h = s // 86400, (s % 86400) // 3600
        return f"{d}d {h}h" if h else f"{d}d"
    except Exception:
        return "?"


def _fetch_one_status(name: str, docker: DockerClient,
                      registry: RegistryClient,
                      sm: SnapshotManager,
                      config: "Config",
                      load_snaps: bool = True) -> tuple:
    """Fetch (name, health, update, version, date, image, snaps, backup_col, mounts,
    uptime, restarts, ports, network, compose)."""
    try:
        data = docker.inspect(name)
        image = data.get("Config", {}).get("Image", "")
        state = data.get("State", {})
        raw_status = state.get("Status", "unknown")
        hobj = state.get("Health")
        if hobj is None:
            health = raw_status
        else:
            hs = hobj.get("Status", "")
            health = hs if hs in ("healthy", "unhealthy", "starting") else raw_status
        try:
            pinned_tag = config.pinned_tags.get(name, "")
            active_ref = _get_active_image_ref(config, name, data)
            update = "yes" if registry.has_update(data, pinned_tag=pinned_tag,
                                                  image_ref_override=active_ref) else "no"
        except RegistryError:
            update = "?"
        version = data.get("ImageVersion", "")
        if not version:
            tag = image.rsplit(":", 1)[-1] if ":" in image else ""
            version = tag if tag and any(c.isdigit() for c in tag) else "?"
        date = data.get("ImageCreated", "") or "?"
        binds = data.get("HostConfig", {}).get("Binds") or []
        rules = config.volume_backup.get(name, {})
        globally_off = not config.volume_backup_enabled
        container_off = not rules.get("enabled", True)
        backup_off = globally_off or container_off
        skip_mounts = set(rules.get("skip_mounts", []))
        include_only = rules.get("include_only_mounts")
        mount_lines, symbol_lines = [], []
        for b in binds:
            parts = b.split(":")
            host, container_path = parts[0], parts[1] if len(parts) > 1 else ""
            mount_lines.append(f"{host} → {container_path}")
            if backup_off:
                symbol_lines.append("-")
            elif include_only is not None:
                symbol_lines.append("*" if container_path in include_only else "-")
            elif container_path in skip_mounts:
                symbol_lines.append("X")
            else:
                symbol_lines.append("+")
        mounts = "\n".join(mount_lines) if mount_lines else "—"
        backup_col = "\n".join(symbol_lines) if symbol_lines else "—"
        snap_count = len(sm.list(name)) if load_snaps else "?"
        # --- sprint 5: inspect-derived columns ---
        uptime = _fmt_uptime(state.get("StartedAt", ""))
        restarts = str(state.get("RestartCount", 0))
        port_bindings = data.get("HostConfig", {}).get("PortBindings") or {}
        host_ports = []
        for _bindings in port_bindings.values():
            for _b in (_bindings or []):
                _hp = _b.get("HostPort", "")
                if _hp and _hp not in host_ports:
                    host_ports.append(_hp)
        ports = ",".join(sorted(host_ports, key=lambda x: int(x) if x.isdigit() else 0)) if host_ports else "—"
        network_mode = data.get("HostConfig", {}).get("NetworkMode", "")
        if network_mode in ("host", "none"):
            network = network_mode
        elif network_mode.startswith("container:"):
            network = "ctr:" + network_mode[10:]
        else:
            _networks = data.get("NetworkSettings", {}).get("Networks", {})
            network = next(iter(_networks), network_mode or "—")
        compose = data.get("Config", {}).get("Labels", {}).get("com.docker.compose.project", "—")
        return (name, health, update, version, date, image, snap_count, backup_col, mounts,
                uptime, restarts, ports, network, compose)
    except DockerError:
        return (name, "error", "?", "?", "?", "?", "?", "—", "—", "—", "?", "—", "—", "—")


def _browse_path(start: Path, mode: str = "dir", filter_ext: str = "") -> Path | None:
    """Interactive filesystem navigator.

    mode='dir'  — navigate and confirm a directory; [0] selects the current dir.
    mode='file' — navigate directories; selecting a matching file returns it.
    filter_ext  — when set (e.g. '.json'), only files with that extension are listed.

    Returns the chosen Path or None if the user cancels with c.
    """
    current = start.resolve()
    while True:
        title = "Select Directory" if mode == "dir" else "Select File"
        print(f"\n─── {title} {'─' * max(1, 44 - len(title))}")
        print(f"  {current}\n")

        try:
            all_entries = sorted(current.iterdir(), key=lambda p: p.name.lower())
        except PermissionError:
            print("  (permission denied — moving up)")
            current = current.parent
            continue

        dirs = [e for e in all_entries if e.is_dir()]
        files = (
            [e for e in all_entries if e.is_file()
             and (not filter_ext or e.suffix == filter_ext)]
            if mode == "file" else []
        )

        # Build numbered item list: optional ".." first, then dirs, then files.
        items = []
        if current != current.parent:  # not at filesystem root
            items.append(("..", current.parent))
        for d in dirs:
            items.append((f"{d.name}/", d))
        for f in files:
            items.append((f.name, f))

        if mode == "dir":
            print(f"  [ 0]  Confirm this location")
        for i, (label, _) in enumerate(items, 1):
            print(f"  [{i:2}]  {label}")
        print()

        n = len(items)
        if mode == "dir":
            prompt = f"[0] confirm, [1-{n}] navigate, m=new folder, p=permissions, d=delete folder, c to cancel: " if n else "[0] confirm, m=new folder, p=permissions, d=delete folder, c to cancel: "
        else:
            prompt = f"[1-{n}] select, m=new folder, p=permissions, d=delete folder, c to cancel: " if n else "m=new folder, p=permissions, d=delete folder, c to cancel: "

        try:
            raw = input(prompt).strip().lower()
        except (EOFError, KeyboardInterrupt):
            print()
            return None

        if raw in ("c", "cancel"):
            return None
        if mode == "dir" and raw == "0":
            return current

        if raw == "m":
            try:
                folder_name = input("  New folder name: ").strip()
            except (EOFError, KeyboardInterrupt):
                print()
                continue
            if not folder_name or "/" in folder_name or folder_name in (".", ".."):
                print("  Invalid folder name.")
                continue
            new_dir = current / folder_name
            try:
                new_dir.mkdir(mode=0o700)
                print(f"  Created: {new_dir}")
                current = new_dir
            except FileExistsError:
                print(f"  Already exists: {new_dir}")
            except OSError as e:
                print(f"  Create failed: {e}")
            continue

        if raw == "p":
            presets = [
                (0o700, "rwx------"),
                (0o750, "rwxr-x---"),
                (0o755, "rwxr-xr-x"),
                (0o777, "rwxrwxrwx"),
            ]
            try:
                sym_cur, oct_cur = _format_mode(current.stat().st_mode)
                print(f"\n  Current: {sym_cur}  ({oct_cur})")
            except OSError:
                pass
            for i, (mode_val, sym) in enumerate(presets, 1):
                print(f"  {i}  {oct(mode_val)}  {sym}")
            print("  5  Custom")
            print()
            try:
                p = input("[1-5]: ").strip()
            except (EOFError, KeyboardInterrupt):
                print()
                continue
            if p in ("1", "2", "3", "4"):
                new_mode = presets[int(p) - 1][0]
            elif p == "5":
                try:
                    raw_oct = input("Octal (e.g. 0o750): ").strip()
                    new_mode = int(raw_oct, 8)
                except (EOFError, KeyboardInterrupt, ValueError):
                    print("  Invalid.")
                    continue
            else:
                print("  Invalid choice.")
                continue
            try:
                current.chmod(new_mode)
                sym_new, oct_new = _format_mode(current.stat().st_mode)
                print(f"  Mode set: {sym_new}  ({oct_new})")
                log(f"[browse_path] chmod {current}: {oct_new}")
            except OSError as e:
                print(f"  chmod failed: {e}")
            continue

        if raw == "d":
            if current == current.parent:
                print("  Cannot delete filesystem root.")
                continue
            all_items = list(current.rglob("*"))
            file_count = sum(1 for p in all_items if p.is_file())
            dir_count = sum(1 for p in all_items if p.is_dir())
            if file_count == 0 and dir_count == 0:
                summary = "empty folder"
            else:
                parts = []
                if file_count:
                    parts.append(f"{file_count} file{'s' if file_count != 1 else ''}")
                if dir_count:
                    parts.append(f"{dir_count} subfolder{'s' if dir_count != 1 else ''}")
                summary = ", ".join(parts)
            print(f"\n  Delete: {current}")
            print(f"  Contents: {summary}")
            print("  This cannot be undone.")
            try:
                confirm = input("  Type 'yes' to confirm: ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                print()
                continue
            if confirm != "yes":
                print("  Cancelled.")
                continue
            target_to_delete = current
            current = current.parent
            try:
                shutil.rmtree(str(target_to_delete))
                print(f"  Deleted: {target_to_delete}")
                log(f"[browse_path] deleted dir {target_to_delete}")
            except OSError as e:
                print(f"  Delete failed: {e}")
                current = target_to_delete
            continue

        if not raw.isdigit() or not (1 <= int(raw) <= n):
            print("Invalid choice.")
            continue

        _, target = items[int(raw) - 1]
        if target.is_dir():
            current = target
        else:
            return target  # file selected in file mode


def _prompt_missing_volume(container_path: str, archive_name: str) -> Path | None:
    print(f"\n  Volume archive not found: {container_path}")
    print(f"  Expected filename: {archive_name}")
    print("  1  Locate archive")
    print("  2  Skip this mount")
    print("  q  Quit")
    while True:
        try:
            choice = input("  [1/2/q]: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return None
        if choice in ("q", "quit"):
            print("\nGoodbye.")
            sys.exit(0)
        if choice == "1":
            return _browse_path(Path("/"), mode="file", filter_ext=".gz")
        if choice == "2":
            return None
        print("  Invalid choice.")


def _show_skipped_volumes_dialogue(container: str, skipped: list) -> None:
    width = max(1, 44 - len(container))
    print(f"\n  ── Volumes not restored {'─' * width}")
    print("  These mounts were not backed up. Their data was not changed by the rollback.\n")
    _print_table(
        ["Container path", "Host path", "Reason"],
        [(e["container_path"], e.get("host_path", ""), e["reason"]) for e in skipped],
        max_widths={1: 40},
    )
    print(f"\n  To restore a skipped volume from an external archive, run:")
    print(f"    update_zen restore-volume {container}")
    try:
        input("\n  Press Enter to continue.")
    except (EOFError, KeyboardInterrupt):
        print()


def _show_unrestored_named_volumes_dialogue(container: str, volumes: list) -> None:
    width = max(1, 38 - len(container))
    print(f"\n  ── Named volumes not restored {'─' * width}")
    print("  These named volumes existed at backup time but have no archive.\n")
    _print_table(
        ["Volume name", "Container path"],
        [(v["Name"], v["Destination"]) for v in volumes],
    )
    print(f"\n  To restore from an external archive, run:")
    print(f"    update_zen restore-volume {container}")
    try:
        input("\n  Press Enter to continue.")
    except (EOFError, KeyboardInterrupt):
        print()


def _execute_rollback(config: Config, sm: SnapshotManager,
                       container: str, snap: "Snapshot") -> None:
    """Execute rollback to snap: print compose notice, run Engine.rollback, show post-rollback dialogues."""
    try:
        snap_id = snap.path.name.removesuffix(".tar.gz")
        with tarfile.open(snap.path, "r:gz") as tar:
            tar.getmember(f"{snap_id}_compose.yaml")
        print("\n  Compose file included in this snapshot.")
    except KeyError:
        pass

    Engine(config).rollback(container, snap, ext_overrides={})

    vol_data = sm.load_volumes(snap)
    skipped = vol_data.get("skipped", [])
    if skipped:
        _show_skipped_volumes_dialogue(container, skipped)
    try:
        inspect_data = sm.load(snap)
    except Exception:
        inspect_data = {}
    all_named = _get_named_volumes(inspect_data)
    if all_named:
        restored_paths = {v["container_path"] for v in vol_data.get("volumes", [])}
        unrestored = [v for v in all_named if v["Destination"] not in restored_paths]
        if unrestored:
            _show_unrestored_named_volumes_dialogue(container, unrestored)


def _interactive_snapshot_list(config: Config, sm: SnapshotManager,
                                container: str,
                                enc: "EncryptionManager | None" = None,
                                rollback_mode: bool = False) -> None:
    """Combined snapshot list screen.

    rollback_mode=True : selecting a snapshot immediately executes the rollback.
    rollback_mode=False: selecting a snapshot shows details and offers a rollback sub-choice.
    """
    snaps = sm.list(container)
    if not snaps:
        print(f"No snapshots for {container}.")
        return

    while True:
        title = "Rollback" if rollback_mode else "Snapshots"
        print(f"\n─── {container} — {title} {'─' * max(1, 44 - len(container) - len(title))}")
        for i, snap in enumerate(snaps, 1):
            ts = snap.timestamp.strftime("%Y-%m-%d %H:%M")
            version_str = f"  {snap.version}" if snap.version else ""
            # Shorten digest to just the hash prefix for readability
            if snap.digest and "@sha256:" in snap.digest:
                ref_short = "sha256:" + snap.digest.split("@sha256:")[1][:12]
            else:
                ref_short = snap.digest or snap.image_ref
            # Content flags
            flags = []
            snap_id = snap.path.name.removesuffix(".tar.gz")
            try:
                with tarfile.open(snap.path, "r:gz") as _tar:
                    _members = _tar.getnames()
                for member, label in ((f"{snap_id}_compose.yaml", "compose"),
                                      (f"{snap_id}_env.env", "env"),
                                      (f"{snap_id}_image.tar", "image")):
                    if member in _members:
                        flags.append(label)
            except Exception:
                pass
            # Volume archive count
            try:
                vol_data = sm.load_volumes(snap)
                n_vols = len(vol_data.get("volumes", []))
                if n_vols:
                    vol_label = f"{n_vols} vol{'s' if n_vols != 1 else ''}"
                    if "image" in flags:
                        flags.insert(flags.index("image"), vol_label)
                    else:
                        flags.append(vol_label)
            except Exception:
                pass
            # Bundle size + per-mount archive count on disk
            try:
                sz = snap.path.stat().st_size
                if sz < 1024:
                    size_str = f"bundle: {sz}B"
                elif sz < 1024 * 1024:
                    size_str = f"bundle: {sz / 1024:.0f}KB"
                elif sz < 1024 * 1024 * 1024:
                    size_str = f"bundle: {sz / 1024 / 1024:.1f}MB"
                else:
                    size_str = f"bundle: {sz / 1024 / 1024 / 1024:.1f}GB"
            except OSError:
                size_str = ""
            vol_archive_count = 0
            try:
                vol_archive_count = sum(
                    1 for _ in snap.path.parent.glob(f"{snap_id}_*.tar.gz")
                )
            except OSError:
                pass
            vol_archive_part = f"  +{vol_archive_count} vol archive{'s' if vol_archive_count != 1 else ''}" if vol_archive_count else ""
            flag_str = f"  [{', '.join(flags)}]" if flags else ""
            size_part = f"  {size_str}{vol_archive_part}" if size_str else ""
            print(f"  [{i}]  {ts}{version_str}  {ref_short}{flag_str}{size_part}")
        print()
        n = len(snaps)
        verb = "roll back to" if rollback_mode else "select"
        try:
            raw = input(f"[1-{n}] {verb}, 0 to go back, q to quit: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return
        if raw == "0":
            return
        if raw in ("q", "quit"):
            print("\nGoodbye.")
            sys.exit(0)
        if not raw.isdigit() or not (1 <= int(raw) <= n):
            print("Invalid choice.")
            continue

        snap = snaps[int(raw) - 1]

        if rollback_mode:
            _execute_rollback(config, sm, container, snap)
            return

        # View mode — show snapshot details and offer rollback sub-choice
        ts = snap.timestamp.strftime("%Y-%m-%d %H:%M")
        if snap.digest and "@sha256:" in snap.digest:
            ref_display = "sha256:" + snap.digest.split("@sha256:")[1][:12]
        else:
            ref_display = snap.digest or snap.image_ref
        version_part = f"  {snap.version}" if snap.version else ""
        print(f"\n─── {container} — {ts}{version_part} {'─' * max(1, 44 - len(container) - 16)}")
        print(f"    {ref_display}\n")
        print("  1   Roll back to this snapshot")
        print("  0   Back")
        print()
        try:
            sub = input("[1], 0 to go back, q to quit: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            continue
        if sub == "0":
            continue
        if sub in ("q", "quit"):
            print("\nGoodbye.")
            sys.exit(0)
        if sub == "1":
            _execute_rollback(config, sm, container, snap)
            return


def _interactive_exclude_patterns(config: Config, container: str) -> None:
    while True:
        rules = dict(config.volume_backup.get(container, {}))
        excl = rules.get("exclude", [])

        print(f"\n─── Exclude patterns for {container} {'─' * max(1, 40 - len(container))}")
        if excl:
            for i, pat in enumerate(excl, 1):
                print(f"  [{i:2}]  {pat}")
        else:
            print("  (none)")
        print()
        print("   a  Add pattern")
        if excl:
            print("  [#]  Remove pattern by number")
        print("   0  Back")
        print("   q  Quit")
        print()

        try:
            raw = input("Choice: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print()
            return

        if raw == "0":
            return
        if raw in ("q", "quit"):
            print("\nGoodbye.")
            sys.exit(0)
        elif raw == "a":
            try:
                pat = input("Glob pattern to exclude (e.g. *.log): ").strip()
            except (EOFError, KeyboardInterrupt):
                print()
                continue
            if pat and pat not in excl:
                excl.append(pat)
                rules["exclude"] = excl
                config.volume_backup[container] = rules
                config.save()
                print(f"Added '{pat}'.")
            elif pat in excl:
                print(f"'{pat}' is already in the list.")
        elif raw.isdigit() and excl and 1 <= int(raw) <= len(excl):
            removed = excl.pop(int(raw) - 1)
            if excl:
                rules["exclude"] = excl
            else:
                rules.pop("exclude", None)
            if rules:
                config.volume_backup[container] = rules
            else:
                config.volume_backup.pop(container, None)
            config.save()
            print(f"Removed '{removed}'.")
        else:
            print("Invalid choice.")


def _interactive_mount_action(config: Config, container: str,
                               container_path: str, host_path: str,
                               vol_name: str = "",
                               all_mounts: "list[str] | None" = None) -> None:
    rules = dict(config.volume_backup.get(container, {}))
    skip_mounts = list(rules.get("skip_mounts", []))
    include_only = rules.get("include_only_mounts")  # None = no whitelist active
    in_skip = container_path in skip_mounts
    in_whitelist = include_only is not None and container_path in include_only
    whitelist_active = include_only is not None
    mount_paths = dict(rules.get("mount_paths", {}))
    custom_path = mount_paths.get(container_path)
    enc_vols = list(config.encryption.get("encrypt_volumes", {}).get(container, []))
    all_enc = "all" in enc_vols
    is_enc = all_enc or container_path in enc_vols

    enc_badge = "  [enc]" if is_enc else ""
    print(f"\n─── Mount: {container_path}{enc_badge} {'─' * max(1, 44 - len(container_path) - len(enc_badge))}")
    if vol_name:
        print(f"  Volume name: {vol_name}")
    else:
        print(f"  Host path:   {host_path}")
    print()

    # Build options dynamically based on current state
    options = []
    if in_skip:
        options.append("Unskip this mount")
    else:
        options.append("Skip this mount")

    if whitelist_active:
        if in_whitelist:
            options.append("Remove from include-only whitelist")
        else:
            options.append("Add to include-only whitelist")
    else:
        options.append("Start include-only whitelist with this mount")

    if custom_path:
        options.append(f"Change save path  (current: {custom_path})")
        options.append("Clear save path (use default location)")
    else:
        options.append("Set custom save path")
    options.append("Backup this mount now")
    options.append("Restore this mount from archive")
    enc_option_idx = len(options)
    options.append("Disable encryption for this mount" if is_enc
                   else "Enable encryption for this mount")
    browse_option_idx = len(options) + 1
    options.append("Browse archive folder")

    for i, label in enumerate(options, 1):
        print(f"  {i}  {label}")
    print("  0  Back")
    print("  q  Quit")
    print()

    try:
        raw = input(f"[1-{len(options)}], 0 to go back, q to quit: ").strip()
    except (EOFError, KeyboardInterrupt):
        print()
        return

    if raw == "0":
        return
    if raw in ("q", "quit"):
        print("\nGoodbye.")
        sys.exit(0)
    elif raw == "1":
        if in_skip:
            skip_mounts.remove(container_path)
            if skip_mounts:
                rules["skip_mounts"] = skip_mounts
            else:
                rules.pop("skip_mounts", None)
            print(f"Unskipped {container_path}.")
        else:
            if container_path not in skip_mounts:
                skip_mounts.append(container_path)
            rules["skip_mounts"] = skip_mounts
            # removing from include_only if present keeps state consistent
            if include_only is not None:
                new_only = [p for p in include_only if p != container_path]
                if new_only:
                    rules["include_only_mounts"] = new_only
                else:
                    rules.pop("include_only_mounts", None)
            print(f"Skipped {container_path}.")
    elif raw == "2":
        if whitelist_active:
            if in_whitelist:
                new_only = [p for p in include_only if p != container_path]
                if new_only:
                    rules["include_only_mounts"] = new_only
                else:
                    rules.pop("include_only_mounts", None)
                print(f"Removed {container_path} from whitelist.")
            else:
                rules["include_only_mounts"] = list(include_only) + [container_path]
                print(f"Added {container_path} to whitelist.")
        else:
            rules["include_only_mounts"] = [container_path]
            rules.pop("skip_mounts", None)
            print(f"Whitelist created with {container_path}. All other mounts will be skipped.")
    elif raw == "3":
        # "Set custom save path" (no custom_path) or "Change save path" (custom_path set)
        chosen = _browse_path(Path("/"), mode="dir")
        if chosen:
            mount_paths[container_path] = str(chosen)
            rules["mount_paths"] = mount_paths
            print(f"Custom save path set to {chosen}.")
        else:
            return
    elif raw == "4" and custom_path:
        # "Clear save path"
        mount_paths.pop(container_path, None)
        if mount_paths:
            rules["mount_paths"] = mount_paths
        else:
            rules.pop("mount_paths", None)
        print(f"Cleared custom save path for {container_path}.")
    elif (raw == "5" and custom_path) or (raw == "4" and not custom_path):
        # "Backup this mount now"
        p = Path(host_path)
        if not p.exists():
            label = f"Volume source path not found: {host_path}" if vol_name else f"Host path not found: {host_path}"
            print(label)
            return
        timestamp = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
        backup_base = (Path(custom_path) if custom_path
                       else Path(rules["save_path"]) if rules.get("save_path")
                       else config.snapshot_dir_for(container))
        ext_dir = backup_base / container
        ext_archive = ext_dir / f"{timestamp}.tar.gz"
        exclude_patterns = rules.get("exclude", [])
        def _tar_filter(tarinfo):
            for pat in exclude_patterns:
                if fnmatch.fnmatch(tarinfo.name, pat):
                    return None
            return tarinfo
        try:
            ext_dir.mkdir(parents=True, exist_ok=True)
            with tarfile.open(ext_archive, "w:gz") as tar:
                tar.add(host_path, arcname=host_path,
                        filter=_tar_filter if exclude_patterns else None)
            print(f"Backed up to {ext_archive}.")
        except Exception as e:
            print(f"Backup failed: {e}")
        return
    elif (raw == "6" and custom_path) or (raw == "5" and not custom_path):
        # "Restore this mount from archive"
        backup_base = (Path(custom_path) if custom_path
                       else Path(rules["save_path"]) if rules.get("save_path")
                       else config.snapshot_dir_for(container))
        restore_start = backup_base / container
        if not restore_start.exists():
            restore_start = backup_base if backup_base.exists() else Path("/")
        located = _browse_path(restore_start, mode="file", filter_ext=".gz")
        if located:
            try:
                with tarfile.open(located, "r:gz") as tar:
                    tar.extractall(path="/")
                print(f"Restored from {located}.")
            except Exception as e:
                print(f"Restore failed: {e}")
        return
    elif raw.isdigit() and int(raw) == enc_option_idx + 1:
        enc_map = dict(config.encryption.get("encrypt_volumes", {}))
        if is_enc:
            if all_enc:
                # Expand "all" shorthand to an explicit list minus this mount
                base = all_mounts if all_mounts is not None else []
                new_list = [m for m in base if m != container_path]
                if new_list:
                    enc_map[container] = new_list
                else:
                    enc_map.pop(container, None)
            else:
                new_list = [m for m in enc_vols if m != container_path]
                if new_list:
                    enc_map[container] = new_list
                else:
                    enc_map.pop(container, None)
            print(f"Encryption disabled for {container_path}.")
        else:
            enc_map[container] = list(enc_vols) + [container_path]
            print(f"Encryption enabled for {container_path}.")
        config.encryption["encrypt_volumes"] = enc_map
        config.save()
        return
    elif raw.isdigit() and int(raw) == browse_option_idx:
        if custom_path:
            archive_dir = Path(custom_path) / container
        elif rules.get("save_path"):
            archive_dir = Path(rules["save_path"]) / container
        else:
            archive_dir = config.snapshot_dir_for(container) / container
        if not archive_dir.exists():
            print(f"  Directory does not exist: {archive_dir}")
        else:
            selected = _browse_path(archive_dir, mode="file")
            if selected is not None:
                _file_action_menu(selected)
        return
    else:
        print("Invalid choice.")
        return

    if rules:
        config.volume_backup[container] = rules
    else:
        config.volume_backup.pop(container, None)
    config.save()


def _interactive_volume_encryption_menu(config: Config, docker: DockerClient,
                                         container: str) -> None:
    while True:
        try:
            data = docker.inspect(container)
        except DockerError as e:
            print(f"Error inspecting {container}: {e}")
            return

        binds = data.get("HostConfig", {}).get("Binds") or []
        named_vols = _get_named_volumes(data)
        mounts = []
        for bind in binds:
            parts = bind.split(":")
            if len(parts) > 1:
                mounts.append(parts[1])
        for vol in named_vols:
            mounts.append(vol["Destination"])

        enc_vols = list(config.encryption.get("encrypt_volumes", {}).get(container, []))
        all_enc = "all" in enc_vols

        print(f"\n─── Volume encryption: {container} {'─' * max(1, 36 - len(container))}")
        print()
        if not mounts:
            print("  (no bind mounts or named volumes)")
        else:
            for i, cp in enumerate(mounts, 1):
                enc_flag = "[enc]" if (all_enc or cp in enc_vols) else "     "
                print(f"  {i}  {enc_flag}  {cp}")
        print()
        print("   a  Encrypt all mounts")
        print("   n  Disable all encryption")
        print("   0  Back")
        print("   q  Quit")
        print()

        n = len(mounts)
        prompt = (f"[1-{n}] toggle mount, [a/n], 0 to go back, q to quit: " if n
                  else "[a/n], 0 to go back, q to quit: ")
        try:
            raw = input(prompt).strip().lower()
        except (EOFError, KeyboardInterrupt):
            print()
            return
        if raw == "0":
            return
        if raw in ("q", "quit"):
            print("\nGoodbye.")
            sys.exit(0)
        elif raw == "a":
            enc_map = dict(config.encryption.get("encrypt_volumes", {}))
            enc_map[container] = ["all"]
            config.encryption["encrypt_volumes"] = enc_map
            config.save()
            print(f"All mounts of {container} will be encrypted.")
        elif raw == "n":
            enc_map = dict(config.encryption.get("encrypt_volumes", {}))
            enc_map.pop(container, None)
            config.encryption["encrypt_volumes"] = enc_map
            config.save()
            print(f"Volume encryption disabled for {container}.")
        elif raw.isdigit() and n and 1 <= int(raw) <= n:
            cp = mounts[int(raw) - 1]
            enc_map = dict(config.encryption.get("encrypt_volumes", {}))
            if all_enc:
                # Expand "all" shorthand into explicit list, minus the toggled mount
                new_list = [m for m in mounts if m != cp]
                if new_list:
                    enc_map[container] = new_list
                else:
                    enc_map.pop(container, None)
                config.encryption["encrypt_volumes"] = enc_map
                config.save()
                print(f"Encryption disabled for {cp}.")
            elif cp in enc_vols:
                new_list = [m for m in enc_vols if m != cp]
                if new_list:
                    enc_map[container] = new_list
                else:
                    enc_map.pop(container, None)
                config.encryption["encrypt_volumes"] = enc_map
                config.save()
                print(f"Encryption disabled for {cp}.")
            else:
                new_list = list(enc_vols) + [cp]
                enc_map[container] = new_list
                config.encryption["encrypt_volumes"] = enc_map
                config.save()
                print(f"Encryption enabled for {cp}.")
        else:
            print("Invalid choice.")


def _interactive_volumes_menu(config: Config, docker: DockerClient,
                               container: str) -> None:
    while True:
        try:
            data = docker.inspect(container)
        except DockerError as e:
            print(f"Error: {e}", file=sys.stderr)
            return

        binds = data.get("HostConfig", {}).get("Binds") or []
        rules = config.volume_backup.get(container, {})
        skip_mounts = set(rules.get("skip_mounts", []))
        include_only = rules.get("include_only_mounts")
        globally_off = not config.volume_backup_enabled
        container_off = not rules.get("enabled", True)
        backup_off = globally_off or container_off

        named_vols = _get_named_volumes(data)
        enc_vols = config.encryption.get("encrypt_volumes", {}).get(container, [])
        if not enc_vols:
            enc_header = ""
        elif "all" in enc_vols:
            enc_header = "  [encryption: all mounts]"
        else:
            enc_header = f"  [encryption: {len(enc_vols)} mount{'s' if len(enc_vols) != 1 else ''}]"

        def _mount_status(container_path: str) -> str:
            if backup_off:
                return "disabled"
            if include_only is not None:
                return "backed up" if container_path in include_only else "skipped (not in whitelist)"
            if container_path in skip_mounts:
                return "skipped"
            return "backed up"

        mount_data = []   # (container_path, host_path, status, vol_name)
        for bind in binds:
            parts = bind.split(":")
            host_path = parts[0]
            container_path = parts[1] if len(parts) > 1 else ""
            mount_data.append((container_path, host_path, _mount_status(container_path), ""))
        for vol in named_vols:
            mount_data.append((vol["Destination"], vol["Source"],
                               _mount_status(vol["Destination"]), vol["Name"]))

        disabled_label = ""
        if globally_off:
            disabled_label = "  [backup DISABLED globally]"
        elif container_off:
            disabled_label = "  [backup DISABLED]"
        trailer = disabled_label + enc_header
        print(f"\n─── Volume backup: {container}{trailer} {'─' * max(1, 40 - len(container) - len(trailer))}")
        print()

        if mount_data:
            _print_table(["#", "CONTAINER PATH", "HOST PATH / VOLUME", "STATUS"],
                         [(str(i), cp, vn or hp, st)
                          for i, (cp, hp, st, vn) in enumerate(mount_data, 1)])
        else:
            print("  (no bind mounts or named volumes)")
        print()

        excl_summary = ", ".join(rules.get("exclude", [])) or "none"
        backup_on = rules.get("enabled", True)
        toggle_label = "Disable backup for this container" if backup_on else "Enable backup for this container"
        save_path = rules.get("save_path", "")
        save_path_label = (f"Change default volume save path  (current: {save_path})"
                           if save_path else "Set default volume save path")
        print("   e  Configure volume encryption")
        print(f"   x  Exclude patterns  ({excl_summary})")
        print(f"   d  {save_path_label}")
        print(f"   t  {toggle_label}")
        print("   r  Reset all rules")
        print("   b  Backup all volumes now")
        print("   f  Browse archive folder")
        print("   0  Back")
        print("   q  Quit")
        print()

        n = len(mount_data)
        base_letters = "e/x/d/t/r/b/f"
        prompt = (f"[1-{n}] select mount, [{base_letters}], 0 to go back, q to quit: " if n
                  else f"[{base_letters}], 0 to go back, q to quit: ")
        try:
            raw = input(prompt).strip().lower()
        except (EOFError, KeyboardInterrupt):
            print()
            return

        if raw == "0":
            return
        if raw in ("q", "quit"):
            print("\nGoodbye.")
            sys.exit(0)
        elif raw == "e":
            _interactive_volume_encryption_menu(config, docker, container)
        elif raw == "x":
            _interactive_exclude_patterns(config, container)
        elif raw == "d":
            if save_path:
                print(f"\n  Current save path: {save_path}")
                print("  1  Change path")
                print("  2  Clear path")
                print("  0  Cancel")
                try:
                    sub = input("[1/2/0]: ").strip()
                except (EOFError, KeyboardInterrupt):
                    print()
                    continue
                if sub == "1":
                    chosen = _browse_path(Path("/"), mode="dir")
                    if chosen:
                        rules = dict(config.volume_backup.get(container, {}))
                        rules["save_path"] = str(chosen)
                        config.volume_backup[container] = rules
                        config.save()
                        print(f"Default volume save path set to {chosen}.")
                elif sub == "2":
                    rules = dict(config.volume_backup.get(container, {}))
                    rules.pop("save_path", None)
                    if rules:
                        config.volume_backup[container] = rules
                    else:
                        config.volume_backup.pop(container, None)
                    config.save()
                    print("Default volume save path cleared.")
            else:
                chosen = _browse_path(Path("/"), mode="dir")
                if chosen:
                    rules = dict(config.volume_backup.get(container, {}))
                    rules["save_path"] = str(chosen)
                    config.volume_backup[container] = rules
                    config.save()
                    print(f"Default volume save path set to {chosen}.")
        elif raw == "t":
            rules = dict(config.volume_backup.get(container, {}))
            if backup_on:
                rules["enabled"] = False
                print(f"Volume backup disabled for {container}.")
            else:
                rules.pop("enabled", None)
                print(f"Volume backup enabled for {container}.")
            if rules:
                config.volume_backup[container] = rules
            else:
                config.volume_backup.pop(container, None)
            config.save()
        elif raw == "r":
            try:
                yn = input(f"Reset all volume rules for {container}? [y/N]: ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                print()
                continue
            if yn == "y":
                config.volume_backup.pop(container, None)
                config.save()
                print("Rules cleared.")
        elif raw == "b":
            timestamp = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
            staging = Path(tempfile.mkdtemp(prefix="rbp_vol_"))
            try:
                do_pause = (config.pause_for_backup
                            and container not in config.pause_for_backup_disabled)
                if do_pause:
                    try:
                        docker._run(["pause", container])
                    except DockerError as e:
                        print(f"Could not pause {container}: {e} — backing up live")
                        do_pause = False
                try:
                    def _pw_fn(cp: str) -> "str | None":
                        return _get_password(config, container, mount=cp)
                    Engine(config)._backup_volumes(container, timestamp, data,
                                                   staging, paused=do_pause,
                                                   password_fn=_pw_fn)
                finally:
                    if do_pause:
                        try:
                            docker._run(["unpause", container])
                        except DockerError as e:
                            print(f"WARNING: failed to unpause {container}: {e}")
                idx_path = staging / f"{timestamp}_volumes.json"
                if idx_path.exists():
                    idx = json.loads(idx_path.read_text())
                    n_done = len(idx.get("volumes", []))
                    n_skip = len(idx.get("skipped", []))
                    print(f"Done: {n_done} archived, {n_skip} skipped.")
            except Exception as e:
                print(f"Backup failed: {e}")
            finally:
                shutil.rmtree(str(staging), ignore_errors=True)
        elif raw == "f":
            rules_f = config.volume_backup.get(container, {})
            if rules_f.get("save_path"):
                archive_dir = Path(rules_f["save_path"]) / container
            else:
                archive_dir = config.snapshot_dir_for(container) / container
            if not archive_dir.exists():
                print(f"  Directory does not exist: {archive_dir}")
            else:
                browse_start = archive_dir
                while True:
                    selected = _browse_path(browse_start, mode="file")
                    if selected is None:
                        break
                    browse_start = selected.parent
                    _file_action_menu(selected)
        elif raw.isdigit() and n and 1 <= int(raw) <= n:
            cp, hp, _, vn = mount_data[int(raw) - 1]
            all_cp = [m[0] for m in mount_data]
            _interactive_mount_action(config, container, cp, hp, vol_name=vn,
                                      all_mounts=all_cp)
        else:
            print("Invalid choice.")


def _interactive_registries_menu(config: Config, docker: DockerClient,
                                  container: str) -> None:
    # Auto-seed: inspect once and write to config so the list always has an entry.
    if container not in config.registry_alternatives:
        try:
            data = docker.inspect(container)
        except DockerError as e:
            print(f"Error inspecting {container}: {e}")
            return
        current_image = data.get("Config", {}).get("Image", "")
        if not current_image:
            print("Could not determine image reference.")
            return
        config.registry_alternatives[container] = {
            "refs": [current_image],
            "active": current_image,
        }
        config.save()

    while True:
        alts = config.registry_alternatives.get(container, {})
        refs = alts.get("refs", [])
        active = alts.get("active", "")
        n = len(refs)

        print(f"\n{'─' * 3} Registry sources: {container} {'─' * max(1, 36 - len(container))}")
        if active:
            reg_host = RegistryClient._parse_image_ref(active)[0]
            print(f"  Active: {active}  |  Registry: {reg_host}\n")

        tag_width = max((len(r) for r in refs), default=0)
        for i, ref in enumerate(refs, 1):
            reg_host = RegistryClient._parse_image_ref(ref)[0]
            marker = "  (active)" if ref == active else ""
            print(f"  [{i}]  {ref:<{tag_width}}  {reg_host}{marker}")

        print()
        print("   a  Add registry")
        if n > 1:
            print("   r  Remove an entry")
        print("   0  Back")
        print("   q  Quit")
        print()

        opts = f"1-{n}/a" if n > 1 else "1/a"
        if n > 1:
            opts += "/r"
        try:
            raw = input(f"[{opts}], 0 to go back, q to quit: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print()
            return

        if raw == "0":
            return
        if raw in ("q", "quit"):
            print("\nGoodbye.")
            sys.exit(0)

        elif raw == "a":
            try:
                new_ref = input("Enter image ref (e.g. myregistry.com:5000/nginx:latest): ").strip()
            except (EOFError, KeyboardInterrupt):
                print()
                continue
            if not new_ref:
                print("No input — cancelled.")
                continue
            reg, repo, tag = RegistryClient._parse_image_ref(new_ref)
            print(f"  → registry: {reg}  repo: {repo}  tag: {tag}")
            try:
                yn = input("Add this? [Y/n]: ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                print()
                continue
            if yn in ("n", "no"):
                print("Cancelled.")
                continue
            if new_ref in refs:
                print("Already in the list.")
                continue
            config.registry_alternatives[container] = {
                "refs": list(refs) + [new_ref],
                "active": active,
            }
            config.save()
            print(f"Added {new_ref}.")

        elif raw == "r" and n > 1:
            try:
                idx_raw = input(f"Remove which entry [1-{n}], 0 to cancel: ").strip()
            except (EOFError, KeyboardInterrupt):
                print()
                continue
            if idx_raw == "0":
                continue
            if not idx_raw.isdigit() or not (1 <= int(idx_raw) <= n):
                print("Invalid choice.")
                continue
            idx = int(idx_raw) - 1
            removed = refs[idx]
            new_refs = [r for i, r in enumerate(refs) if i != idx]
            new_active = active
            if removed == active:
                new_active = new_refs[0]
                print(f"Active registry reset to: {new_active}")
            config.registry_alternatives[container] = {
                "refs": new_refs,
                "active": new_active,
            }
            config.save()
            print(f"Removed {removed}.")

        elif raw.isdigit() and 1 <= int(raw) <= n:
            chosen = refs[int(raw) - 1]
            if chosen == active:
                print("Already active.")
            else:
                config.registry_alternatives[container] = {"refs": list(refs), "active": chosen}
                config.save()
                print(f"Active registry set to: {chosen}")

        else:
            print("Invalid choice.")


def _pick_version_tag(config: Config, docker: DockerClient,
                       registry: RegistryClient, name: str) -> str | None:
    """Fetch tag list for name's image, display it, and return the chosen tag or None."""
    try:
        data = docker.inspect(name)
    except DockerError as e:
        print(f"Error inspecting {name}: {e}")
        return None
    if not data.get("Config", {}).get("Image", ""):
        print("Could not determine image reference.")
        return None
    image_ref = _get_active_image_ref(config, name, data)
    current = data.get("ImageVersion", "")
    if not current:
        tag = image_ref.rsplit(":", 1)[-1] if ":" in image_ref else ""
        current = tag if tag and any(c.isdigit() for c in tag) else ""
    print("Fetching versions...")
    versions = registry.list_versions(image_ref)
    if not versions:
        print("No version history available for this image.")
        return None
    no_dates = all(d == "?" for _, d in versions)
    tag_width = max(len(t) for t, _ in versions)
    registry_host = image_ref.split("/")[0] if "/" in image_ref else "docker.io"
    total = len(versions)
    page_size = 15
    page = 0

    while True:
        start = page * page_size
        end = min(start + page_size, total)
        num_pages = (total + page_size - 1) // page_size

        print()
        if num_pages > 1:
            print(f"  -- page {page + 1} of {num_pages} --")
        for i in range(start, end):
            tag, date = versions[i]
            marker = "  ← current" if tag == current else ""
            date_col = f"  {date}" if not no_dates else ""
            print(f"  [{i + 1:2}]  {tag:<{tag_width}}{date_col}{marker}")
        if no_dates:
            print(f"\n  (release dates unavailable for {registry_host})")

        nav = []
        if page > 0:
            nav.append("[p]rev")
        if end < total:
            nav.append("[n]ext")
        nav_str = f"  {', '.join(nav)}" if nav else ""
        print()
        try:
            raw = input(f"Select [1-{total}]{nav_str}, 0 cancel, q quit: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print()
            return None

        if raw == "0":
            return None
        if raw in ("q", "quit"):
            print("\nGoodbye.")
            sys.exit(0)
        if raw == "n" and end < total:
            page += 1
            continue
        if raw == "p" and page > 0:
            page -= 1
            continue
        if raw.isdigit() and 1 <= int(raw) <= total:
            return versions[int(raw) - 1][0]
        print("Invalid choice.")


def _interactive_version_select(config: Config, docker: DockerClient,
                                registry: RegistryClient, name: str,
                                effective_ar: bool,
                                enc: "EncryptionManager | None" = None) -> None:
    try:
        data = docker.inspect(name)
    except DockerError as e:
        print(f"Error inspecting {name}: {e}")
        return
    if not data.get("Config", {}).get("Image", ""):
        print("Could not determine image reference.")
        return
    image_ref = _get_active_image_ref(config, name, data)
    current = data.get("ImageVersion", "")
    if not current:
        tag = image_ref.rsplit(":", 1)[-1] if ":" in image_ref else ""
        current = tag if tag and any(c.isdigit() for c in tag) else ""

    selected_tag = _pick_version_tag(config, docker, registry, name)
    if not selected_tag:
        return

    if selected_tag == current:
        try:
            yn = input(f"{selected_tag} is already running. Pull latest image and recreate? [y/N]: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nCancelled.")
            return
        if yn != "y":
            return

    print(f"\n  Selected: {selected_tag}\n")
    print("  1  Update to this version now")
    print("  2  Pin to this version (update on next run)")
    print("  3  Pin and update now")
    print("  0  Cancel")
    print()
    try:
        action = input("[1-3], 0 to cancel: ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\nCancelled.")
        return
    if action == "0":
        return
    if action in ("2", "3"):
        config.pinned_tags[name] = selected_tag
        config.save()
        print(f"Pinned {name} to {selected_tag}.")
    if action in ("1", "3"):
        Engine(config).update(name, tag=selected_tag, auto_rollback=effective_ar)


def _write_cron_config(config: "Config", container: str, recipe: str,
                       mount: "str | None", password: str) -> Path:
    """Generate a minimal per-job cron config directory with its own config.json
    and credentials.json (both plaintext). Returns the job directory path."""
    job_name = f"{container}_{recipe}"
    if mount:
        job_name += f"_{_sanitize_mount_name(mount)}"
    job_dir = CRON_CONFIG_DIR / job_name
    job_dir.mkdir(parents=True, exist_ok=True)
    job_dir.chmod(0o700)
    os.chown(job_dir, _INVOKING_UID, _INVOKING_GID)

    enc_containers = [container] if config.is_encryption_enabled(container) else []
    enc_volumes = {}
    raw_enc_vols = config.encryption.get("encrypt_volumes", {}).get(container)
    if raw_enc_vols:
        enc_volumes = {container: raw_enc_vols}

    minimal: dict = {
        "snapshot_dir": _to_portable_path(config.snapshot_dir),
        "log_file": _to_portable_path(config.log_file),
        "max_snapshots": config.max_snapshots,
        "volume_backup_enabled": config.volume_backup_enabled,
        "auto_rollback": config.auto_rollback,
        "health_timeout_sec": config.health_timeout_sec,
        "pause_for_backup": config.pause_for_backup,
        "image_export_enabled": config.image_export_enabled,
        "restart_stack_siblings": config.restart_stack_siblings,
        "gateway_wait_sec": config.gateway_wait_sec,
        "sibling_wait_sec": config.sibling_wait_sec,
        "encryption": {
            "mode": "saved",
            "encrypt_containers": enc_containers,
            "encrypt_volumes": enc_volumes,
            "saved_passwords": {},
        },
    }

    if container in config.snapshot_dir_overrides:
        minimal["snapshot_dir_overrides"] = {container: config.snapshot_dir_overrides[container]}
    if container in config.volume_backup:
        minimal["volume_backup"] = {container: _portablize_volume_backup(
            {container: config.volume_backup[container]})[container]}
    if container in config.max_snapshots_overrides:
        minimal["max_snapshots_overrides"] = {container: config.max_snapshots_overrides[container]}
    if container in config.snapshot_permission_overrides:
        minimal["snapshot_permission_overrides"] = {
            container: config.snapshot_permission_overrides[container]}
    if container in config.auto_rollback_disabled:
        minimal["auto_rollback_disabled"] = [container]
    if container in config.image_export_disabled:
        minimal["image_export_disabled"] = [container]
    if container in config.pause_for_backup_disabled:
        minimal["pause_for_backup_disabled"] = [container]
    if container in config.env_backup_disabled:
        minimal["env_backup_disabled"] = [container]
    if container in config.registry_alternatives:
        minimal["registry_alternatives"] = {container: config.registry_alternatives[container]}
    if container in config.pinned_tags:
        minimal["pinned_tags"] = {container: config.pinned_tags[container]}
    if config.snapshot_dir_mode != 0o700:
        minimal["snapshot_dir_mode"] = config.snapshot_dir_mode
    if config.snapshot_file_mode != 0o600:
        minimal["snapshot_file_mode"] = config.snapshot_file_mode

    cfg_path = job_dir / "config.json"
    cfg_path.write_bytes((json.dumps(minimal, indent=2) + "\n").encode())
    cfg_path.chmod(0o600)
    os.chown(cfg_path, _INVOKING_UID, _INVOKING_GID)

    saved_pws: dict = {}
    if password:
        saved_pws[container] = password
    for key, pw in config.encryption.get("saved_passwords", {}).items():
        if key.startswith(f"{container}::"):
            saved_pws[key] = pw

    cred_path = job_dir / "credentials.json"
    cred_path.write_bytes((json.dumps({"saved_passwords": saved_pws}, indent=2) + "\n").encode())
    cred_path.chmod(0o600)
    os.chown(cred_path, _INVOKING_UID, _INVOKING_GID)

    return job_dir


def _interactive_cron_add(config: Config, container: str) -> bool:
    """Prompt the user to pick a recipe and schedule, add to config, and apply.
    Returns True if a job was added."""
    existing_jobs = config.cron_jobs.get(container, [])
    existing_non_mount = {j.get("recipe") for j in existing_jobs
                          if not _CRON_RECIPES.get(j.get("recipe", ""), {}).get("requires_mount")}
    available = [(name, rec) for name, rec in _CRON_RECIPES.items()
                 if name not in existing_non_mount or rec.get("requires_mount")]
    if not available:
        print("All available recipes are already configured for this container.")
        return False

    print(f"\n─── Add scheduled job: {container} {'─' * max(1, 38 - len(container))}")
    print()
    for i, (rname, rec) in enumerate(available, 1):
        print(f"  {i}  {rname:<20}  {rec['description']}")
        print(f"       Default schedule: {rec['default_schedule']}")
    print()
    try:
        raw = input(f"[1-{len(available)}] or 0 to cancel: ").strip()
    except (EOFError, KeyboardInterrupt):
        print()
        return False
    if raw == "0":
        return False
    if not raw.isdigit() or not (1 <= int(raw) <= len(available)):
        print("Invalid choice.")
        return False

    recipe_name, rec = available[int(raw) - 1]

    chosen_mount = ""
    if rec.get("requires_mount"):
        try:
            inspect_data = DockerClient().inspect(container)
        except DockerError as e:
            print(f"Could not inspect {container}: {e}")
            return False
        binds = inspect_data.get("HostConfig", {}).get("Binds") or []
        named_vols = _get_named_volumes(inspect_data)
        mount_paths = [b.split(":")[1] for b in binds
                       if len(b.split(":")) >= 2 and b.split(":")[0].startswith("/")]
        mount_paths += [v["Destination"] for v in named_vols]
        if not mount_paths:
            print(f"No bind mounts or named volumes found on {container}.")
            return False
        existing_mounts = {j.get("mount", "") for j in existing_jobs
                           if j.get("recipe") == recipe_name}
        print()
        print("  Select mount to back up:")
        for i, mp in enumerate(mount_paths, 1):
            note = "  (already scheduled)" if mp in existing_mounts else ""
            print(f"  {i}  {mp}{note}")
        print()
        try:
            mraw = input(f"[1-{len(mount_paths)}] or 0 to cancel: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return False
        if mraw == "0":
            return False
        if not mraw.isdigit() or not (1 <= int(mraw) <= len(mount_paths)):
            print("Invalid choice.")
            return False
        chosen_mount = mount_paths[int(mraw) - 1]
        if any(j.get("recipe") == recipe_name and j.get("mount") == chosen_mount
               for j in existing_jobs):
            print(f"A job for {recipe_name} --mount {chosen_mount} already exists.")
            return False

    default_sched = rec["default_schedule"]
    try:
        sched_raw = input(f"Schedule [{default_sched}] (Enter for default): ").strip()
    except (EOFError, KeyboardInterrupt):
        print()
        return False
    schedule = sched_raw if sched_raw else default_sched
    if sched_raw and not _cron_validate_schedule(sched_raw):
        print("Invalid schedule. Must be 5 space-separated fields (e.g. '0 3 * * *').")
        return False

    entry: dict = {"recipe": recipe_name, "schedule": schedule, "enabled": True}
    if chosen_mount:
        entry["mount"] = chosen_mount

    if config.is_encryption_enabled(container):
        print(f"\n  {container} has snapshot encryption — a cron config will be generated.")
        import getpass
        pw = config.get_saved_password(container)
        if pw is None:
            try:
                pw = getpass.getpass(f"  Container password for {container}: ")
            except (EOFError, KeyboardInterrupt):
                print()
                print("  Skipping cron config — job may fail if saved password is absent.")
                pw = None
        if pw:
            job_dir = _write_cron_config(config, container, recipe_name,
                                         chosen_mount or None, pw)
            entry["cron_config"] = _to_portable_path(job_dir)
            print(f"  Cron config: {job_dir}")

    jobs = list(existing_jobs)
    jobs.append(entry)
    config.cron_jobs[container] = jobs
    config.save()
    try:
        for line in _cron_apply(config, container):
            print(line)
    except RuntimeError as e:
        print(f"Saved to config but crontab apply failed: {e}")
    return True


def _interactive_cron_job_menu(config: Config, container: str, job_idx: int) -> None:
    while True:
        jobs = config.cron_jobs.get(container, [])
        if job_idx >= len(jobs):
            return
        job      = jobs[job_idx]
        recipe   = job.get("recipe", "")
        schedule = job.get("schedule", "")
        enabled  = job.get("enabled", False)
        rec      = _CRON_RECIPES.get(recipe)
        rec_label = rec["label"] if rec else f"{recipe} (unknown recipe)"

        toggle_label = "Disable" if enabled else "Enable"
        state = "enabled" if enabled else "disabled"
        print(f"\n─── {container}:{recipe} {'─' * max(1, 46 - len(container) - len(recipe))}")
        print(f"  Recipe   : {rec_label}")
        print(f"  Schedule : {schedule}")
        print(f"  Status   : {state}")
        print()
        print(f"  1  {toggle_label}")
        print("  2  Change schedule")
        print("  3  Delete this job")
        print("  0  Back")
        print()
        try:
            raw = input("[1-3], 0 to go back: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return
        if raw == "0":
            return
        if raw in ("q", "quit"):
            print("\nGoodbye.")
            sys.exit(0)

        if raw == "1":
            jobs = list(config.cron_jobs.get(container, []))
            jobs[job_idx]["enabled"] = not enabled
            config.cron_jobs[container] = jobs
            config.save()
            try:
                for line in _cron_apply(config, container):
                    print(line)
            except RuntimeError as e:
                print(f"Saved to config but crontab apply failed: {e}")

        elif raw == "2":
            try:
                new_sched = input(f"New schedule [{schedule}] (Enter to cancel): ").strip()
            except (EOFError, KeyboardInterrupt):
                print()
                continue
            if not new_sched:
                continue
            if not _cron_validate_schedule(new_sched):
                print("Invalid schedule. Must be 5 space-separated fields (e.g. '0 3 * * *').")
                continue
            jobs = list(config.cron_jobs.get(container, []))
            jobs[job_idx]["schedule"] = new_sched
            config.cron_jobs[container] = jobs
            config.save()
            try:
                for line in _cron_apply(config, container):
                    print(line)
            except RuntimeError as e:
                print(f"Saved to config but crontab apply failed: {e}")

        elif raw == "3":
            try:
                yn = input(f"Delete job '{recipe}' for {container}? [y/N]: ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                print()
                continue
            if yn != "y":
                continue
            try:
                content = _crontab_read()
                _crontab_write(_crontab_remove(content, container, recipe))
            except RuntimeError as e:
                print(f"Warning: crontab update failed: {e}")
            new_jobs = [j for j in config.cron_jobs.get(container, [])
                        if j.get("recipe") != recipe]
            if new_jobs:
                config.cron_jobs[container] = new_jobs
            else:
                config.cron_jobs.pop(container, None)
            config.save()
            print(f"  removed  {container}:{recipe}")
            return
        else:
            print("Invalid choice.")


def _interactive_cron_menu(config: Config, container: str) -> None:
    while True:
        try:
            content = _crontab_read()
        except RuntimeError:
            content = ""
        jobs = config.cron_jobs.get(container, [])

        print(f"\n─── {container} — Scheduled jobs {'─' * max(1, 30 - len(container))}")
        print()
        if jobs:
            rows = []
            for job in jobs:
                recipe   = job.get("recipe", "")
                schedule = job.get("schedule", "")
                enabled  = job.get("enabled", False)
                applied  = _crontab_is_applied(content, container, recipe)
                if enabled and not applied:
                    status = "enabled (drift!)"
                elif enabled:
                    status = "enabled"
                else:
                    status = "disabled"
                rows.append((recipe, schedule, status))
            _print_table(["RECIPE", "SCHEDULE", "STATUS"], rows)
        else:
            print("  (no jobs configured)")
        print()
        print("  a  Add a job")
        print("  0  Back")
        print("  q  Quit")
        print()
        n = len(jobs)
        prompt = (f"[1-{n}/a], 0 to go back, q to quit: " if n
                  else "[a], 0 to go back, q to quit: ")
        try:
            raw = input(prompt).strip().lower()
        except (EOFError, KeyboardInterrupt):
            print()
            return
        if raw == "0":
            return
        if raw in ("q", "quit"):
            print("\nGoodbye.")
            sys.exit(0)
        elif raw == "a":
            _interactive_cron_add(config, container)
        elif raw.isdigit() and 1 <= int(raw) <= n:
            _interactive_cron_job_menu(config, container, int(raw) - 1)
        else:
            print("Invalid choice.")


def _interactive_cron_overview(config: Config) -> None:
    while True:
        rows = _cron_status(config)
        drift = any(r["enabled"] and not r["applied"] for r in rows)

        print(f"\n─── Scheduled jobs — all containers ────────────────")
        print()
        if not rows:
            print("  (no jobs configured)")
            print("  Open a container → 'c' Config → 'j' Scheduled jobs to add one.")
        else:
            table_rows = []
            for r in rows:
                enabled_s = "yes" if r["enabled"] else "no"
                if r["enabled"] and not r["applied"]:
                    applied_s = "NO (drift)"
                elif r["applied"]:
                    applied_s = "yes"
                else:
                    applied_s = "no"
                table_rows.append((r["container"], r["recipe"], r["schedule"],
                                   enabled_s, applied_s))
            _print_table(
                ["CONTAINER", "RECIPE", "SCHEDULE", "ENABLED", "APPLIED"],
                table_rows,
            )
            if drift:
                print("\n  ! Drift detected.")
        print()
        print("  a  Apply all  (sync config → crontab)")
        print("  0  Back")
        print()
        try:
            raw = input("[a], 0 to go back: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print()
            return
        if raw == "0":
            return
        elif raw == "a":
            try:
                changes = _cron_apply(config)
            except RuntimeError as e:
                print(f"Error: {e}")
                continue
            if not changes:
                print("Nothing to apply.")
            else:
                for line in changes:
                    print(line)
        else:
            print("Invalid choice.")


def _interactive_container_chmod(config: Config, container: str) -> None:
    """Bulk-apply a permission profile to all snapshot/archive files for a container."""
    snap_dirs = _collect_container_snapshot_dirs(config, container)
    if not snap_dirs:
        print(f"  No snapshot directories found for {container}.")
        return

    has_override = container in config.snapshot_permission_overrides
    cur_dm = config.snapshot_dir_mode_for(container)
    cur_fm = config.snapshot_file_mode_for(container)
    cur_label = _permission_profile_label(cur_dm, cur_fm)
    cur_source = "container override" if has_override else "global default"

    print(f"\n─── {container} — Snapshot Permissions {'─' * max(1, 30 - len(container))}")
    print()
    print(f"  Current: {cur_label}  (dirs {cur_dm:04o}, files {cur_fm:04o})  [{cur_source}]")
    print()
    print("  Snapshot directories:")
    for d in snap_dirs:
        try:
            fcount = sum(1 for e in d.iterdir() if e.is_file())
        except OSError:
            fcount = "?"
        print(f"    {d}  ({fcount} files)")
    print()
    for i, (label, dm, fm, note) in enumerate(_PERMISSION_PROFILES, 1):
        print(f"  {i}  {label:<8}  dirs {dm:04o}, files {fm:04o}  ({note})")
    print("  4  Custom    enter separately")
    if has_override:
        print(f"  5  Clear override  (revert to global default)")
    print()

    dir_mode = file_mode = None
    profile_label = ""
    while True:
        prompt = "[1-4/5] or 0 to cancel: " if has_override else "[1-4] or 0 to cancel: "
        try:
            raw = input(prompt).strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return
        if raw == "0":
            return
        if raw in ("1", "2", "3"):
            label, dir_mode, file_mode, _ = _PERMISSION_PROFILES[int(raw) - 1]
            profile_label = f"{label}  (dirs {dir_mode:04o}, files {file_mode:04o})"
            break
        if raw == "4":
            try:
                d_str = input("  Dir octal (e.g. 700 or 0750): ").strip()
            except (EOFError, KeyboardInterrupt):
                print()
                continue
            if not re.fullmatch(r"[0-7]{3,4}", d_str):
                print("  Invalid: enter 3 or 4 octal digits.")
                continue
            try:
                f_str = input("  File octal (e.g. 600 or 0640): ").strip()
            except (EOFError, KeyboardInterrupt):
                print()
                continue
            if not re.fullmatch(r"[0-7]{3,4}", f_str):
                print("  Invalid: enter 3 or 4 octal digits.")
                continue
            dir_mode = int(d_str, 8)
            file_mode = int(f_str, 8)
            profile_label = f"Custom  (dirs {dir_mode:04o}, files {file_mode:04o})"
            break
        if raw == "5" and has_override:
            config.snapshot_permission_overrides.pop(container)
            config.save()
            print(f"  Override cleared — {container} will use the global default.")
            return
        print("Invalid choice.")

    print(f"\n  Profile: {profile_label}")
    print("  Will apply to:")
    for d in snap_dirs:
        print(f"    {d}")
    print()
    try:
        yn = input("Proceed? [y/N]: ").strip().lower()
    except (EOFError, KeyboardInterrupt):
        print()
        return
    if yn != "y":
        return

    total_dirs = total_files = 0
    for d in snap_dirs:
        d_changed, f_changed = _bulk_chmod_tree(d, dir_mode, file_mode)
        total_dirs += d_changed
        total_files += f_changed
        log(f"[container_chmod] {container}: {d} → dirs {dir_mode:04o} files {file_mode:04o} "
            f"({d_changed} dirs, {f_changed} files)")

    config.snapshot_permission_overrides[container] = {
        "dir_mode": dir_mode,
        "file_mode": file_mode,
    }
    config.save()

    print(f"  Done: {total_dirs} director{'ies' if total_dirs != 1 else 'y'}, "
          f"{total_files} file{'s' if total_files != 1 else ''} updated.")


def _container_config_menu(config: Config, docker: DockerClient,
                            sm: SnapshotManager, registry: RegistryClient,
                            name: str,
                            enc: "EncryptionManager | None") -> tuple:
    """Per-container configuration screen. Returns (config, enc)."""
    while True:
        container_ar_off = name in config.auto_rollback_disabled
        enc_on = config.is_encryption_enabled(name)
        pinned = config.pinned_tags.get(name)

        print(f"\n─── {name} — Configure {'─' * max(1, 40 - len(name))}")
        print()
        enc_state = "ON" if enc_on else "OFF"
        print(f"  e  Encryption: {enc_state}")
        if enc_on:
            _pw_st_label = _enc_pw_status(config, name)
            print(f"  k  Password...  ({_pw_st_label})")
        print("  g  Registry sources")
        pin_label = (f"Version pin: {pinned}  (change or clear)"
                     if pinned else "Version pin: none  (set)")
        print(f"  p  {pin_label}")
        print("  b  Backup toggles")
        ar_label = "Enable auto-rollback" if container_ar_off else "Disable auto-rollback"
        print(f"  a  {ar_label}")
        n_cron = len(config.cron_jobs.get(name, []))
        cron_label = f"{n_cron} job{'s' if n_cron != 1 else ''} configured"
        print(f"  j  Scheduled jobs  ({cron_label})")
        excluded = name in config.exclude
        excl_label = ("Re-attach to update_zen  (currently detached)"
                      if excluded else "Detach from update_zen")
        print(f"  d  {excl_label}")
        print()

        opts = "e/k/g/p/b/a/j/d" if enc_on else "e/g/p/b/a/j/d"
        try:
            raw = input(f"[{opts}], 0 to go back, q to quit: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print()
            return config, enc
        if raw == "0":
            return config, enc
        if raw in ("q", "quit"):
            print("\nGoodbye.")
            sys.exit(0)

        if raw == "e":
            enc_containers = list(config.encryption.get("encrypt_containers", []))
            if name in enc_containers:
                enc_containers.remove(name)
                config.encryption["encrypt_containers"] = enc_containers
                config.save()
                print(f"Encryption disabled for {name}.")
            else:
                enc_containers.append(name)
                config.encryption["encrypt_containers"] = enc_containers
                config.save()
                print(f"Encryption enabled for {name}.")
                print("  Password will be prompted on next update/rollback.")
                print("  Press 'k' to save a password now.")
        elif raw == "k" and enc_on:
            _interactive_password_menu(config, name)
        elif raw == "g":
            _interactive_registries_menu(config, docker, name)
        elif raw == "p":
            if pinned:
                print(f"\n  Current pin: {pinned}")
                print("  1  Change pin")
                print("  2  Clear pin")
                print("  0  Cancel")
                try:
                    sub = input("[1/2/0]: ").strip()
                except (EOFError, KeyboardInterrupt):
                    print()
                    continue
                if sub == "1":
                    tag = _pick_version_tag(config, docker, registry, name)
                    if tag:
                        config.pinned_tags[name] = tag
                        config.save()
                        print(f"Version pin set to {tag}.")
                elif sub == "2":
                    config.pinned_tags.pop(name)
                    config.save()
                    print(f"Version pin cleared for {name}.")
            else:
                tag = _pick_version_tag(config, docker, registry, name)
                if tag:
                    config.pinned_tags[name] = tag
                    config.save()
                    print(f"Version pin set to {tag}.")
        elif raw == "b":
            _backup_toggles_menu(config, name)
        elif raw == "a":
            if container_ar_off:
                config.auto_rollback_disabled.remove(name)
                print(f"Auto-rollback enabled for {name}.")
            else:
                config.auto_rollback_disabled.append(name)
                print(f"Auto-rollback disabled for {name}.")
            config.save()
        elif raw == "j":
            _interactive_cron_menu(config, name)
        elif raw == "d":
            if name in config.exclude:
                config.exclude.remove(name)
                config.save()
                print(f"{name} re-attached to update_zen.")
            else:
                config.exclude.append(name)
                config.save()
                print(f"{name} detached from update_zen.")
                return config, enc
        else:
            print("Invalid choice.")

    return config, enc


def _updates_menu(config: Config, docker: DockerClient,
                  registry: RegistryClient, sm: SnapshotManager,
                  name: str, enc: "EncryptionManager | None") -> bool:
    _state_changed = False
    while True:
        effective_ar = config.auto_rollback and name not in config.auto_rollback_disabled
        print(f"\n─── {name} — Updates & Rollback {'─' * max(1, 30 - len(name))}")
        print()
        print("  1  Update now")
        print("  2  Rollback")
        print("  3  Compose update")
        print("  4  Select version...")
        print("  5  Check for updates")
        print()
        try:
            raw = input("[1-5], 0 to go back, q to quit: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print()
            return _state_changed
        if raw == "0":
            return _state_changed
        if raw in ("q", "quit"):
            print("\nGoodbye.")
            sys.exit(0)
        if not raw.isdigit() or not (1 <= int(raw) <= 5):
            print("Invalid choice.")
            continue
        choice = int(raw)
        print()
        if choice == 1:
            Engine(config).update(name, auto_rollback=effective_ar)
            _state_changed = True
        elif choice == 2:
            _interactive_snapshot_list(config, sm, name, enc, rollback_mode=True)
            _state_changed = True
        elif choice == 3:
            Engine(config).compose_update(name, auto_rollback=effective_ar)
            _state_changed = True
        elif choice == 4:
            _interactive_version_select(config, docker, registry, name, effective_ar, enc)
            _state_changed = True
        elif choice == 5:
            try:
                data = docker.inspect(name)
                pinned_tag = config.pinned_tags.get(name, "")
                active_ref = _get_active_image_ref(config, name, data)
                has = registry.has_update(data, pinned_tag=pinned_tag,
                                          image_ref_override=active_ref)
                print(f"Update available: {'yes' if has else 'no'}")
            except (DockerError, RegistryError) as e:
                print(f"Check failed: {e}")
    return _state_changed


def _snapshots_menu(config: Config, sm: SnapshotManager,
                    name: str, enc: "EncryptionManager | None") -> None:
    while True:
        snap_override = config.snapshot_dir_overrides.get(name, "")
        snap_limit_override = config.max_snapshots_overrides.get(name)
        snap_limit = config.max_snapshots_for(name)
        snap_count = len(sm.list(name))
        excess = max(0, snap_count - snap_limit)

        print(f"\n─── {name} — Snapshots {'─' * max(1, 40 - len(name))}")
        print()
        print(f"  l  List / browse  ({snap_count} snapshot{'s' if snap_count != 1 else ''})")
        print("  n  New snapshot now")
        print(f"  p  Prune old  ({snap_limit} kept, {excess} excess)")
        snap_dir_label = (f"Directory: {snap_override}  (change or clear)"
                          if snap_override
                          else f"Directory: global default  ({config.snapshot_dir_for(name)})")
        print(f"  d  {snap_dir_label}")
        snap_limit_label = (f"Keep limit: {snap_limit_override}  (change or clear)"
                            if snap_limit_override is not None
                            else f"Keep limit: global default  ({config.max_snapshots})")
        print(f"  k  {snap_limit_label}")
        print("  m  File permissions")
        print("  f  Browse snapshot folder")
        print()
        try:
            raw = input("[l/n/p/d/k/m/f], 0 to go back, q to quit: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print()
            return
        if raw == "0":
            return
        if raw in ("q", "quit"):
            print("\nGoodbye.")
            sys.exit(0)

        if raw == "l":
            _interactive_snapshot_list(config, sm, name, enc, rollback_mode=False)
        elif raw == "n":
            Engine(config).snapshot(name)
        elif raw == "p":
            if excess <= 0:
                print("No excess snapshots to prune.")
                continue
            try:
                yn = input(
                    f"  {snap_count} snapshots, limit {snap_limit} — "
                    f"will delete {excess} oldest. Continue? [y/N]: "
                ).strip().lower()
            except (EOFError, KeyboardInterrupt):
                print()
                continue
            if yn != "y":
                continue
            sm._rotate(name)
            remaining = len(sm.list(name))
            print(f"Pruned. {remaining} snapshot{'s' if remaining != 1 else ''} remaining.")
        elif raw == "d":
            if snap_override:
                print(f"\n  Current override: {snap_override}")
                print("  1  Change directory")
                print("  2  Clear override  (revert to global)")
                print("  0  Cancel")
                try:
                    sub = input("[1/2/0]: ").strip()
                except (EOFError, KeyboardInterrupt):
                    print()
                    continue
                if sub == "1":
                    chosen = _browse_path(Path("/"), mode="dir")
                    if chosen:
                        config.snapshot_dir_overrides[name] = str(chosen)
                        config.save()
                        print(f"Snapshot dir set to {chosen}.")
                elif sub == "2":
                    config.snapshot_dir_overrides.pop(name)
                    config.save()
                    print("Snapshot dir override cleared.")
            else:
                chosen = _browse_path(Path("/"), mode="dir")
                if chosen:
                    config.snapshot_dir_overrides[name] = str(chosen)
                    config.save()
                    print(f"Snapshot dir set to {chosen}.")
        elif raw == "k":
            if snap_limit_override is not None:
                print(f"\n  Current override: {snap_limit_override}")
                print("  1  Change limit")
                print("  2  Clear override  (revert to global)")
                print("  0  Cancel")
                try:
                    sub = input("[1/2/0]: ").strip()
                except (EOFError, KeyboardInterrupt):
                    print()
                    continue
                if sub == "1":
                    try:
                        val = input(f"Snapshot limit for {name} (min 1): ").strip()
                    except (EOFError, KeyboardInterrupt):
                        print()
                        continue
                    if val.isdigit() and int(val) >= 1:
                        config.max_snapshots_overrides[name] = int(val)
                        config.save()
                        print(f"Snapshot limit set to {int(val)}.")
                    else:
                        print("Invalid value — must be a whole number >= 1.")
                elif sub == "2":
                    config.max_snapshots_overrides.pop(name)
                    config.save()
                    print(f"Snapshot limit cleared — reverts to global ({config.max_snapshots}).")
            else:
                try:
                    val = input(f"Snapshot limit for {name} (min 1, Enter to cancel): ").strip()
                except (EOFError, KeyboardInterrupt):
                    print()
                    continue
                if not val:
                    continue
                if val.isdigit() and int(val) >= 1:
                    config.max_snapshots_overrides[name] = int(val)
                    config.save()
                    print(f"Snapshot limit for {name} set to {int(val)}.")
                else:
                    print("Invalid value — must be a whole number >= 1.")
        elif raw == "m":
            _interactive_container_chmod(config, name)
        elif raw == "f":
            snap_dir = config.snapshot_dir_for(name) / name
            if not snap_dir.exists():
                print(f"  Snapshot directory does not exist: {snap_dir}")
            else:
                browse_start = snap_dir
                while True:
                    selected = _browse_path(browse_start, mode="file")
                    if selected is None:
                        break
                    browse_start = selected.parent
                    _file_action_menu(selected)
        else:
            print("Invalid choice.")


def _container_control_menu(config: Config, docker: DockerClient,
                             sm: SnapshotManager, name: str) -> bool:
    _state_changed = False
    while True:
        try:
            _data = docker.inspect(name)
            _state = _data.get("State", {})
            _hobj = _state.get("Health")
            health = _hobj.get("Status", _state.get("Status", "unknown")) if _hobj else _state.get("Status", "unknown")
        except DockerError:
            health = "unknown"

        pause_label = "Unpause" if health == "paused" else "Pause"
        print(f"\n─── {name} — Container Control {'─' * max(1, 31 - len(name))}")
        print(f"  ({health})")
        print()
        print("  r  Restart")
        print(f"  p  {pause_label}")
        print("  s  Stop")
        print("  a  Start")
        print("  f  Force recreate")
        print("  k  Kill")
        print()
        try:
            raw = input("[r/p/s/a/f/k], 0 to go back, q to quit: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print()
            return _state_changed
        if raw == "0":
            return _state_changed
        if raw in ("q", "quit"):
            print("\nGoodbye.")
            sys.exit(0)

        if raw == "r":
            try:
                docker.stop(name)
                docker.start(name)
                print(f"Restarted {name}.")
            except DockerError as e:
                print(f"Restart failed: {e}")
            _state_changed = True
        elif raw == "p":
            if health == "paused":
                try:
                    docker.unpause(name)
                    print(f"Unpaused {name}.")
                except DockerError as e:
                    print(f"Unpause failed: {e}")
            else:
                try:
                    docker.pause(name)
                    print(f"Paused {name}.")
                except DockerError as e:
                    print(f"Pause failed: {e}")
            _state_changed = True
        elif raw == "s":
            try:
                docker.stop(name)
                print(f"Stopped {name}.")
            except DockerError as e:
                print(f"Stop failed: {e}")
            _state_changed = True
        elif raw == "a":
            try:
                docker.start(name)
                print(f"Started {name}.")
            except DockerError as e:
                print(f"Start failed: {e}")
            _state_changed = True
        elif raw == "f":
            try:
                confirm = input(
                    f"  Force recreate {name}? Container will be stopped, removed,\n"
                    f"  and restarted from its current config (no image pull). [y/N]: "
                ).strip().lower()
            except (EOFError, KeyboardInterrupt):
                print()
                continue
            if confirm == "y":
                try:
                    data = docker.inspect(name)
                    spec = sm.to_spec(data, pin_digest=False)
                    docker.stop(name)
                    docker.remove(name)
                    docker.run(spec)
                    print(f"Recreated {name}.")
                except DockerError as e:
                    print(f"Force recreate failed: {e}")
                _state_changed = True
        elif raw == "k":
            try:
                confirm = input(f"  Kill {name}? Sends SIGKILL immediately. [y/N]: ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                print()
                continue
            if confirm == "y":
                try:
                    docker.kill(name)
                    print(f"Killed {name}.")
                except DockerError as e:
                    print(f"Kill failed: {e}")
                _state_changed = True
        else:
            print("Invalid choice.")
    return _state_changed


def _info_menu(config: Config, docker: DockerClient, name: str) -> None:
    while True:
        print(f"\n─── {name} — Info {'─' * max(1, 44 - len(name))}")
        print()
        print("  d  Details")
        print("  l  Logs")
        print("  t  Stats")
        print()
        try:
            raw = input("[d/l/t], 0 to go back, q to quit: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print()
            return
        if raw == "0":
            return
        if raw in ("q", "quit"):
            print("\nGoodbye.")
            sys.exit(0)

        if raw == "d":
            try:
                data = docker.inspect(name)
                cfg = data.get("Config", {})
                hcfg = data.get("HostConfig", {})
                state = data.get("State", {})
                cid = data.get("Id", "")[:12]
                created = (data.get("Created") or "")[:10]
                status = state.get("Status", "?")
                started = _fmt_uptime(state.get("StartedAt", ""))
                img = cfg.get("Image", "")
                digests = data.get("RepoDigests") or []
                digest_short = (digests[0].split("@sha256:")[-1][:12]
                                if digests and "@sha256:" in digests[0] else "")
                restart_pol = hcfg.get("RestartPolicy") or {}
                restart_name = restart_pol.get("Name") or "no"
                max_retry = restart_pol.get("MaximumRetryCount", 0)
                restart = (f"{restart_name}:{max_retry}"
                           if restart_name == "on-failure" and max_retry
                           else restart_name)
                mem_limit = int(hcfg.get("Memory") or 0)
                mem_str = (f"{mem_limit // (1024*1024)}MiB"
                           if mem_limit else "unlimited")
                cpu_shares = int(hcfg.get("CpuShares") or 0)
                cpu_str = f"{cpu_shares} shares" if cpu_shares else "unlimited"
                print(f"\n─── {name} — details {'─' * max(1, 40 - len(name))}")
                print(f"  ID       :  {cid}")
                print(f"  Created  :  {created}")
                print(f"  Status   :  {status}  (up {started})")
                print(f"  Image    :  {img}")
                if digest_short:
                    print(f"  Digest   :  sha256:{digest_short}...")
                print(f"  Restart  :  {restart}")
                print(f"  Memory   :  {mem_str}")
                print(f"  CPU      :  {cpu_str}")
                nets = (data.get("NetworkSettings") or {}).get("Networks") or {}
                if nets:
                    print("\n  Networks")
                    for net_name, net_info in nets.items():
                        ip = (net_info or {}).get("IPAddress", "")
                        print(f"    {net_name:<20}  {ip}")
                raw_ports = hcfg.get("PortBindings") or {}
                if raw_ports:
                    print("\n  Ports")
                    for cport, bindings in sorted(raw_ports.items()):
                        for b in (bindings or []):
                            hip = b.get("HostIp", "0.0.0.0") or "0.0.0.0"
                            hport = b.get("HostPort", "")
                            print(f"    {hip}:{hport} → {cport}")
                binds = hcfg.get("Binds") or []
                named_vols = _get_named_volumes(data)
                if binds or named_vols:
                    print("\n  Mounts")
                    for b in binds:
                        parts = b.split(":")
                        hpath = parts[0]
                        cpath = parts[1] if len(parts) > 1 else ""
                        print(f"    {hpath} → {cpath}  (bind)")
                    for v in named_vols:
                        print(f"    {v['Name']} → {v['Destination']}  (volume)")
                print()
            except DockerError as e:
                print(f"Details failed: {e}")
            try:
                input("  Press Enter to continue.")
            except (EOFError, KeyboardInterrupt):
                print()
        elif raw == "l":
            try:
                output = docker.logs(name)
                lines = output.splitlines()
                print(f"\n─── {name} — docker logs (last {len(lines)}) {'─' * max(1, 34 - len(name))}")
                print(output.rstrip())
                print()
            except DockerError as e:
                print(f"Could not fetch logs: {e}")
            try:
                input("  Press Enter to continue.")
            except (EOFError, KeyboardInterrupt):
                print()
        elif raw == "t":
            try:
                s = docker.stats(name)
                print(f"\n─── {name} — stats {'─' * max(1, 41 - len(name))}")
                print(f"  CPU     :  {s.get('CPUPerc', '?')}")
                print(f"  Memory  :  {s.get('MemUsage', '?')}  ({s.get('MemPerc', '?')})")
                print(f"  Net I/O :  {s.get('NetIO', '?')}")
                print(f"  Block   :  {s.get('BlockIO', '?')}")
                print(f"  PIDs    :  {s.get('PIDs', '?')}")
                print()
            except DockerError as e:
                print(f"Stats failed: {e}")
            try:
                input("  Press Enter to continue.")
            except (EOFError, KeyboardInterrupt):
                print()
        else:
            print("Invalid choice.")


def _backup_toggles_menu(config: Config, name: str) -> None:
    while True:
        container_pfb_off = name in config.pause_for_backup_disabled
        container_env_off = name in config.env_backup_disabled
        container_img_off = name in config.image_export_disabled

        pfb_state = "OFF" if container_pfb_off else "ON"
        env_state = "OFF" if container_env_off else "ON"
        if not config.image_export_enabled:
            img_state = "OFF  (globally off)"
        else:
            img_state = "OFF" if container_img_off else "ON"

        print(f"\n─── {name} — Backup Toggles {'─' * max(1, 34 - len(name))}")
        print()
        print(f"  1  Pause for backup: {pfb_state}")
        print(f"  2  Env vars backup: {env_state}")
        print(f"  3  Image export: {img_state}")
        print()
        try:
            raw = input("[1-3], 0 to go back, q to quit: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print()
            return
        if raw == "0":
            return
        if raw in ("q", "quit"):
            print("\nGoodbye.")
            sys.exit(0)

        if raw == "1":
            if container_pfb_off:
                config.pause_for_backup_disabled.remove(name)
                print(f"Pause for backup enabled for {name}.")
            else:
                config.pause_for_backup_disabled.append(name)
                print(f"Pause for backup disabled for {name}.")
            config.save()
        elif raw == "2":
            if container_env_off:
                config.env_backup_disabled.remove(name)
                config.save()
                print(f"Env backup enabled for {name}.")
            else:
                config.env_backup_disabled.append(name)
                config.save()
                print(f"Env backup disabled for {name}.")
        elif raw == "3":
            if container_img_off:
                config.image_export_disabled.remove(name)
                config.save()
                print(f"Image export enabled for {name}.")
            else:
                config.image_export_disabled.append(name)
                config.save()
                print(f"Image export disabled for {name}.")
            if not config.image_export_enabled:
                print("  (Note: image export is disabled globally — enable in settings)")
        else:
            print("Invalid choice.")


def _action_menu(config: Config, docker: DockerClient,
                 registry: RegistryClient, sm: SnapshotManager,
                 status: tuple, enc: "EncryptionManager | None" = None) -> bool:
    name, health, update, version, date, image, snaps, backup_col, mounts, *_ = status
    _state_changed = False
    while True:
        effective_ar = config.auto_rollback and name not in config.auto_rollback_disabled
        enc_on = config.is_encryption_enabled(name)
        container_env_off = name in config.env_backup_disabled
        container_img_off = (name in config.image_export_disabled
                             or not config.image_export_enabled)
        if snaps == "?":
            snaps = len(sm.list(name))
        print(f"\n{'─' * 3} {name} {'─' * max(1, 50 - len(name))}")
        update_label = {"yes": "update available", "no": "up to date"}.get(update, "update unknown")
        snap_label = f"{snaps} snapshot{'s' if snaps != 1 else ''}"
        ar_label = "" if effective_ar else " | auto-rollback OFF"
        pin_label = f" | pin: {config.pinned_tags[name]}" if name in config.pinned_tags else ""
        alts = config.registry_alternatives.get(name, {})
        active_ref = alts.get("active", "")
        reg_label = ""
        if active_ref and active_ref in alts.get("refs", []) and active_ref != image:
            reg_host = RegistryClient._parse_image_ref(active_ref)[0]
            reg_label = f" | registry: {reg_host}"
        if enc_on:
            _pw_st = _enc_pw_status(config, name)
            enc_badge = f" | [enc:{_pw_st}]"
        else:
            enc_badge = ""
        env_badge = " | [no-env]" if container_env_off else ""
        img_badge = " | [no-img]" if container_img_off else ""
        snap_limit_badge = (f" | [keep:{config.max_snapshots_overrides[name]}]"
                            if name in config.max_snapshots_overrides else "")
        print(f"    {image} | {health} | {update_label} | {snap_label}{ar_label}{pin_label}{reg_label}{enc_badge}{env_badge}{img_badge}{snap_limit_badge}\n")
        print("  u  Updates & Rollback")
        print("  s  Snapshots")
        print("  v  Volumes")
        print("  x  Container Control")
        print("  i  Info")
        print("  c  Configure")
        print()
        try:
            raw = input("[u/s/v/x/i/c], 0 to go back, q to quit: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print()
            return _state_changed
        if raw == "0":
            return _state_changed
        if raw in ("q", "quit"):
            print("\nGoodbye.")
            sys.exit(0)

        if raw == "u":
            if _updates_menu(config, docker, registry, sm, name, enc):
                name, health, update, version, date, image, snaps, backup_col, mounts, *_ = _fetch_one_status(
                    name, docker, registry, sm, config
                )
                _state_changed = True
        elif raw == "s":
            _snapshots_menu(config, sm, name, enc)
            snaps = len(sm.list(name))
        elif raw == "v":
            _interactive_volumes_menu(config, docker, name)
        elif raw == "x":
            if _container_control_menu(config, docker, sm, name):
                name, health, update, version, date, image, snaps, backup_col, mounts, *_ = _fetch_one_status(
                    name, docker, registry, sm, config
                )
                _state_changed = True
        elif raw == "i":
            _info_menu(config, docker, name)
        elif raw == "c":
            _exclude_before = list(config.exclude)
            config, enc = _container_config_menu(config, docker, sm, registry, name, enc)
            if config.exclude != _exclude_before:
                _state_changed = True
                if name in config.exclude:
                    return _state_changed
            name, health, update, version, date, image, snaps, backup_col, mounts, *_ = _fetch_one_status(
                name, docker, registry, sm, config
            )
        else:
            print("Invalid choice.")


def _interactive_password_menu(config: Config, container: str) -> None:
    """Per-container password sub-menu: set/delete saved password and change global mode."""
    import getpass
    _modes = ["session", "always", "saved"]
    _mode_labels = {
        "session": "once per session — cache in memory, prompt again next run",
        "always":  "always prompt — never cache, never save",
        "saved":   "save to config — use saved password, no prompt when set",
    }
    while True:
        mode = config.encryption.get("mode", "session")
        saved_pw = config.get_saved_password(container)
        if saved_pw is not None:
            status = "saved password set"
        elif container in _session_cache:
            status = "session-cached (will prompt next run)"
        else:
            status = "no password stored (will prompt on next operation)"

        print(f"\n─── {container} — password ─────────────────────────────")
        print(f"  Status : {status}")
        print(f"  Mode   : {mode} — {_mode_labels.get(mode, mode)}")
        print()
        print("  1  Set / change saved password")
        max_opt = 1
        if saved_pw is not None:
            print("  2  Delete saved password")
            max_opt = 2
        print(f"  3  Change password mode  (global, current: {mode})")
        print()
        try:
            raw = input(f"[1-{max_opt}/3], 0 to go back, q to quit: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return
        if raw == "0":
            return
        if raw in ("q", "quit"):
            print("\nGoodbye.")
            sys.exit(0)
        if raw == "1":
            try:
                pw1 = getpass.getpass(f"New password for {container}: ")
            except (EOFError, KeyboardInterrupt):
                print()
                continue
            if not pw1:
                print("Password cannot be empty.")
                continue
            try:
                pw2 = getpass.getpass("Confirm password: ")
            except (EOFError, KeyboardInterrupt):
                print()
                continue
            if pw1 != pw2:
                print("Passwords do not match.")
                continue
            config.set_saved_password(container, pw1)
            _session_cache[container] = pw1
            print(f"Password saved for {container}.")
        elif raw == "2" and saved_pw is not None:
            try:
                yn = input(f"Delete saved password for {container}? [y/N]: ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                print()
                continue
            if yn == "y":
                pw_map = dict(config.encryption.get("saved_passwords", {}))
                pw_map.pop(container, None)
                config.encryption["saved_passwords"] = pw_map
                config.save()
                print(f"Saved password deleted for {container}.")
        elif raw == "3":
            print(f"\n─── Password mode ─────────────────────────────────")
            print()
            for i, m in enumerate(_modes, 1):
                marker = "*" if m == mode else " "
                print(f"  [{marker}] {i}  {m:<10}  {_mode_labels[m]}")
            print()
            try:
                choice = input("[1-3] to select, 0 to cancel: ").strip()
            except (EOFError, KeyboardInterrupt):
                print()
                continue
            if choice in ("1", "2", "3"):
                new_mode = _modes[int(choice) - 1]
                config.encryption["mode"] = new_mode
                config.save()
                print(f"Mode set to: {new_mode}")
        else:
            print("Invalid choice.")


def _interactive_saved_passwords_menu(config: Config) -> None:
    import getpass
    while True:
        saved = config.encryption.get("saved_passwords", {})
        entries = sorted(saved.keys())
        print(f"\n─── Saved passwords ─────────────────────────────────")
        print()
        if not entries:
            print("  (no saved passwords)")
        else:
            for i, key in enumerate(entries, 1):
                kind = "volume mount" if "::" in key else "container snapshot"
                print(f"  [{i}]  {key:<34}  {kind}")
        print()
        print("   a  Add password")
        print("   p  Purge all")
        print("   0  Back")
        print("   q  Quit")
        print()
        n = len(entries)
        prompt = (f"[1-{n}] delete entry, [a/p], 0 to go back, q to quit: " if n
                  else "[a/p], 0 to go back, q to quit: ")
        try:
            raw = input(prompt).strip().lower()
        except (EOFError, KeyboardInterrupt):
            print()
            return
        if raw == "0":
            return
        if raw in ("q", "quit"):
            print("\nGoodbye.")
            sys.exit(0)
        elif raw == "a":
            try:
                container = input("Container name: ").strip()
            except (EOFError, KeyboardInterrupt):
                print()
                continue
            if not container:
                print("Container name cannot be empty.")
                continue
            try:
                mount_raw = input("Volume mount path (blank = container snapshot): ").strip()
            except (EOFError, KeyboardInterrupt):
                print()
                continue
            mount = mount_raw or None
            label = f"{container}::{mount}" if mount else container
            try:
                password = getpass.getpass(f"Password for {label}: ")
            except (EOFError, KeyboardInterrupt):
                print()
                continue
            if not password:
                print("Password cannot be empty.")
                continue
            config.set_saved_password(container, password, mount)
            print(f"Password saved for {label}.")
        elif raw == "p":
            if not entries:
                print("No saved passwords to purge.")
                continue
            try:
                yn = input(f"Purge all {len(entries)} saved password"
                           f"{'s' if len(entries) != 1 else ''}? [y/N]: ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                print()
                continue
            if yn == "y":
                removed = config.purge_saved_passwords()
                print(f"Purged {removed} saved password{'s' if removed != 1 else ''}.")
        elif raw.isdigit() and n and 1 <= int(raw) <= n:
            key = entries[int(raw) - 1]
            try:
                yn = input(f"Delete password for '{key}'? [y/N]: ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                print()
                continue
            if yn == "y":
                pw_map = dict(config.encryption.get("saved_passwords", {}))
                pw_map.pop(key, None)
                config.encryption["saved_passwords"] = pw_map
                config.save()
                print(f"Deleted password for '{key}'.")
        else:
            print("Invalid choice.")


def _interactive_encryption_menu(config: Config,
                                  enc: "EncryptionManager | None") -> tuple:
    import getpass
    _ts_re = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}-\d{2}-\d{2}$")
    _modes = ["session", "always", "saved"]
    _mode_desc = {
        "session": "once per session — cache in memory, prompt again next run",
        "always":  "always prompt — never cache, never save",
        "saved":   "save to config — use saved password, no prompt when set",
    }
    while True:
        saved_count = len(config.encryption.get("saved_passwords", {}))
        mode = config.encryption.get("mode", "session")
        enc_containers = config.encryption.get("encrypt_containers", [])

        print(f"\n─── Encryption ─────────────────────────────────────")
        print(f"  Saved passwords : {saved_count}")
        print(f"  Mode            : {mode} — {_mode_desc.get(mode, mode)}")
        c_count = len(enc_containers)
        if c_count:
            print(f"  Containers      : {c_count} encrypted")
        if not enc_containers:
            print("  (no containers encrypted — use the action menu key 'e' to enable per container)")
        print()
        cfg_enc_status = "enabled" if EncryptionManager(None).is_encrypted(
            config._path.read_bytes()) else "disabled"
        print("  1  Saved passwords")
        print(f"  2  Password mode         (current: {mode})")
        print("  3  Per-container status")
        print(f"  4  Config file encryption (currently: {cfg_enc_status})")
        print()
        try:
            raw = input("[1-4], 0 to go back, q to quit: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return config, enc
        if raw == "0":
            return config, enc
        if raw in ("q", "quit"):
            print("\nGoodbye.")
            sys.exit(0)

        if raw == "1":
            _interactive_saved_passwords_menu(config)

        elif raw == "4":
            _interactive_config_encryption_menu(config)

        elif raw == "2":
            # Mode selector
            print(f"\n─── Password mode ───────────────────────────────────")
            print()
            for i, m in enumerate(_modes, 1):
                marker = "*" if m == mode else " "
                print(f"  [{marker}] {i}  {m:<10}  {_mode_desc[m]}")
            print()
            try:
                choice = input("[1-3] to select, 0 to cancel: ").strip()
            except (EOFError, KeyboardInterrupt):
                print()
                continue
            if choice in ("1", "2", "3"):
                new_mode = _modes[int(choice) - 1]
                config.encryption["mode"] = new_mode
                config.save()
                print(f"Mode set to: {new_mode}")

        elif raw == "3":
            # Per-container status — interactive: select a container to purge its passwords
            while True:
                enc_vols = config.encryption.get("encrypt_volumes", {})
                saved_pw = config.encryption.get("saved_passwords", {})
                sorted_containers = sorted(enc_containers)
                print(f"\n─── Per-container encryption status ────────────────")
                print()
                if not sorted_containers:
                    print("  No containers have encryption enabled.")
                    print("  Open a container's action menu and press 'e' to enable.")
                    print()
                    try:
                        input("Press Enter to continue...")
                    except (EOFError, KeyboardInterrupt):
                        print()
                    break
                for i, c in enumerate(sorted_containers, 1):
                    vols = enc_vols.get(c, [])
                    v_label = ("all mounts" if "all" in vols
                               else f"{len(vols)} mount(s)" if vols
                               else "snapshot only")
                    pw_count = sum(1 for k in saved_pw
                                   if k == c or k.startswith(f"{c}::"))
                    pw_st = _enc_pw_status(config, c)
                    pw_label = f"  [{pw_st}]" + (f" ({pw_count} saved)" if pw_count else "")
                    print(f"  [{i}]  {c:<24}  {v_label}{pw_label}")
                print()
                print("  Enter a number to manage that container's passwords.")
                print()
                try:
                    sel = input(f"[1-{len(sorted_containers)}] or 0 to go back: ").strip()
                except (EOFError, KeyboardInterrupt):
                    print()
                    break
                if sel == "0":
                    break
                if sel.isdigit() and 1 <= int(sel) <= len(sorted_containers):
                    chosen = sorted_containers[int(sel) - 1]
                    _interactive_password_menu(config, chosen)
                else:
                    print("Invalid choice.")

        else:
            print("Invalid choice.")


def _interactive_config_encryption_menu(config: "Config") -> None:
    """Enable, disable, or change the master password for config-file-at-rest encryption."""
    import getpass
    from cryptography.exceptions import InvalidTag
    global _master_password

    while True:
        is_enc = EncryptionManager(None).is_encrypted(config._path.read_bytes())
        status = "ENABLED" if is_enc else "disabled"
        print(f"\n─── Config file encryption ─────────────────────────")
        print(f"  Status : {status}")
        if is_enc:
            print("  Both config.json and credentials.json are encrypted at rest.")
            print("  The master password is required every time Update Zen starts.")
        else:
            print("  Config files are stored as plaintext (protected by file permissions).")
        print()
        if is_enc:
            print("  1  Change master password")
            print("  2  Disable (decrypt config files)")
        else:
            print("  1  Enable (encrypt config files)")
        print()
        try:
            raw = input("[1-2], 0 to go back: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return
        if raw == "0":
            return

        if not is_enc and raw == "1":
            print()
            try:
                pw1 = getpass.getpass("New master password: ")
            except (EOFError, KeyboardInterrupt):
                print()
                continue
            if not pw1:
                print("Password cannot be empty.")
                continue
            try:
                pw2 = getpass.getpass("Confirm master password: ")
            except (EOFError, KeyboardInterrupt):
                print()
                continue
            if pw1 != pw2:
                print("Passwords do not match.")
                continue
            _master_password = pw1
            config.save()
            _save_credentials(config.encryption["saved_passwords"], config._path.parent)
            print("  Config files encrypted. Master password required at every startup.")
            print("  Cron jobs on non-encrypted containers continue working unchanged.")
            print("  For encrypted containers, set up cron via the container menu to")
            print("  generate a standalone cron config that does not need the master password.")

        elif is_enc and raw == "1":
            print()
            try:
                pw1 = getpass.getpass("New master password: ")
            except (EOFError, KeyboardInterrupt):
                print()
                continue
            if not pw1:
                print("Password cannot be empty.")
                continue
            try:
                pw2 = getpass.getpass("Confirm master password: ")
            except (EOFError, KeyboardInterrupt):
                print()
                continue
            if pw1 != pw2:
                print("Passwords do not match.")
                continue
            _master_password = pw1
            config.save()
            _save_credentials(config.encryption["saved_passwords"])
            print("  Master password updated.")

        elif is_enc and raw == "2":
            print()
            try:
                yn = input("Decrypt config files and disable master password? [y/N]: ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                print()
                continue
            if yn != "y":
                continue
            saved_pws = dict(config.encryption["saved_passwords"])
            _master_password = None
            config.save()
            _save_credentials(saved_pws, config._path.parent)
            print("  Config files are now plaintext. No master password required at startup.")

        else:
            print("Invalid choice.")


def _backup_config(config: Config) -> None:
    """Pack config.json (and optionally credentials.json) into a timestamped tar.gz, optionally encrypted."""
    import getpass

    timestamp = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
    archive_name = f"config_backup_{timestamp}.tar.gz"

    print(f"\n  Source:  {config._path}")

    include_credentials = False
    if CREDENTIALS_FILE.exists():
        try:
            yn_cred = input("Include saved passwords (credentials.json)? [y/N]: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print()
            return
        include_credentials = (yn_cred == "y")
        if include_credentials:
            print(f"           {CREDENTIALS_FILE}")
    print()

    dest_dir = _browse_path(config._path.parent, mode="dir")
    if dest_dir is None:
        return

    try:
        yn = input("Encrypt the backup? [y/N]: ").strip().lower()
    except (EOFError, KeyboardInterrupt):
        print()
        return

    password = None
    if yn == "y":
        try:
            pw1 = getpass.getpass("Backup password: ")
        except (EOFError, KeyboardInterrupt):
            print()
            return
        if not pw1:
            print("Password cannot be empty.")
            return
        try:
            pw2 = getpass.getpass("Confirm password: ")
        except (EOFError, KeyboardInterrupt):
            print()
            return
        if pw1 != pw2:
            print("Passwords do not match.")
            return
        password = pw1

    tar_path = dest_dir / archive_name
    try:
        with tarfile.open(tar_path, "w:gz", compresslevel=1) as tar:
            tar.add(config._path, arcname="config.json")
            if include_credentials:
                tar.add(CREDENTIALS_FILE, arcname="credentials.json")
        tar_path.chmod(0o600)
    except OSError as e:
        print(f"  Backup failed: {e}")
        log(f"[backup_config] failed to write {tar_path}: {e}")
        return

    if password is not None:
        rbpe_path = dest_dir / (archive_name + ".rbpe")
        try:
            EncryptionManager(config).encrypt_file(tar_path, rbpe_path, password=password)
            rbpe_path.chmod(0o600)
            tar_path.unlink()
            final_path = rbpe_path
        except Exception as e:
            print(f"  Encryption failed: {e}")
            log(f"[backup_config] encryption failed for {tar_path}: {e}")
            tar_path.unlink(missing_ok=True)
            return
    else:
        final_path = tar_path

    print(f"  Backup saved: {final_path}")
    log(f"[backup_config] wrote {final_path}")


def _restore_config(config: Config) -> Config:
    """Restore config.json (and optionally credentials.json) from a backup archive."""
    import getpass

    print("\n  Select a backup file (.tar.gz or .tar.gz.rbpe)")
    backup_path = _browse_path(config._path.parent, mode="file")
    if backup_path is None:
        return config

    tar_path = backup_path
    tmp_path = None

    try:
        if backup_path.name.endswith(".rbpe"):
            try:
                password = getpass.getpass("Backup password: ")
            except (EOFError, KeyboardInterrupt):
                print()
                return config
            fd, tmp_str = tempfile.mkstemp(suffix=".tar.gz")
            os.close(fd)
            tmp_path = Path(tmp_str)
            try:
                EncryptionManager(config).decrypt_file(backup_path, tmp_path, password=password)
            except Exception as e:
                print(f"  Decryption failed: {e}")
                log(f"[restore_config] decryption failed for {backup_path}: {e}")
                return config
            tar_path = tmp_path

        try:
            with tarfile.open(tar_path, "r:gz") as tar:
                members = tar.getnames()
        except Exception as e:
            print(f"  Could not read archive: {e}")
            log(f"[restore_config] failed to open {tar_path}: {e}")
            return config

        has_config = "config.json" in members
        has_creds = "credentials.json" in members
        if not has_config:
            print("  This archive does not contain config.json — not a valid config backup.")
            return config

        print(f"\n  Archive contains:")
        print(f"    config.json")
        if has_creds:
            print(f"    credentials.json")
        print()
        print(f"  1  Overwrite live config  ({config._path})")
        print(f"  2  Extract to a different folder")
        print()
        try:
            dest_choice = input("[1/2] or 0 to cancel: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return config

        if dest_choice == "0":
            return config
        elif dest_choice == "1":
            dest_config = config._path
            dest_creds = CREDENTIALS_FILE
        elif dest_choice == "2":
            dest_dir = _browse_path(config._path.parent, mode="dir")
            if dest_dir is None:
                return config
            dest_config = dest_dir / "config.json"
            dest_creds = dest_dir / "credentials.json"
        else:
            print("Invalid choice.")
            return config

        print(f"\n  Will write:")
        print(f"    {dest_config}")
        if has_creds:
            print(f"    {dest_creds}")
        print()
        try:
            yn = input("Proceed? [y/N]: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print()
            return config
        if yn != "y":
            return config

        try:
            with tarfile.open(tar_path, "r:gz") as tar:
                cfg_f = tar.extractfile(tar.getmember("config.json"))
                dest_config.write_bytes(cfg_f.read())
                dest_config.chmod(0o600)
                if has_creds:
                    creds_f = tar.extractfile(tar.getmember("credentials.json"))
                    dest_creds.write_bytes(creds_f.read())
                    dest_creds.chmod(0o600)
        except Exception as e:
            print(f"  Restore failed: {e}")
            log(f"[restore_config] extraction failed from {backup_path}: {e}")
            return config

        print(f"  Restored: {dest_config}")
        if has_creds:
            print(f"  Restored: {dest_creds}")
        log(f"[restore_config] restored from {backup_path} → {dest_config}")

        if dest_choice == "1":
            try:
                config = Config.load(config._path)
                print("  Live config reloaded.")
            except Exception as e:
                print(f"  Warning: could not reload config: {e}")

        return config

    finally:
        if tmp_path is not None and tmp_path.exists():
            tmp_path.unlink()


def _format_mode(st_mode: int) -> tuple:
    """Return (symbolic, octal_str) for the permission bits of st_mode."""
    import stat as _stat
    mode = _stat.S_IMODE(st_mode)
    bits = []
    for shift in (6, 3, 0):
        bits.append("r" if mode & (0o4 << shift) else "-")
        bits.append("w" if mode & (0o2 << shift) else "-")
        bits.append("x" if mode & (0o1 << shift) else "-")
    return "".join(bits), f"{mode:04o}"


def _interactive_chmod(config: Config, target: str = "file") -> None:
    """Browse to a file or directory, display its permissions, and apply a new mode."""
    path = _browse_path(Path("/"), mode=target)
    if path is None:
        return

    try:
        st = os.stat(path)
    except OSError as e:
        print(f"  Cannot stat {path}: {e}")
        return

    symbolic, octal = _format_mode(st.st_mode)
    try:
        import pwd as _pwd, grp as _grp
        owner = _pwd.getpwuid(st.st_uid).pw_name
        group = _grp.getgrgid(st.st_gid).gr_name
    except (ImportError, KeyError):
        owner = str(st.st_uid)
        group = str(st.st_gid)

    print(f"\n  Path:   {path}")
    print(f"  Owner:  {owner} / {group}")
    print(f"  Mode:   {symbolic}  ({octal})")
    print()
    print(f"  1  0600  rw-------  owner read/write only")
    print(f"  2  0644  rw-r--r--  owner read/write, others read")
    print(f"  3  0755  rwxr-xr-x  owner full, others read/execute")
    print(f"  4  0400  r--------  owner read-only")
    print(f"  5  Enter custom octal")
    print()

    while True:
        try:
            raw = input("[1-5] or 0 to cancel: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return
        if raw == "0":
            return
        if raw == "1":
            new_mode = 0o600
        elif raw == "2":
            new_mode = 0o644
        elif raw == "3":
            new_mode = 0o755
        elif raw == "4":
            new_mode = 0o400
        elif raw == "5":
            try:
                octal_str = input("  Octal (e.g. 644 or 0755): ").strip()
            except (EOFError, KeyboardInterrupt):
                print()
                continue
            if not re.fullmatch(r"[0-7]{3,4}", octal_str):
                print("  Invalid: enter 3 or 4 octal digits (e.g. 644 or 0755).")
                continue
            new_mode = int(octal_str, 8)
        else:
            print("Invalid choice.")
            continue

        try:
            os.chmod(path, new_mode)
        except OSError as e:
            print(f"  chmod failed: {e}")
            log(f"[chmod] failed {path} → {new_mode:04o}: {e}")
            return

        symbolic_new, octal_new = _format_mode(os.stat(path).st_mode)
        print(f"  Mode set: {symbolic_new}  ({octal_new})")
        log(f"[chmod] {path}: {octal} → {octal_new}")
        return


def _interactive_move_file(config: Config) -> None:
    """Browse to a source file, pick a destination directory, optionally rename, and move."""
    print("\n  Select source file")
    src = _browse_path(Path("/"), mode="file")
    if src is None:
        return

    print("\n  Select destination directory")
    dest_dir = _browse_path(src.parent, mode="dir")
    if dest_dir is None:
        return

    try:
        raw_name = input(f"  Destination filename [{src.name}]: ").strip()
    except (EOFError, KeyboardInterrupt):
        print()
        return
    dst_name = raw_name if raw_name else src.name
    dst = dest_dir / dst_name

    if dst == src:
        print("  Source and destination are the same — nothing to do.")
        return

    print(f"\n  Move: {src}")
    print(f"    →   {dst}")
    if dst.exists():
        print(f"  Warning: {dst.name} already exists and will be overwritten.")
    print()
    try:
        yn = input("Confirm? [y/N]: ").strip().lower()
    except (EOFError, KeyboardInterrupt):
        print()
        return
    if yn != "y":
        return

    try:
        shutil.move(str(src), str(dst))
    except (PermissionError, FileNotFoundError, shutil.Error, OSError) as e:
        print(f"  Move failed: {e}")
        log(f"[move_file] failed {src} → {dst}: {e}")
        return

    print(f"  Moved to: {dst}")
    log(f"[move_file] {src} → {dst}")


def _interactive_delete_file(config: Config) -> None:
    """Browse to a file and permanently delete it after confirmation."""
    print("\n  Select the file to delete")
    path = _browse_path(Path("/"), mode="file")
    if path is None:
        return
    print(f"\n  File: {path}")
    try:
        yn = input("Delete this file? [y/N]: ").strip().lower()
    except (EOFError, KeyboardInterrupt):
        print()
        return
    if yn != "y":
        return
    try:
        path.unlink()
        print(f"  Deleted: {path}")
        log(f"[delete_file] deleted {path}")
    except OSError as e:
        print(f"  Delete failed: {e}")
        log(f"[delete_file] failed to delete {path}: {e}")


def _interactive_create_folder(config: Config) -> None:
    """Browse to a parent directory and create a new subfolder."""
    print("\n  Select the parent directory")
    parent = _browse_path(Path("/"), mode="dir")
    if parent is None:
        return
    try:
        folder_name = input(f"  Parent: {parent}\n  New folder name: ").strip()
    except (EOFError, KeyboardInterrupt):
        print()
        return
    if not folder_name or "/" in folder_name or folder_name in (".", ".."):
        print("  Invalid folder name.")
        return
    new_dir = parent / folder_name
    try:
        new_dir.mkdir(mode=0o700)
        print(f"  Created: {new_dir}")
        log(f"[create_folder] created {new_dir}")
    except FileExistsError:
        print(f"  Already exists: {new_dir}")
    except OSError as e:
        print(f"  Create failed: {e}")
        log(f"[create_folder] failed to create {new_dir}: {e}")


def _file_action_menu(path: Path) -> None:
    """Per-file action sub-menu: delete, move/rename, or change permissions."""
    while True:
        print(f"\n─── {path.name} {'─' * max(1, 48 - len(path.name))}")
        print(f"  Path: {path}")
        try:
            st = path.stat()
            sym, oct_str = _format_mode(st.st_mode)
            sz = st.st_size
            if sz < 1024:
                sz_str = f"{sz} B"
            elif sz < 1024 * 1024:
                sz_str = f"{sz / 1024:.1f} KB"
            else:
                sz_str = f"{sz / 1024 / 1024:.1f} MB"
            print(f"  Size: {sz_str}  |  {sym}  ({oct_str})")
        except OSError:
            pass
        print()
        print("  1  Delete")
        print("  2  Move / rename")
        print("  3  Change permissions")
        print("  0  Back")
        print()
        try:
            raw = input("[1-3], 0 to go back: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return
        if raw == "0":
            return
        elif raw == "1":
            try:
                yn = input(f"  Delete {path.name}? [y/N]: ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                print()
                continue
            if yn != "y":
                continue
            try:
                path.unlink()
                print(f"  Deleted: {path}")
                log(f"[file_action] deleted {path}")
                return
            except OSError as e:
                print(f"  Delete failed: {e}")
                log(f"[file_action] delete failed {path}: {e}")
        elif raw == "2":
            print("\n  Select destination directory")
            dest_dir = _browse_path(path.parent, mode="dir")
            if dest_dir is None:
                continue
            try:
                raw_name = input(f"  Filename [{path.name}]: ").strip()
            except (EOFError, KeyboardInterrupt):
                print()
                continue
            dst_name = raw_name if raw_name else path.name
            dst = dest_dir / dst_name
            if dst == path:
                print("  Same location — nothing to do.")
                continue
            try:
                shutil.move(str(path), str(dst))
                print(f"  Moved to: {dst}")
                log(f"[file_action] moved {path} → {dst}")
                return
            except (PermissionError, FileNotFoundError, shutil.Error, OSError) as e:
                print(f"  Move failed: {e}")
                log(f"[file_action] move failed {path} → {dst}: {e}")
        elif raw == "3":
            presets = [
                (0o600, "rw-------"),
                (0o644, "rw-r--r--"),
                (0o755, "rwxr-xr-x"),
                (0o400, "r--------"),
            ]
            print()
            for i, (mode, sym) in enumerate(presets, 1):
                print(f"  {i}  {oct(mode)}  {sym}")
            print("  5  Custom")
            print()
            try:
                p = input("[1-5]: ").strip()
            except (EOFError, KeyboardInterrupt):
                print()
                continue
            if p in ("1", "2", "3", "4"):
                new_mode = presets[int(p) - 1][0]
            elif p == "5":
                try:
                    raw_oct = input("Octal (e.g. 0o640): ").strip()
                    new_mode = int(raw_oct, 8)
                except (EOFError, KeyboardInterrupt, ValueError):
                    print("  Invalid.")
                    continue
            else:
                print("  Invalid choice.")
                continue
            try:
                path.chmod(new_mode)
                sym_new, oct_new = _format_mode(path.stat().st_mode)
                print(f"  Mode set: {sym_new}  ({oct_new})")
                log(f"[file_action] chmod {path}: {oct_new}")
            except OSError as e:
                print(f"  chmod failed: {e}")
        else:
            print("  Invalid choice.")


def _interactive_file_manager(config: Config,
                               enc: "EncryptionManager | None" = None) -> tuple:
    """File manager menu — config backup/restore, chmod, move."""
    while True:
        print(f"\n─── File Manager ───────────────────────────────────")
        print(f"  1  Backup config")
        print(f"  2  Restore config backup")
        print(f"  3  File manager")
        print()
        try:
            raw = input("[1-3], 0 to go back: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return config, enc
        if raw == "0":
            return config, enc
        if raw == "1":
            _backup_config(config)
        elif raw == "2":
            config = _restore_config(config)
        elif raw == "3":
            browse_start = Path("/")
            while True:
                selected = _browse_path(browse_start, mode="file")
                if selected is None:
                    break
                browse_start = selected.parent
                _file_action_menu(selected)
        else:
            print("Invalid choice.")


def _all_snapshot_container_names(config: Config) -> list:
    """Return sorted list of all container names found across every snapshot base directory."""
    seen: set = set()
    result = []
    for base_dir in _enc_snapshot_dirs(config):
        if not base_dir.exists():
            continue
        try:
            for d in base_dir.iterdir():
                if d.is_dir() and d.name not in seen:
                    seen.add(d.name)
                    result.append(d.name)
        except OSError:
            pass
    return sorted(result)


def _interactive_global_chmod(config: Config) -> Config:
    """Set the global snapshot permission profile and optionally bulk-apply to all containers."""
    cur_dm = config.snapshot_dir_mode
    cur_fm = config.snapshot_file_mode
    cur_label = _permission_profile_label(cur_dm, cur_fm)
    overrides = config.snapshot_permission_overrides
    n_overrides = len(overrides)

    print(f"\n─── Settings — Snapshot Permissions ────────────────")
    print()
    print(f"  Global default: {cur_label}  (dirs {cur_dm:04o}, files {cur_fm:04o})")
    if overrides:
        parts = []
        for ctr, modes in overrides.items():
            lbl = _permission_profile_label(modes["dir_mode"], modes["file_mode"])
            parts.append(f"{ctr} ({lbl})")
        print(f"  Container overrides: {', '.join(parts)}")
    else:
        print("  Container overrides: none")
    print()
    for i, (label, dm, fm, note) in enumerate(_PERMISSION_PROFILES, 1):
        print(f"  {i}  {label:<8}  dirs {dm:04o}, files {fm:04o}  ({note})")
    print("  4  Custom    enter separately")
    print()

    dir_mode = file_mode = None
    profile_label = ""
    while True:
        try:
            raw = input("[1-4] or 0 to cancel: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return config
        if raw == "0":
            return config
        if raw in ("1", "2", "3"):
            label, dir_mode, file_mode, _ = _PERMISSION_PROFILES[int(raw) - 1]
            profile_label = f"{label}  (dirs {dir_mode:04o}, files {file_mode:04o})"
            break
        if raw == "4":
            try:
                d_str = input("  Dir octal (e.g. 700 or 0750): ").strip()
            except (EOFError, KeyboardInterrupt):
                print()
                continue
            if not re.fullmatch(r"[0-7]{3,4}", d_str):
                print("  Invalid: enter 3 or 4 octal digits.")
                continue
            try:
                f_str = input("  File octal (e.g. 600 or 0640): ").strip()
            except (EOFError, KeyboardInterrupt):
                print()
                continue
            if not re.fullmatch(r"[0-7]{3,4}", f_str):
                print("  Invalid: enter 3 or 4 octal digits.")
                continue
            dir_mode = int(d_str, 8)
            file_mode = int(f_str, 8)
            profile_label = f"Custom  (dirs {dir_mode:04o}, files {file_mode:04o})"
            break
        print("Invalid choice.")

    if dir_mode != cur_dm or file_mode != cur_fm:
        config.snapshot_dir_mode = dir_mode
        config.snapshot_file_mode = file_mode
        config.save()
        print(f"  Global profile set to {profile_label}.")

    try:
        yn = input("Apply to existing snapshot files? [y/N]: ").strip().lower()
    except (EOFError, KeyboardInterrupt):
        print()
        return config
    if yn != "y":
        return config

    if n_overrides:
        print()
        print("  a  All containers")
        print("  s  Skip containers with custom overrides")
        print()
        try:
            scope = input("[a/s] or 0 to cancel: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print()
            return config
        if scope == "0":
            return config
        if scope not in ("a", "s"):
            print("Invalid choice.")
            return config
    else:
        scope = "a"

    all_containers = _all_snapshot_container_names(config)
    if not all_containers:
        print("  No snapshot directories found.")
        return config

    if scope == "s":
        containers = [c for c in all_containers if c not in config.snapshot_permission_overrides]
        skipped = [c for c in all_containers if c in config.snapshot_permission_overrides]
    else:
        containers = all_containers
        skipped = []

    if not containers:
        print("  All containers have custom overrides — nothing to apply.")
        if skipped:
            print(f"  Skipped: {', '.join(skipped)}")
        return config

    rows = []
    total_dirs = total_files = 0
    for ctr in containers:
        snap_dirs = _collect_container_snapshot_dirs(config, ctr)
        ctr_dirs = ctr_files = 0
        for d in snap_dirs:
            dd, ff = _bulk_chmod_tree(d, dir_mode, file_mode)
            ctr_dirs += dd
            ctr_files += ff
            log(f"[global_chmod] {ctr}: {d} → dirs {dir_mode:04o} files {file_mode:04o} "
                f"({dd} dirs, {ff} files)")
        total_dirs += ctr_dirs
        total_files += ctr_files
        rows.append((ctr,
                     f"{ctr_dirs} dir{'s' if ctr_dirs != 1 else ''}",
                     f"{ctr_files} file{'s' if ctr_files != 1 else ''}"))

    print()
    _print_table(["CONTAINER", "DIRS", "FILES"], rows)
    if skipped:
        print(f"\n  Skipped (custom override): {', '.join(skipped)}")
    print(f"\n  Total: {total_dirs} director{'ies' if total_dirs != 1 else 'y'}, "
          f"{total_files} file{'s' if total_files != 1 else ''} updated.")
    return config


_HOME_COLUMNS = [
    {"id": "num",       "header": "\n#",           "always": True},
    {"id": "name",      "header": "\nCONTAINER",   "always": True},
    {"id": "enc",       "header": "\nENC",          "always": False},
    {"id": "saved_pw",  "header": "SVD\nPWD",       "always": False},
    {"id": "hlth",      "header": "\nHLTH",         "always": False},
    {"id": "updt",      "header": "\nUPDT",         "always": False},
    {"id": "image",     "header": "\nIMAGE",        "always": False},
    {"id": "ver",       "header": "\nVER",          "always": False},
    {"id": "date",      "header": "\nDATE",         "always": False},
    {"id": "snaps",     "header": "\nSNAPS",        "always": False},
    {"id": "pin",       "header": "\nPIN",          "always": False},
    {"id": "cron",      "header": "\nCRON",         "always": False},
    {"id": "auto_rb",   "header": "AUTO\nRB",       "always": False},
    {"id": "img_exp",   "header": "IMG\nEXP",       "always": False},
    {"id": "vol_bak",   "header": "VOL\nBAK",       "always": False},
    {"id": "uptime",    "header": "\nUPTIME",       "always": False},
    {"id": "restarts",  "header": "RE-\nSTARTS",    "always": False},
    {"id": "ports",     "header": "\nPORTS",        "always": False},
    {"id": "network",   "header": "\nNETWORK",      "always": False},
    {"id": "compose",   "header": "\nCOMPOSE",      "always": False},
    {"id": "pct",       "header": "\n%",            "always": False},
    {"id": "mounts",    "header": "\nMOUNTS",       "always": False},
    {"id": "snap_path", "header": "SNAPSHOT\nPATH", "always": False},
]


def _interactive_column_menu(config: Config) -> Config:
    _col_meta = {
        "enc":       ("ENC",           "Encryption enabled for this container"),
        "saved_pw":  ("SVD PWD",       "Password saved in credentials.json"),
        "hlth":      ("HLTH",          "Container health status"),
        "updt":      ("UPDT",          "Update available from registry"),
        "image":     ("IMAGE",         "Running image tag"),
        "ver":       ("VER",           "Running version from image labels"),
        "date":      ("DATE",          "Image creation date"),
        "snaps":     ("SNAPS",         "Stored snapshot count"),
        "pin":       ("PIN",           "Active version pin"),
        "cron":      ("CRON",          "Scheduled job count"),
        "auto_rb":   ("AUTO RB",       "Auto-rollback enabled"),
        "img_exp":   ("IMG EXP",       "Image export before updates"),
        "vol_bak":   ("VOL BAK",       "Volume backup enabled"),
        "uptime":    ("UPTIME",        "Time since container started"),
        "restarts":  ("RESTARTS",      "Restart count"),
        "ports":     ("PORTS",         "Published host ports"),
        "network":   ("NETWORK",       "Network mode or name"),
        "compose":   ("COMPOSE",       "Compose project name"),
        "pct":       ("%",             "Per-mount backup status symbols"),
        "mounts":    ("MOUNTS",        "Volume mount paths"),
        "snap_path": ("SNAPSHOT PATH", "Effective snapshot save location"),
    }
    _toggleable = [c for c in _HOME_COLUMNS if not c["always"]]
    _all_ids = [c["id"] for c in _toggleable]
    while True:
        hidden = set(config.hidden_columns)
        n_hidden = sum(1 for cid in _all_ids if cid in hidden)
        print(f"\n─── Column Visibility ────────────────────────────────────────────────────")
        always_names = "  |  ".join(
            c["header"].replace("\n", " ").strip() for c in _HOME_COLUMNS if c["always"]
        )
        print(f"  Always shown: {always_names}")
        print()
        for idx, col in enumerate(_toggleable, 1):
            mark = "□" if col["id"] in hidden else "■"
            name, desc = _col_meta.get(col["id"], (col["id"], ""))
            print(f"  [{mark}] {idx:>2}  {name:<15}  {desc}")
        print()
        n_vis = len(_all_ids) - n_hidden
        print(f"  {n_vis} of {len(_all_ids)} optional columns shown")
        print()
        print("  a  Show all    n  Hide all    0  Back    q  Quit")
        print()
        n = len(_toggleable)
        try:
            raw = input(f"[1-{n}] to toggle, a/n, 0 to go back: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print()
            return config
        if raw == "0":
            return config
        if raw in ("q", "quit"):
            print("\nGoodbye.")
            sys.exit(0)
        elif raw == "a":
            config.hidden_columns.clear()
            config.save()
            print("All columns shown.")
        elif raw == "n":
            config.hidden_columns = list(_all_ids)
            config.save()
            print("All optional columns hidden.")
        elif raw.isdigit() and 1 <= int(raw) <= n:
            col = _toggleable[int(raw) - 1]
            cid = col["id"]
            if cid in config.hidden_columns:
                config.hidden_columns.remove(cid)
            else:
                config.hidden_columns.append(cid)
            config.save()
        else:
            print("Invalid choice.")


def _settings_snapshots_menu(config: Config) -> Config:
    while True:
        ie_state = "ON" if config.image_export_enabled else "OFF"
        perm_label = _permission_profile_label(config.snapshot_dir_mode, config.snapshot_file_mode)
        n_perm_overrides = len(config.snapshot_permission_overrides)
        perm_note = (f"  ({n_perm_overrides} container override{'s' if n_perm_overrides != 1 else ''})"
                     if n_perm_overrides else "")

        print(f"\n─── Settings — Snapshots ───────────────────────────")
        print()
        print(f"  1  Global snapshot directory: {config.snapshot_dir}")
        print(f"  2  Rotation limit (global): {config.max_snapshots}")
        print(f"  3  File permissions: {perm_label}{perm_note}")
        print(f"  4  Image export before updates: {ie_state}")
        print()
        try:
            raw = input("[1-4], 0 to go back, q to quit: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return config
        if raw == "0":
            return config
        if raw in ("q", "quit"):
            print("\nGoodbye.")
            sys.exit(0)

        if raw == "1":
            chosen = _browse_path(config.snapshot_dir, mode="dir")
            if chosen:
                chosen.mkdir(parents=True, exist_ok=True)
                config.snapshot_dir = chosen
                config.save()
                print(f"Snapshot directory set to {chosen}.")
        elif raw == "2":
            try:
                val = input(f"Enter new global snapshot limit (current: {config.max_snapshots}, min 1): ").strip()
            except (EOFError, KeyboardInterrupt):
                print()
                continue
            if val.isdigit() and int(val) >= 1:
                config.max_snapshots = int(val)
                config.save()
                print(f"Global snapshot limit set to {config.max_snapshots}.")
            else:
                print("Invalid value — must be a whole number >= 1.")
        elif raw == "3":
            config = _interactive_global_chmod(config)
        elif raw == "4":
            config.image_export_enabled = not config.image_export_enabled
            config.save()
            new_state = "ON" if config.image_export_enabled else "OFF"
            print(f"Image export set to {new_state}.")
        else:
            print("Invalid choice.")
    return config


def _settings_volumes_menu(config: Config) -> Config:
    while True:
        vb_state = "ON" if config.volume_backup_enabled else "OFF"
        pfb_state = "ON" if config.pause_for_backup else "OFF"

        print(f"\n─── Settings — Volumes ─────────────────────────────")
        print()
        print(f"  1  Volume backup (all containers): {vb_state}")
        print(f"  2  Pause container during volume backup (all containers): {pfb_state}")
        print()
        try:
            raw = input("[1-2], 0 to go back, q to quit: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return config
        if raw == "0":
            return config
        if raw in ("q", "quit"):
            print("\nGoodbye.")
            sys.exit(0)

        if raw == "1":
            config.volume_backup_enabled = not config.volume_backup_enabled
            config.save()
            new_state = "ON" if config.volume_backup_enabled else "OFF"
            print(f"Volume backup set to {new_state}.")
        elif raw == "2":
            config.pause_for_backup = not config.pause_for_backup
            config.save()
            new_state = "ON" if config.pause_for_backup else "OFF"
            print(f"Pause for backup set to {new_state}.")
        else:
            print("Invalid choice.")
    return config


def _settings_display_menu(config: Config) -> Config:
    while True:
        pg_state = "ON" if config.pagination_enabled else "OFF"
        _n_hidden_cols = sum(1 for c in _HOME_COLUMNS if not c["always"] and c["id"] in config.hidden_columns)
        _n_total_cols = sum(1 for c in _HOME_COLUMNS if not c["always"])

        print(f"\n─── Settings — Display ─────────────────────────────")
        print()
        print(f"  1  Column visibility: {_n_total_cols - _n_hidden_cols} of {_n_total_cols} optional columns shown")
        print(f"  2  Container list pagination: {pg_state}")
        print()
        try:
            raw = input("[1-2], 0 to go back, q to quit: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return config
        if raw == "0":
            return config
        if raw in ("q", "quit"):
            print("\nGoodbye.")
            sys.exit(0)

        if raw == "1":
            config = _interactive_column_menu(config)
        elif raw == "2":
            config.pagination_enabled = not config.pagination_enabled
            config.save()
            new_state = "ON" if config.pagination_enabled else "OFF"
            print(f"Container list pagination set to {new_state}.")
        else:
            print("Invalid choice.")
    return config


def _settings_config_files_menu(config: Config,
                                  enc: "EncryptionManager | None") -> tuple:
    while True:
        print(f"\n─── Settings — Config Files ────────────────────────")
        print()
        print(f"  1  Switch config file: {config._path}")
        print(f"  2  View recent log")
        print(f"  3  Log file path: {_to_portable_path(config.log_file)}")
        print()
        try:
            raw = input("[1-3], 0 to go back, q to quit: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return config, enc
        if raw == "0":
            return config, enc
        if raw in ("q", "quit"):
            print("\nGoodbye.")
            sys.exit(0)

        if raw == "1":
            print("\n  1  Load an existing config file")
            print("  2  Create a new config in a chosen folder")
            print()
            try:
                sub = input("[1-2] or 0 to cancel: ").strip()
            except (EOFError, KeyboardInterrupt):
                print()
                continue
            if sub == "1":
                chosen = _browse_path(config._path.parent, mode="file", filter_ext=".json")
                if chosen:
                    try:
                        new_cfg = Config.load(chosen)
                        print(f"Switched to config: {chosen}")
                        return new_cfg, None
                    except Exception as e:
                        print(f"Could not load config: {e}")
            elif sub == "2":
                chosen = _browse_path(config._path.parent, mode="dir")
                if chosen:
                    new_path = chosen / "config.json"
                    new_cfg = Config.load(new_path)
                    print(f"New config created at {new_path}.")
                    return new_cfg, None
        elif raw == "2":
            log_path = Path(config.log_file)
            if not log_path.exists():
                print("  (log file not found)")
            else:
                lines = log_path.read_text(errors="replace").splitlines()
                tail = lines[-50:] if len(lines) > 50 else lines
                print(f"\n─── Recent log ({log_path}) {'─' * max(1, 44 - len(str(log_path)))}")
                for line in tail:
                    print(f"  {line}")
                print()
            try:
                input("  Press Enter to continue.")
            except (EOFError, KeyboardInterrupt):
                print()
        elif raw == "3":
            chosen = _browse_path(config.log_file.parent, mode="dir")
            if chosen:
                global _active_log_file
                config.log_file = chosen / "update_zen.log"
                _active_log_file = config.log_file
                config.save()
                print(f"Log file set to {config.log_file}.")
        else:
            print("Invalid choice.")
    return config, enc


def _settings_maintenance_menu(config: Config) -> Config:
    while True:
        excl_n = len(config.exclude)
        excl_summary = (f"{excl_n} detached: {', '.join(config.exclude)}"
                        if config.exclude else "none")
        orphan_n = len(_collect_orphans(config))
        orphan_summary = (f"{orphan_n} orphaned artifact{'s' if orphan_n != 1 else ''} found"
                          if orphan_n else "clean")

        print(f"\n─── Settings — Maintenance ─────────────────────────")
        print()
        print(f"  1  Cleanup orphans: {orphan_summary}")
        print(f"  2  Detached containers: {excl_summary}")
        print()
        try:
            raw = input("[1-2], 0 to go back, q to quit: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return config
        if raw == "0":
            return config
        if raw in ("q", "quit"):
            print("\nGoodbye.")
            sys.exit(0)

        if raw == "1":
            import shutil
            orphans = _collect_orphans(config)
            if not orphans:
                print("No orphaned artifacts found.")
                try:
                    input("  Press Enter to continue.")
                except (EOFError, KeyboardInterrupt):
                    print()
                continue
            total_bytes = sum(o["size_bytes"] for o in orphans)
            rows = [
                (o["container"], o["type"], _fmt_bytes(o["size_bytes"]), str(o["path"]))
                for o in orphans
            ]
            print(f"\nOrphaned artifacts — {len(orphans)} item{'s' if len(orphans) != 1 else ''}, "
                  f"{_fmt_bytes(total_bytes)} total:\n")
            _print_table(["CONTAINER", "TYPE", "SIZE", "PATH"], rows)
            print()
            try:
                yn = input(f"Delete {len(orphans)} item{'s' if len(orphans) != 1 else ''}? [y/N] ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                print()
                continue
            if yn != "y":
                continue
            deleted = 0
            freed = 0
            for o in orphans:
                p = o["path"]
                try:
                    if o["type"] == "staging":
                        shutil.rmtree(p)
                    else:
                        p.unlink()
                    log(f"[cleanup] removed {o['type']}: {p}")
                    deleted += 1
                    freed += o["size_bytes"]
                except OSError as e:
                    log(f"[cleanup] failed to remove {p}: {e}")
            print(f"Removed {deleted} item{'s' if deleted != 1 else ''}, freed {_fmt_bytes(freed)}.")
        elif raw == "2":
            if not config.exclude:
                print("No detached containers.")
            else:
                print()
                for i, c in enumerate(config.exclude, 1):
                    print(f"  {i}  {c}")
                print()
                try:
                    sel = input("Re-attach container [1-N], 0 to cancel: ").strip()
                except (EOFError, KeyboardInterrupt):
                    print()
                    continue
                if sel.isdigit() and 1 <= int(sel) <= len(config.exclude):
                    detached = config.exclude[int(sel) - 1]
                    config.exclude.remove(detached)
                    config.save()
                    print(f"{detached} re-attached to update_zen.")
        else:
            print("Invalid choice.")
    return config


def _interactive_settings(config: Config,
                           enc: "EncryptionManager | None" = None) -> tuple:
    """Show the settings menu and return the (possibly updated) (Config, enc) pair."""
    while True:
        vb_state = "ON" if config.volume_backup_enabled else "OFF"
        ar_state = "ON" if config.auto_rollback else "OFF"
        _enc_containers_v2 = config.encryption.get("encrypt_containers", [])
        if _enc_containers_v2:
            _enc_c = len(_enc_containers_v2)
            _enc_saved = len(config.encryption.get("saved_passwords", {}))
            enc_state = (f"active | mode: {config.encryption.get('mode', 'session')}"
                         f" | {_enc_c} container{'s' if _enc_c != 1 else ''} encrypted"
                         + (f" | {_enc_saved} saved pw" if _enc_saved else ""))
        else:
            enc_state = "disabled"
        n_cron_total = sum(len(v) for v in config.cron_jobs.values())

        print(f"\n─── Settings ───────────────────────────────────────")
        print(f"    volume backup: {vb_state}  |  auto-rollback: {ar_state}"
              f"  |  encryption: {enc_state}")
        print(f"    snapshots: {config.snapshot_dir}")
        print()
        print("  s  Snapshots        (directory, rotation, permissions, image export)")
        print("  v  Volumes          (backup on/off, pause-for-backup)")
        print(f"  a  Auto-rollback    (global: {ar_state})")
        print(f"  e  Encryption       ({enc_state})")
        print(f"  j  Jobs / Schedule  ({n_cron_total} job{'s' if n_cron_total != 1 else ''} configured)")
        print("  d  Display          (columns, pagination, snapshot path)")
        print("  c  Config files     (switch config, log path, view log)")
        print("  m  Maintenance      (orphan cleanup, detached containers)")
        print()
        try:
            raw = input("[s/v/a/e/j/d/c/m], 0 to go back, q to quit: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print()
            return config, enc
        if raw == "0":
            return config, enc
        if raw in ("q", "quit"):
            print("\nGoodbye.")
            sys.exit(0)

        if raw == "s":
            config = _settings_snapshots_menu(config)
        elif raw == "v":
            config = _settings_volumes_menu(config)
        elif raw == "a":
            config.auto_rollback = not config.auto_rollback
            config.save()
            new_state = "ON" if config.auto_rollback else "OFF"
            print(f"Auto-rollback set to {new_state}.")
        elif raw == "e":
            config, enc = _interactive_encryption_menu(config, enc)
        elif raw == "j":
            _interactive_cron_overview(config)
        elif raw == "d":
            config = _settings_display_menu(config)
        elif raw == "c":
            new_config, enc = _settings_config_files_menu(config, enc)
            if new_config is not config:
                return new_config, enc
            config = new_config
        elif raw == "m":
            config = _settings_maintenance_menu(config)
        else:
            print("Invalid choice.")


def _batch_update(config: Config, docker: DockerClient,
                   registry: RegistryClient, sm: SnapshotManager,
                   results: list) -> None:
    """Confirmation + sequential update for all containers showing UPDATE=yes."""
    candidates = [r for r in results if r[2] == "yes"]
    if not candidates:
        print("No containers with available updates.")
        return

    print(f"\n─── Update all {'─' * 45}")
    print()
    print("  These containers have available updates:\n")
    for i, row in enumerate(candidates, 1):
        name, health, update, version, date, image, snaps, backup_col, mounts, *_ = row
        print(f"  [{i}]  {name:<30}  {version or image}")
    print()
    ar_off = [r[0] for r in candidates if r[0] in config.auto_rollback_disabled]
    if ar_off:
        print(f"  Note: auto-rollback is OFF for: {', '.join(ar_off)}")
        print()
    n = len(candidates)
    try:
        yn = input(f"Proceed with all {n} update{'s' if n != 1 else ''}? [y/N]: ").strip().lower()
    except (EOFError, KeyboardInterrupt):
        print()
        return
    if yn != "y":
        return

    outcomes: list[tuple[str, bool, str]] = []
    for row in candidates:
        name = row[0]
        effective_ar = config.auto_rollback and name not in config.auto_rollback_disabled
        print(f"\n{'─' * 3} {name} {'─' * max(1, 50 - len(name))}")
        try:
            ok = Engine(config).update(name, auto_rollback=effective_ar)
            outcomes.append((name, bool(ok), ""))
        except Exception as e:
            outcomes.append((name, False, str(e)))

    print(f"\n─── Batch update complete {'─' * 35}")
    for name, ok, err in outcomes:
        mark = "OK" if ok else "FAILED"
        suffix = f"  ({err})" if err else ""
        print(f"  {mark:<8}  {name}{suffix}")
    print()


def cmd_interactive(config: Config) -> None:
    enc = None  # passwords resolved lazily per-container; upfront unlock removed in Sprint 3
    docker = DockerClient()
    registry = RegistryClient()
    sm = SnapshotManager(config)
    try:
        _ps = docker._run(["ps", "--format", "{{.Names}}"])
        _init_names = sorted(
            n.strip() for n in _ps.stdout.splitlines()
            if n.strip() and n.strip() not in config.exclude
        )
    except DockerError as e:
        print(f"Error listing containers: {e}", file=sys.stderr)
        sys.exit(1)
    print()
    print()
    print(_SPLASH_SISYPHUS)
    print()
    print()
    print(_SPLASH_TITLE)
    print()
    print()
    _cfg_source = "UPDATE_ZEN_CONFIG" if os.environ.get("UPDATE_ZEN_CONFIG") else "default"
    log(f"Update Zen {_VERSION}")
    print()
    print(f"Tip of the Day: {random.choice(_TIPS)}")
    print()
    print(f"Config: {CONFIG_FILE}")
    print()
    _init_fetch_done = False
    if _init_names:
        print(f"Fetching status for {len(_init_names)} container{'s' if len(_init_names) != 1 else ''}...")
        with concurrent.futures.ThreadPoolExecutor(max_workers=_STATUS_WORKERS) as pool:
            _init_futures = {
                pool.submit(_fetch_one_status, n, docker, registry, sm, config, False): n
                for n in _init_names
            }
            print("\n  -- press any key to continue --", end="", flush=True)
            _getchar()
            print()
            _init_results_map = {}
            for future in concurrent.futures.as_completed(_init_futures):
                row = future.result()
                _init_results_map[row[0]] = row
            _init_fetch_done = True
    else:
        print("\n  -- press any key to continue --", end="", flush=True)
        _getchar()
        print()
    _first_iter = True
    _cached_names = None
    _cached_results_map = None

    _should_refetch = False
    while True:
        if _first_iter and _init_fetch_done:
            _cached_names = _init_names
            _cached_results_map = _init_results_map
        elif _first_iter or _should_refetch:
            try:
                result = docker._run(["ps", "--format", "{{.Names}}"])
                _cached_names = sorted(
                    n.strip() for n in result.stdout.splitlines()
                    if n.strip() and n.strip() not in config.exclude
                )
            except DockerError as e:
                print(f"Error listing containers: {e}", file=sys.stderr)
                sys.exit(1)
            if not _cached_names:
                print("No running containers.")
                return
            if not _first_iter:
                print(f"Fetching status for {len(_cached_names)} container{'s' if len(_cached_names) != 1 else ''}...")
            with concurrent.futures.ThreadPoolExecutor(max_workers=_STATUS_WORKERS) as pool:
                futures = {
                    pool.submit(_fetch_one_status, n, docker, registry, sm, config, False): n
                    for n in _cached_names
                }
                _cached_results_map = {}
                for future in concurrent.futures.as_completed(futures):
                    row = future.result()
                    _cached_results_map[row[0]] = row
        _first_iter = False
        _should_refetch = False

        names = _cached_names
        results_map = _cached_results_map
        if not names:
            print("No running containers.")
            return
        results = sorted(
            (results_map[n] for n in names if n in results_map),
            key=lambda r: (r[2] != "yes", r[0].lower()),
        )
        print()
        _enc_v2 = config.encryption.get("encrypt_containers", [])
        if _enc_v2:
            _enc_mode = config.encryption.get("mode", "session")
            _enc_saved_n = len(config.encryption.get("saved_passwords", {}))
            _enc_c_n = len(_enc_v2)
            _enc_parts = [f"mode: {_enc_mode}"]
            if _enc_c_n:
                _enc_parts.append(f"{_enc_c_n} container{'s' if _enc_c_n != 1 else ''} encrypted")
            if _enc_saved_n:
                _enc_parts.append(f"{_enc_saved_n} saved pw")
            print(f"[ENC] {' | '.join(_enc_parts)}")
            print()
        _hidden = set(config.hidden_columns)
        _active_cols = [c for c in _HOME_COLUMNS if c["always"] or c["id"] not in _hidden]
        _snap_path_active = any(c["id"] == "snap_path" for c in _active_cols)
        _tbl_headers = [c["header"] for c in _active_cols]
        _name_col_idx = next(i for i, c in enumerate(_active_cols) if c["id"] == "name")
        _tbl_max_widths = {_name_col_idx: 28}
        _enc_containers = config.encryption.get("encrypt_containers", [])
        _hlth_sym = {
            "healthy":    "+",
            "running":    "*",
            "unhealthy":  "X",
            "starting":   "~",
            "exited":     "-",
            "paused":     "|",
            "restarting": "@",
            "dead":       "X",
            "removing":   "X",
            "created":    "-",
            "unknown":    "?",
            "error":      "?",
        }
        _tbl_rows = []
        for i, r in enumerate(results, 1):
            # --- pre-compute values shared across multiple columns ---
            _pin = config.pinned_tags.get(r[0], "")
            if _pin:
                _img_disp = _pin
            else:
                _raw_img = r[5]
                _tag = _raw_img.rsplit(":", 1)[-1] if ":" in _raw_img else ""
                _img_disp = "latest" if not _tag or _tag == "latest" else _tag
            _img_disp = (_img_disp[:9] + "...") if len(_img_disp) > 12 else _img_disp
            # pct / mounts default; overridden below when snap_path is active
            _backup_cell = r[7]
            _mounts_cell = r[8]
            _snap_path_col = ""
            if _snap_path_active:
                _snap_raw = str(_to_portable_path(Path(config.snapshot_dir_for(r[0]))))
                _snap_disp = (_snap_raw[:51] + "...") if len(_snap_raw) > 54 else _snap_raw
                _mounts_raw = r[8]
                _backup_raw = r[7]
                if _mounts_raw != "—":
                    _rules = config.volume_backup.get(r[0], {})
                    _mount_paths_map = _rules.get("mount_paths", {})
                    _save_path = _rules.get("save_path")
                    _per_mount_paths = []
                    for _ml in _mounts_raw.split("\n"):
                        _cp = _ml.rsplit(" → ", 1)[-1] if " → " in _ml else ""
                        if _cp and _cp in _mount_paths_map:
                            _mp_raw = str(_to_portable_path(Path(_mount_paths_map[_cp])))
                        elif _save_path:
                            _mp_raw = str(_to_portable_path(Path(_save_path)))
                        else:
                            _mp_raw = _snap_raw
                        _per_mount_paths.append((_mp_raw[:51] + "...") if len(_mp_raw) > 54 else _mp_raw)
                    _snap_path_col = _snap_disp + "\n" + "\n".join(_per_mount_paths)
                    _mounts_cell = "\n" + _mounts_raw
                    _backup_cell = "\n" + _backup_raw
                else:
                    _snap_path_col = _snap_disp
            # --- build row by dispatching on each active column id ---
            _row = []
            for _col in _active_cols:
                _cid = _col["id"]
                if _cid == "num":
                    _row.append(str(i))
                elif _cid == "name":
                    _row.append(((r[0][:25] + "...") if len(r[0]) > 28 else r[0]).ljust(28))
                elif _cid == "enc":
                    _row.append("■" if r[0] in _enc_containers else "□")
                elif _cid == "saved_pw":
                    _row.append("■" if config.get_saved_password(r[0]) else "□")
                elif _cid == "hlth":
                    _row.append(_hlth_sym.get(r[1], r[1]))
                elif _cid == "updt":
                    _row.append(r[2])
                elif _cid == "image":
                    _row.append(_img_disp)
                elif _cid == "ver":
                    _row.append((r[3][:9] + "...") if len(r[3]) > 12 else r[3])
                elif _cid == "date":
                    _row.append(r[4])
                elif _cid == "pct":
                    _row.append(_backup_cell)
                elif _cid == "mounts":
                    _row.append(_mounts_cell)
                elif _cid == "snap_path":
                    _row.append(_snap_path_col)
                elif _cid == "snaps":
                    _row.append(str(r[6]))
                elif _cid == "pin":
                    _pin_disp = (_pin[:9] + "...") if len(_pin) > 12 else _pin
                    _row.append(_pin_disp if _pin_disp else "—")
                elif _cid == "cron":
                    _cron_n = len(config.cron_jobs.get(r[0], []))
                    _row.append(str(_cron_n) if _cron_n else "—")
                elif _cid == "auto_rb":
                    _ar_on = config.auto_rollback and r[0] not in config.auto_rollback_disabled
                    _row.append("■" if _ar_on else "□")
                elif _cid == "img_exp":
                    _ie_on = config.image_export_enabled and r[0] not in config.image_export_disabled
                    _row.append("■" if _ie_on else "□")
                elif _cid == "vol_bak":
                    _vb_on = (config.volume_backup_enabled and
                              config.volume_backup.get(r[0], {}).get("enabled", True))
                    _row.append("■" if _vb_on else "□")
                elif _cid == "uptime":
                    _row.append(r[9])
                elif _cid == "restarts":
                    _row.append(r[10])
                elif _cid == "ports":
                    _row.append(r[11])
                elif _cid == "network":
                    _row.append(r[12])
                elif _cid == "compose":
                    _row.append(r[13])
                else:
                    _row.append("")
            _tbl_rows.append(tuple(_row))
        if config.pagination_enabled:
            try:
                _term_lines = os.get_terminal_size().lines
            except OSError:
                _term_lines = 40
            _page_size = max(5, _term_lines // 4)
            _pages = [_tbl_rows[i:i + _page_size] for i in range(0, len(_tbl_rows), _page_size)]
            for _pi, _page_rows in enumerate(_pages):
                _print_table(_tbl_headers, _page_rows, max_widths=_tbl_max_widths)
                if _pi < len(_pages) - 1:
                    print(f"\n  -- page {_pi + 1} of {len(_pages)}, press any key for next --", end="", flush=True)
                    _getchar()
                    print()
                    print()
        else:
            _print_table(_tbl_headers, _tbl_rows, max_widths=_tbl_max_widths)
        print()
        n = len(results)
        while True:
            try:
                raw = input(f"Select container [1-{n}], u=update all, s=settings, f=files, r=reload, q=quit: ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                print("\nGoodbye.")
                return
            if raw in ("q", "quit", "exit"):
                return
            if raw in ("u", "update all", "update"):
                _batch_update(config, docker, registry, sm, results)
                break
            if raw in ("s", "settings"):
                _exclude_before = list(config.exclude)
                config, enc = _interactive_settings(config, enc)
                sm = SnapshotManager(config)
                if config.exclude != _exclude_before:
                    _should_refetch = True
                break
            if raw in ("f", "files"):
                config, enc = _interactive_file_manager(config, enc)
                sm = SnapshotManager(config)
                break
            if raw in ("r", "reload"):
                _should_refetch = True
                break
            if not raw or not raw.isdigit() or not (1 <= int(raw) <= n):
                print("Invalid choice.")
                continue
            if _action_menu(config, docker, registry, sm, results[int(raw) - 1], enc):
                _should_refetch = True
            break


def cmd_config(args: argparse.Namespace) -> None:
    editors = list(filter(None, [
        os.environ.get("VISUAL"),
        os.environ.get("EDITOR"),
        "nano", "vi", "vim",
    ]))
    editor = next((e for e in editors if shutil.which(e)), None)
    if not editor:
        print("No editor found. Set the $EDITOR environment variable.", file=sys.stderr)
        sys.exit(1)

    config_path = args.config._path
    backup = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="wb", suffix=".json.bak", delete=False
        ) as f:
            backup = Path(f.name)
            f.write(config_path.read_bytes())

        while True:
            subprocess.run([editor, str(config_path)])
            try:
                Config.load(config_path)
                break  # valid
            except Exception as e:
                print(f"\nConfig validation failed: {e}")
                print("  r  Re-open editor")
                print("  b  Restore backup (discard edits)")
                print("  q  Quit without restoring")
                try:
                    choice = input("[r/b/q]: ").strip().lower()
                except (EOFError, KeyboardInterrupt):
                    choice = "q"
                if choice == "r":
                    continue
                if choice == "b":
                    shutil.copy2(backup, config_path)
                    print("Backup restored.")
                break  # q or b — exit loop
    finally:
        if backup and backup.exists():
            backup.unlink()


def cmd_pin(args: argparse.Namespace) -> None:
    config = args.config
    container = args.container
    if args.tag:
        config.pinned_tags[container] = args.tag
        config.save()
        print(f"Pinned {container} to {args.tag}.")
    else:
        pin = config.pinned_tags.get(container)
        if pin:
            print(f"{container} is pinned to: {pin}")
        else:
            print(f"{container} has no version pin.")


def cmd_unpin(args: argparse.Namespace) -> None:
    config = args.config
    container = args.container
    if container in config.pinned_tags:
        config.pinned_tags.pop(container)
        config.save()
        print(f"Version pin cleared for {container}.")
    else:
        print(f"{container} has no version pin.")


def cmd_image_export(args: argparse.Namespace) -> None:
    config = args.config
    action = args.action
    container = getattr(args, "container", None)

    if action == "status":
        state = "ON" if config.image_export_enabled else "OFF"
        print(f"Image export globally: {state}")
        if config.image_export_disabled:
            print(f"Disabled for: {', '.join(sorted(config.image_export_disabled))}")
        else:
            print("No per-container opt-outs.")
        return

    if action == "enable":
        if container:
            if container in config.image_export_disabled:
                config.image_export_disabled.remove(container)
                config.save()
                print(f"Image export re-enabled for {container}.")
            else:
                print(f"Image export is already enabled for {container}.")
        else:
            config.image_export_enabled = True
            config.save()
            print("Image export enabled globally.")

    elif action == "disable":
        if container:
            if container not in config.image_export_disabled:
                config.image_export_disabled.append(container)
                config.save()
                print(f"Image export disabled for {container}.")
            else:
                print(f"Image export is already disabled for {container}.")
        else:
            config.image_export_enabled = False
            config.save()
            print("Image export disabled globally.")


def cmd_cron(args: argparse.Namespace) -> None:
    config = args.config
    action = getattr(args, "cron_action", None)

    if not action or action == "status":
        rows = _cron_status(config)
        if not rows:
            print("No scheduled jobs configured.")
            print("Use 'update_zen cron add <container> <recipe>' to add one.")
            return
        drift = any(r["enabled"] and not r["applied"] for r in rows)
        table_rows = []
        for r in rows:
            enabled_s = "yes" if r["enabled"] else "no"
            if r["enabled"] and not r["applied"]:
                applied_s = "NO (drift)"
            elif r["applied"]:
                applied_s = "yes"
            else:
                applied_s = "no"
            table_rows.append((r["container"], r["recipe"], r["schedule"],
                                enabled_s, applied_s))
        _print_table(
            ["CONTAINER", "RECIPE", "SCHEDULE", "ENABLED", "APPLIED"],
            table_rows,
        )
        if drift:
            print("\n  ! Drift detected — run 'update_zen cron apply' to fix.")
        return

    if action == "apply":
        container = getattr(args, "container", None)
        try:
            changes = _cron_apply(config, container)
        except RuntimeError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
        if not changes:
            print("Nothing to apply.")
        else:
            for line in changes:
                print(line)
        return

    if action == "recipes":
        print()
        for name, rec in _CRON_RECIPES.items():
            print(f"  {name}")
            print(f"      {rec['description']}")
            print(f"      Default schedule : {rec['default_schedule']}")
            print(f"      Command          : {rec['command']}")
            print()
        return

    if action == "add":
        container = args.container
        recipe    = args.recipe
        schedule  = args.schedule.strip() if args.schedule else ""
        mount     = getattr(args, "mount", None) or ""

        if not _cron_validate_container_name(container):
            print(f"Invalid container name '{container}'. "
                  "Container names must match [a-zA-Z0-9][a-zA-Z0-9_.-]*",
                  file=sys.stderr)
            sys.exit(1)

        rec = _CRON_RECIPES.get(recipe)
        if rec is None:
            print(f"Unknown recipe '{recipe}'. Available recipes:", file=sys.stderr)
            for name in _CRON_RECIPES:
                print(f"  {name}", file=sys.stderr)
            sys.exit(1)

        if rec.get("requires_mount") and not mount:
            print(f"Recipe '{recipe}' requires --mount PATH.", file=sys.stderr)
            sys.exit(1)

        if not schedule:
            schedule = rec["default_schedule"]
        elif not _cron_validate_schedule(schedule):
            print(f"Invalid cron schedule '{schedule}'. "
                  "Must be 5 space-separated fields (e.g. '0 3 * * *').", file=sys.stderr)
            sys.exit(1)

        existing = config.cron_jobs.get(container, [])
        if any(j.get("recipe") == recipe and j.get("mount", "") == mount for j in existing):
            dup_key = f"{recipe} --mount {mount}" if mount else recipe
            print(f"Job '{dup_key}' already exists for {container}. "
                  "Use 'cron enable/disable' to toggle it.", file=sys.stderr)
            sys.exit(1)

        jobs = list(existing)
        entry: dict = {"recipe": recipe, "schedule": schedule, "enabled": True}
        if mount:
            entry["mount"] = mount
        jobs.append(entry)
        config.cron_jobs[container] = jobs
        config.save()

        if config.is_encryption_enabled(container):
            print(
                f"Warning: {container} has snapshot encryption enabled.\n"
                "  The cron job was saved but has no standalone cron config.\n"
                "  Open the container cron menu in the TUI to generate one,\n"
                "  or the job will fail to read saved passwords at runtime."
            )

        try:
            changes = _cron_apply(config, container)
        except RuntimeError as e:
            print(f"Saved to config but crontab apply failed: {e}", file=sys.stderr)
            sys.exit(1)
        for line in changes:
            print(line)
        return

    if action == "remove":
        container = args.container
        recipe    = args.recipe

        jobs = config.cron_jobs.get(container, [])
        idx = next((i for i, j in enumerate(jobs) if j.get("recipe") == recipe), -1)
        if idx == -1:
            print(f"No job '{recipe}' found for {container}.", file=sys.stderr)
            sys.exit(1)

        # Strip from crontab before removing from config
        try:
            content = _crontab_read()
            content = _crontab_remove(content, container, recipe)
            _crontab_write(content)
        except RuntimeError as e:
            print(f"Warning: crontab update failed: {e}", file=sys.stderr)

        new_jobs = [j for j in jobs if j.get("recipe") != recipe]
        if new_jobs:
            config.cron_jobs[container] = new_jobs
        else:
            config.cron_jobs.pop(container, None)
        config.save()
        print(f"  removed  {container}:{recipe}")
        return

    if action in ("enable", "disable"):
        container = args.container
        recipe    = args.recipe
        enable    = (action == "enable")

        jobs = config.cron_jobs.get(container, [])
        idx = next((i for i, j in enumerate(jobs) if j.get("recipe") == recipe), -1)
        if idx == -1:
            print(f"No job '{recipe}' found for {container}. "
                  "Use 'cron add' first.", file=sys.stderr)
            sys.exit(1)

        if jobs[idx].get("enabled") == enable:
            state = "enabled" if enable else "disabled"
            print(f"Job '{recipe}' for {container} is already {state}.")
            return

        jobs[idx]["enabled"] = enable
        config.cron_jobs[container] = jobs
        config.save()

        try:
            changes = _cron_apply(config, container)
        except RuntimeError as e:
            print(f"Saved to config but crontab apply failed: {e}", file=sys.stderr)
            sys.exit(1)
        for line in changes:
            print(line)
        return


def _enc_snapshot_dirs(config: Config) -> set:
    dirs: set = {config.snapshot_dir}
    for p in config.snapshot_dir_overrides.values():
        dirs.add(Path(p))
    for rules in config.volume_backup.values():
        if rules.get("save_path"):
            dirs.add(Path(rules["save_path"]))
        for mp in rules.get("mount_paths", {}).values():
            dirs.add(Path(mp))
    return dirs


def _fmt_bytes(n: int) -> str:
    if n >= 1_073_741_824:
        return f"{n / 1_073_741_824:.1f} GB"
    if n >= 1_048_576:
        return f"{n / 1_048_576:.1f} MB"
    if n >= 1024:
        return f"{n / 1024:.1f} KB"
    return f"{n} B"


def _collect_orphans(config: "Config", container: "str | None" = None) -> list:
    """Scan all snapshot dirs for orphaned _staging_* dirs and *.tmp files."""
    def _dir_size(p: Path) -> int:
        total = 0
        try:
            for f in p.rglob("*"):
                if f.is_file():
                    try:
                        total += f.stat().st_size
                    except OSError:
                        pass
        except OSError:
            pass
        return total

    orphans = []
    for base_dir in _enc_snapshot_dirs(config):
        if not base_dir.exists():
            continue
        try:
            subdirs = [d for d in base_dir.iterdir() if d.is_dir()]
        except OSError:
            continue
        for container_dir in subdirs:
            ctr_name = container_dir.name
            if container and ctr_name != container:
                continue
            try:
                entries = list(container_dir.iterdir())
            except OSError:
                continue
            for entry in entries:
                if entry.is_dir() and entry.name.startswith("_staging_"):
                    orphans.append({
                        "type": "staging",
                        "path": entry,
                        "size_bytes": _dir_size(entry),
                        "container": ctr_name,
                    })
                elif entry.is_file() and entry.name.endswith(".tmp"):
                    try:
                        size = entry.stat().st_size
                    except OSError:
                        size = 0
                    orphans.append({
                        "type": "tmp",
                        "path": entry,
                        "size_bytes": size,
                        "container": ctr_name,
                    })
    return orphans


def _rekey_bundle(path: Path, old_pw: str, new_pw: str, enc: "EncryptionManager") -> bool:
    """Re-encrypt text members of a .tar.gz main bundle from old_pw to new_pw.

    Binary members (_image.tar, etc.) are copied unchanged. Returns True if any
    member was changed. Raises on crypto errors (wrong password, corrupt data).
    """
    tmp_path = path.with_suffix(".rekey_tmp")
    changed = False
    try:
        with tarfile.open(path, "r:gz") as src, \
             tarfile.open(tmp_path, "w:gz", compresslevel=1) as dst:
            for member in src:
                if not member.isfile():
                    continue
                name = member.name
                data = src.extractfile(member).read()
                if (name.endswith(".json") or name.endswith(".yaml")
                        or name.endswith(".env")) and enc.is_encrypted(data):
                    data = enc.decrypt_bytes(data, old_pw)
                    data = enc.encrypt_bytes(data, new_pw)
                    changed = True
                info = tarfile.TarInfo(name=name)
                info.size = len(data)
                dst.addfile(info, io.BytesIO(data))
        if changed:
            tmp_path.rename(path)
        else:
            tmp_path.unlink()
    except Exception:
        tmp_path.unlink(missing_ok=True)
        raise
    return changed


def _rekey_volume_archive(path: Path, old_pw: str, new_pw: str,
                          enc: "EncryptionManager") -> None:
    """Decrypt an RBPE volume archive with old_pw and re-encrypt it with new_pw, in place."""
    dec_tmp = path.with_suffix(".dec_tmp")
    new_tmp = path.with_suffix(".new_tmp")
    try:
        enc.decrypt_file(path, dec_tmp, old_pw)
        enc.encrypt_file(dec_tmp, new_tmp, new_pw)
        new_tmp.rename(path)
    finally:
        dec_tmp.unlink(missing_ok=True)
        new_tmp.unlink(missing_ok=True)


def cmd_encrypt(args: argparse.Namespace) -> None:
    config = args.config
    action = args.action
    enc = EncryptionManager(config)
    _ts_re = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}-\d{2}-\d{2}$")

    if action == "setup":
        container = args.container
        enc_cfg = config.encryption
        containers = list(enc_cfg.get("encrypt_containers", []))
        added_container = container not in containers
        if added_container:
            containers.append(container)
            enc_cfg["encrypt_containers"] = containers

        all_volumes = getattr(args, "all_volumes", False)
        volumes = list(getattr(args, "volume", None) or [])

        if all_volumes:
            vol_map = dict(enc_cfg.get("encrypt_volumes", {}))
            vol_map[container] = ["all"]
            enc_cfg["encrypt_volumes"] = vol_map
            config.save()
            if added_container:
                print(f"Encryption enabled for {container} (snapshots + all volumes).")
            else:
                print(f"Volume encryption set to all mounts for {container}.")
        elif volumes:
            vol_map = dict(enc_cfg.get("encrypt_volumes", {}))
            existing = list(vol_map.get(container, []))
            added_vols = [v for v in volumes if v not in existing]
            existing.extend(added_vols)
            vol_map[container] = existing
            enc_cfg["encrypt_volumes"] = vol_map
            config.save()
            if added_container:
                print(f"Encryption enabled for {container}.")
            if added_vols:
                print(f"  Added to volume encrypt list: {', '.join(added_vols)}")
            elif not added_container:
                print(f"No changes — {container} already configured with those volumes.")
        else:
            if added_container:
                config.save()
                print(f"Encryption enabled for {container} (snapshots only).")
                print(f"  Use --all-volumes or --volume /path to also encrypt volume archives.")
                print(f"  Use 'encrypt password set {container}' to pre-save the password.")
            else:
                print(f"{container} is already in the encryption list.")

    elif action == "remove":
        container = args.container
        enc_cfg = config.encryption
        volume = getattr(args, "volume", None)

        if volume:
            vol_map = dict(enc_cfg.get("encrypt_volumes", {}))
            existing = list(vol_map.get(container, []))
            if volume in existing:
                existing.remove(volume)
                if existing:
                    vol_map[container] = existing
                else:
                    vol_map.pop(container, None)
                enc_cfg["encrypt_volumes"] = vol_map
                config.save()
                print(f"Removed volume {volume} from encryption for {container}.")
            else:
                print(f"{volume} is not in the encryption list for {container}.")
        else:
            containers = list(enc_cfg.get("encrypt_containers", []))
            if container in containers:
                containers.remove(container)
                enc_cfg["encrypt_containers"] = containers
                vol_map = dict(enc_cfg.get("encrypt_volumes", {}))
                if container in vol_map:
                    vol_map.pop(container)
                    enc_cfg["encrypt_volumes"] = vol_map
                config.save()
                print(f"Encryption disabled for {container}.")
            else:
                print(f"{container} is not in the encryption list.")

    elif action == "password":
        import getpass as _gp
        sub = args.password_action
        if sub == "set":
            container = args.container
            volume = getattr(args, "volume", None)
            label = f"{container}::{volume}" if volume else container
            if not sys.stdin.isatty():
                print("Error: stdin is not a TTY — cannot prompt for password.", file=sys.stderr)
                sys.exit(1)
            try:
                pw = _gp.getpass(f"Password for {label}: ")
            except (EOFError, KeyboardInterrupt):
                print()
                sys.exit(0)
            if not pw:
                print("Error: password cannot be empty.", file=sys.stderr)
                sys.exit(1)
            config.set_saved_password(container, pw, volume)
            print(f"Password saved for {label}.")

        elif sub == "delete":
            container = args.container
            volume = getattr(args, "volume", None)
            key = f"{container}::{volume}" if volume else container
            saved = config.encryption.get("saved_passwords", {})
            if key in saved:
                saved.pop(key)
                config.save()
                print(f"Saved password for {key} deleted.")
            else:
                print(f"No saved password found for {key}.")

        elif sub == "purge":
            target = getattr(args, "purge_container", None)
            count = config.purge_saved_passwords(target)
            if target:
                print(f"Purged {count} saved password(s) for {target}.")
            else:
                print(f"Purged {count} saved password(s).")

    elif action == "status":
        enc_cfg = config.encryption
        mode = enc_cfg.get("mode", "session")
        containers = list(enc_cfg.get("encrypt_containers", []))
        vol_map = enc_cfg.get("encrypt_volumes", {})
        saved_pws = enc_cfg.get("saved_passwords", {})

        print(f"Password mode   : {mode}")
        print(f"Saved passwords : {len(saved_pws)}")

        if not containers:
            print("\nNo containers have encryption enabled.")
            print("Use 'update_zen encrypt setup <container>' to enable encryption.")
            return

        print(f"\nEncrypted containers ({len(containers)}):")
        rows = []
        for c in sorted(containers):
            vol_cfg = vol_map.get(c, [])
            if not vol_cfg:
                vol_label = "snapshots only"
            elif "all" in vol_cfg:
                vol_label = "all volumes"
            else:
                vol_label = ", ".join(vol_cfg)
            pw_count = sum(1 for k in saved_pws if k == c or k.startswith(f"{c}::"))
            rows.append((c, vol_label, str(pw_count) if pw_count else "—"))
        _print_table(["CONTAINER", "VOLUMES", "SAVED PW"], rows)

    elif action == "rotate":
        container = args.container
        if not config.is_encryption_enabled(container):
            print(f"Error: encryption is not enabled for '{container}'.", file=sys.stderr)
            sys.exit(1)
        if not sys.stdin.isatty():
            print("Error: stdin is not a TTY — cannot prompt for password.", file=sys.stderr)
            sys.exit(1)
        import getpass
        from cryptography.exceptions import InvalidTag

        try:
            old_password = getpass.getpass(f"Current encryption password for {container}: ")
        except (EOFError, KeyboardInterrupt):
            print()
            sys.exit(0)
        if not old_password:
            print("Error: password cannot be empty.", file=sys.stderr)
            sys.exit(1)

        try:
            found = _verify_enc_password_for(config, container, old_password)
        except InvalidTag:
            print("Error: incorrect password.", file=sys.stderr)
            sys.exit(1)
        if not found:
            print("No encrypted files found for this container — password accepted without verification.")

        try:
            new_password = getpass.getpass("New encryption password: ")
        except (EOFError, KeyboardInterrupt):
            print()
            sys.exit(0)
        if not new_password:
            print("Error: password cannot be empty.", file=sys.stderr)
            sys.exit(1)
        try:
            confirm = getpass.getpass("Confirm new password: ")
        except (EOFError, KeyboardInterrupt):
            print()
            sys.exit(0)
        if new_password != confirm:
            print("Error: passwords do not match.", file=sys.stderr)
            sys.exit(1)

        enc_rk = EncryptionManager(config)
        container_dir = config.snapshot_dir_for(container) / container
        bundle_done = vol_done = 0
        include_archives = getattr(args, "include_archives", False)

        if container_dir.exists():
            for path in sorted(container_dir.glob("*.tar.gz")):
                sid = path.name.removesuffix(".tar.gz")
                if _ts_re.match(sid):
                    try:
                        if _rekey_bundle(path, old_password, new_password, enc_rk):
                            bundle_done += 1
                    except Exception as e:
                        log(f"[rotate] failed to rekey {path.name}: {e}")
                elif include_archives and _is_encrypted_file(path):
                    try:
                        _rekey_volume_archive(path, old_password, new_password, enc_rk)
                        vol_done += 1
                    except Exception as e:
                        log(f"[rotate] failed to rekey volume archive {path.name}: {e}")

        new_mode = getattr(args, "mode", None) or config.encryption.get("mode", "session")
        config.encryption["mode"] = new_mode
        if config.get_saved_password(container):
            config.set_saved_password(container, new_password)
        config.save()

        print(f"Password rotated for '{container}'.")
        print(f"  Bundles re-keyed:         {bundle_done}")
        if include_archives:
            print(f"  Volume archives re-keyed: {vol_done}")
        else:
            print("  Volume archives: skipped (pass --include-archives to rekey).")

    elif action == "disable":
        container = args.container
        if not config.is_encryption_enabled(container):
            print(f"Error: encryption is not enabled for '{container}'.", file=sys.stderr)
            sys.exit(1)
        if not sys.stdin.isatty():
            print("Error: stdin is not a TTY — cannot prompt for password.", file=sys.stderr)
            sys.exit(1)
        import getpass
        from cryptography.exceptions import InvalidTag

        try:
            password = getpass.getpass(f"Encryption password for {container}: ")
        except (EOFError, KeyboardInterrupt):
            print()
            sys.exit(0)
        if not password:
            print("Error: password cannot be empty.", file=sys.stderr)
            sys.exit(1)

        try:
            found = _verify_enc_password_for(config, container, password)
        except InvalidTag:
            print("Error: incorrect password.", file=sys.stderr)
            sys.exit(1)
        if not found:
            print("No encrypted files found for this container — disabling without decryption.")

        enc_dis = EncryptionManager(config)
        container_dir = config.snapshot_dir_for(container) / container
        bundle_done = vol_done = 0

        if container_dir.exists():
            for path in sorted(container_dir.glob("*.tar.gz")):
                sid = path.name.removesuffix(".tar.gz")
                if _ts_re.match(sid):
                    # Main bundle: rebundle with text members decrypted
                    tmp_path = path.with_suffix(".rebundle_tmp")
                    bundle_changed = False
                    try:
                        with tarfile.open(path, "r:gz") as src, \
                             tarfile.open(tmp_path, "w:gz", compresslevel=1) as dst:
                            for member in src:
                                if not member.isfile():
                                    continue
                                name = member.name
                                data = src.extractfile(member).read()
                                if (name.endswith(".json") or name.endswith(".yaml")
                                        or name.endswith(".env")) \
                                        and enc_dis.is_encrypted(data):
                                    data = enc_dis.decrypt_bytes(data, password)
                                    bundle_changed = True
                                info = tarfile.TarInfo(name=name)
                                info.size = len(data)
                                dst.addfile(info, io.BytesIO(data))
                        if bundle_changed:
                            tmp_path.rename(path)
                            bundle_done += 1
                        else:
                            tmp_path.unlink()
                    except Exception as e:
                        tmp_path.unlink(missing_ok=True)
                        log(f"[disable] failed to rebundle {path.name}: {e}")
                elif _is_encrypted_file(path):
                    # Per-mount volume archive: decrypt RBPE in-place
                    dec_tmp = path.with_suffix(".dec_tmp")
                    try:
                        enc_dis.decrypt_file(path, dec_tmp, password)
                        dec_tmp.rename(path)
                        vol_done += 1
                    except Exception as e:
                        dec_tmp.unlink(missing_ok=True)
                        log(f"[disable] failed to decrypt {path.name}: {e}")

        # Remove container from encryption config and purge saved passwords
        enc_containers = list(config.encryption.get("encrypt_containers", []))
        if container in enc_containers:
            enc_containers.remove(container)
        config.encryption["encrypt_containers"] = enc_containers
        vol_map = dict(config.encryption.get("encrypt_volumes", {}))
        vol_map.pop(container, None)
        if vol_map:
            config.encryption["encrypt_volumes"] = vol_map
        else:
            config.encryption.pop("encrypt_volumes", None)
        config.purge_saved_passwords(container)
        config.save()

        print(f"Encryption disabled for '{container}'.")
        print(f"  Bundles decrypted:         {bundle_done}")
        print(f"  Volume archives decrypted: {vol_done}")


def cmd_install(args: argparse.Namespace) -> None:
    script_path = Path(__file__).resolve()
    wrapper = Path("/usr/local/bin/update_zen")
    sudoers_file = Path("/etc/sudoers.d/update_zen")

    wrapper.write_text(
        "#!/bin/bash\n"
        f'[ "$(id -u)" -ne 0 ] && exec sudo {wrapper} "$@"\n'
        f'exec {sys.executable} {script_path} "$@"\n'
    )
    wrapper.chmod(0o755)
    log(f"Installed wrapper → {wrapper}")

    invoking_user = os.environ.get("SUDO_USER")
    if invoking_user:
        sudoers_file.write_text(
            f"{invoking_user} ALL=(ALL) NOPASSWD: {wrapper}\n"
        )
        sudoers_file.chmod(0o440)
        log(f"Added NOPASSWD rule for {invoking_user} → {sudoers_file}")
    else:
        log("Warning: NOPASSWD rule not added — run install as a regular user, not directly as root.")

    try:
        result = subprocess.run(
            ["apt-get", "install", "-y", "python3-cryptography"],
            capture_output=True, text=True,
        )
        if result.returncode == 0:
            log("Installed python3-cryptography")
        else:
            log("Warning: could not install python3-cryptography — install manually if you plan to use encryption.")
    except FileNotFoundError:
        log("Warning: apt-get not found — install python3-cryptography manually if you plan to use encryption.")

    log("Install complete — 'update_zen' now runs without sudo or a password prompt.")


# === CLI ===

def main() -> None:
    # Auto-elevate — all operations need root-level Docker access.
    if os.getuid() != 0:
        try:
            os.execvp("sudo", ["sudo", sys.executable,
                                str(Path(__file__).resolve())] + sys.argv[1:])
        except FileNotFoundError:
            print("Error: sudo not found. Please run as root.", file=sys.stderr)
            sys.exit(1)

    # Restrict all file writes to owner-only from this point forward.
    os.umask(0o077)

    # Resolve config path before anything else so _ensure_dirs and Config.load
    # both use the same path. parse_known_args ignores unrecognised args (the
    # subcommand and its flags) so this mini-parse is safe to run before the
    # main argparse setup. sys.argv is preserved through execvp; env vars are not.
    _pre = argparse.ArgumentParser(add_help=False)
    _pre.add_argument("--config", dest="config_path", metavar="PATH", default=None)
    _pre_args, _remaining_argv = _pre.parse_known_args()
    _config_path = Path(_pre_args.config_path) if _pre_args.config_path else CONFIG_FILE

    try:
        _ensure_dirs(_config_path)
    except OSError as e:
        if _pre_args.config_path:
            _hint = f" (check --config {_pre_args.config_path!r})"
        elif os.environ.get("UPDATE_ZEN_CONFIG"):
            _hint = f" (check UPDATE_ZEN_CONFIG={os.environ['UPDATE_ZEN_CONFIG']!r})"
        else:
            _hint = ""
        print(f"Error: could not create required directories: {e}{_hint}", file=sys.stderr)
        sys.exit(1)

    global _master_password, _active_log_file
    if _config_path.exists():
        _raw_cfg = _config_path.read_bytes()
        if EncryptionManager(None).is_encrypted(_raw_cfg):
            if not sys.stdin.isatty():
                print(
                    "Error: config.json is encrypted; cannot prompt for master password "
                    "in non-TTY mode.",
                    file=sys.stderr,
                )
                print(
                    "  Use a per-job cron config (--config PATH) for automated invocations.",
                    file=sys.stderr,
                )
                sys.exit(1)
            _master_password = _prompt_master_password_startup(_config_path)

    config = Config.load(_config_path)
    _active_log_file = config.log_file
    if config.encryption.get("encrypt_containers"):
        try:
            import cryptography  # noqa: F401
        except ImportError:
            print(
                "Error: encryption is enabled in config but the 'cryptography' package is not installed.\n"
                "Run: sudo apt-get install -y python3-cryptography\n"
                "Or disable encryption: update_zen encrypt disable --container <name>",
                file=sys.stderr,
            )
            sys.exit(1)

    if not _remaining_argv:
        cmd_interactive(config)
        return

    if _pre_args.config_path:
        _cfg_source = "--config flag"
    elif os.environ.get("UPDATE_ZEN_CONFIG"):
        _cfg_source = "UPDATE_ZEN_CONFIG env var"
    else:
        _cfg_source = "default"
    log(f"Update Zen {_VERSION} | Config: {_config_path} ({_cfg_source})")

    parser = argparse.ArgumentParser(
        prog="update_zen",
        description="Docker container update manager with config snapshot rollback.",
    )
    parser.add_argument(
        "--config", metavar="PATH", default=None,
        help=(
            "Path to config.json. Overrides UPDATE_ZEN_CONFIG env var. "
            "Defaults to ~/.update_zen/config.json."
        ),
    )
    sub = parser.add_subparsers(dest="command", metavar="command")
    sub.required = True

    p_check = sub.add_parser("check", help="Scan containers for available image updates.")
    p_check.add_argument(
        "containers", nargs="*", metavar="container",
        help="Containers to check (default: all running).",
    )
    p_check.set_defaults(func=cmd_check)

    p_status = sub.add_parser("status", help="Show container state, digest, and snapshot count.")
    p_status.set_defaults(func=cmd_status)

    p_doctor = sub.add_parser("doctor", help="Validate config, paths, and permissions.")
    p_doctor.set_defaults(func=cmd_doctor)

    p_cleanup = sub.add_parser(
        "cleanup", help="Find and remove orphaned staging dirs and temp files.",
    )
    p_cleanup.add_argument(
        "--yes", action="store_true",
        help="Delete found artifacts after confirmation prompt (default: dry run).",
    )
    p_cleanup.add_argument(
        "--container", metavar="NAME", default=None,
        help="Limit scan to one container's directories.",
    )
    p_cleanup.set_defaults(func=cmd_cleanup)

    p_convert = sub.add_parser(
        "convert-snapshots",
        help="Migrate legacy .json-format snapshots to .tar.gz bundles.",
    )
    p_convert.add_argument(
        "--container", metavar="NAME", default=None,
        help="Limit conversion to one container.",
    )
    p_convert.add_argument(
        "--dry-run", dest="dry_run", action="store_true",
        help="Print what would be converted without touching files.",
    )
    p_convert.set_defaults(func=cmd_convert_snapshots)

    p_tags = sub.add_parser("tags", help="List available image tags for a container.")
    p_tags.add_argument("container", help="Container name.")
    p_tags.set_defaults(func=cmd_tags)

    p_update = sub.add_parser("update", help="Pull latest image and recreate a container.")
    p_update.add_argument("container", help="Container to update.")
    p_update.add_argument(
        "--no-auto-rollback", dest="auto_rollback", action="store_false", default=True,
        help="Do not roll back automatically if the update fails the health check.",
    )
    p_update.add_argument(
        "--compose", action="store_true", default=False,
        help=(
            "Update via 'docker compose up --force-recreate' instead of "
            "stop/rm/run.  Required for stacks where containers share a "
            "network namespace (e.g. Gluetun-routed stacks).  The container "
            "must have Compose labels (created by 'docker compose up')."
        ),
    )
    p_update.add_argument(
        "--tag", default="",
        help=(
            "Pull and deploy a specific image tag instead of the current one. "
            "Use 'update_zen tags <container>' to see available tags. "
            "Ignored when --compose is used."
        ),
    )
    p_update.set_defaults(func=cmd_update)

    p_rollback = sub.add_parser("rollback", help="Recreate a container from a saved snapshot.")
    p_rollback.add_argument("container", help="Container to roll back.")
    p_rollback.add_argument(
        "--snap", type=int, choices=[1, 2, 3], metavar="N",
        help="Snapshot index to restore (1=newest). Prompts interactively if omitted.",
    )
    p_rollback.set_defaults(func=cmd_rollback)

    p_list = sub.add_parser("list-snaps", help="List saved snapshots for a container.")
    p_list.add_argument("container", help="Container name.")
    p_list.set_defaults(func=cmd_list_snaps)

    p_snap = sub.add_parser("snapshot", help="Take a snapshot of a container without updating it.")
    p_snap.add_argument("container", help="Container name.")
    p_snap.set_defaults(func=cmd_snapshot)

    p_rv = sub.add_parser(
        "restore-volume",
        help="Restore an individual volume mount from a snapshot archive.",
    )
    p_rv.add_argument("container", help="Container name.")
    p_rv.add_argument(
        "snapshot_id", nargs="?", default=None,
        help="Snapshot ID (timestamp string). Prompts interactively if omitted.",
    )
    p_rv.set_defaults(func=cmd_restore_volume)

    p_volumes = sub.add_parser(
        "volumes", help="View and manage volume backup settings.",
    )
    volumes_sub = p_volumes.add_subparsers(dest="volumes_action")
    volumes_sub.required = False

    p_vshow = volumes_sub.add_parser("show", help="Show bind mounts and backup rules for a container.")
    p_vshow.add_argument("container", help="Container name.")
    p_vshow.set_defaults(func=cmd_volumes)

    p_vset = volumes_sub.add_parser("set", help="Modify backup rules for a container's volumes.")
    p_vset.add_argument("container", help="Container name.")
    p_vset.add_argument(
        "--skip", metavar="PATH", action="append", default=[],
        help="Add a container path to skip_mounts (repeatable).",
    )
    p_vset.add_argument(
        "--unskip", metavar="PATH", action="append", default=[],
        help="Remove a container path from skip_mounts.",
    )
    p_vset.add_argument(
        "--only", metavar="PATH", action="append", default=[],
        help="Replace include_only_mounts with these paths (repeatable).",
    )
    p_vset.add_argument(
        "--no-only", dest="clear_only", action="store_true",
        help="Clear include_only_mounts so all mounts are backed up.",
    )
    p_vset.add_argument(
        "--exclude", metavar="PATTERN", action="append", default=[],
        help="Add a glob pattern to exclude from archives (repeatable).",
    )
    p_vset.add_argument(
        "--no-exclude", metavar="PATTERN", dest="no_exclude",
        action="append", default=[],
        help="Remove a glob pattern from the exclude list.",
    )
    p_vset.add_argument(
        "--mount-path", metavar=("CONTAINER_PATH", "ARCHIVE_DIR"),
        nargs=2, action="append", default=[],
        help=(
            "Set a custom archive directory for a specific container path. "
            "Repeatable. Example: --mount-path /app/config /mnt/nas/plex-config"
        ),
    )
    p_vset.add_argument(
        "--no-mount-path", metavar="CONTAINER_PATH", dest="no_mount_path",
        action="append", default=[],
        help="Remove the custom archive directory for a container path.",
    )
    p_vset.add_argument(
        "--save-path", metavar="DIR", dest="save_path",
        help=(
            "Set a custom archive directory for this container's combined volume backup. "
            "Individual mounts can still override this via --mount-path."
        ),
    )
    p_vset.add_argument(
        "--no-save-path", dest="no_save_path", action="store_true",
        help="Clear the container-level save path (reverts to global snapshot_dir).",
    )
    p_vset.add_argument(
        "--encrypt", metavar="PATH", dest="encrypt_vol",
        action="append", default=[],
        help="Add a container mount path to the volume encryption list (repeatable).",
    )
    p_vset.add_argument(
        "--no-encrypt", metavar="PATH", dest="no_encrypt_vol",
        action="append", default=[],
        help="Remove a container mount path from the volume encryption list (repeatable).",
    )
    p_vset.add_argument(
        "--reset", action="store_true",
        help="Remove all backup rules for this container.",
    )
    vset_toggle = p_vset.add_mutually_exclusive_group()
    vset_toggle.add_argument(
        "--disable", action="store_true",
        help="Disable volume backup for this container.",
    )
    vset_toggle.add_argument(
        "--enable", action="store_true",
        help="Re-enable volume backup for this container.",
    )
    p_vset.set_defaults(func=cmd_volumes_set)

    p_vbackup = volumes_sub.add_parser("backup", help="Back up volumes for a container now.")
    p_vbackup.add_argument("container", help="Container name.")
    p_vbackup.add_argument(
        "--mount", metavar="PATH", default=None,
        help="Back up only this specific container mount path.",
    )
    p_vbackup.set_defaults(func=cmd_volumes_backup)

    p_volumes.set_defaults(func=cmd_volumes, volumes_action=None)

    p_pin = sub.add_parser("pin", help="Pin a container to a specific image tag.")
    p_pin.add_argument("container", help="Container name.")
    p_pin.add_argument("tag", nargs="?", default="",
        help="Tag to pin to (e.g. '4.0.2'). Omit to show current pin.")
    p_pin.set_defaults(func=cmd_pin)

    p_unpin = sub.add_parser("unpin", help="Clear the version pin for a container.")
    p_unpin.add_argument("container", help="Container name.")
    p_unpin.set_defaults(func=cmd_unpin)

    p_ie = sub.add_parser(
        "image-export",
        help="Manage image export (pre-update docker save). Enabled by default.",
    )
    p_ie_sub = p_ie.add_subparsers(dest="action")
    p_ie_sub.required = True

    p_ie_status = p_ie_sub.add_parser("status", help="Show image export settings.")
    p_ie_status.set_defaults(func=cmd_image_export)

    p_ie_enable = p_ie_sub.add_parser(
        "enable", help="Enable image export globally, or for one container.")
    p_ie_enable.add_argument("container", nargs="?", default=None,
        help="Container to opt back in (omit to enable globally).")
    p_ie_enable.set_defaults(func=cmd_image_export)

    p_ie_disable = p_ie_sub.add_parser(
        "disable", help="Disable image export globally, or for one container.")
    p_ie_disable.add_argument("container", nargs="?", default=None,
        help="Container to opt out (omit to disable globally).")
    p_ie_disable.set_defaults(func=cmd_image_export)

    p_cron = sub.add_parser("cron", help="Manage scheduled jobs (cron recipes).")
    p_cron_sub = p_cron.add_subparsers(dest="cron_action", metavar="action")

    p_cron_status = p_cron_sub.add_parser("status", help="Show all configured jobs and crontab state.")
    p_cron_status.set_defaults(func=cmd_cron)

    p_cron_apply = p_cron_sub.add_parser(
        "apply", help="Sync config → crontab (idempotent). Enables/disables entries to match config.")
    p_cron_apply.add_argument(
        "container", nargs="?", default=None,
        help="Apply jobs for one container only (default: all).")
    p_cron_apply.set_defaults(func=cmd_cron)

    p_cron_recipes = p_cron_sub.add_parser("recipes", help="List available job recipe templates.")
    p_cron_recipes.set_defaults(func=cmd_cron)

    p_cron_add = p_cron_sub.add_parser("add", help="Add a scheduled job for a container.")
    p_cron_add.add_argument("container", help="Container name.")
    p_cron_add.add_argument("recipe", help="Recipe name (see 'cron recipes').")
    p_cron_add.add_argument(
        "--schedule", default="",
        help="Custom cron expression (default: recipe default).")
    p_cron_add.add_argument(
        "--mount", metavar="PATH", default=None,
        help="Container mount path (required for mount_volume_backup recipe).")
    p_cron_add.set_defaults(func=cmd_cron)

    p_cron_remove = p_cron_sub.add_parser(
        "remove", help="Remove a scheduled job from config and crontab.")
    p_cron_remove.add_argument("container", help="Container name.")
    p_cron_remove.add_argument("recipe", help="Recipe name.")
    p_cron_remove.set_defaults(func=cmd_cron)

    p_cron_enable = p_cron_sub.add_parser(
        "enable", help="Enable a job (apply to crontab).")
    p_cron_enable.add_argument("container", help="Container name.")
    p_cron_enable.add_argument("recipe", help="Recipe name.")
    p_cron_enable.set_defaults(func=cmd_cron)

    p_cron_disable = p_cron_sub.add_parser(
        "disable", help="Disable a job (remove from crontab, keep in config).")
    p_cron_disable.add_argument("container", help="Container name.")
    p_cron_disable.add_argument("recipe", help="Recipe name.")
    p_cron_disable.set_defaults(func=cmd_cron)

    p_cron.set_defaults(func=cmd_cron, cron_action=None)

    p_encrypt = sub.add_parser("encrypt", help="Manage snapshot encryption.")
    p_enc_sub = p_encrypt.add_subparsers(dest="action", metavar="action")
    p_enc_sub.required = True

    p_enc_setup = p_enc_sub.add_parser("setup", help="Enable encryption for a container.")
    p_enc_setup.add_argument("container", help="Container name to enable encryption for.")
    p_enc_setup.add_argument(
        "--volume", metavar="PATH", action="append", default=[],
        help="Also encrypt this volume mount path (repeatable).",
    )
    p_enc_setup.add_argument(
        "--all-volumes", dest="all_volumes", action="store_true",
        help="Encrypt all volume mounts for this container.",
    )
    p_enc_setup.set_defaults(func=cmd_encrypt)

    p_enc_remove = p_enc_sub.add_parser(
        "remove", help="Disable encryption for a container or a specific volume mount.")
    p_enc_remove.add_argument("container", help="Container name.")
    p_enc_remove.add_argument(
        "--volume", metavar="PATH",
        help="Remove only this volume mount from encryption (leaves snapshot encryption active).",
    )
    p_enc_remove.set_defaults(func=cmd_encrypt)

    p_enc_pw = p_enc_sub.add_parser("password", help="Manage saved passwords.")
    p_pw_sub = p_enc_pw.add_subparsers(dest="password_action", metavar="sub_action")
    p_pw_sub.required = True

    p_pw_set = p_pw_sub.add_parser("set", help="Save a password for a container or volume mount.")
    p_pw_set.add_argument("container", help="Container name.")
    p_pw_set.add_argument(
        "--volume", metavar="PATH",
        help="Volume mount path. If omitted, sets the container-level snapshot password.",
    )
    p_pw_set.set_defaults(func=cmd_encrypt)

    p_pw_delete = p_pw_sub.add_parser("delete", help="Delete a saved password entry.")
    p_pw_delete.add_argument("container", help="Container name.")
    p_pw_delete.add_argument(
        "--volume", metavar="PATH",
        help="Volume mount path. If omitted, deletes the container-level password.",
    )
    p_pw_delete.set_defaults(func=cmd_encrypt)

    p_pw_purge = p_pw_sub.add_parser(
        "purge", help="Remove all saved passwords, or all for one container.")
    p_pw_purge.add_argument(
        "--container", metavar="NAME", dest="purge_container",
        help="Limit purge to passwords for this container.",
    )
    p_pw_purge.set_defaults(func=cmd_encrypt)

    p_enc_status = p_enc_sub.add_parser("status", help="Show encryption configuration and status.")
    p_enc_status.set_defaults(func=cmd_encrypt)

    p_enc_rotate = p_enc_sub.add_parser(
        "rotate",
        help="Change the encryption password for a container, re-keying all its snapshots.",
    )
    p_enc_rotate.add_argument(
        "--container", metavar="NAME", required=True,
        help="Container whose snapshots should be re-keyed.",
    )
    p_enc_rotate.add_argument(
        "--include-archives", action="store_true", default=False,
        help="Also re-key per-mount volume archives (slow for large archives).",
    )
    p_enc_rotate.add_argument(
        "--mode", choices=["session", "every_time"], default=None,
        help="Change the password prompt mode at the same time.",
    )
    p_enc_rotate.set_defaults(func=cmd_encrypt)

    p_enc_disable = p_enc_sub.add_parser(
        "disable",
        help="Decrypt all snapshots for a container and remove it from the encryption list.",
    )
    p_enc_disable.add_argument(
        "--container", metavar="NAME", required=True,
        help="Container to decrypt and remove from encryption.",
    )
    p_enc_disable.set_defaults(func=cmd_encrypt)

    p_config = sub.add_parser(
        "config",
        help="Open the config file in an editor. "
             "Path follows --config flag, then UPDATE_ZEN_CONFIG env var, "
             "then ~/.update_zen/config.json.",
    )
    p_config.set_defaults(func=cmd_config)

    p_install = sub.add_parser(
        "install",
        help="Install update_zen system-wide with passwordless sudo.",
    )
    p_install.set_defaults(func=cmd_install)

    args = parser.parse_args()
    args.config = config
    args.func(args)


if __name__ == "__main__":
    main()
