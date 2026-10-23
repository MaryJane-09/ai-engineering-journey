# SE 00 Lesson 03: GPU Setup & Cloud

These study notes are based on the [official GPU Setup & Cloud lesson](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/00-setup-and-tooling/03-gpu-setup-and-cloud). They describe the course's local, Colab, and cloud options; they do not claim that the learner ran a benchmark or used a cloud GPU.

## What you should learn

The lesson teaches how to check whether PyTorch can see a local NVIDIA GPU, select a Colab T4 for a cloud experiment, compare CPU and GPU matrix multiplication, and estimate an idealized model parameter count from available VRAM using the fp16 rule of thumb.

The reason to learn this is practical: many early lessons run on a CPU, but larger training workloads can benefit from GPU parallelism. Knowing whether code actually selected a GPU prevents you from assuming that installing PyTorch alone makes computation run there.

## CPU memory, GPU memory, and CUDA

The CPU normally works with system RAM. An NVIDIA GPU has its own video memory (VRAM), separate from system RAM. VRAM limits how much model state and intermediate data can fit on the GPU. CUDA is NVIDIA's platform for running computations on NVIDIA GPUs; PyTorch exposes availability and device information through `torch.cuda`.

A machine with no supported GPU can still use PyTorch on CPU. The lesson's fallback is explicit:

```python
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using: {device}")
```

The conditional selects the CUDA device only if PyTorch reports it available; otherwise it selects CPU. This avoids hard-coding a device that is not present.

## Option 1: check a local NVIDIA GPU

Start with the system utility:

```bash
nvidia-smi
```

It should display NVIDIA device information when a supported GPU and driver are available. Then ask PyTorch what it can access:

```python
import torch

print(f"CUDA available: {torch.cuda.is_available()}")
print(f"CUDA version: {torch.version.cuda}")
if torch.cuda.is_available():
    print(f"GPU: {torch.cuda.get_device_name(0)}")
    print(f"Memory: {torch.cuda.get_device_properties(0).total_memory / 1e9:.1f} GB")
```

The Boolean tells you if CUDA is usable by this PyTorch install. The version field reports the CUDA version associated with the build. The conditional avoids querying device zero when no CUDA GPU is available; when available, it prints the device name and total memory in decimal gigabytes. On Windows, the lesson directs learners to the PyTorch install selector for the matching command. Do not infer GPU availability solely from having installed the package.

## Option 2: use Google Colab

The lesson's sequence is:

1. Open Google Colab.
2. Choose **Runtime > Change runtime type > T4 GPU**.
3. Run `!nvidia-smi` in a notebook cell and verify that a GPU name appears.
4. Run the course notebook or benchmark in that runtime.

The notebook's `!` prefix runs a shell command from a cell. Selecting a GPU runtime and seeing the device in `nvidia-smi` verifies that the session has a GPU attached. A local CPU result is not comparable to a Colab GPU result unless you have confirmed which device each run used.

## Option 3: use a cloud GPU instance

The official lesson names Lambda Labs, RunPod, and Vast.ai as examples and shows this pattern:

```bash
ssh user@your-gpu-instance
pip install torch torchvision torchaudio
python -c "import torch; print(torch.cuda.get_device_name(0))"
```

`ssh` opens a remote shell on the instance. The package command installs PyTorch and its vision/audio packages there. The final one-line Python program asks PyTorch for the first CUDA device name. The example assumes that the instance has a configured GPU and compatible PyTorch install; it is not a complete cloud provisioning or security guide. The lesson lists an hourly cost range, so treat its figure as a rough course estimate and check a provider's current pricing before launching resources.

## Compare CPU and GPU matrix multiplication

The course creates two random square tensors and times their matrix product:

```python
import torch
import time

size = 5000
a_cpu = torch.randn(size, size)
b_cpu = torch.randn(size, size)

start = time.time()
c_cpu = a_cpu @ b_cpu
cpu_time = time.time() - start
print(f"CPU: {cpu_time:.3f}s")

if torch.cuda.is_available():
    a_gpu = a_cpu.to("cuda")
    b_gpu = b_cpu.to("cuda")
    torch.cuda.synchronize()
    start = time.time()
    c_gpu = a_gpu @ b_gpu
    torch.cuda.synchronize()
    gpu_time = time.time() - start
    print(f"GPU: {gpu_time:.3f}s")
    print(f"Speedup: {cpu_time / gpu_time:.0f}x")
```

The `@` operator performs matrix multiplication. The `.to("cuda")` calls copy the CPU tensors to GPU memory. CUDA work is asynchronous: Python may continue before the GPU has finished, so the synchronizations around the timed GPU operation make the timer wait for completion. Without them, the reported GPU time can measure dispatch rather than finished computation.

The CPU time is printed on every run. GPU time and speedup appear only when CUDA is available. Exact timings depend on the hardware and runtime; the lesson does not prescribe a particular number. It warns that a first GPU run includes startup cost and recommends using a second run for comparison. Do not compare numbers until you have verified the selected device.

## Estimate model fit with fp16

The lesson's rule of thumb is about **2 bytes per parameter** for fp16 weights. To estimate an idealized upper bound, divide available VRAM in bytes by two. The official exercise hint says to leave a margin because activations and the CUDA context also use memory. Therefore this estimate is not a promise that a model with that parameter count will fit during training; training needs memory beyond the parameter weights.

## Common mistakes and limits

- **Assuming the GPU is in use because one is installed:** check both `nvidia-smi` and `torch.cuda.is_available()`.
- **Timing asynchronous GPU work without synchronization:** wait for the device before stopping the timer.
- **Treating the first GPU run as representative:** the course notes startup cost and says to compare a later run.
- **Confusing VRAM with system RAM:** model fit on a GPU depends on its separate VRAM.
- **Treating 2 bytes per parameter as the full training footprint:** activations and CUDA context consume additional memory.
- **No local GPU:** use CPU for lessons that permit it, or select Colab/cloud for GPU-required work.

The lesson does not cover detailed driver installation, cloud instance provisioning, resource cleanup, or a full memory model for training. It gives verification and benchmark patterns, not a universal fix for every driver/runtime mismatch.

## Key takeaways

- Confirm that PyTorch sees the device before running GPU code.
- Use CPU, Colab, or a cloud instance according to the workload and hardware available.
- Synchronize CUDA around timed work because GPU execution is asynchronous.
- Treat the fp16 calculation as a weight-only estimate and leave room for overhead.

## Self-check

1. How do system RAM and VRAM differ?
2. Why does the benchmark synchronize CUDA before reading the end time?
3. What does the benchmark print if CUDA is unavailable?
4. Why does the fp16 estimate overstate the size of a model that can be trained?

## Your recorded progress

The progress log records a 3/3 quiz and says the learner explained CPU use of system RAM, CUDA selection of an available NVIDIA GPU, synchronization for GPU timing, and the 2-byte fp16 parameter estimate before training overhead. It does not record a benchmark or cloud run. See [`LEARNING.md`](../../../LEARNING.md), entry for 2026-10-23, SE 00/03.
