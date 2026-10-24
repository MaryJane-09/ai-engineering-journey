# SE 00 Lesson 08: Editor Setup Exercise

## Goal

Use Pylance to catch a type mismatch before running code, and use Black to format Python code on save.

## Install missing extensions

Python, Pylance, and Debugpy are already available in the workspace. In a terminal, install the other recommended extensions:

```bash
code --install-extension ms-toolsai.jupyter
code --install-extension eamodio.gitlens
code --install-extension ms-vscode-remote.remote-ssh
code --install-extension ms-python.black-formatter
code --install-extension charliermarsh.ruff
```

## Configure VS Code

Open **Preferences: Open User Settings (JSON)** from the Command Palette and add these settings, preserving any existing settings:

```json
{
  "python.analysis.typeCheckingMode": "basic",
  "editor.formatOnSave": true,
  "notebook.output.scrolling": true,
  "[python]": {
    "editor.defaultFormatter": "ms-python.black-formatter"
  }
}
```

## Check the setup

Open [`editor-check.py`](editor-check.py) in VS Code. Its `greet` parameter is annotated as `str`, while the call passes the integer `42`; Pylance should flag the mismatch. To check formatting, temporarily change the call to `greet( 42 )` and save; Black should remove the extra spaces.

Run it from the repository root with `python3 phases/phase-00/08-editor-setup/editor-check.py`; it prints `42`. The type annotation is for editor-time checking and does not stop Python from running the call.

To repeat the formatting check, temporarily change the call to `greet( 42 )`, save, and verify Black changes it back to `greet(42)`.

## Observed result

Pylance showed the expected type warning: `Literal[42]` could not be assigned to the `str` parameter. After saving with Black, the call changed from `greet(  42  )` to `greet(42)`. The learner also ran the function with Python and observed `42`.

**Status: Complete.** The retained script reproduces the type warning; the format-on-save observation is recorded above.
