# Self-Improvement Backlog

## Improvement: Build Level 1 local kernel

Source:
Initial bootstrap specification.

Problem:
Forge is currently only documentation and has no executable CLI.

Proposed change:
Create minimal Python package with `forge status`, `forge run --task`, and `forge verify`.

Acceptance criteria:
- CLI starts.
- `forge status` prints current state.
- `forge run --task "test"` creates a run folder.
- `forge verify` runs static test command.
- Basic tests pass.

Risk:
low

Status:
completed in run 20260508-193351

## Improvement: Add conservative state updater

Source:
Level 2 maturity model.

Problem:
Forge can create runs and learn from them, but state files still require manual edits after behavior changes.

Proposed change:
Add a state updater that records latest run, test health, and conservative capability or limitation updates after runs.

Acceptance criteria:
- Successful runs can record latest run and verified capabilities.
- Failed runs update limitations without claiming success.
- State updates remain readable markdown.
- Tests cover success and failure state updates.

Risk:
low
