from __future__ import annotations

from pathlib import Path


def read_markdown(root: Path, relative_path: str) -> str:
    path = root / relative_path
    if not path.exists():
        return f"Missing file: {relative_path}\n"
    return path.read_text(encoding="utf-8")


def first_heading_block(text: str, heading: str) -> str:
    lines = text.splitlines()
    capture = False
    block: list[str] = []
    for line in lines:
        if line.strip().lower() == heading.lower():
            capture = True
            continue
        if capture and line.startswith("#"):
            break
        if capture:
            block.append(line)
    return "\n".join(block).strip()


def first_nonempty_line(text: str, fallback: str = "Unknown") -> str:
    for line in text.splitlines():
        stripped = line.strip()
        if stripped and not stripped.startswith("#"):
            return stripped
    return fallback
