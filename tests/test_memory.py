from __future__ import annotations

from forge.config import load_config
from forge.memory import learn_from_run
from forge.run_context import create_run

from .conftest import make_minimal_forge


def test_learn_latest_writes_success_lesson(tmp_path):
    make_minimal_forge(tmp_path)
    create_run(tmp_path, "Record lesson", load_config(tmp_path), run_id="run-001")

    result = learn_from_run(tmp_path, "latest")

    assert result.run_id == "run-001"
    assert result.outcome == "success"
    assert "Outcome: success" in result.lessons_path.read_text(encoding="utf-8")
    assert "Verified run run-001" in (tmp_path / ".forge/memory/success_patterns.md").read_text(encoding="utf-8")


def test_learn_failed_run_updates_backlog(tmp_path):
    make_minimal_forge(tmp_path, test_command="python -c \"raise SystemExit(1)\"")
    create_run(tmp_path, "Fail verification", load_config(tmp_path), run_id="run-002")

    result = learn_from_run(tmp_path, "run-002")

    assert result.outcome == "failure"
    assert "Verification failed in run-002" in (tmp_path / ".forge/memory/failure_patterns.md").read_text(encoding="utf-8")
    assert "Fix failed run run-002" in (tmp_path / ".forge/backlog/self_improvement_backlog.md").read_text(encoding="utf-8")
