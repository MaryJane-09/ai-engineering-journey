# SE 00 Lesson 02: Git & Collaboration

These study notes explain the [official Git & Collaboration lesson](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/00-setup-and-tooling/02-git-and-collaboration). The course lesson is the source for the workflow and terminology below. The learner's progress record is kept separate at the end.

## What you should learn

The lesson teaches how to set a Git identity, save and publish work with `add`, `commit`, and `push`, isolate experiments on branches, ignore generated or large files, and inspect project history with `git log`.

This matters because experiments change code. Version control gives you named snapshots you can revisit and a separate remote copy you can use for backup and collaboration. Branches let you try an idea without moving the main line of work until you choose to merge it.

## The Git workflow

The course describes four places a change can occupy:

1. **Working directory:** the files you are editing.
2. **Staging area:** the selected changes prepared for the next snapshot.
3. **Local repository:** committed snapshots and their history.
4. **Remote repository:** a hosted copy such as GitHub.

The standard direction is working directory → staging area → local commit → remote push. `git add` selects changes for staging; it does not create a commit or upload anything. `git commit` records the staged snapshot locally. `git push` sends local commits to the remote. This is why “saved locally” and “backed up on GitHub” are separate states.

## Step-by-step daily workflow

First inspect the working tree, then stage the file you intend to include, commit it with a useful message, and push the branch:

```bash
git status
git add file.py
git commit -m "Add perceptron implementation"
git push origin main
```

`git status` shows changed, staged, and untracked files. `git add file.py` stages that path. The commit message summarizes the snapshot. `origin` names the remote and `main` is the branch being pushed in this example. Review the status before staging so you know what the next commit will contain. The course presents this as the daily sequence, not as a command to run blindly in every repository.

## Isolate an experiment with a branch

```bash
git checkout -b experiment/new-optimizer
# Make and commit the experiment's changes here.
git checkout main
git merge experiment/new-optimizer
```

`git checkout -b` creates a branch at the current commit and switches to it. Commits made on that branch advance its history without advancing `main`. When you are satisfied, switch to `main` and merge the experiment branch so its changes become part of the main line.

A branch is not a separate full copy of every file; in the lesson's terminology it is a pointer to a commit that moves forward as you work. This model explains why branches are cheap and why an experimental commit stays separate until merged.

## Work with the course repository

The official repository is not writable by every learner. The lesson's workflow is to fork it on GitHub, clone your fork, create a personal branch, and push that branch to your fork:

```bash
git clone https://github.com/YOUR-USERNAME/ai-engineering-from-scratch.git
cd ai-engineering-from-scratch
git checkout -b my-progress
# Work through lessons and commit your files.
git push origin my-progress
```

Replace `YOUR-USERNAME` with the account that owns the fork. In this setup, `origin` points at your fork, so pushing your branch does not attempt to write to the course maintainers' repository.

## Keep generated files out of Git

The lesson asks learners to create `.gitignore` patterns for model checkpoint files such as `.pt`, `.pth`, and `.safetensors`. These files can be large and are often generated; ignoring them keeps them out of the normal untracked-file list and prevents accidental commits. A `.gitignore` pattern only controls files Git is not already tracking; the lesson's exercise checks that newly created matching files do not appear as untracked changes.

Example patterns from the lesson's exercise:

```gitignore
*.pt
*.pth
*.safetensors
```

## Read the history

```bash
git log --oneline
git log --oneline -- phases/00-setup-and-tooling
git show --stat <hash>
```

`git log --oneline` gives a compact list of commits. Adding a path limits history to commits that changed that part of the repository. `git show --stat` summarizes which files a chosen commit touched. Together, these commands help you understand how the project evolved without opening every file.

## Common mistakes and lesson scope

- **Confusing add, commit, and push:** they operate at different stages. Staging is not saving a snapshot; committing is local; pushing publishes commits to the remote.
- **Working directly on the main line during an experiment:** create a branch first so the experiment remains isolated until merge.
- **Pushing to the upstream course repository:** fork it first and push to your own fork.
- **Committing model checkpoints accidentally:** add the relevant patterns to `.gitignore`, then inspect `git status`.
- **Assuming a branch is an independent full copy:** it is a movable pointer to a commit, according to the lesson's key terms.

The lesson introduces branch creation and merging but does not teach merge-conflict resolution, rebasing, or advanced history editing. It explicitly says those advanced commands are not needed for this course. If a merge conflict occurs, this lesson alone does not give a full resolution procedure.

## Key takeaways

- `git add` stages selected changes; `git commit` records a local snapshot; `git push` publishes commits to a remote.
- Use branches to keep experiments separate from `main` until you decide to merge them.
- Fork repositories you cannot write to and push your work to your fork.
- Use `.gitignore` for generated artifacts and `git log` / `git show` to inspect history.

## Self-check

1. What changes after `git add`, and what does not happen yet?
2. Which step creates a local snapshot? Which step sends it to GitHub?
3. Why does a branch help contain an experiment?
4. Why should a learner fork the course repository before pushing?
5. What do `git log --oneline -- <path>` and `git show --stat <hash>` help you inspect?

## Your recorded progress

The progress log records a 3/3 quiz and says the learner explained that `git add` stages without committing or pushing and that branches keep experimental commits on a separate line. It does not claim a particular fork, branch, or Git experiment was completed. See [`LEARNING.md`](../../../LEARNING.md), entry for 2026-10-23, SE 00/02.
