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

## Docker socket access and exercise result

The learner's initial Docker command was rejected with `permission denied` for `/var/run/docker.sock` before the container started. Running the volume exercise with `sudo` succeeded: Docker downloaded `alpine:3.20` and listed the repository files from `/workspace`. The command-line user lacked access to the daemon socket; the image and volume syntax were valid. The mount maps a host directory on the left to a path inside the container on the right. Docker documents that membership in the `docker` group grants root-level privileges, so use `sudo` or review that security tradeoff before changing group membership.

## Learner evidence and review

The learner asked for an explanation of the two sides of the volume mount; the hands-on run confirmed the repository appeared at `/workspace` inside the container. The learner explained that the files remain because they existed before the container was created; the host directory is mounted into the container, so removing the container does not remove the host files. The learner requested an explanation of GPU access: the host supplies the physical NVIDIA GPU and driver, the NVIDIA Container Toolkit connects Docker to that GPU, `--gpus all` requests that all available GPUs be exposed to the container, and the container image supplies the CUDA libraries its software needs. The learner correctly identified the host as the source of the NVIDIA driver and explained that Compose services use service names as hostnames on their shared network. Docker review complete. Quiz score: 0/3.
