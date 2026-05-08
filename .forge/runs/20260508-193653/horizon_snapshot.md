## Vision

# Horizon Vision

Forge should become a local-first, self-improving, layered AI software-building pipeline.

It should use Codex CLI inside a controlled runtime to implement small improvements.

Forge should improve itself through:

```text
state
horizon
gap analysis
task selection
controlled execution
verification
learning
state update
```

Forge must remain inspectable, reversible, and policy-bounded.

## Target Architecture

# Target Architecture

Final target:

```text
Human task or issue
 -> Intake
 -> State reader
 -> Horizon reader
 -> Gap analyzer
 -> Planner
 -> Context selector
 -> Codex runner
 -> Patch writer
 -> Git guard
 -> Test runner
 -> Review
 -> Learning
 -> State update
 -> Branch or PR
```

Initial target:

```text
Task string
 -> run folder
 -> static plan
 -> verify
 -> lessons
 -> state update
```

## Maturity Model

# Maturity Model

## Level 0 — Manual Prototype

- Architecture exists only as documentation.
- No executable Forge CLI.

## Level 1 — Local Kernel

- Python CLI exists.
- Run folders exist.
- Fixed verification works.
- State files are readable.
- Basic tests pass.

## Level 2 — Self-Aware Kernel

- Forge can report its own capabilities.
- Forge can report its own limitations.
- Forge can update current state after runs.
- Forge can produce gap analysis.

## Level 3 — Self-Improving Kernel

- Forge can select one small improvement.
- Forge can run an improvement through a controlled loop.
- Forge can learn from the result.
- Forge can update backlog and memory.

## Level 4 — Codex-Driven Builder

- Forge can invoke Codex CLI through a wrapper.
- Forge can build prompts from state, horizon, task, and memory.
- Forge can validate diffs.
- Forge can retry once on test failure.

## Level 5 — Issue-to-PR Pipeline

- Forge can read GitHub issues.
- Forge can create branches and pull requests.
- Forge can classify risk.
- Forge can require human approval for high-risk changes.
- GitHub Actions may optionally trigger Forge.

## Roadmap

# Roadmap

## Next milestone

Reach Level 1 — Local Kernel.

## Ordered roadmap

1. Create Python package skeleton.
2. Add `forge status`.
3. Add run folder creation.
4. Add `forge verify`.
5. Add gap analysis.
6. Add `forge improve`.
7. Add `forge learn`.
8. Add state updater.
9. Add git guard.
10. Add Codex runner wrapper.
11. Add branch-based self-improvement.
12. Add GitHub issue/PR integration.

## Principles

# Principles

- Local-first before cloud automation.
- Small verified changes before autonomy.
- Explicit markdown memory before hidden memory.
- State and horizon before self-improvement.
- Policy and tests before merge.
- Codex executes; Forge orchestrates.
- Self-improvement must be inspectable and reversible.
