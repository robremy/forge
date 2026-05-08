---
name: planning
description: Turn a Forge task specification into a small implementation plan.
---

# Planning Skill

Use this skill after intake or gap analysis.

## Output

Write:

```text
implementation steps
files likely involved
tests to add or update
run artifacts to produce
risks
rollback strategy
```

## Rules

- Prefer one small change.
- Do not introduce broad abstractions.
- Keep tests close to changed behavior.
- Respect protected paths.
