---
name: coding
description: Implement a small bounded Forge task.
---

# Coding Skill

Use this skill to implement a planned task.

## Inputs

```text
task specification
plan
current state
horizon
relevant memory
allowed write paths
protected paths
```

## Rules

- Modify only files needed for the task.
- Add or update tests.
- Do not change protected files.
- Do not invent shell commands.
- Keep implementation simple.
- Preserve run artifact formats.
- Keep the CLI predictable.

## Output

Expected result:

```text
code changes
tests
short implementation summary
known limitations
```
