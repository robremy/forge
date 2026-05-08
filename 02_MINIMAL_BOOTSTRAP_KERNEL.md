# 02 — Minimal Bootstrap Kernel

The first implementation must be small.

Forge must initially be a stable kernel that can run, record, verify, and learn.

## Kernel responsibilities

The kernel must:

1. Parse CLI commands.
2. Load static config.
3. Read current state.
4. Read horizon.
5. Create run folders.
6. Write run artifacts.
7. Run fixed verification commands.
8. Capture test output.
9. Record lessons.
10. Update current state.
11. Propose the next improvement.

## Minimum commands

### `forge status`

Shows:

```text
current maturity level
working capabilities
known limitations
latest run
next suggested improvement
```

### `forge verify`

Runs fixed checks from configuration.

Never accept commands from a model response.

### `forge run --task "..."`

Creates a new run folder and records:

```text
task.md
state_snapshot.md
horizon_snapshot.md
plan.md
outcome.md
```

In the earliest version, this command may only create artifacts and run verification. Codex integration can be added after the kernel is stable.

### `forge improve`

Reads:

```text
.forge/state/current_state.md
.forge/horizon/vision.md
.forge/horizon/maturity_model.md
.forge/backlog/self_improvement_backlog.md
```

Then selects one small next improvement.

### `forge learn --run latest`

Reads one run and updates:

```text
.forge/memory/failure_patterns.md
.forge/memory/success_patterns.md
.forge/memory/coding_rules.md
.forge/backlog/self_improvement_backlog.md
```

## Minimum package modules

```text
src/forge/main.py
src/forge/config.py
src/forge/run_context.py
src/forge/state.py
src/forge/horizon.py
src/forge/gap.py
src/forge/memory.py
src/forge/test_runner.py
src/forge/git_guard.py
```

## Add Codex later

Codex integration belongs behind a single interface:

```text
src/forge/codex_runner.py
```

The rest of Forge should not depend directly on Codex CLI internals.

## First success criterion

The first version is successful if it can honestly describe itself and produce a useful next self-improvement task.
