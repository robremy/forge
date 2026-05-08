from __future__ import annotations

from forge.config import load_config
from forge.test_runner import run_verification

from .conftest import make_minimal_forge


def test_verify_uses_static_configured_command(tmp_path):
    make_minimal_forge(tmp_path, test_command="python -c \"print('configured-check')\"")

    result = run_verification(tmp_path, load_config(tmp_path))

    assert result.exit_code == 0
    assert "configured-check" in result.as_text()


def test_verify_reports_failure(tmp_path):
    make_minimal_forge(tmp_path, test_command="python -c \"raise SystemExit(7)\"")

    result = run_verification(tmp_path, load_config(tmp_path))

    assert result.exit_code == 7
