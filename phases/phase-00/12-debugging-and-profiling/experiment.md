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

## Evidence

**Pending.** Bring back the slowest meaningful function in the profile and one sentence explaining what profiling does not prove.

## Reflection prompt

If data loading dominates a training profile, what should you investigate before trying to upgrade the GPU?
