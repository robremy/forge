from __future__ import annotations

import subprocess
from dataclasses import dataclass
from pathlib import Path

from .config import ForgeConfig


@dataclass(frozen=True)
class CommandResult:
    label: str
    command: str
    exit_code: int
    output: str


@dataclass(frozen=True)
class VerificationResult:
    results: tuple[CommandResult, ...]

    @property
    def exit_code(self) -> int:
        for result in self.results:
            if result.exit_code != 0:
                return result.exit_code
        return 0

    def as_text(self) -> str:
        if not self.results:
            return "No verification commands configured.\n"
        parts = []
        for result in self.results:
            parts.append(
                f"## {result.label}\n\n"
                f"Command: {result.command}\n"
                f"Exit code: {result.exit_code}\n\n"
                f"{result.output.strip()}\n"
            )
        return "\n".join(parts)


def run_verification(root: Path, config: ForgeConfig) -> VerificationResult:
    commands = [
        ("tests", config.runtime.test_command),
        ("lint", config.runtime.lint_command),
    ]
    results: list[CommandResult] = []
    for label, command in commands:
        if not command:
            continue
        completed = subprocess.run(
            command,
            cwd=root,
            shell=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        results.append(
            CommandResult(
                label=label,
                command=command,
                exit_code=completed.returncode,
                output=completed.stdout,
            )
        )
    return VerificationResult(tuple(results))
