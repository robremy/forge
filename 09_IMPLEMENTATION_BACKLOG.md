# 09 — Implementation Backlog

This is the recommended build order.

Do not skip ahead.

## Phase 1 — Bootstrap CLI

### Task 1: Create Python package skeleton

Acceptance criteria:

- `src/forge/` exists.
- `forge` CLI entrypoint exists.
- `pytest` can run.
- Basic import test passes.

### Task 2: Add `forge status`

Acceptance criteria:

- Reads `.forge/state/current_state.md`.
- Reads `.forge/horizon/maturity_model.md`.
- Prints current maturity.
- Handles missing files gracefully.
- Has tests.

### Task 3: Add run folder creation

Acceptance criteria:

- `forge run --task "..."`
- Creates `.forge/runs/<run-id>/`.
- Writes `task.md`.
- Writes `state_snapshot.md`.
- Writes `horizon_snapshot.md`.
- Has tests.

### Task 4: Add `forge verify`

Acceptance criteria:

- Reads static config.
- Runs fixed test command.
- Captures output.
- Returns non-zero on failure.
- Has tests using a harmless command.

## Phase 2 — Self-understanding

### Task 5: Add gap analysis

Acceptance criteria:

- Reads state and horizon.
- Writes `gap_analysis.md`.
- Selects one missing capability.
- Has tests with fixture markdown.

### Task 6: Add `forge improve`

Acceptance criteria:

- Reads gap analysis and backlog.
- Proposes one next improvement.
- Prints reason and acceptance criteria.
- Does not modify code yet.
- Has tests.

### Task 7: Add state updater

Acceptance criteria:

- Updates `.forge/state/current_state.md` after run.
- Records latest run.
- Records capabilities/limitations conservatively.
- Has tests.

## Phase 3 — Learning

### Task 8: Add `forge learn --run latest`

Acceptance criteria:

- Reads latest run.
- Writes `lessons.md`.
- Appends useful item to memory or backlog.
- Has tests.

### Task 9: Add failure/success pattern extraction

Acceptance criteria:

- Failed verification updates failure patterns.
- Successful run updates success patterns.
- No duplicate spam.
- Has tests.

## Phase 4 — Safety

### Task 10: Add git guard

Acceptance criteria:

- Detects changed files.
- Rejects protected path changes.
- Rejects path traversal.
- Has tests.

### Task 11: Add policy-based run outcome

Acceptance criteria:

- Run outcome says success/failure/blocked.
- Policy violations fail the run.
- Has tests.

## Phase 5 — Codex integration

### Task 12: Add prompt builder

Acceptance criteria:

- Builds `.forge/runs/<run-id>/prompt.md`.
- Includes task, state, horizon, relevant memory, and allowed scope.
- Has tests.

### Task 13: Add Codex runner wrapper

Acceptance criteria:

- Calls `codex exec` through one module.
- Can be disabled in config.
- Captures output to `codex-output.jsonl` or text.
- Does not let Codex define test commands.
- Has tests using a fake runner.

## Phase 6 — Forge builds Forge

### Task 14: Let `forge improve --run` execute selected improvement

Acceptance criteria:

- Selects one low-risk task.
- Creates run folder.
- Builds prompt.
- Calls runner.
- Runs verify.
- Learns.
- Updates state.

### Task 15: Add branch mode

Acceptance criteria:

- Creates self-improvement branch.
- Does not touch main directly.
- Commits only after tests pass.
- Has dry-run mode.
