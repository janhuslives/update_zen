# Update Zen — Snapshot Coverage Reference

What gets captured in a snapshot, and what doesn't.

---

## What is backed up

Every snapshot is a `.tar.gz` bundle containing:

| Item | Details |
|---|---|
| Container configuration | Full `docker inspect` output — image, env, ports, mounts, labels, restart policy, network config, security options |
| Pre-update image | `docker save` of the image currently running, before the pull |
| Bind mounts | Every host-path volume (`/host/path:/container/path`) archived to its own `.tar.gz` |
| Named volumes | Every named Docker volume (non-anonymous) archived to its own `.tar.gz` |
| Compose file | Captured as a sidecar when the container has compose labels and the file can be resolved |
| Env overrides | A diff of environment variables added beyond the image defaults — for human reference; the full env is already in the inspect JSON |

Bind mounts and named volumes are backed up with the container briefly **paused** by default, so the archive is consistent.

---

## What is not backed up

### Container writable layer

Changes made directly inside the running container — files edited in place, packages installed with `apt`, etc. — that are not in a volume live in Docker's overlay2 write layer and are not archived.

This is intentional. A container with meaningful state only in its writable layer has a data problem that a backup tool shouldn't paper over. Everything that matters should be in a volume; the image covers the rest.

### Anonymous volumes

Named volumes with 64-character hex names (e.g. `a3b2c1d4e5f6...`). Docker creates these automatically for `VOLUME` directives in Dockerfiles when no explicit name is given. They are considered disposable — `docker system prune` removes them. If the data inside one matters, the volume should be given a real name.

### tmpfs mounts

In-memory mounts (`--tmpfs`) are ephemeral by design and are not archived. Runtime secrets mounted via Docker's secrets mechanism (at `/run/secrets/`) fall into this category — the decrypted value at runtime is not what you back up; the secret source is.

### Non-local driver volumes *(warns)*

Named volumes using a custom storage driver — NFS, cloud block storage, or any plugin that provides no host-side `Source` path — cannot be archived by Update Zen. There is no local directory to `tar`.

When a snapshot encounters a volume in this category, **Update Zen warns you** in the snapshot summary and records it in the snapshot's volume index under `skipped`. Your data on that volume is not covered; back it up through whatever mechanism your storage driver provides.

### Container logs

The container's stdout/stderr history is not captured. Logs are observability artifacts, not restore artifacts — they play no role in bringing a container back up. If logs need long-term retention, that belongs to a log shipper or aggregator, not a snapshot.

### In-memory process state

The live state of the running process — heap contents, open file descriptors, socket buffers — is not captured. Doing so requires CRIU (Checkpoint/Restore in Userspace), which has significant kernel and runtime prerequisites and is outside the scope of update-with-rollback. After a rollback, the container starts fresh from the image and its volumes, which is the expected behavior.

### Sockets and device files

Unix domain sockets and device files mounted from the host (e.g. `/dev/dri`) are skipped during volume archival. They are kernel interfaces that cannot be meaningfully archived and must exist on the host for the container to use them.

### Compose file (unresolvable path) *(warns)*

If a container has Docker Compose labels but the compose file cannot be found — because the working directory path no longer exists, has moved, or cannot be resolved from Portainer's internal layout — no compose sidecar is written into the snapshot.

When this happens, **Update Zen warns you** at snapshot time. The snapshot is still valid and rollback will work, but it will use `docker run` reconstruction from the inspect JSON rather than `docker compose up`. This means any `--compose` rollback option will be unavailable for that snapshot.

---

## Summary table

| Component | Backed up | Notes |
|---|---|---|
| Container configuration (inspect) | Yes | Always |
| Pre-update image | Yes | Via `docker save`; can be disabled per container |
| Bind mounts | Yes | Paused for consistency by default |
| Named volumes | Yes | Non-anonymous only |
| Compose file | Yes* | When labels present and path resolves; warns if not |
| Env overrides | Yes* | Reference copy; full env is in inspect JSON |
| Non-local driver volumes | No | Warns when skipped |
| Container writable layer | No | By design |
| Anonymous volumes | No | By design |
| tmpfs mounts | No | By design |
| Container logs | No | By design |
| In-memory process state | No | By design |
| Sockets and device files | No | By design |
