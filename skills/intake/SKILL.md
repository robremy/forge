---
name: intake
description: Convert a human task into a clear Forge task specification.
---

# Intake Skill

Use this skill when Forge receives a human task, issue, or self-improvement request.

## Input

```text
raw task text
current state
horizon
memory
```

## Output

Write a task specification with:

```text
title
goal
background
acceptance criteria
risk level
allowed scope
non-goals
```

## Rules

- Keep the task small.
- Make acceptance criteria testable.
- Identify if the task is self-improvement.
- Do not expand the task beyond what was asked.
