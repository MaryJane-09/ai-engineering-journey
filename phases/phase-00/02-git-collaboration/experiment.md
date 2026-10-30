# SE 00 Lesson 02: Experiment

## Recorded evidence

The learner scored **3/3** and explained that `git add` stages changes without committing or pushing them, and that a branch keeps experimental commits on a separate line. The progress record does not say that a branch exercise was run.

## Practice experiment

### Question 2 — Branch workflow

Use a disposable repository at `/tmp/git-practice`. Initialize a `main` branch, configure a local practice-only Git name and email if needed, create and commit `hello.py`, then create an `experiment` branch, change the file, and commit again. Inspect `git status` and `git log --oneline --all --decorate --graph`. Do not push this temporary repository.

In your answer, include the command sequence and explain which commit each branch points to and whether the experiment commit changed `main`.

**Answer and evidence:** The learner ran the branch exercise and reported:

```text
* bc409f3 (experiment) add experiment line
* 70a6d0f (HEAD -> main) add hello script
```

The learner explained that `experiment` contains the experiment commit. `main` still points to `70a6d0f`; the branch commit does not move `main` unless the branches are merged. The temporary repository was not pushed.

## Status

Quiz evidence and this hands-on branch experiment are recorded as complete.
