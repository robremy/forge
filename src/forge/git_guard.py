from __future__ import annotations

from pathlib import Path, PurePosixPath


DEFAULT_PROTECTED = (
    ".git/",
    ".env",
    ".github/",
    ".devcontainer/",
    "AGENTS.md",
    "forge.yml",
    ".forge/horizon/",
    ".forge/policy/",
)


def normalize_repo_path(path: str) -> str:
    value = path.replace("\\", "/").strip()
    pure = PurePosixPath(value)
    if pure.is_absolute() or any(part == ".." for part in pure.parts):
        raise ValueError(f"Unsafe path: {path}")
    return pure.as_posix()


def is_protected_path(path: str, protected: tuple[str, ...] = DEFAULT_PROTECTED) -> bool:
    normalized = normalize_repo_path(path)
    for rule in protected:
        clean_rule = rule.replace("\\", "/")
        if clean_rule.endswith("/"):
            if normalized == clean_rule[:-1] or normalized.startswith(clean_rule):
                return True
        elif normalized == clean_rule:
            return True
    return False


def validate_changed_paths(paths: list[str], protected: tuple[str, ...] = DEFAULT_PROTECTED) -> list[str]:
    violations: list[str] = []
    for path in paths:
        try:
            if is_protected_path(path, protected):
                violations.append(path)
        except ValueError:
            violations.append(path)
    return violations


def stays_within(root: Path, candidate: Path) -> bool:
    root_resolved = root.resolve()
    candidate_resolved = candidate.resolve()
    return candidate_resolved == root_resolved or root_resolved in candidate_resolved.parents
