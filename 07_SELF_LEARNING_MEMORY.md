# 07 — Self-Learning Memory

Forge learns through explicit markdown memory.

No hidden memory is required.

## Memory types

```text
failure patterns
success patterns
coding rules
human preferences
context strategy
self-improvement backlog
```

## Memory files

```text
.forge/memory/coding_rules.md
.forge/memory/failure_patterns.md
.forge/memory/success_patterns.md
.forge/memory/human_preferences.md
.forge/backlog/self_improvement_backlog.md
```

## What to learn from each run

After every run, capture:

```text
task
plan
changed files
test result
review result
retry count
human feedback
final outcome
lesson
```

## Lesson format

Use this format:

```md
## Lesson: <short title>

Run: <run-id>
Outcome: success | failure | partial

Observation:
<what happened>

Cause:
<why it happened>

Rule:
<what Forge should do differently next time>

Follow-up task:
<specific improvement if needed>
```

## Learning categories

### Failure pattern

Example:

```text
CLI behavior changed but tests were not updated.
```

Rule:

```text
When CLI files change, inspect and update CLI tests.
```

### Success pattern

Example:

```text
Small diff with explicit tests passed first try.
```

Rule:

```text
Prefer narrow diffs and targeted tests.
```

### Human preference

Example:

```text
Prefer direct readable implementation over abstraction.
```

Rule:

```text
Do not introduce architecture layers unless they reduce an observed gap.
```

## Self-improvement backlog

Every durable improvement idea should become a backlog item.

Backlog item format:

```md
## Improvement: <title>

Source:
<run-id or manual>

Problem:
<observed limitation>

Proposed change:
<small implementation task>

Acceptance criteria:
- ...
- ...

Risk:
low | medium | high
```

## Rule

Learning may happen automatically.

Self-modification must happen through a controlled run.
