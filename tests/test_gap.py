from __future__ import annotations

from forge.gap import analyze_gap
from forge.horizon import read_horizon
from forge.state import read_state

from .conftest import make_minimal_forge


def test_gap_selects_level_one_kernel(tmp_path):
    make_minimal_forge(tmp_path)

    gap = analyze_gap(read_state(tmp_path), read_horizon(tmp_path))

    assert "Level 1" in gap.target_capability
    assert "local kernel" in gap.smallest_useful_improvement.lower()
    assert gap.risk_level == "low"


def test_gap_selects_state_updater_after_kernel_exists(tmp_path):
    make_minimal_forge(tmp_path)
    (tmp_path / ".forge/state/current_state.md").write_text(
        "# Current State\n\nLevel 1 - Local Kernel\n\nNo automatic state updater exists yet.\n",
        encoding="utf-8",
    )
    (tmp_path / ".forge/state/capabilities.md").write_text(
        "# Capabilities\n\n- Can parse forge CLI commands.\n",
        encoding="utf-8",
    )

    gap = analyze_gap(read_state(tmp_path), read_horizon(tmp_path))

    assert "Level 2" in gap.target_capability
    assert "state updater" in gap.smallest_useful_improvement.lower()
