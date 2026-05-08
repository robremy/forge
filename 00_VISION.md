# 00 — Forge Vision

Forge is a local-first, self-improving build pipeline.

It should convert a human task into a tested code improvement while also improving its own ability to build future improvements.

## One-sentence definition

Forge is a layered, self-learning software-building pipeline that understands its current state, understands its target horizon, identifies the gap, and safely improves itself through small verified steps.

## Why Forge exists

Normal coding agents can write code, but they often lack persistent self-understanding.

Forge adds:

```text
state
horizon
gap analysis
policy
memory
verification
controlled self-improvement
```

## Final target

Given a feature request, Forge should be able to:

1. Understand the request.
2. Read its current state.
3. Read the target architecture.
4. Identify the smallest useful gap.
5. Plan a bounded improvement.
6. Use Codex CLI to implement the improvement.
7. Check the diff against policies.
8. Run fixed tests.
9. Review the result.
10. Learn from success or failure.
11. Update its state and memory.
12. Create a branch or pull request for human review.

## First target

The first target is not full autonomy.

The first target is a minimal self-improving kernel that can build Forge itself.

## Central design law

Forge may think and propose through agents, but policies, deterministic checks, and tests decide whether a change is acceptable.

## Non-goals for the first version

Do not build these initially:

- GitHub Actions automation.
- Auto-merge.
- Cloud runners.
- Multi-repository management.
- Complex plugin system.
- Full graphical dashboard.
- Hidden or opaque memory.
