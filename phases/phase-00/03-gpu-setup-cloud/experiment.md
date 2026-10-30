# SE 00 Lesson 03: Experiment

## Recorded evidence

The learner scored **3/3** and explained that CPU work uses system RAM, CUDA selects an available NVIDIA GPU, GPU timing needs synchronization, and fp16 weights use roughly two bytes per parameter before training overhead. The progress record does not report a benchmark or cloud run. CUDA was unavailable on the learner's hardware.

## Practice experiment

### Question 3 — CPU/GPU benchmark

Create `gpu_benchmark.py` in this lesson folder. Use PyTorch to time a matrix multiplication on CPU. If CUDA is available, move the tensors to CUDA, synchronize before starting and after the operation, and report the GPU time and speedup. If CUDA is unavailable, print that clearly and report the CPU time only. Run from the repository root with `.venv/bin/python phases/phase-00/03-gpu-setup-cloud/gpu_benchmark.py`. In your answer, include the code and output and explain why synchronization matters for GPU timing.

**First attempt:**

```python
import torch
# Running on cpu CUDA not available
a = torch.rand(3, 5)
b = torch.rand(5, 4)

result = torch.matmul(a, b)

print("Output Shape:", result.shape)
```

Output: `Output Shape: torch.Size([3, 4])`.

The learner correctly explained that GPU timing needs synchronization because GPU operations are asynchronous and otherwise the measured time may be incorrect.

**Answer and evidence:** The learner expanded the example to time a CPU matrix multiplication and checked CUDA availability:

```python
import time
import torch

a = torch.rand(800, 90)
b = torch.rand(90, 500)

start = time.perf_counter()
result = torch.matmul(a, b)
end = time.perf_counter()

total_time = end - start
print(f"Total Time: {total_time}")
print("Output Shape:", result.shape)
print(torch.cuda.is_available())
```

Output:

```text
Total Time: 0.018939012981718406
Output Shape: torch.Size([800, 500])
False
```

This confirms the expected matrix shape and records a CPU timing of about 0.019 seconds on this run. CUDA is unavailable, so there is no GPU timing or speedup to compare. Synchronization is needed for GPU timing because PyTorch queues CUDA work asynchronously; synchronizing before and after the timed operation makes the measured interval include completion of that work. No GPU synchronization was needed for this CPU-only run.

## Status

The original lesson quiz evidence and CPU benchmark exercise are recorded. A CUDA benchmark remains unavailable on this machine.
