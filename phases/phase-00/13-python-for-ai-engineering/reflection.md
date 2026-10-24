# SE 00 Lesson 13: Reflection

## Learner reflection

The learner correctly predicted that a function with a mutable list default returns a shared list across calls. They initially chose per-mini-batch normalization statistics, then explained that using test data would leak information into the test set.

## Takeaway

Compute normalization statistics from training data, then reuse those values for validation and test. As the learner put it, this avoids “leaks to the tests.”

## Question to revisit

Why does a generator need to be recreated for each training epoch?
