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
