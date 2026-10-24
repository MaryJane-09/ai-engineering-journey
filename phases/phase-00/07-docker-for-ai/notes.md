# SE 00 Lesson 07: Docker for AI

These notes summarize the [official Docker for AI lesson](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/00-setup-and-tooling/07-docker-for-ai). The host-to-container volume exercise is pending; see [`experiment.md`](experiment.md).

## Images and containers

A Dockerfile is a recipe for building an image. An image is the read-only template; a container is a running instance of that image. Containers isolate a process and its filesystem and network while sharing the host OS kernel. Dockerfile instructions form layers, and unchanged layers can be reused from cache during rebuilds.

The image packages the runtime and dependencies. It does not automatically preserve files written only inside a container after that container is removed.

## Volumes: host path and container path

In `-v ~/models:/models`, the left side (`~/models`) is a directory on the host computer. The right side (`/models`) is its mount location inside the container. Files in the host directory are visible inside the container and persist when the container stops or is rebuilt. Mount code, datasets, and large model weights instead of storing them only in the container's writable layer.

## GPU access

The NVIDIA Container Toolkit exposes an NVIDIA GPU from the host to a container, commonly through `docker run --gpus all`. The container image contains CUDA user-space libraries/toolkit; the host supplies the GPU and driver. A CPU-only setup can run by removing GPU configuration and the `--gpus` option.

## Docker Compose

Compose describes and runs multiple services from YAML. Compose places services on a shared network, where one service can reach another by its service name. For example, an `ai-dev` service can connect to Qdrant at `http://qdrant:6333`; it does not need the host machine's IP address.

## Troubleshooting daemon access

If Docker reports `permission denied` for `/var/run/docker.sock`, the current user cannot access the Docker daemon. The container has not started, so the error does not indicate a problem with the image or volume mount. On Linux, a user with sudo access can test a one-off command with `sudo docker`; otherwise, an administrator must grant Docker access and the user must start a new login session. Access to the Docker daemon is highly privileged.

## Learner evidence and review

The learner asked for an explanation of the two sides of the volume mount and did not know the answers to the three post-lesson checks. Review volume persistence, NVIDIA GPU exposure, and Compose DNS by service name. Quiz score: 0/3.
