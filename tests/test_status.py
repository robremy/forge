from __future__ import annotations

from forge.main import command_status

from .conftest import make_minimal_forge


def test_status_prints_current_state(tmp_path, monkeypatch, capsys):
    make_minimal_forge(tmp_path)
    code = command_status(tmp_path)

    output = capsys.readouterr().out

    assert code == 0
    assert "Forge status" in output
    assert "Current maturity: Level 0 - Manual Prototype" in output
    assert "Can read markdown specs" in output
    assert "No executable package" in output
    assert "Latest run: none" in output
    assert "Build Level 1 local kernel" in output


def test_status_handles_missing_files(tmp_path, capsys):
    make_minimal_forge(tmp_path)
    (tmp_path / ".forge/state/capabilities.md").unlink()

    code = command_status(tmp_path)
    output = capsys.readouterr().out

    assert code == 0
    assert "none recorded" in output
