# 437a221 — Cross-check ghcr version tags against real registry tags

## Background

A user's "Compose update" of `dispatcharr` failed twice with `manifest
unknown`:

```
[UPDATE dispatcharr] pinning to tag 'v0.29.0': ghcr.io/dispatcharr/dispatcharr:latest → ghcr.io/dispatcharr/dispatcharr:v0.29.0
[UPDATE dispatcharr] registry digest lookup failed (tag not found for ghcr.io/dispatcharr/dispatcharr:v0.29.0: 404 Not Found), falling back to tag pull
[UPDATE dispatcharr] pulling ghcr.io/dispatcharr/dispatcharr:v0.29.0
Error response from daemon: manifest unknown
```

The container was originally recreated from `docker run` and never
started successfully. `v0.29.0` had been chosen via the interactive
"Select version..." menu and stored in `pinned_tags`, so every
subsequent update attempt (plain and compose) kept retrying the same
nonexistent tag.

## Root Cause

`RegistryClient.list_versions()` builds its version list for `ghcr.io`
images from the **GitHub Releases API** (`_fetch_github_dates`), using
each release's `tag_name` (e.g. `v0.29.0`) directly as a Docker tag. The
code's own comment stated the assumption plainly: "ghcr.io images mirror
the GitHub release tag as the Docker tag."

That assumption doesn't hold for Dispatcharr. Its GitHub releases are
tagged `v0.29.0`, but the images actually pushed to
`ghcr.io/dispatcharr/dispatcharr` are tagged without the `v` and with a
build-timestamp suffix (`0.29.0-20260824230206`, etc.). `list_versions()`
never verified the GitHub-derived tag actually existed on the registry
before offering it in the menu, so picking it silently stored a
dead pin.

Fixing that surfaced two more bugs in the fallback path (the raw
registry tag list, used when no GitHub/Docker-Hub date source is
available):

1. `list_tags()` only fetched the first page of a registry's
   `GET /v2/<repo>/tags/list` response. ghcr.io paginates that endpoint
   via an RFC5988 `Link: <...>; rel="next"` header, defaulting to ~100
   tags per page. Dispatcharr has 3,592 tags (mostly commit-SHA build
   tags), so the real semver-ish tags weren't even present in the first
   page — the fallback would have found nothing either.
2. The "is this tag version-like" filter was `tag.lstrip("v")[:1].isdigit()`
   — true for any tag starting with a digit, including 40-char
   commit-SHA tags like `839abd281ca6a1cded692d1876cc06659c333758`
   (`8` is a digit). Those sorted above real version tags under the
   existing `_version_key` scheme, since alphabetic sort keys rank above
   the exact-numeric case in the reverse-sorted tuple comparison.

## Implementation

- **`list_versions()`** (ghcr.io branch): after fetching GitHub release
  dates, cross-check the tag names against `list_tags()`'s real registry
  tag set and drop any that don't exist. If the cross-check empties the
  date-sourced list out, the function falls through to the existing
  registry-tag-list branch instead of reporting "no version history
  available."
- **`list_tags()`**: added `_get_json_with_link()`, a small variant of
  `_get_json()` that also parses the `Link` response header. `list_tags()`
  now loops on `rel="next"` until exhausted (capped at 50 pages as a
  runaway backstop) and returns the deduplicated, sorted union of every
  page.
- **`_VERSION_TAG_RE`**: replaced the digit-prefix heuristic with
  `^v?\d+(\.\d+){1,3}([.\-][0-9A-Za-z]+)*$` — requires at least one dot
  after the leading digit run, which real version strings have and
  40-character hex commit-SHA tags don't. Applied in both places the old
  heuristic was used (the dates branch and the registry-tag-list
  fallback branch).

Verified against the live `ghcr.io/dispatcharr/dispatcharr` registry:
`list_tags()` now returns all 3,592 tags (up from 100), `0.29.0` and its
timestamped/arch variants are present and confirmed pullable via
`docker manifest inspect`, and `list_versions()` surfaces those real tags
sorted correctly instead of `v0.29.0` or SHA-tag noise. Unit-checked
`_VERSION_TAG_RE` against semver tags, `v`-prefixed tags, build-suffixed
tags, bare `latest`, digit-only tags, and both SHA tags from the log
above.

## Files Changed

| File | Change |
|---|---|
| `update_zen.py` | `RegistryClient.list_versions()`: cross-check ghcr GitHub-release tags against real registry tags, fall back to raw tag list when none match. `RegistryClient.list_tags()`: follow Link-header pagination via new `_get_json_with_link()`. `RegistryClient._VERSION_TAG_RE`: new regex replacing the digit-prefix version-tag heuristic in both filter sites. |
