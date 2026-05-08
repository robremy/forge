---
name: gap-analyzer
description: Compare current state with target horizon and propose the smallest useful improvement.
---

# Gap Analyzer Skill

Use this skill after reading state and horizon.

## Input

```text
state summary
horizon summary
backlog
memory
```

## Output

Create gap analysis:

```text
target capability
current limitation
gap
smallest useful improvement
acceptance criteria
risk level
reason for priority
```

## Selection rules

Choose an improvement that is:

```text
small
testable
reversible
low-risk
aligned with the next maturity level
```

Do not choose high-risk policy or sandbox changes automatically.
