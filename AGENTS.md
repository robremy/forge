# AGENTS.md — Forge Build Instructions for Codex

You are building Forge.

Forge is a local-first, self-improving build pipeline. It uses Codex CLI as an execution engine, but Forge itself is responsible for orchestration, safety, memory, and state tracking.

## Main objective

Build a minimal Python CLI that can eventually improve itself.

The first version must support:

```bash
forge status
forge run --task "..."
forge improve
forge verify
forge learn --run latest
```

## Core architecture

Use this loop:

```text
State + Horizon -> Gap -> Improvement Task -> Run -> Verify -> Learn -> Updated State
```

## Hard rules

- Make small, focused changes.
- Prefer simple code over clever abstractions.
- Do not build unnecessary features.
- Do not add GitHub Actions in the first version.
- Do not auto-merge anything.
- Do not allow direct writes to `main`.
- Do not let large language model output define arbitrary shell commands.
- Test commands must come from static config, not from a model response.
- Preserve readable markdown memory.
- Every behavior change needs a test.
- Every run must write artifacts under `.forge/runs/<run-id>/`.
- Every self-improvement must be branch-based or local-diff-based, never silent.

## Protected files in early bootstrap

Treat these as protected unless the task explicitly says otherwise:

```text
AGENTS.md
forge.yml
.devcontainer/
.github/
.forge/horizon/
.forge/policy/
```

The system may read protected files, but it must not modify them during normal self-improvement runs.

## Preferred implementation style

Use Python.

Recommended package layout:

```text
src/forge/
  __init__.py
  main.py
  config.py
  run_context.py
  state.py
  horizon.py
  gap.py
  orchestrator.py
  memory.py
  git_guard.py
  test_runner.py
  codex_runner.py
```

Use `argparse` or `typer`. Prefer the simpler option unless the project already uses a CLI framework.

## Minimum test approach

Use `pytest`.

Minimum tests:

```text
tests/test_status.py
tests/test_run_context.py
tests/test_git_guard.py
tests/test_memory.py
tests/test_gap.py
```

## Output requirements

When implementing any task, preserve these outputs:

```text
.forge/runs/<run-id>/task.md
.forge/runs/<run-id>/state_snapshot.md
.forge/runs/<run-id>/horizon_snapshot.md
.forge/runs/<run-id>/gap_analysis.md
.forge/runs/<run-id>/plan.md
.forge/runs/<run-id>/diff.patch
.forge/runs/<run-id>/test-output.txt
.forge/runs/<run-id>/review.md
.forge/runs/<run-id>/lessons.md
.forge/runs/<run-id>/outcome.md
```

If a file cannot yet be produced in the bootstrap version, create a clear placeholder and mark it as not implemented.

## Definition of done for first implementation

The first implementation is done when:

- `forge status` prints current state and maturity level.
- `forge verify` runs configured tests.
- `forge run --task "..."` creates a run folder and records the task.
- `forge improve` reads state and horizon and proposes one next improvement.
- `forge learn --run latest` writes or updates lessons.
- Tests pass.
