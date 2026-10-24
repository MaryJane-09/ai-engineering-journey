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
