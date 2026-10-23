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
| SE 00 — Setup & Tooling | 06 | Python Environments | Not started |
| SE 00 — Setup & Tooling | 07 | Docker for AI | Not started |
| SE 00 — Setup & Tooling | 08 | Editor Setup | Not started |
| SE 00 — Setup & Tooling | 09 | Data Management | Not started |
| SE 00 — Setup & Tooling | 10 | Terminal & Shell | Not started |
| SE 00 — Setup & Tooling | 11 | Linux for AI | Not started |
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

## Between-lesson practice

| Lesson | Task | Evidence to bring back | Status |
|--------|------|------------------------|--------|
| SE 00/05 Jupyter Notebooks | See `phases/phase-00/05-jupyter-notebooks/experiment.md`: add a Markdown cell and assignment/conversion cells, run all; restart and run the conversion first; then rerun from the top. | The learner saw `NameError: name 'temperature_c' is not defined` when running the conversion first, then got `68.0` after running from the top. They explained that the assignment cell creates the variable in kernel memory before the conversion cell uses it. | **Complete** |

## Review queue
<empty for now; learn adds lessons the quizzes flag>
