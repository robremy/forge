# Maturity Model

## Level 0 — Manual Prototype

- Architecture exists only as documentation.
- No executable Forge CLI.

## Level 1 — Local Kernel

- Python CLI exists.
- Run folders exist.
- Fixed verification works.
- State files are readable.
- Basic tests pass.

## Level 2 — Self-Aware Kernel

- Forge can report its own capabilities.
- Forge can report its own limitations.
- Forge can update current state after runs.
- Forge can produce gap analysis.

## Level 3 — Self-Improving Kernel

- Forge can select one small improvement.
- Forge can run an improvement through a controlled loop.
- Forge can learn from the result.
- Forge can update backlog and memory.

## Level 4 — Codex-Driven Builder

- Forge can invoke Codex CLI through a wrapper.
- Forge can build prompts from state, horizon, task, and memory.
- Forge can validate diffs.
- Forge can retry once on test failure.

## Level 5 — Issue-to-PR Pipeline

- Forge can read GitHub issues.
- Forge can create branches and pull requests.
- Forge can classify risk.
- Forge can require human approval for high-risk changes.
- GitHub Actions may optionally trigger Forge.
