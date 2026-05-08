# Forge Bootstrap Specification

This folder contains the minimal markdown specification for building Forge with Codex.

Forge is a local-first, self-improving build pipeline. Its first job is to build itself safely and incrementally.

## Core idea

Forge should be able to answer five questions before it improves itself:

1. What is my current state?
2. What is the target horizon?
3. What gap exists between current state and target state?
4. What is the smallest safe improvement that reduces that gap?
5. Did the improvement work, and what should be learned from it?

## Build target

Build a minimal Python CLI called `forge`.

Minimum commands:

```bash
forge status
forge run --task "..."
forge improve
forge verify
forge learn --run latest
```

## Runtime target

The intended runtime stack is:

```text
Windows 11
  -> WSL 2 Ubuntu
  -> VS Code
  -> Dev Container
  -> Forge CLI
  -> Codex CLI via codex exec
  -> Markdown Skills
  -> Git branch/commit
  -> Self-learning memory
```

GitHub Actions is optional and should not be part of the first bootstrap version.

## How Codex should use this package

Start with:

1. `AGENTS.md`
2. `00_VISION.md`
3. `01_LAYERED_ARCHITECTURE.md`
4. `02_MINIMAL_BOOTSTRAP_KERNEL.md`
5. `03_STATE_HORIZON_GAP_LOOP.md`
6. `09_IMPLEMENTATION_BACKLOG.md`
7. the `skills/*/SKILL.md` files

Then implement only the first small working increment.

## Bootstrap principle

Do not build the whole final system at once.

Build the smallest stable kernel first:

```text
CLI -> run folder -> fixed checks -> diff capture -> learning file -> state update
```

After that, Forge can use its own improvement loop to grow.
