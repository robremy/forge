from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .markdown import read_markdown


HORIZON_FILES = (
    ".forge/horizon/vision.md",
    ".forge/horizon/target_architecture.md",
    ".forge/horizon/maturity_model.md",
    ".forge/horizon/roadmap.md",
    ".forge/horizon/principles.md",
)


@dataclass(frozen=True)
class HorizonSnapshot:
    vision: str
    target_architecture: str
    maturity_model: str
    roadmap: str
    principles: str

    def as_markdown(self) -> str:
        sections = (
            ("Vision", self.vision),
            ("Target Architecture", self.target_architecture),
            ("Maturity Model", self.maturity_model),
            ("Roadmap", self.roadmap),
            ("Principles", self.principles),
        )
        return "\n\n".join(f"## {title}\n\n{body.strip()}" for title, body in sections) + "\n"


def read_horizon(root: Path) -> HorizonSnapshot:
    return HorizonSnapshot(
        vision=read_markdown(root, ".forge/horizon/vision.md"),
        target_architecture=read_markdown(root, ".forge/horizon/target_architecture.md"),
        maturity_model=read_markdown(root, ".forge/horizon/maturity_model.md"),
        roadmap=read_markdown(root, ".forge/horizon/roadmap.md"),
        principles=read_markdown(root, ".forge/horizon/principles.md"),
    )
