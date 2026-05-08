# 06 — Runtime: Windows 11, WSL, VS Code, Dev Container, Codex

Forge should be local-first.

## Intended runtime stack

```text
Windows 11
  -> WSL 2 Ubuntu
  -> VS Code Remote WSL
  -> Dev Container
  -> Forge CLI
  -> Codex CLI
  -> Skills
```

## Windows 11

Role:

```text
host operating system
VS Code UI
Docker Desktop
browser/GitHub UI
```

Windows should not be the primary build environment.

## WSL 2

Role:

```text
Linux filesystem
Git repositories
shell
local development base
```

Recommended project location:

```bash
/home/<user>/projects/forge
```

Avoid building primarily from:

```text
C:\Users\...
```

## VS Code

Role:

```text
human cockpit
diff inspection
terminal
manual review
Codex extension
Dev Container entrypoint
```

## Dev Container

Role:

```text
reproducible runtime
isolated dependencies
stable Python/Codex/Git environment
```

The container should eventually include:

```text
python
git
gh
codex
pytest
ruff
```

## Codex CLI

Role:

```text
execution engine
code modification
test assistance
small task implementation
```

Forge should call Codex through a controlled wrapper.

Example conceptual call:

```bash
codex exec --cd /workspace --json < .forge/runs/<run-id>/prompt.md
```

## Codex extension

Role:

```text
interactive human assistance
manual inspection
not the core orchestrator
```

## Skills

Role:

```text
reusable task workflows
clear instructions for recurring agent tasks
```

Skills should be stored in:

```text
skills/<skill-name>/SKILL.md
```

## Important distinction

Codex executes.

Forge orchestrates.

Codex must not own policy, memory, state, or test command selection.
