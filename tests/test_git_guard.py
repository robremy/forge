from __future__ import annotations

import pytest

from forge.git_guard import is_protected_path, normalize_repo_path, validate_changed_paths


def test_protected_path_detection():
    assert is_protected_path("AGENTS.md")
    assert is_protected_path(".github/workflows/main.yml")
    assert is_protected_path(".forge/horizon/vision.md")
    assert not is_protected_path("src/forge/main.py")


def test_path_traversal_is_unsafe():
    with pytest.raises(ValueError):
        normalize_repo_path("../secrets.txt")

    violations = validate_changed_paths(["tests/test_ok.py", "..\\escape.txt"])
    assert violations == ["..\\escape.txt"]
