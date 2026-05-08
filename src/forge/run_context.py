from __future__ import annotations

import subprocess
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from .config import ForgeConfig
from .gap import analyze_gap
from .horizon import read_horizon
from .state import read_state
from .test_runner import VerificationResult, run_verification


REQUIRED_ARTIFACTS = (
    "task.md",
    "state_snapshot.md",
    "horizon_snapshot.md",
    "gap_analysis.md",
    "plan.md",
    "diff.patch",
    "test-output.txt",
    "review.md",
    "lessons.md",
    "outcome.md",
)


@dataclass(frozen=True)
class RunResult:
    run_id: str
    run_dir: Path
    verification: VerificationResult


def new_run_id(now: datetime | None = None) -> str:
    moment = now or datetime.now(timezone.utc)
    return moment.strftime("%Y%m%d-%H%M%S")


def create_run(root: Path, task: str, config: ForgeConfig, run_id: str | None = None) -> RunResult:
    actual_run_id = run_id or new_run_id()
    run_dir = root / ".forge" / "runs" / actual_run_id
    run_dir.mkdir(parents=True, exist_ok=False)

    state = read_state(root)
    horizon = read_horizon(root)
    gap = analyze_gap(state, horizon)

    _write(run_dir / "task.md", f"# Task\n\n{task.strip()}\n")
    _write(run_dir / "state_snapshot.md", state.as_markdown())
    _write(run_dir / "horizon_snapshot.md", horizon.as_markdown())
    _write(run_dir / "gap_analysis.md", gap.as_markdown())
    _write(
        run_dir / "plan.md",
        "# Plan\n\n"
        "- Record the task and snapshots.\n"
        "- Run deterministic verification from forge.yml.\n"
        "- Record outcome and placeholders for later review and learning.\n",
    )
    _write(run_dir / "diff.patch", _git_diff(root))
    verification = run_verification(root, config)
    _write(run_dir / "test-output.txt", verification.as_text())
    _write(run_dir / "review.md", "# Review\n\nNot implemented in bootstrap kernel.\n")
    _write(run_dir / "lessons.md", "# Lessons\n\nNot implemented until `forge learn` is run.\n")
    _write(run_dir / "outcome.md", _outcome_markdown(actual_run_id, verification))
    return RunResult(actual_run_id, run_dir, verification)


def latest_run_dir(root: Path) -> Path | None:
    runs_root = root / ".forge" / "runs"
    if not runs_root.exists():
        return None
    dirs = [path for path in runs_root.iterdir() if path.is_dir()]
    if not dirs:
        return None
    return sorted(dirs, key=lambda path: path.name)[-1]


def _write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def _git_diff(root: Path) -> str:
    completed = subprocess.run(
        ["git", "-c", f"safe.directory={root.as_posix()}", "diff", "--no-ext-diff"],
        cwd=root,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if completed.returncode != 0:
        return f"Diff capture unavailable.\n\n{completed.stdout.strip()}\n"
    return completed.stdout or "No diff captured at run creation.\n"


def _outcome_markdown(run_id: str, verification: VerificationResult) -> str:
    status = "success" if verification.exit_code == 0 else "failure"
    return (
        "# Outcome\n\n"
        f"Run: {run_id}\n"
        f"Status: {status}\n"
        f"Verification exit code: {verification.exit_code}\n"
    )
