# Current State

Forge is currently a minimal local kernel.

## Current maturity

Level 1 — Local Kernel

## Working

- Conceptual architecture exists.
- Markdown build instructions exist.
- Skills are specified as markdown.
- Horizon and state structure are defined.
- Python CLI package exists.
- `forge status` reports current state.
- `forge run --task` creates run folders and required artifacts.
- `forge verify` runs static commands from `forge.yml`.
- `forge improve` proposes one gap-based next task.
- `forge learn --run latest` writes run lessons and updates markdown memory.
- Basic pytest coverage passes.

## Not working yet

- No self-improvement executor exists yet.
- No Codex CLI wrapper exists yet.
- No automatic state updater exists yet.
- No branch mode exists yet.

## Immediate next goal

Reach Level 2 — Self-Aware Kernel.

That means:

- update current state after runs;
- produce richer gap analysis;
- keep capabilities and limitations conservative;
- prepare controlled self-improvement execution.
