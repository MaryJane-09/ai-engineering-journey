# SE 00 Lesson 09: Reflection

## Learner reflection

The learner connected a fixed seed with reproducible splits and identified DVC as a way to reproduce experiments with versioned data across machines. After clarification, they stated that the seed repeats the shuffle and the test split provides a fair final check.

## Takeaway

A fixed seed repeats the partition. A held-out test split measures the model after training and tuning are complete.

## Question to revisit

Why is Parquet usually a better storage format for ML datasets than CSV?
