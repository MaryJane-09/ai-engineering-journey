# Repository Guidelines

## Project Structure & Module Organization

This repository tracks one learner's AI engineering journey; it is not the upstream course implementation. `LEARNING.md` is the progress record, including the selected roadmap, assessment results, current lesson, and review queue. `README.md` describes the repository. `skills-lock.json` records installed course skills and their upstream source. Add lesson notes, experiments, code, and project artifacts in clearly named directories as they are created; keep generated or private credentials out of version control. The upstream course's `phases/` tree is not currently part of this checkout.

## Build, Test, and Development Commands

There is no application build or test suite configured in this repository. Use Git and text tools to review changes:

- `git status --short` — inspect changed files.
- `git diff --check` — catch whitespace errors.
- `git diff` — review the final patch.
- `rg --files` — list tracked project files.

When adding executable lesson work, document the specific run command and dependencies alongside that artifact rather than assuming a repository-wide command.

## Coding Style & Naming Conventions

Use Markdown with descriptive headings, concise paragraphs, and fenced code blocks labeled with their language. Keep learning records factual and update progress only when supported by learner evidence. Use descriptive, lowercase kebab-case names for new lesson or project directories (for example, `lesson-notes/` or `vector-experiment/`). Follow the formatter and conventions of the language used by each individual artifact; no repository-wide formatter or linter is configured.

## Testing Guidelines

No testing framework or coverage target is configured. For documentation-only changes, run `git diff --check` and review the rendered Markdown structure. For code experiments, include a small reproducible command and record relevant inputs and output; add focused tests when the artifact warrants them.

## Commit & Pull Request Guidelines

Recent history uses short conventional prefixes such as `docs:`, `chore:`, and `Initial commit`. Use a concise imperative summary, such as `docs: add setup lesson notes`. Pull requests should explain the learning artifact or record change, list commands run and results where applicable, and link relevant lesson or project context. Include screenshots only when a visual artifact changes.

## Security & Configuration

Never commit API keys, tokens, private datasets, or machine-specific secrets. Keep local configuration out of tracked files and provide safe examples with placeholder values when documenting setup.
