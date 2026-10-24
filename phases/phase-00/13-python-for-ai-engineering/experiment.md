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
