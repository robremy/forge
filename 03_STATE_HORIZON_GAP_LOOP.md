# 03 — State, Horizon, Gap Loop

Forge's central intelligence is not a single prompt.

It is this loop:

```text
Current State + Target Horizon -> Gap Analysis -> Next Improvement -> Verification -> Updated State
```

## State

State describes what Forge currently is.

Stored in:

```text
.forge/state/current_state.md
.forge/state/capabilities.md
.forge/state/limitations.md
.forge/state/architecture.md
.forge/state/test_health.md
```

The state must be factual and conservative.

## Horizon

Horizon describes what Forge wants to become.

Stored in:

```text
.forge/horizon/vision.md
.forge/horizon/target_architecture.md
.forge/horizon/maturity_model.md
.forge/horizon/roadmap.md
.forge/horizon/principles.md
```

The horizon must be stable and protected.

## Gap

Gap analysis compares state with horizon.

A useful gap has:

```text
target capability
current limitation
missing mechanism
smallest next task
risk level
acceptance criteria
```

## Next improvement selection

The next improvement should be:

```text
small
testable
reversible
aligned with horizon
low risk
useful for future self-improvement
```

## Example

Current state:

```text
Forge can create run folders, but cannot summarize latest run.
```

Horizon:

```text
Forge should understand and report its current state.
```

Gap:

```text
No status command exists.
```

Next task:

```text
Add `forge status` command that reads state files and latest run metadata.
```

Acceptance criteria:

```text
- `forge status` exits with code 0.
- It prints current maturity.
- It prints latest run.
- It prints next suggested improvement.
- Unit tests cover missing and present state files.
```

## Rule

Forge must not improve randomly.

Every self-improvement task must point to a gap between current state and target horizon.
