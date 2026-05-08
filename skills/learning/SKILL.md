---
name: learning
description: Convert run outcomes into durable markdown lessons.
---

# Learning Skill

Use this skill after every run.

## Input

```text
task
plan
diff
test output
review result
outcome
human feedback if available
```

## Output

Write:

```text
lessons.md
updates to failure_patterns.md
updates to success_patterns.md
updates to self_improvement_backlog.md
```

## Lesson format

```md
## Lesson: <title>

Run: <run-id>
Outcome: success | failure | partial

Observation:
...

Cause:
...

Rule:
...

Follow-up task:
...
```

## Rule

Learning may update memory. It must not silently change core policy.
