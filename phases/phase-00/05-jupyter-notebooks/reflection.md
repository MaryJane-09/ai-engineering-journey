# SE 00 Lesson 05: Reflection

## Learner reflection

The learner explained that after restarting the kernel, running only the conversion cell fails because `temperature_c` has not been recorded in memory. Running all cells from the top first declares the variable, so the later conversion can use it.

## Takeaway

Notebook cells share the kernel's memory. Their displayed order alone does not guarantee the order in which they were run; restarting and running all cells checks that the notebook can rebuild its state in sequence.

## Question to revisit

When an experiment is stable and its code is useful in more than one place, what parts should move into a Python module or script?
