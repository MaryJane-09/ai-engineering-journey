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

Open a scratch Python file, enter the code below, and save it:

```python
def greet(name: str) -> None:
    print(name)

greet(42)
```

Pylance should flag the integer argument where a string is expected. To check formatting, change the last line to `greet( 42 )` and save; Black should remove the extra spaces.

## Observed result so far

The learner installed Remote SSH, Black Formatter, and Ruff. Running `python3 code_1.py` printed `42`. This confirms Python executed the function; Python type annotations do not enforce argument types at runtime.

Pylance reported that argument `Literal[42]` cannot be assigned to the `str` parameter `name`. This confirms the editor detected the type mismatch before execution.

## Observed result

Pylance showed the expected type warning: `Literal[42]` could not be assigned to the `str` parameter. After saving with Black, the call changed from `greet(  42  )` to `greet(42)`. The learner also ran the function with Python and observed `42`.

**Status: Complete.** The scratch test confirmed editor-time type diagnostics and format-on-save.
