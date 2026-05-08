---
name: review
description: Review a Forge change for correctness, safety, and alignment with the task.
---

# Review Skill

Use this skill after code changes and tests.

## Check

```text
does the change satisfy acceptance criteria?
do tests pass?
are protected files untouched?
is the diff small and relevant?
does the change move Forge toward the horizon?
were lessons or state updates produced?
```

## Output

```text
verdict: pass | fail | needs-human-review
reasons
required fixes
risk level
```

## Fail conditions

Fail if:

```text
protected files changed without approval
tests fail
scope is much broader than task
state claims unsupported capabilities
shell commands are model-generated
```
