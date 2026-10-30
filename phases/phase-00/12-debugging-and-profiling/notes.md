# SE 00 Lesson 12: Debugging & Profiling

These notes summarize the [official Debugging & Profiling lesson](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/00-setup-and-tooling/12-debugging-and-profiling). The short profiling exercise is complete; see [`experiment.md`](experiment.md).

## Debug correctness at three levels

AI code can run without crashing and still produce useless results. Check:

1. **Python flow:** use logs and `breakpoint()` to inspect where execution goes and what values it sees.
2. **Tensor health:** inspect shape, dtype, device, value range, and whether values or gradients contain NaN/Inf.
3. **Training behavior:** track train/validation loss and other metrics over time. A valid-looking run does not prove the model is correct.

Use a conditional breakpoint at a suspicious step, such as when loss is too high or NaN. In the debugger, inspect `outputs.shape`, `loss.item()`, `torch.isnan(loss)`, and gradients. Logs add timestamps and severity and can be saved to a file for long runs.

## Profiling performance

A profiler measures resource use, such as execution time and memory allocation. It helps answer **where is the time or memory going?** It does not establish that model outputs are correct.

`cProfile` reports function calls and time. Sort by cumulative time to find functions that take the most time including their nested calls. A common finding is that data loading takes more time than model computation; if the profile confirms this, improve the data loader (for example, try `num_workers > 0`) before switching to a faster GPU.

`tracemalloc` helps identify Python memory allocations. PyTorch exposes GPU memory metrics. TensorBoard can plot training and validation curves: train loss falling while validation loss rises can indicate overfitting. Suspiciously high test accuracy can indicate data leakage, such as overlap between train and test examples.

## Learner evidence and review

The learner correctly identified the data loader as the first place to investigate when profiling shows data loading dominates, and chose gradient checks plus `breakpoint()` for NaN loss. They ran the `cProfile` exercise; `time.sleep` took 0.100 seconds of a 0.101-second profile. They asked what profiling does not prove; the tutor clarified that measuring resource use does not verify output correctness or model generalization. In review, the learner identified test-file access as a possible source of leakage and explained that a time profile reveals slow functions but not whether their outputs are correct. Review complete. Quiz score: 1/3.
