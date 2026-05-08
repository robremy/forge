# 01 — Layered Architecture

Forge must be built as a layered system.

Each layer has one responsibility. Higher layers set goals and constraints. Lower layers execute.

## Layer model

```text
Layer 8 — Horizon and Governance
Layer 7 — Self-Learning and Memory
Layer 6 — Review and Verification
Layer 5 — Execution
Layer 4 — Planning and Context
Layer 3 — Orchestration
Layer 2 — Runtime Environment
Layer 1 — Human Interface
Layer 0 — Repository
```

## Layer 0 — Repository

The actual codebase.

For bootstrap, the repository is Forge itself.

## Layer 1 — Human Interface

Input and output for the human.

Initial interface:

```bash
forge status
forge run --task "..."
forge improve
forge verify
forge learn --run latest
```

Later interface:

```text
GitHub issues
Pull request comments
Manual workflow dispatch
```

## Layer 2 — Runtime Environment

Initial intended runtime:

```text
Windows 11 host
WSL 2 Ubuntu
VS Code
Dev Container
Python
Git
Codex CLI
```

## Layer 3 — Orchestration

Forge decides the sequence:

```text
read state
read horizon
analyze gap
create task
create run folder
call Codex or produce plan
verify
learn
update state
```

## Layer 4 — Planning and Context

Converts a task into a safe plan.

Outputs:

```text
specification
plan
selected context
allowed write scope
risk level
```

## Layer 5 — Execution

Executes the plan.

In bootstrap:

```text
write run artifacts
optionally call codex exec
capture diff
run fixed checks
```

## Layer 6 — Review and Verification

Verifies result.

Checks:

```text
tests pass
diff is allowed
protected files not changed
task output exists
lessons produced
```

## Layer 7 — Self-Learning and Memory

Records what happened and improves future runs.

Memory is explicit markdown, not hidden state.

## Layer 8 — Horizon and Governance

Defines what Forge wants to become and what it must never do.

This layer contains:

```text
vision
target architecture
maturity model
safety policies
self-improvement rules
```

## Critical boundary

Codex may propose and edit code, but Forge must own:

```text
orchestration
policy
test command selection
diff validation
memory update
state update
```
