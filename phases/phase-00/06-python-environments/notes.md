# SE 00 Lesson 06: Python Environments

These notes summarize the [official Python Environments lesson](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/00-setup-and-tooling/06-python-environments). The learner completed the environment isolation experiment; see [`experiment.md`](experiment.md).

## Why isolate dependencies

Projects can require different versions of Python packages. A virtual environment gives a project its own interpreter context and installed packages, so installing or upgrading a package in one environment does not change another. A project `.venv` should not be committed; record dependencies in project configuration and lockfiles instead.

Create an environment with `uv venv` or Python's built-in `python -m venv`. Activate it before installing packages, or explicitly target its interpreter. Check the active interpreter with `which python` or `python -c "import sys; print(sys.executable)"`; a version command such as `python --version` does not tell you which environment supplied Python.

## Dependency declarations and lockfiles

`pyproject.toml` describes project metadata and dependencies, often with version ranges. A lockfile records the exact resolved versions, including transitive dependencies, so installs can reproduce a consistent package set. A lockfile guides installation; it does not itself contain or install the packages.

## Choosing a tool

- Use `uv` or built-in `venv` for ordinary Python package isolation.
- Conda can also manage non-Python dependencies such as CUDA toolkits and system libraries. Prefer one package manager within a Conda environment; pip changes may bypass Conda's dependency tracking and create conflicts.
- Separate environments by project or by phase when dependencies conflict or differ substantially.

## Troubleshooting

- **Wrong interpreter:** inspect `sys.executable` and ensure it points inside the intended `.venv`.
- **Package conflicts:** check the environment and package manager used for each install; avoid mixing Conda and pip unless necessary.
- **CUDA unavailable in PyTorch:** compare driver support reported by `nvidia-smi` with the CUDA version PyTorch was built for, available as `torch.version.cuda`. Driver and build compatibility matters; the version strings are not interchangeable.
- **Environment in Git:** ignore `.venv/`; commit dependency declarations and the appropriate lockfile instead.

## Learner evidence and review

The learner identified `.venv` as the isolation mechanism and correctly described a lockfile as supporting dependency reuse. The experiment showed NumPy 1.26.4 in `.venv-a` and NumPy 2.5.4 in the repository `.venv`. The learner initially thought installing into a second environment would change the existing environment, and named `python3 --version` as a way to identify the active environment. Review interpreter-path checks, package-manager conflicts, and CUDA compatibility. Quiz score: 0/3.
