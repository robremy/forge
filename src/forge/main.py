from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .config import ConfigError, load_config
from .gap import analyze_gap
from .horizon import read_horizon
from .markdown import first_heading_block
from .memory import learn_from_run
from .run_context import create_run, latest_run_dir
from .state import current_maturity, read_state
from .test_runner import run_verification


EXIT_GENERAL_FAILURE = 1
EXIT_CONFIG_ERROR = 2
EXIT_VERIFICATION_FAILED = 3
EXIT_POLICY_VIOLATION = 4
EXIT_RUN_NOT_FOUND = 5


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    root = Path.cwd()

    try:
        if args.command == "status":
            return command_status(root)
        if args.command == "verify":
            return command_verify(root)
        if args.command == "run":
            return command_run(root, args.task)
        if args.command == "improve":
            return command_improve(root)
        if args.command == "learn":
            return command_learn(root, args.run)
    except ConfigError as exc:
        print(f"Config error: {exc}", file=sys.stderr)
        return EXIT_CONFIG_ERROR
    except FileNotFoundError as exc:
        print(str(exc), file=sys.stderr)
        return EXIT_RUN_NOT_FOUND

    parser.print_help()
    return EXIT_GENERAL_FAILURE


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="forge")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("status", help="Print current Forge state.")
    subparsers.add_parser("verify", help="Run static configured checks.")

    run_parser = subparsers.add_parser("run", help="Create a controlled run.")
    run_parser.add_argument("--task", required=True)

    subparsers.add_parser("improve", help="Propose one next self-improvement.")

    learn_parser = subparsers.add_parser("learn", help="Learn from a run.")
    learn_parser.add_argument("--run", required=True)

    return parser


def command_status(root: Path) -> int:
    state = read_state(root)
    latest = latest_run_dir(root)
    backlog = _read_optional(root / ".forge/backlog/self_improvement_backlog.md")
    print("Forge status")
    print(f"Current maturity: {current_maturity(state)}")
    print("Working capabilities:")
    print(_bullet_block(state.capabilities, preferred_heading="## Existing capabilities"))
    print("Known limitations:")
    print(_bullet_block(state.limitations))
    print(f"Latest run: {latest.name if latest else 'none'}")
    print(f"Next suggested improvement: {_next_improvement(backlog)}")
    return 0


def command_verify(root: Path) -> int:
    config = load_config(root)
    result = run_verification(root, config)
    print(result.as_text())
    return 0 if result.exit_code == 0 else EXIT_VERIFICATION_FAILED


def command_run(root: Path, task: str) -> int:
    config = load_config(root)
    result = create_run(root, task, config)
    print(f"Created run: {result.run_id}")
    print(f"Run folder: {result.run_dir}")
    print(f"Verification exit code: {result.verification.exit_code}")
    return 0 if result.verification.exit_code == 0 else EXIT_VERIFICATION_FAILED


def command_improve(root: Path) -> int:
    state = read_state(root)
    horizon = read_horizon(root)
    gap = analyze_gap(state, horizon)
    print("Selected improvement task")
    print(f"Task: {gap.smallest_useful_improvement}")
    print(f"Reason: {gap.reason_for_priority}")
    print("Acceptance criteria:")
    for item in gap.acceptance_criteria:
        print(f"- {item}")
    print(f"Risk level: {gap.risk_level}")
    return 0


def command_learn(root: Path, run_ref: str) -> int:
    result = learn_from_run(root, run_ref)
    print(f"Learned from run: {result.run_id}")
    print(f"Outcome: {result.outcome}")
    print(f"Lessons: {result.lessons_path}")
    return 0


def _read_optional(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def _bullet_block(text: str, preferred_heading: str | None = None) -> str:
    source = text
    if preferred_heading:
        preferred = first_heading_block(text, preferred_heading)
        if preferred:
            source = preferred
    bullets = [line for line in source.splitlines() if line.strip().startswith("- ")]
    if not bullets:
        return "- none recorded"
    return "\n".join(bullets)


def _next_improvement(backlog: str) -> str:
    sections = backlog.split("\n## Improvement:")
    for section in sections[1:]:
        if "Status:\ncompleted" in section or "Status:\r\ncompleted" in section:
            continue
        title = section.splitlines()[0].strip()
        if title:
            return title
    for line in backlog.splitlines():
        if line.startswith("## Improvement:"):
            return line.removeprefix("## Improvement:").strip()
    block = first_heading_block(backlog, "## Improvement")
    return block.splitlines()[0] if block else "none recorded"
