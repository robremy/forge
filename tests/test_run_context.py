from __future__ import annotations

from forge.config import load_config
from forge.run_context import REQUIRED_ARTIFACTS, create_run, latest_run_dir

from .conftest import make_minimal_forge


def test_create_run_writes_required_artifacts(tmp_path):
    make_minimal_forge(tmp_path)
    config = load_config(tmp_path)

    result = create_run(tmp_path, "Add status command", config, run_id="run-001")

    assert result.run_id == "run-001"
    assert result.verification.exit_code == 0
    for name in REQUIRED_ARTIFACTS:
        assert (result.run_dir / name).exists(), name
    assert "Add status command" in (result.run_dir / "task.md").read_text(encoding="utf-8")
    assert latest_run_dir(tmp_path) == result.run_dir
