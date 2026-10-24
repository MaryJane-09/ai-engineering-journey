# SE 00 Lesson 07: Host-to-Container Volume Experiment

## Goal

Observe a host directory from inside a temporary container, and identify the host path and container path in a volume mount.

## Procedure

From the repository root, run:

```bash
docker run --rm -v "$PWD:/workspace" alpine:3.20 ls /workspace
```

Docker may need to download the Alpine image the first time. `--rm` removes the temporary container after it exits. The current repository directory on the host is mounted at `/workspace` inside the container.

## Evidence

**Pending.** Bring back the command output and state which path is on the host and which is inside the container. Do not mark this exercise complete until it has been run.
