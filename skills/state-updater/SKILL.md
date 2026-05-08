---
name: state-updater
description: Update Forge's current state after a run.
---

# State Updater Skill

Use this skill after review and learning.

## Input

```text
previous state
run outcome
test result
new capability if any
new limitation if any
lessons
```

## Output

Update:

```text
.forge/state/current_state.md
.forge/state/capabilities.md
.forge/state/limitations.md
.forge/state/test_health.md
```

## Rules

- Be conservative.
- Do not claim success if tests failed.
- Record partial progress honestly.
- Keep state readable.
- Link capability claims to run outcomes where possible.
