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

## Troubleshooting and remaining evidence

On Linux, if the learner has sudo access, retry the same command with `sudo` before `docker`:

```bash
sudo docker run --rm -v "$PWD:/workspace" alpine:3.20 ls /workspace
```

Otherwise, an administrator can grant the account Docker daemon access (commonly through the `docker` group), after which the learner must log out and back in. Docker daemon access is highly privileged. Once the command runs, bring back its output and identify which path is on the host and which is inside the container.

**Pending.** The experiment is not complete until Docker lists the mounted repository contents.
