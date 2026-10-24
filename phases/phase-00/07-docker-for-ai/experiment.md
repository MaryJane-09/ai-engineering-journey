# SE 00 Lesson 07: Host-to-Container Volume Experiment

## Goal

Observe a host directory from inside a temporary container, and identify the host path and container path in a volume mount.

## Procedure

From the repository root, run:

```bash
docker run --rm -v "$PWD:/workspace" alpine:3.20 ls /workspace
```

Docker may need to download the Alpine image the first time. `--rm` removes the temporary container after it exits. The current repository directory on the host is mounted at `/workspace` inside the container.

## Attempted result

The learner ran the command, but Docker returned `permission denied` while connecting to `/var/run/docker.sock`. The daemon rejected the request before starting the container, so this attempt did not verify the volume mount.

## Result

Docker returned `permission denied` while connecting to `/var/run/docker.sock`, before starting a container. The learner reports that Docker access cannot be granted in this environment. Therefore, the volume mount was not tested and this hands-on exercise is **unavailable here**. The conceptual mapping remains: `$PWD` is the host path, and `/workspace` is the container path.
