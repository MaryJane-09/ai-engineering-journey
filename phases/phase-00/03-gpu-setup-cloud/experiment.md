# SE 00 Lesson 03: Experiment

## Recorded evidence

The learner scored **3/3** and explained that CPU work uses system RAM, CUDA selects an available NVIDIA GPU, GPU timing needs synchronization, and fp16 weights use roughly two bytes per parameter before training overhead. The progress record does not report a benchmark or cloud run. CUDA was unavailable on the learner's hardware.

## Practice experiment

Run the device-selection check from the [lesson notes](notes.md) and record whether PyTorch selects CPU or CUDA. If CUDA is available, time the same matrix operation with synchronization before and after the GPU work. If CUDA is unavailable, record the CPU result and explain why there is no GPU timing to compare.

## Status

Quiz evidence is recorded. No device check, benchmark, or cloud run is claimed here.
