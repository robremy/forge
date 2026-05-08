from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .run_context import latest_run_dir


@dataclass(frozen=True)
class LessonResult:
    run_id: str
    outcome: str
    lessons_path: Path


def learn_from_run(root: Path, run_ref: str) -> LessonResult:
    run_dir = latest_run_dir(root) if run_ref == "latest" else root / ".forge" / "runs" / run_ref
    if run_dir is None or not run_dir.exists():
        raise FileNotFoundError(f"Run not found: {run_ref}")

    run_id = run_dir.name
    outcome_text = _read(run_dir / "outcome.md")
    test_output = _read(run_dir / "test-output.txt")
    outcome = "success" if "Status: success" in outcome_text else "failure"
    lesson = _lesson_markdown(run_id, outcome, test_output)

    lessons_path = run_dir / "lessons.md"
    lessons_path.write_text(lesson, encoding="utf-8")

    if outcome == "success":
        _append_unique(root / ".forge/memory/success_patterns.md", _success_entry(run_id))
    else:
        _append_unique(root / ".forge/memory/failure_patterns.md", _failure_entry(run_id))
        _append_unique(root / ".forge/backlog/self_improvement_backlog.md", _followup_entry(run_id))

    return LessonResult(run_id=run_id, outcome=outcome, lessons_path=lessons_path)


def _read(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def _lesson_markdown(run_id: str, outcome: str, test_output: str) -> str:
    observation = "Verification passed." if outcome == "success" else "Verification failed or was incomplete."
    cause = "The configured checks completed successfully." if outcome == "success" else "The run needs follow-up based on test-output.txt."
    rule = "Keep changes small and verify them with static commands." if outcome == "success" else "Do not claim new capability until verification passes."
    followup = "None." if outcome == "success" else "Inspect failed verification and add the smallest fix."
    summary = first_output_line(test_output)
    return (
        f"## Lesson: Run {run_id} {outcome}\n\n"
        f"Run: {run_id}\n"
        f"Outcome: {outcome}\n\n"
        f"Observation:\n{observation}\n\n"
        f"Cause:\n{cause}\n\n"
        f"Rule:\n{rule}\n\n"
        f"Follow-up task:\n{followup}\n\n"
        f"Verification summary:\n{summary}\n"
    )


def first_output_line(text: str) -> str:
    for line in text.splitlines():
        if line.strip():
            return line.strip()
    return "No verification output recorded."


def _append_unique(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    existing = _read(path)
    if text.strip() in existing:
        return
    separator = "\n\n" if existing.strip() else ""
    path.write_text(existing.rstrip() + separator + text.strip() + "\n", encoding="utf-8")


def _success_entry(run_id: str) -> str:
    return (
        f"## Success Pattern: Verified run {run_id}\n\n"
        "Small controlled runs with static verification are safe to learn from."
    )


def _failure_entry(run_id: str) -> str:
    return (
        f"## Failure Pattern: Verification failed in {run_id}\n\n"
        "A run with failed verification must produce a concrete follow-up before state claims improve."
    )


def _followup_entry(run_id: str) -> str:
    return (
        f"## Improvement: Fix failed run {run_id}\n\n"
        "Source:\n"
        f"{run_id}\n\n"
        "Problem:\n"
        "Verification failed or did not complete.\n\n"
        "Proposed change:\n"
        "Inspect test-output.txt and make the smallest corrective change.\n\n"
        "Acceptance criteria:\n"
        "- The failed check passes.\n"
        "- The run lesson explains what changed.\n\n"
        "Risk:\n"
        "low"
    )
