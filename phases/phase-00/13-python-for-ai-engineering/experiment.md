# SE 00 Lesson 13: Fit Normalization on Training Data

## Goal

Compare feature statistics fit on training rows only with statistics fit using test rows too.

## Procedure

Run from the repository root:

```bash
python3 phases/phase-00/13-python-for-ai-engineering/normalization-check.py
```

The script uses training values `[1.0, 2.0, 3.0]` and a very different test value `[100.0]`. It prints the population mean and standard deviation for the train-only set and for the combined set.

## Expected output

```text
train only: (2.0, 0.816496580927726)
train plus test: (26.5, 42.44113570582201)
```

## Observed result

The learner ran the script and observed:

```text
train only: (2.0, 0.816496580927726)
train plus test: (26.5, 42.44113570582201)
```

The learner explained that using test data to fit the statistics would leak information into the test set.

**Status: Complete.** Fit the statistics using the training split only, then apply the same values to validation and test data.

## Reflection prompt

Which Python behavior from this lesson could silently change the data used in a later training epoch?

## Mini-batch practice

### Question 13 — Build a reusable mini-batch generator

Create `mini_batches.py` in this lesson folder. Write a generator that yields batches from the values `list(range(10))`, using a batch size of `4`. Print the batches for two epochs and include the final partial batch. Explain why you need a fresh generator for each epoch. Run the script with `.venv/bin/python phases/phase-00/13-python-for-ai-engineering/mini_batches.py`, and record your code and output.

**Answer and evidence:** The learner wrote a generator that slices the input into batches and creates a new generator for each epoch:

```python
def get_batch_generator(data, batch_size):
    """Yields successive batch_size chunks from data."""
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]

def main():
    data = list(range(10))
    batch_size = 4
    epochs = 2

    for epoch in range(1, epochs + 1):
        print(f"--- Epoch {epoch} ---")
        batch_gen = get_batch_generator(data, batch_size)

        for batch in batch_gen:
            print(f"Batch: {batch}")
        print()

if __name__ == "__main__":
    main()
```

Output:

```text
--- Epoch 1 ---
Batch: [0, 1, 2, 3]
Batch: [4, 5, 6, 7]
Batch: [8, 9]

--- Epoch 2 ---
Batch: [0, 1, 2, 3]
Batch: [4, 5, 6, 7]
Batch: [8, 9]
```

The learner explained that generators are single-use iterators and cannot be reset or rewound after exhaustion, so each epoch needs a fresh generator instance.
