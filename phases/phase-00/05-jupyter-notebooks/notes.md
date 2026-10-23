# SE 00 Lesson 05: Jupyter Notebooks

These study notes summarize the [official Jupyter Notebooks lesson](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/00-setup-and-tooling/05-jupyter-notebooks). The notebook artifact in this directory records the learner's small arithmetic exercise; it is not a copy of the full course lesson.

## What notebooks are

A Jupyter notebook (`.ipynb`) is an interactive document made of cells. Code cells run Python and can show results inline; Markdown cells hold formatted notes. A **kernel** is the Python process that runs code cells. Cells in one notebook share that process and its memory, so a variable created by one cell can be used by another.

This shared state makes experimentation convenient, but it can hide dependencies. If a later cell uses a variable from an earlier cell, running them out of order can make the notebook behave differently. Restarting the kernel clears its memory. Restart and Run All checks whether the notebook can recreate its results from the first cell onward.

## The recorded exercise

The first exercise used this expression:

```python
20 * 9 / 5 + 32
```

The learner ran it and observed `68.0`. Jupyter displays the value of a cell's final expression automatically. The notebook was then extended with Markdown notes and the variable-based experiment below; see [`notebook-basics.ipynb`](notebook-basics.ipynb).

The learner extended the notebook with an assignment cell and a conversion cell:

```python
temperature_c = 20
temperature_c * 9 / 5 + 32
```

After restarting the kernel and running only the conversion cell, the learner observed `NameError: name 'temperature_c' is not defined`. Running all cells from the top produced `68.0`. The learner explained that the first cell creates `temperature_c` in the kernel before the conversion cell uses it. This is direct evidence of how shared kernel state depends on cell execution order.

## Timing code

Jupyter provides magic commands that are interpreted by the notebook environment rather than by ordinary Python:

- `%timeit expression` runs a short expression repeatedly and reports timing statistics. Use it to compare small operations.
- `%%time` runs the whole cell once and reports elapsed time. Use it for a longer operation, such as a training run.

## Notebook or script?

Use notebooks to explore data, prototype an idea, visualize results, and explain an experiment. Move code into a `.py` script when it becomes a reusable utility, a training pipeline, or production code. In short: explore in notebooks, ship in scripts.

## Run the artifact

The project `.venv` needs JupyterLab installed. From the repository root:

```bash
uv pip install --python .venv/bin/python jupyterlab
source .venv/bin/activate
jupyter lab phases/phase-00/05-jupyter-notebooks/notebook-basics.ipynb
```

This installs JupyterLab into the project environment, activates that environment, and opens the notebook. The notebook format is shared by JupyterLab, classic Jupyter Notebook, and VS Code's Jupyter extension.

## Common traps

- **Out-of-order execution:** a cell may depend on a variable created by a cell run earlier. Restart and Run All checks a clean top-to-bottom run.
- **Hidden stale state:** deleting or changing a cell does not remove variables already held in the kernel. Restart the kernel to clear them.
- **Keeping production code only in a notebook:** move reusable logic and scheduled or production work into scripts or modules.

## Self-check

1. What does the kernel do, and why do cells share its state?
2. Why can running cells out of order make a notebook fail from the top?
3. When is `%timeit` a better fit than `%%time`?
4. When should exploratory code move to a Python script?

## Your recorded progress

The progress log records a 3/3 quiz. The learner explained that a cell cannot use a variable before it exists, that restarting clears stale kernel state, chose `%timeit` for a short comparison, and identified reusable code as a reason to use a script. In the follow-up experiment, the learner saw the expected `NameError`, ran all cells from the top, and got `68.0`. See [`LEARNING.md`](../../../LEARNING.md), entry for 2026-10-23, SE 00/05 and the completed between-lesson practice row.
