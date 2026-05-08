---
name: security
description: Check a Forge run for policy, path, shell, and self-modification risks.
---

# Security Skill

Use this skill during review or before committing a self-improvement.

## Check

```text
protected files
path traversal
unexpected shell commands
dependency changes
workflow changes
secret exposure
sandbox bypass
policy modifications
```

## Output

```text
risk level
blocking issues
warnings
safe to continue: yes | no
```

## Rule

High-risk changes need explicit human approval.
