# SE 00 Lesson 09: Reproducible Data Splits

## Goal

Create a 70/15/15 train/validation/test split from 20 row IDs, then confirm that a fixed seed produces the same rows in each split on a second run.

## Procedure

Run this command twice from the repository root:

```bash
python3 -c 'import random; rows=list(range(20)); random.Random(42).shuffle(rows); train, val, test=rows[:14], rows[14:17], rows[17:]; print("sizes:", len(train), len(val), len(test)); print("splits:", train, val, test)'
```

The seed is `42`; the slices make 14 training rows, 3 validation rows, and 3 test rows. Compare the printed rows across both runs.

## First observed result

The learner's first run produced sizes `14`, `3`, and `3`, with these row IDs:

```text
train:      [19, 5, 14, 4, 9, 13, 15, 18, 6, 12, 17, 10, 1, 11]
validation: [2, 16, 7]
test:       [8, 0, 3]
```

## Second observed result

The second run produced sizes `14`, `3`, and `3`, with the same train, validation, and test row IDs as the first run.

**Status: Complete.** The repeated output confirms the fixed seed reproduces the partition.

## Reflection prompt

Which was easier to confuse: using a fixed seed for reproducibility, or holding out test data for a final evaluation? Explain the difference in one sentence.
