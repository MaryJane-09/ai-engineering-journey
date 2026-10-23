# SE 00 Lesson 01: Dev Environment

These are study notes based on the [official Dev Environment lesson](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/00-setup-and-tooling/01-dev-environment). They explain the course material in a reference format; they are not copies of the lesson's verifier output or the learner's original setup files.

## What you should learn

The lesson aims to help you set up Python, Node.js, and Rust; use virtual environments and package managers; check GPU access; and understand the four layers of an AI engineering environment. Julia is also introduced as an optional runtime for math-heavy work.

This matters because later lessons rely on these tools. A missing library, mismatched runtime, or unsuitable GPU build can look like a problem in the lesson code when the actual problem is the environment underneath it.

## The four-layer stack

The course's model is easiest to understand from the bottom up:

1. **System foundation:** operating system, shell, Git, editor, and GPU drivers. These provide the machine and basic tools.
2. **Package managers:** `uv`, `pnpm`, `cargo`, and Julia's package manager. They install language packages and tools.
3. **Language runtimes:** Python, Node.js (which runs JavaScript and, with tools, TypeScript), Rust, and Julia. A runtime executes programs written in its language.
4. **AI/ML libraries:** PyTorch, JAX, and Transformers. These depend on a runtime and its packages.

The dependency direction explains the install order: libraries need runtimes, and runtimes need the system. The lesson recommends installing bottom-up and adding later tools when a lesson needs them rather than installing the entire future stack at once.

## Build the environment in the lesson's order

Run these commands in a course checkout and adapt the platform-specific system commands to your machine. The official lesson gives macOS, Ubuntu/Debian, and Windows through WSL2 examples.

### 1. Prepare the system

On Ubuntu or Debian, the lesson uses:

```bash
sudo apt update
sudo apt install -y build-essential git curl wget unzip
```

`apt update` refreshes package metadata; `apt install` adds the compiler/build tools and utilities used by later installers. `unzip` matters on Linux because the lesson's `fnm` installer needs it. On macOS, the course instead uses Xcode command-line tools and Homebrew. On Windows, it recommends WSL2 with Ubuntu.

### 2. Install Python and isolate packages

The course uses `uv` for Python installation and package management:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv python install 3.12
uv venv
source .venv/bin/activate
uv pip install numpy matplotlib jupyter
```

The first command installs `uv`; `uv python install` installs Python 3.12; `uv venv` creates a project-local `.venv`; activation makes that environment's Python and packages the current shell's defaults; and `uv pip install` adds the listed packages to it. On Windows, the lesson gives `.venv\Scripts\activate` as the activation form.

A virtual environment keeps project packages separate from other Python projects. This makes it easier to reproduce the lesson setup and reduces version conflicts. The lesson's small verification snippet prints the Python and NumPy versions, creates `[1, 2, 3]`, and computes its dot product with itself (`14`). A different version number is normal; import errors indicate that the package may not be installed in the active environment.

### 3. Install Node.js for TypeScript work

```bash
curl -fsSL https://fnm.vercel.app/install | bash
fnm install 22
fnm use 22
npm install -g pnpm
node -e "console.log('Node', process.version)"
```

`fnm` manages Node versions; these commands install and select Node 22. `pnpm` is the package manager the course uses for TypeScript projects. The final command prints the active Node version, so you can check which runtime your shell selected.

If the installer reports `Not installing fnm due to missing dependencies.`, the lesson says Linux needs `unzip`; install it using the system package manager and retry. On Apple Silicon when running under Rosetta, the lesson gives an arm64 Homebrew install and shell initialization sequence. That is a platform-specific fix, not a standard step for every Mac.

### 4. Install Rust and optionally Julia

The Rust installer is followed by version checks:

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
rustc --version
cargo --version
```

`rustc` is the compiler and `cargo` is Rust's package/build tool. The lesson includes Julia as optional:

```bash
curl -fsSL https://install.julialang.org | sh
julia -e 'println("Julia ", VERSION)'
```

The `-e` option asks Julia to evaluate the quoted expression and print its version.

### 5. Choose a PyTorch build for the available hardware

For an NVIDIA GPU, the lesson demonstrates this CUDA-enabled PyTorch install on Linux (on Windows, use the matching command from the PyTorch selector):

```bash
uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
```

The `--index-url` selects the course example's CUDA 12.4 wheel index. On Apple Silicon, install the plain PyTorch build instead:

```bash
uv pip install torch torchvision torchaudio
```

The plain build includes MPS support, and the lesson specifically warns not to use the Linux/Windows CUDA wheel index on Mac. CUDA is NVIDIA's GPU platform; MPS is Apple's Metal backend. A Mac without CUDA is expected, not a failed setup.

Check what PyTorch can use:

```python
import torch

print(f"CUDA available: {torch.cuda.is_available()}")
print(f"MPS available:  {torch.backends.mps.is_available()}")
if torch.cuda.is_available():
    print(f"GPU: {torch.cuda.get_device_name(0)}")
```

The Boolean checks distinguish available accelerators. The GPU name is printed only when CUDA is available. If neither accelerator is available, the lesson says most early lessons can still run on CPU; later training-heavy work can use Colab or a cloud GPU.

### 6. Run the route preflight

From the root of the course checkout (the directory containing its `README.md` and `phases/`), run:

```bash
python3 phases/00-setup-and-tooling/01-dev-environment/code/verify.py --route beginner
```

The route option limits checks to what the selected route needs. The lesson says a successful beginner preflight prints a ready message and the next runnable lesson command. A failed required check reports a detected path or import error and a corrective command; fix the first required failure and rerun. Optional later tools do not block the selected route. Other route names and `--show-later` are documented in the official lesson.

## Common mistakes the lesson warns about

- Installing packages into a different Python than the one running the lesson: activate `.venv` before installing and running Python commands.
- Treating a missing GPU as a setup failure: CPU is sufficient for many lessons.
- Installing a CUDA-only wheel on Apple Silicon: use the plain PyTorch build there.
- Missing `unzip` on Linux before using `fnm`: add it, then rerun the installer.
- Installing every tool for all future phases immediately: use the preflight for the chosen route and install later tools when needed.

## Scope notes

The lesson provides platform setup commands and preflight checks, but it does not promise that every hardware/driver combination will work with one generic CUDA install command. It directs Windows learners to the PyTorch selector and recommends using each preflight's specific corrective command. When a failure does not match those cases, use the reported error and the relevant vendor documentation rather than guessing a fix.

## Key takeaways

- Work bottom-up through system, package managers, runtimes, and AI libraries.
- Use a project-local Python environment so dependencies stay isolated.
- Select a GPU-capable framework build that matches the actual hardware; CPU-only is still a valid starting point.
- Run the course preflight from the course root and act on required failures before starting the route.

## Self-check

1. Why should the environment layers be installed bottom-up?
2. What does activating `.venv` change for the current shell?
3. Why is CUDA unavailable on Apple Silicon not itself an error?
4. What information does the beginner route preflight give you?

## Your recorded progress

The learning record says the beginner verifier passed (2/2), the listed Python libraries were installed and tested in `.venv`, Hello World ran in Python, TypeScript, Rust, and Julia, and the four-layer stack and virtual environments were reviewed. It records CPU-only PyTorch and CUDA unavailable on the learner's hardware. These are progress-log claims, not attached original command output. See [`LEARNING.md`](../../../LEARNING.md), entry for 2026-10-22, SE 00/01.
