# My AI Engineering Path
<!-- Managed by the ai-engineering-from-scratch learning skills.
     Repo: https://github.com/rohitg00/ai-engineering-from-scratch -->

## Mission
I want to become a very capable AI engineer who understands the fundamentals and everything else involved, not just how to use AI tools. I want to learn the mathematics, Python, machine learning, LLMs, RAG, and AI agents well enough to build reliable, useful AI products independently. I want to build a future where I can be confident and reliable with my skills, and build world-changing projects confidently. Build goal: not sure yet.

## Placement
- Date: 2026-10-22
- Score: 2/10 (Math & Statistics 0/2, Classical ML 0/2, Deep Learning 0/2, NLP & Transformers 1/2, Applied AI 1/2)
- Assessment preserved: Math & Statistics 0/2; Classical ML 0/2; Deep Learning 0/2; NLP & Transformers 1/2; Applied AI 1/2. Use the zero-score areas for extra support when those topics arise; placement does not change the requested lesson order.
- Entry point: Official roadmap, from SE 00 — Setup & Tooling
- Pace: ~10 hours/week

## Official roadmap
Source: [official course README and Contents](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/README.md#contents). The installed course material in this workspace does not include the course `README.md`, `ROADMAP.md`, or `phases/` lesson files; the official online README was consulted for the roadmap and the first lesson.

Study rule: follow every phase and lesson in the published order, starting at SE 00. Do not skip or reorder based on placement results. Verify lesson titles and sequence against the official course source as each phase is reached; do not invent missing titles. Advance only after the learner demonstrates understanding and completes the lesson assessment/exercises.

Phases, in official order: SE 00 — Setup & Tooling; 01 — Math Foundations; 02 — ML Fundamentals; 03 — Deep Learning Core; 04 — Computer Vision; 05 — NLP; 06 — Speech & Audio; 07 — Transformers; 08 — Generative AI; 09 — Reinforcement Learning; 10 — LLMs from Scratch; 11 — LLM Engineering; 12 — Multimodal; 13 — Tools & Protocols; 14 — Agent Engineering; 15 — Autonomous Systems; 16 — Multi-Agent & Swarms; 17 — Infrastructure & Production; 18 — Ethics & Alignment; 19 — Capstone Projects.

### Lesson order and progress
Only the complete SE 00 lesson list is recorded here so far; later phase lesson titles will be added from the official source as each phase is reached.

| Phase | # | Official lesson | Status |
|-------|---:|----------------|--------|
| SE 00 — Setup & Tooling | 01 | Dev Environment | **Completed** |
| SE 00 — Setup & Tooling | 02 | Git & Collaboration | **Completed** |
| SE 00 — Setup & Tooling | 03 | GPU Setup & Cloud | **Completed** |
| SE 00 — Setup & Tooling | 04 | APIs & Keys | **Completed** |
| SE 00 — Setup & Tooling | 05 | Jupyter Notebooks | **Completed** |
| SE 00 — Setup & Tooling | 06 | Python Environments | **Completed** |
| SE 00 — Setup & Tooling | 07 | Docker for AI | **Completed** |
| SE 00 — Setup & Tooling | 08 | Editor Setup | **Completed** |
| SE 00 — Setup & Tooling | 09 | Data Management | **Completed** |
| SE 00 — Setup & Tooling | 10 | Terminal & Shell | **Completed** |
| SE 00 — Setup & Tooling | 11 | Linux for AI | **Completed** |
| SE 00 — Setup & Tooling | 12 | Debugging & Profiling | Not started |
| SE 00 — Setup & Tooling | 13 | Python for AI Engineering | Not started |

## Progress log
| Date | Lesson | Quiz | Note |
|------|--------|------|------|
| 2026-10-22 | [SE 00/01 Dev Environment](phases/phase-00/01-dev-environment/notes.md) | — | Passed beginner verifier (2/2); installed and tested PyTorch, NumPy, Matplotlib, and Jupyter in `.venv`; successfully ran Hello World in Python, TypeScript, Rust, and Julia; reviewed virtual environments and the four-layer stack. CPU-only PyTorch; CUDA unavailable on current hardware. |
| 2026-10-23 | [SE 00/02 Git & Collaboration](phases/phase-00/02-git-collaboration/notes.md) | 3/3 | Explained that `git add` stages changes without committing or pushing them, and that branches keep experimental commits on a separate line. |
| 2026-10-23 | [SE 00/03 GPU Setup & Cloud](phases/phase-00/03-gpu-setup-cloud/notes.md) | 3/3 | Explained that CPU workloads use system RAM, CUDA selects an available NVIDIA GPU, GPU timing requires synchronization, and fp16 needs about 2 bytes per parameter before training overhead. |
| 2026-10-23 | [SE 00/04 APIs & Keys](phases/phase-00/04-apis-keys/notes.md) | 3/3 | Explained API key purpose, `.env` loading and ignore rules, what the SDK handles, 401 errors, and 429 rate limits. Created the troubleshooting artifact; live API call deferred because it requires separate API billing. |
| 2026-10-23 | [SE 00/05 Jupyter Notebooks](phases/phase-00/05-jupyter-notebooks/notes.md) | 3/3 | Initially unsure why notebook cells depend on execution order; then explained that a later cell cannot use a variable until it exists, and that restarting clears stale kernel state. Ran `20 * 9 / 5 + 32` in Jupyter and got `68.0`; chose `%timeit` for short comparisons and scripts for reusable code. |
| 2026-10-24 | [SE 00/06 Python Environments](phases/phase-00/06-python-environments/notes.md) | 0/3 | Recognized that a lockfile preserves dependencies and that separate `.venv` folders isolate packages; reviewed how to confirm the active interpreter, why pip and Conda can conflict, and how to check CUDA compatibility. Requested shorter lessons with key questions and explicit explanations in the notes. |
| 2026-10-24 | [SE 00/07 Docker for AI](phases/phase-00/07-docker-for-ai/notes.md) | 0/3 | Reviewed image versus container, host-to-container volume mounts, NVIDIA GPU access, and Compose service-name networking. Asked for explicit explanation of the mount paths and requested concise lessons. |
| 2026-10-24 | [SE 00/08 Editor Setup](phases/phase-00/08-editor-setup/notes.md) | 1/3 | Correctly identified that Remote SSH runs code on the remote machine. Installed Remote SSH, Black Formatter, and Ruff; Python printed `42`, Pylance flagged `Literal[42]` as incompatible with `str`, and saving with Black changed the call to `greet(42)`. |
| 2026-10-24 | [SE 00/09 Data Management](phases/phase-00/09-data-management/notes.md) | 2/3 | Correctly identified that a fixed seed makes splits reproducible and that DVC supports versioned data for reproducible experiments. Clarified that a separate test split is for final evaluation; review Parquet's advantages over CSV. |
| 2026-10-24 | [SE 00/10 Terminal & Shell](phases/phase-00/10-terminal-and-shell/notes.md) | 2/3 | Explained that `> output.log 2>&1` captures both normal output and errors. `tmux` is unavailable in this environment; review detach/reattach sessions and SSH local port forwarding. |
| 2026-10-24 | [SE 00/11 Linux for AI](phases/phase-00/11-linux-for-ai/notes.md) | 0/3; repeated items 3/3; fresh retake 1/3 | On the repeated questions, corrected all three initial misses. In the fresh retake, answered `rsync` correctly; review `~` for the home directory and the `apt update`/`apt install` sequence. |

## Between-lesson practice

| Lesson | Task | Evidence to bring back | Status |
|--------|------|------------------------|--------|
| SE 00/05 Jupyter Notebooks | See `phases/phase-00/05-jupyter-notebooks/experiment.md`: add a Markdown cell and assignment/conversion cells, run all; restart and run the conversion first; then rerun from the top. | The learner saw `NameError: name 'temperature_c' is not defined` when running the conversion first, then got `68.0` after running from the top. They explained that the assignment cell creates the variable in kernel memory before the conversion cell uses it. | **Complete** |
| SE 00/06 Python Environments | See `phases/phase-00/06-python-environments/experiment.md`: create a second environment, install a pinned NumPy version, and compare its version with the repository `.venv`. | The learner installed NumPy 1.26.4 in `.venv-a`; the repository `.venv` reports 2.5.4. The interpreter paths point to their separate environments. | **Complete** |
| SE 00/07 Docker for AI | See `phases/phase-00/07-docker-for-ai/experiment.md`: run a temporary container with the repository mounted at `/workspace`, then list the mounted files. | Docker denied access to `/var/run/docker.sock` before a container started. The learner reports daemon access cannot be granted in this environment, so the volume mount cannot be tested here. | **Unavailable** |
| SE 00/08 Editor Setup | See `phases/phase-00/08-editor-setup/experiment.md`: enable the listed Python/notebook settings and check Pylance and Black in a scratch file. | Python printed `42`; Pylance flagged the integer argument as incompatible with `str`; saving with Black changed the call to `greet(42)`. | **Complete** |
| SE 00/09 Data Management | See `phases/phase-00/09-data-management/experiment.md`: create reproducible 70/15/15 splits from 20 rows with a fixed seed; run it twice and compare the split outputs. | Both runs produced sizes 14/3/3 and identical row groups: train `[19, 5, 14, 4, 9, 13, 15, 18, 6, 12, 17, 10, 1, 11]`, validation `[2, 16, 7]`, test `[8, 0, 3]`. | **Complete** |
| SE 00/10 Terminal & Shell | See `phases/phase-00/10-terminal-and-shell/experiment.md`: write a small fake training log, then use `grep` and `awk` through a pipe to extract loss values. | The learner got `0.8`, `0.4`, and `0.2`, then explained: `>` redirects output to a file; `|` sends one command's output as input to the next. | **Complete** |
| SE 00/11 Linux for AI | See `phases/phase-00/11-linux-for-ai/experiment.md`: create a temporary shell script, observe it fail without execute permission, add the bit with `chmod +x`, then run it. | Bring back the before/after permissions from `ls -l` and the script's output after the permission change. | **Pending** |

## Review queue
- SE 00/06 Python Environments — review how to identify the active virtual environment, why pip and Conda can conflict, and how to compare PyTorch's CUDA build with driver support.
- SE 00/07 Docker for AI — review how volumes persist host data, how the NVIDIA Container Toolkit exposes the host GPU, and how Compose service names resolve on its shared network.
- SE 00/08 Editor Setup — review notebook output scrolling and what basic type checking catches before code runs.
- SE 00/09 Data Management — review why Parquet is usually smaller and faster to query than CSV.
- SE 00/10 Terminal & Shell — review how to detach and reattach to `tmux`, and how `ssh -L` forwards a remote port to localhost.
- SE 00/11 Linux for AI — review `~` for the current user's home, the `sudo apt update` then `sudo apt install` sequence, and reinforce `chmod +x`, `du` directory sizes, and macOS vs. Linux `sed -i` syntax from the initial quiz misses.
