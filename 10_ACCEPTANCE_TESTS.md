# 10 — Acceptance Tests

These are high-level acceptance tests for the minimal Forge system.

## Test 1 — Status works without full state

Given some state files are missing

When:

```bash
forge status
```

Then:

```text
command exits 0
prints clear missing-file warnings
does not crash
```

## Test 2 — Run creates artifacts

When:

```bash
forge run --task "Add status command"
```

Then a run folder exists with:

```text
task.md
state_snapshot.md
horizon_snapshot.md
plan.md
outcome.md
```

## Test 3 — Verify uses static commands only

Given `forge.yml` contains:

```yaml
runtime:
  test_command: "pytest"
```

When:

```bash
forge verify
```

Then Forge runs only that configured command.

## Test 4 — Improve proposes a gap-based task

Given current state says:

```text
No status command exists.
```

And horizon says:

```text
Forge should report current state.
```

When:

```bash
forge improve
```

Then output contains:

```text
Add forge status command
```

## Test 5 — Learn records lessons

Given a run has failed verification

When:

```bash
forge learn --run latest
```

Then:

```text
lessons.md exists
failure_patterns.md is updated
self_improvement_backlog.md contains a concrete follow-up task
```

## Test 6 — Protected file guard

Given a diff modifies:

```text
AGENTS.md
.github/workflows/main.yml
```

When git guard runs

Then the run is blocked unless explicit high-risk approval is present.

## Test 7 — State updates conservatively

After a successful run

Then:

```text
current_state.md mentions the new capability
test_health.md mentions test result
latest run is recorded
```

After a failed run

Then:

```text
current_state.md does not claim the capability works
limitations.md is updated
```
