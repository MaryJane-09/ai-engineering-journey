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

## Build practice

### Question 7 — Build a small Python image and mount the lesson folder

In this lesson folder, create `hello.py` that prints its working directory and the sorted names of files in `/workspace`. Create a `Dockerfile` using `python:3.12-slim`, set `/app` as its working directory, copy `hello.py` into the image, and configure it to run with Python. Build the image from this folder and run it with this folder mounted at `/workspace`:

```bash
sudo docker build -t lesson07-hello .
sudo docker run --rm -v "$PWD:/workspace" lesson07-hello
```

Record the contents of both files, the build/run output, and explain which files come from the image and which are visible through the bind mount. Do not include any credentials.

**Answer and evidence:** The learner created this Dockerfile:

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY hello.py .

CMD ["python", "hello.py"]
```

The Python script prints the current working directory and lists the mounted directory:

```python
import os

print(f"Working Directory: {os.getcwd()}")
print("Files in /workspace:")
try:
    files = sorted(os.listdir('/workspace'))
    for file in files:
        print(f"  -{file}")
except FileNotFoundError:
    print("  - /workspace directory not found (is it mounted?)")
```

The image built successfully and was tagged `lesson07-hello:latest`. Docker printed a legacy builder deprecation warning, but the build completed. Running the container produced:

```text
Working Directory: /app
Files in /workspace:
  -Dockerfile
  -experiment.md
  -hello.py
  -notes.md
  -reflection.md
```

The learner identified `/app` as coming from the image and the listed `/workspace` files as coming from the bind mount. The image provides Python, sets `/app` as the working directory, and copies `hello.py`; the runtime mount exposes the host lesson folder at `/workspace`.
