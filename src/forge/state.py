from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .markdown import read_markdown


STATE_FILES = (
    ".forge/state/current_state.md",
    ".forge/state/capabilities.md",
    ".forge/state/limitations.md",
    ".forge/state/architecture.md",
    ".forge/state/test_health.md",
)


@dataclass(frozen=True)
class StateSnapshot:
    current_state: str
    capabilities: str
    limitations: str
    architecture: str
    test_health: str

    def as_markdown(self) -> str:
        sections = (
            ("Current State", self.current_state),
            ("Capabilities", self.capabilities),
            ("Limitations", self.limitations),
            ("Architecture", self.architecture),
            ("Test Health", self.test_health),
        )
        return "\n\n".join(f"## {title}\n\n{body.strip()}" for title, body in sections) + "\n"


def read_state(root: Path) -> StateSnapshot:
    return StateSnapshot(
        current_state=read_markdown(root, ".forge/state/current_state.md"),
        capabilities=read_markdown(root, ".forge/state/capabilities.md"),
        limitations=read_markdown(root, ".forge/state/limitations.md"),
        architecture=read_markdown(root, ".forge/state/architecture.md"),
        test_health=read_markdown(root, ".forge/state/test_health.md"),
    )


def current_maturity(snapshot: StateSnapshot) -> str:
    for line in snapshot.current_state.splitlines():
        stripped = line.strip()
        if stripped.startswith("Level "):
            return stripped
    return "Unknown"
