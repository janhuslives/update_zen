# e1c7c7b — Recognize lscr.io as a ghcr.io-backed registry

## Background

A user updating `sabnzbd` (tracked via `lscr.io/linuxserver/sabnzbd:latest`)
found the "Select version..." menu topped out at `4.2.0-unstable` across
13 pages / 187 entries, with "release dates unavailable for lscr.io" —
even though SABnzbd 5.1.1 (a security-fix release) had been out for days
and was visibly the current stable tag on LinuxServer's own docs.

## Root Cause

`RegistryClient.list_versions()` only special-cased the literal hostname
`ghcr.io` for date-based version lookup (GitHub Releases API). LinuxServer
publishes its images under its own friendly domain, `lscr.io` — parsed by
`_parse_image_ref()` as a distinct registry hostname — so it never took
that branch and fell through to `dates = {}`, i.e. the raw
`list_tags()` fallback with no date source.

That fallback is a bad fit for `linuxserver/sabnzbd`: the repo carries
years of per-architecture and per-build tags (verified live: paging
through `GET /v2/linuxserver/sabnzbd/tags/list` via its real ghcr.io
backend, ~100 tags per page returned **oldest-first**, with no cursor to
jump ahead). `list_tags()`'s existing 50-page cap (5,000 tags) doesn't
come close to reaching the current release — five pages of real traffic
only advanced from tag `3.2.0Beta1-ls31` to `3.4.2-ls47`. The menu's
`4.2.0-unstable` ceiling was exactly where that cap ran out.

Confirmed via `curl` that `lscr.io`'s 401 challenge itself names the real
backend: `WWW-Authenticate: Bearer realm="https://ghcr.io/token"` — lscr.io
is a friendly-domain proxy in front of ghcr.io, same API shape.

Fixing the registry-hostname match surfaced a naming mismatch: LinuxServer
pushes images as `ghcr.io/linuxserver/<app>`, but the GitHub repo backing
each app's release history is named `docker-<app>`
(`linuxserver/docker-sabnzbd`, confirmed via the GitHub Releases API —
`linuxserver/sabnzbd` 404s, `linuxserver/docker-sabnzbd` returns releases
tagged e.g. `5.1.2-ls269`).

It also exposed a latent bug in the existing ghcr.io cross-check
(introduced in `437a221`): it validated GitHub-release tag names against
`list_tags()`'s enumerated set, but that enumeration has the exact same
oldest-first/50-page-cap problem described above. For any ghcr.io image
with a large enough tag history, the cross-check would silently drop
legitimately pullable recent tags because they'd never appear within the
50-page window — not just an lscr.io-specific issue.

## Implementation

- **`list_versions()`**: changed `elif registry == "ghcr.io":` to
  `elif registry in ("ghcr.io", "lscr.io"):`.
- Inside that branch, when the org is `linuxserver`, rewrite the GitHub
  repo name from `<app>` to `docker-<app>` before calling
  `_fetch_github_dates()`.
- Replaced the `list_tags()`-based cross-check with a direct per-candidate
  check: for each GitHub-release-derived tag, call `get_remote_digest()`
  (a single HEAD request) and keep only tags that actually resolve. This
  fixes both the lscr.io case and the pre-existing ghcr.io large-repo gap,
  without depending on any full tag enumeration.

Verified against the live registry (stubbing the POSIX-only imports —
`termios`/`tty`/`pwd`/`grp`/`os.getuid` — to load `RegistryClient` under
Windows for a quick harness): `list_versions("lscr.io/linuxserver/sabnzbd:latest")`
now returns `5.1.2-ls269` (2026-08-25) at the top, followed by
`5.1.1-ls268`, `5.1.1-ls267`, `5.1.0-ls267`, etc., each confirmed pullable.

## Files Changed

| File | Change |
|---|---|
| `update_zen.py` | `RegistryClient.list_versions()`: treat `lscr.io` as ghcr.io-backed, map `linuxserver/<app>` → `linuxserver/docker-<app>` for the GitHub Releases lookup, and replace the full-tag-list cross-check with a per-candidate `get_remote_digest()` verification. |
