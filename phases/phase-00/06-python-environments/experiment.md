# SE 00 Lesson 06: Environment Isolation Experiment

## Goal

Show that installing a package in a second virtual environment does not change the package version in the repository's `.venv`.

## Procedure

From the repository root, create a separate environment and install a pinned NumPy version:

```bash
uv venv /tmp/ai-journey-env-check
uv pip install --python /tmp/ai-journey-env-check/bin/python "numpy==1.26.4"
```

Print the NumPy versions and interpreter paths from both environments:

```bash
.venv/bin/python -c "import sys, numpy; print(sys.executable); print(numpy.__version__)"
/tmp/ai-journey-env-check/bin/python -c "import sys, numpy; print(sys.executable); print(numpy.__version__)"
```

## Expected observation

The second interpreter should report NumPy `1.26.4`; the repository `.venv` should retain its own installed version. The interpreter paths should point into their respective environments.

## Observed result

The learner created `.venv-a` and installed NumPy 1.26.4 there. The repository environment reports NumPy 2.5.4. The interpreter paths were `/home/student/projects/ai-engineering-journey/.venv/bin/python` and `/home/student/projects/ai-engineering-journey/.venv-a/bin/python`, respectively. The different package versions and paths demonstrate that the environments are isolated.
