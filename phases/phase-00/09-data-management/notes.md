# SE 00 Lesson 09: Data Management

These notes summarize the [official Data Management lesson](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/00-setup-and-tooling/09-data-management). The fixed-seed split exercise is pending; see [`experiment.md`](experiment.md).

## Loading, caching, and streaming

Hugging Face's `datasets` library can download a dataset from the Hub, cache it locally, convert formats, and create splits. A cached dataset can load locally on later runs. Use `streaming=True` for very large datasets: it yields rows on demand without downloading the full dataset first, so memory use does not grow with the whole dataset size.

## Formats

- **CSV:** readable and widely supported, but often larger and slower for analytics.
- **JSON:** useful for APIs and nested records, but often larger and slower to scan.
- **Parquet:** compressed, columnar storage; usually smaller and faster when reading selected columns. A strong default for stored ML datasets.
- **Arrow:** an in-memory columnar format used internally by `datasets` for fast processing.

## Train, validation, and test

- **Train:** examples used to fit model parameters.
- **Validation:** examples used during development to compare choices and tune settings.
- **Test:** held out until final evaluation to estimate performance on data not used for training or tuning.

Set a fixed random seed when splitting data so the same rows go into each split again. Reproducibility and data separation solve different problems: a seed repeats the split, while a held-out test set provides an independent final check.

### A 20-row example

Imagine rows numbered 0 through 19. Shuffle them with seed `42`, then assign 14 rows to train, 3 to validation, and 3 to test. Running the same shuffle and assignment again with seed `42` puts the same row IDs in each group. Training uses the first group to learn; validation guides choices during development; the test group stays unused until final evaluation. Changing the seed changes the assignment, but it does not change what each split is for.

## Large files and versioning

Do not commit downloaded model weights and large datasets as ordinary Git blobs. Use `.gitignore` for re-fetchable local files. Git LFS stores large files outside the Git object database while tracking pointers in the repository. DVC tracks dataset versions with small pointer files in Git and stores the data in remote storage; use it when exact data versions need to be reproduced across machines. For this course, `.gitignore` is usually enough.

## Learner evidence and review

The learner linked fixed seeds to reproducible splits and identified DVC as useful for reproducing experiments across machines. After clarification, they explained: “The seed makes the shuffle repeatable and test is for so it can give you a fair final check.” They ran the 20-row split twice and observed identical 14/3/3 sizes and identical row groups. Review Parquet versus CSV. Quiz score: 2/3.
