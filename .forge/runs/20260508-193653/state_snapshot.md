## Current State

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

## Capabilities

# Capabilities

## Existing capabilities

At bootstrap specification stage:

- Can describe intended architecture.
- Can describe maturity model.
- Can describe first implementation tasks.
- Can provide Codex-readable instructions.
- Can parse `forge` CLI commands.
- Can read markdown state and horizon files.
- Can create `.forge/runs/<run-id>/` artifact folders.
- Can write required run artifacts, including clear placeholders.
- Can run deterministic verification commands from `forge.yml`.
- Can propose one gap-based improvement.
- Can learn from the latest run into markdown memory.
- Can detect protected path changes through git guard helpers.

## Target next capabilities

- Conservative state updates after runs.
- Richer gap selection from backlog and maturity model.
- Branch-based self-improvement execution.
- Codex CLI wrapper behind one interface.

## Limitations

# Limitations

Forge has a minimal local kernel, but it is not yet a full self-improving builder.

Known limitations:

- No state updater.
- No Codex runner.
- No branch management.
- No PR integration.
- Gap analysis is intentionally simple.
- Review artifacts are placeholders.
- Diff capture does not include untracked files in bootstrap mode.

## Architecture

# Current Architecture

Current architecture is a minimal Python CLI kernel.

Target bootstrap architecture:

```text
CLI
 -> Config loader
 -> State reader
 -> Horizon reader
 -> Gap analyzer
 -> Run context
 -> Test runner
 -> Memory writer
 -> State updater
```

Implemented modules:

```text
src/forge/main.py
src/forge/config.py
src/forge/run_context.py
src/forge/state.py
src/forge/horizon.py
src/forge/gap.py
src/forge/memory.py
src/forge/git_guard.py
src/forge/test_runner.py
```

## Test Health

# Test Health

Latest known result:

```text
python -m pytest
10 passed
```

`forge verify` also runs:

```text
python -m pytest
python -m compileall -q src/forge
```

Latest successful run:

```text
20260508-193351
```
