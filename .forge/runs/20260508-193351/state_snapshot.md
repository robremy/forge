## Current State

# Current State

Forge is currently a bootstrap specification.

## Current maturity

Level 0 — Manual Prototype

## Working

- Conceptual architecture exists.
- Markdown build instructions exist.
- Skills are specified as markdown.
- Horizon and state structure are defined.

## Not working yet

- No Python CLI exists yet.
- No run folders are generated yet.
- No verification command exists yet.
- No gap analyzer exists yet.
- No self-improvement executor exists yet.
- No Codex CLI wrapper exists yet.

## Immediate next goal

Reach Level 1 — Local Kernel.

That means:

- create a Python CLI;
- implement `forge status`;
- implement `forge run --task`;
- implement `forge verify`;
- create run artifacts;
- add tests.

## Capabilities

# Capabilities

## Existing capabilities

At bootstrap specification stage:

- Can describe intended architecture.
- Can describe maturity model.
- Can describe first implementation tasks.
- Can provide Codex-readable instructions.

## Target next capabilities

- CLI command parsing.
- Markdown state reading.
- Run folder creation.
- Static verification.
- Gap-based improvement selection.

## Limitations

# Limitations

Forge has not yet been implemented.

Known limitations:

- No executable package.
- No tests.
- No config parser.
- No state updater.
- No Codex runner.
- No git guard.
- No branch management.
- No PR integration.

## Architecture

# Current Architecture

Current architecture is specification-only.

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

## Test Health

# Test Health

No tests exist yet.

Target:

```text
pytest passes locally
forge verify calls pytest
test output is captured per run
```
