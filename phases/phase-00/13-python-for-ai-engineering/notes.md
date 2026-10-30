# SE 00 Lesson 13: Python for AI Engineering

These notes summarize the [official Python for AI Engineering lesson](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/00-setup-and-tooling/13-python-for-ai-engineering). The train-only normalization comparison is complete; see [`experiment.md`](experiment.md) and [`normalization-check.py`](normalization-check.py).

## Python patterns used in AI code

- **Names and mutable objects:** assigning `alias = values` makes both names refer to the same list. Use `values.copy()` or `list(values)` when you need a separate list. Nested lists need a new inner list for each row: `[[0] * 3 for _ in range(2)]`.
- **Mutable defaults:** Python evaluates a default once when it defines the function. `def add(item, bucket=[])` reuses one list across calls. Use `bucket=None`, then create `bucket = []` inside the function. In dataclasses, use `field(default_factory=list)`.
- **Generators:** a generator yields one item at a time and is used up after one pass. Create a fresh generator for each training epoch. A list holds every item in memory; a generator is useful when data is large.
- **Batching:** slicing and `itertools.islice` can form mini-batches. Decide explicitly whether the last smaller batch should be kept or dropped.
- **Reusable code:** use type hints, dataclasses for configuration or records, context managers (`with`) for cleanup, and `if __name__ == "__main__":` to keep importable modules from running their demo.

## Reproducible splits and avoiding leakage

Use a seeded random generator, such as `random.Random(42)`, to reproduce a shuffle and split. When standardizing features, calculate the mean and standard deviation using training rows only. Reuse those same values for validation and test rows. If test rows help determine the normalization values, information from the test set has leaked into training and its evaluation is no longer independent.

## Python loops and NumPy

A Python list holds references to Python objects. A loop over millions of floats performs interpreter and type-handling work for each value. A NumPy array stores typed numeric values together and runs vectorized operations in compiled code, usually with less overhead. Use plain Python for clarity on small tasks; use NumPy for large numeric arrays.

## Learner evidence and review

The learner correctly predicted that calls to a function with a mutable list default share the same list. They initially selected per-mini-batch statistics for normalization, then explained that fitting with test data would leak information into the test set. The exercise showed train-only statistics `(2.0, 0.816...)` versus combined statistics `(26.5, 42.441...)`. In review, the learner explained that mean and standard deviation from the training set should be reused for validation and test so those sets do not influence the process. Review complete. Quiz score: 1/2.
