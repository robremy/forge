# 04 — Repository Structure

Codex should build toward this repository structure.

## Target structure

```text
forge/
  AGENTS.md
  README.md
  forge.yml
  pyproject.toml

  .devcontainer/
    devcontainer.json
    Dockerfile

  src/
    forge/
      __init__.py
      main.py
      config.py
      run_context.py
      state.py
      horizon.py
      gap.py
      orchestrator.py
      memory.py
      git_guard.py
      test_runner.py
      codex_runner.py

  tests/
    test_status.py
    test_run_context.py
    test_memory.py
    test_gap.py
    test_git_guard.py
    test_test_runner.py

  skills/
    intake/
      SKILL.md
    state-reader/
      SKILL.md
    gap-analyzer/
      SKILL.md
    planning/
      SKILL.md
    coding/
      SKILL.md
    review/
      SKILL.md
    learning/
      SKILL.md
    state-updater/
      SKILL.md

  .forge/
    state/
      current_state.md
      capabilities.md
      limitations.md
      architecture.md
      test_health.md

    horizon/
      vision.md
      target_architecture.md
      maturity_model.md
      roadmap.md
      principles.md

    memory/
      coding_rules.md
      failure_patterns.md
      success_patterns.md
      human_preferences.md

    backlog/
      self_improvement_backlog.md

    runs/
      .gitkeep
```

## Bootstrap exception

The first implementation may omit:

```text
codex_runner.py
orchestrator.py
some skills
GitHub integration
Dev Container files
```

But it must keep the conceptual structure intact.

## Config file

Use `forge.yml` for deterministic settings.

Example:

```yaml
project:
  name: forge
  type: python-cli

runtime:
  test_command: "pytest"
  lint_command: "python -m py_compile src/forge/*.py"

paths:
  allowed_write:
    - "src/"
    - "tests/"
    - "skills/"
    - ".forge/state/"
    - ".forge/memory/"
    - ".forge/backlog/"
    - "README.md"

  protected:
    - ".git/"
    - ".env"
    - ".github/"
    - ".devcontainer/"
    - "AGENTS.md"
    - "forge.yml"
    - ".forge/horizon/"
    - ".forge/policy/"

self_improvement:
  enabled: true
  direct_main_write: false
  require_tests: true
  require_human_merge: true
```
