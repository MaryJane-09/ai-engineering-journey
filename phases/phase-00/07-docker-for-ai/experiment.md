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

The learner first ran the command, but Docker returned `permission denied` while connecting to `/var/run/docker.sock`. The daemon rejected the request before starting the container, so that attempt did not verify the volume mount.

On 2026-10-29, the learner asked to retry, believing Docker access was available. The same command was run again, first in the normal sandbox and then with elevated command access. Both attempts returned `permission denied` for `/var/run/docker.sock` before a container started. The learner clarified that Docker has not yet been downloaded/installed, which explains why no usable daemon is available. The volume mount remains unverified and the exercise is pending until Docker is installed and running.

Later, the learner ran the documented command in their Ubuntu terminal with `sudo`. Docker downloaded `alpine:3.20`, then listed `AGENTS.md`, `LEARNING.md`, `README.md`, `phases`, and `skills-lock.json` from `/workspace`. This confirms the repository directory was visible inside the temporary container. The command exited and `--rm` removed the container.

## Result

The initial attempts returned `permission denied` because the learner's account could not access the Docker daemon socket. Running the command with `sudo` succeeded: the repository files appeared inside the container at `/workspace`. This hands-on volume exercise is **complete**. The mount maps `$PWD` on the host to `/workspace` in the container.
