from __future__ import annotations

from pathlib import Path


def write_text(root: Path, relative: str, text: str) -> Path:
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


def make_minimal_forge(root: Path, test_command: str = "python -c \"print('ok')\"") -> None:
    write_text(
        root,
        "forge.yml",
        (
            "runtime:\n"
            f"  test_command: \"{test_command}\"\n"
            "  lint_command: \"\"\n"
            "paths:\n"
            "  protected:\n"
            "    - \"AGENTS.md\"\n"
            "    - \".forge/horizon/\"\n"
        ),
    )
    write_text(
        root,
        ".forge/state/current_state.md",
        (
            "# Current State\n\n"
            "## Current maturity\n\n"
            "Level 0 - Manual Prototype\n\n"
            "No Python CLI exists yet.\n"
        ),
    )
    write_text(root, ".forge/state/capabilities.md", "# Capabilities\n\n- Can read markdown specs.\n")
    write_text(root, ".forge/state/limitations.md", "# Limitations\n\n- No executable package.\n")
    write_text(root, ".forge/state/architecture.md", "# Architecture\n\nSpecification-only.\n")
    write_text(root, ".forge/state/test_health.md", "# Test Health\n\nNo tests yet.\n")
    write_text(root, ".forge/horizon/vision.md", "# Vision\n\nForge should improve itself.\n")
    write_text(root, ".forge/horizon/target_architecture.md", "# Target\n\nCLI kernel.\n")
    write_text(root, ".forge/horizon/maturity_model.md", "# Maturity\n\n## Level 1 - Local Kernel\n\nCLI exists.\n")
    write_text(root, ".forge/horizon/roadmap.md", "# Roadmap\n\nBuild kernel.\n")
    write_text(root, ".forge/horizon/principles.md", "# Principles\n\nStay small.\n")
    write_text(
        root,
        ".forge/backlog/self_improvement_backlog.md",
        (
            "# Self-Improvement Backlog\n\n"
            "## Improvement: Build Level 1 local kernel\n\n"
            "Risk:\nlow\n"
        ),
    )
    write_text(root, ".forge/memory/failure_patterns.md", "# Failure Patterns\n")
    write_text(root, ".forge/memory/success_patterns.md", "# Success Patterns\n")
    write_text(root, ".forge/memory/coding_rules.md", "# Coding Rules\n")
