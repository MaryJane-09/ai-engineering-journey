# SE 00 Lesson 01: Experiment

## Recorded work

The learning record says the beginner verifier passed with **2/2**, PyTorch, NumPy, Matplotlib, and Jupyter were installed and tested in `.venv`, and Hello World ran in Python, TypeScript, Rust, and Julia. The learner also reviewed the four-layer stack and virtual environments.

## Result and limits

CPU-only PyTorch was available; CUDA was unavailable on the learner's hardware. The exact verifier command and terminal output were not preserved in this repository, so this file is a record of the progress log rather than a command transcript.

## Reproducible run

The official lesson's beginner verifier is documented in the [lesson notes](notes.md). Run its command from the course repository root if that checkout is available. Preserve the command, exit status, and meaningful output here when repeating it.

## Phase 0 practice exercise

### Question 1 — Environment report

Create `environment_report.py` in this lesson folder. Write a script that prints the Python version, active interpreter path, NumPy version, and whether PyTorch reports CUDA as available. Run it with `python3 phases/phase-00/01-dev-environment/environment_report.py` from the repository root, then bring back the script and its output.

**First attempt:**

```python
import torch
import numpy as np
import pytz as py
print(f"Python available: {py.__version__}")
print (f"Numpy version: {np.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")
```

**Feedback:** NumPy and CUDA checks are present. `pytz` is a time-zone library, not the Python runtime; use Python's `sys` module for `sys.version` and `sys.executable`. The active interpreter path is missing, and no run output has been provided yet.

**Run attempt:** Running `environment_report.py` with the current interpreter failed at `import torch` with `ModuleNotFoundError: No module named 'torch'`. This interpreter is not the repository `.venv` recorded in the earlier setup evidence, or PyTorch is no longer installed there.

**Final answer:** The script reports Python and NumPy versions, CUDA availability, and the active interpreter path:

```python
import torch
import numpy as np
import sys

print(f"Python available: {sys.version}")
print(f"Numpy version: {np.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")
print(f"Interpreter path: {sys.executable}")
```

Run from the repository root with `.venv/bin/python phases/phase-00/01-dev-environment/environment_report.py`.

Output:

```text
Python available: 3.12.16 (main, Oct 26 2026, 14:08:45) [Clang 23.1.3 ]
Numpy version: 2.5.4
CUDA available: False
Interpreter path: /home/jane/ai/ai-engineering-journey/.venv/bin/python
```

The initial run with the shell's default interpreter failed because PyTorch was unavailable there. Using the repository `.venv` resolved the issue. The output also confirms this environment currently reports no CUDA GPU.

### Editor warning follow-up

The learner later added `# type: ignore` to the PyTorch and NumPy imports because the editor showed import warnings. After selecting `/home/jane/ai/ai-engineering-journey/.venv/bin/python` as the editor interpreter, the warnings disappeared and the learner removed the suppressions. This confirmed the editor had been analyzing the file with the wrong interpreter.
