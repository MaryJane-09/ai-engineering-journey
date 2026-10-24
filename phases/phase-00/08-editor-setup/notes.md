# SE 00 Lesson 08: Editor Setup

These notes summarize the [official Editor Setup lesson](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/00-setup-and-tooling/08-editor-setup). The exercise is complete; see [`experiment.md`](experiment.md) and the retained [`editor-check.py`](editor-check.py) artifact.

## Useful editor support

For Python and AI work, VS Code extensions can provide language support, notebook execution, type checking, formatting, linting, Git history, debugging, and remote access. This workspace has VS Code, Python, Pylance, and Debugpy installed. The lesson also recommends Jupyter, GitLens, Remote SSH, Black Formatter, and Ruff.

Pylance uses the Language Server Protocol (LSP) to provide completions, type information, and diagnostics in the editor. `python.analysis.typeCheckingMode: "basic"` enables checks that can flag some wrong argument types and API mistakes before code runs.

## Settings that reduce friction

- `editor.formatOnSave: true` runs the configured formatter when a file is saved. Select Black as the default formatter for Python.
- `notebook.output.scrolling: true` keeps large training-loop output from expanding the notebook panel without limit.
- Integrated terminals support running scripts and monitoring remote machines.
- Remote SSH connects the local editor UI to a server component on a remote machine. Code and commands run on the remote machine, which is useful for GPU servers.

## Learner evidence and review

The learner correctly stated that code runs on the remote machine when using Remote SSH. They installed Remote SSH, Black Formatter, and Ruff, and ran the scratch function with Python; it printed `42`. Pylance flagged `Literal[42]` as incompatible with the parameter type `str`, and saving with Black changed `greet(  42  )` to `greet(42)`. The learner was unsure why notebook output scrolling is useful and what basic type checking catches. Quiz score: 1/3; review those two settings and their purposes.
