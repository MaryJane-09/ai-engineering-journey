# SE 00 Lesson 12: Reflection

## Learner reflection

The learner identified the data loader as the place to investigate when profiling shows data loading dominates. For NaN loss, they chose checking gradients and adding a `breakpoint()` at the failure point. They missed the quiz questions on data leakage and common time-profile findings.

## Takeaway

Profiling locates time and memory costs; debugging checks whether the computation is behaving correctly. A fast or successful run is not proof that model results are valid.

## Question to revisit

What evidence would make 99% test accuracy suspicious?
