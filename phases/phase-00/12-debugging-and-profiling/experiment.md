# SE 00 Lesson 12: Find a Time Bottleneck

## Goal

Use `cProfile` to compare a deliberately slow step with a small computation, then identify the function that dominates cumulative time.

## Procedure

Run this command:

```bash
python3 -c 'import cProfile, time; cProfile.run("time.sleep(0.1); sum(range(10000))", sort="cumtime")'
```

The `sleep` call simulates a slow step. `sum` is the small computation. Read the profile rows sorted by cumulative time.

## Expected observation

`time.sleep` should account for most of the elapsed time. The profile shows where time was spent; it does not check whether an AI model's output is correct.

## Observed result

The learner's profile showed 5 function calls in 0.101 seconds. `time.sleep` accounted for 0.100 seconds of cumulative time; `sum` took less than 0.001 seconds. This identifies the simulated delay as the bottleneck.

## Explanation

Profiling measures resource use, such as elapsed time or memory, and helps locate bottlenecks. It does not prove that a program's result is correct, that a model generalizes, or that there is no data leakage. Use tests, validation data, and tensor checks to investigate correctness.

**Status: Complete.** The learner requested this distinction after reporting the profile output, and the tutor explained it.

## Reflection prompt

If data loading dominates a training profile, what should you investigate before trying to upgrade the GPU?

## Tensor-health practice

### Question 12 — Inspect tensors and detect NaNs

Create `tensor-health.py` in this lesson folder. Using PyTorch, make one tensor with only finite values and one tensor that contains a NaN. For each tensor, print its shape, dtype, device, and whether it contains any NaN values. Run it with `.venv/bin/python phases/phase-00/12-debugging-and-profiling/tensor-health.py`. Record the code and output, then explain why a profiler alone would not catch this correctness problem.

**Answer and evidence:** The learner wrote a helper that reports tensor metadata and checks whether any element is NaN:

```python
import torch

def inspect_tensor_health(name, tensor):
    print(f"--- Tensor: {name} ---")
    print(f"Shape:   {tensor.shape}")
    print(f"Dtype:   {tensor.dtype}")
    print(f"Device:  {tensor.device}")
    print(f"Has NaN: {torch.isnan(tensor).any().item()}")
    print()

def main():
    healthy_tensor = torch.tensor([1.0, 2.5, 3.8, 4.2], dtype=torch.float32, device="cpu")
    nan_tensor = torch.tensor([1.0, float('nan'), 3.8, 4.2], dtype=torch.float32, device="cpu")

    inspect_tensor_health("Healthy Tensor", healthy_tensor)
    inspect_tensor_health("NaN Tensor", nan_tensor)

if __name__ == "__main__":
    main()
```

Output:

```text
--- Tensor: Healthy Tensor ---
Shape:   torch.Size([4])
Dtype:   torch.float32
Device:  cpu
Has NaN: False

--- Tensor: NaN Tensor ---
Shape:   torch.Size([4])
Dtype:   torch.float32
Device:  cpu
Has NaN: True
```

The learner explained that profiling does not guarantee correctness. It measures performance; the tensor-health check separately detects invalid values such as NaN.
