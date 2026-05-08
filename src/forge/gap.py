from __future__ import annotations

from dataclasses import dataclass

from .horizon import HorizonSnapshot
from .state import StateSnapshot


@dataclass(frozen=True)
class GapAnalysis:
    target_capability: str
    current_limitation: str
    gap: str
    smallest_useful_improvement: str
    acceptance_criteria: tuple[str, ...]
    risk_level: str
    reason_for_priority: str

    def as_markdown(self) -> str:
        criteria = "\n".join(f"- {item}" for item in self.acceptance_criteria)
        return (
            "# Gap Analysis\n\n"
            f"Target capability:\n{self.target_capability}\n\n"
            f"Current limitation:\n{self.current_limitation}\n\n"
            f"Gap:\n{self.gap}\n\n"
            f"Smallest useful improvement:\n{self.smallest_useful_improvement}\n\n"
            f"Acceptance criteria:\n{criteria}\n\n"
            f"Risk level:\n{self.risk_level}\n\n"
            f"Reason for priority:\n{self.reason_for_priority}\n"
        )


def analyze_gap(state: StateSnapshot, horizon: HorizonSnapshot) -> GapAnalysis:
    current = state.current_state.lower()
    capabilities = state.capabilities.lower()

    if "no python cli" in current or "cli command parsing" in capabilities:
        return GapAnalysis(
            target_capability="Level 1 - Local Kernel",
            current_limitation="Forge is documentation-only and has no executable CLI.",
            gap="No runnable Python package exists yet.",
            smallest_useful_improvement="Build the Level 1 local kernel with status, run, verify, improve, and learn commands.",
            acceptance_criteria=(
                "forge status prints current state and maturity.",
                "forge run --task creates a run folder and required artifacts.",
                "forge verify runs commands from forge.yml.",
                "forge improve proposes one gap-based task.",
                "forge learn --run latest writes lessons.",
                "pytest passes.",
            ),
            risk_level="low",
            reason_for_priority="The maturity model requires a local kernel before any self-improvement loop can run.",
        )

    limitations = state.limitations.lower()
    if (
        "no state updater" in current
        or "no automatic state updater" in current
        or "no state updater" in limitations
        or "no automatic state updater" in limitations
    ):
        return GapAnalysis(
            target_capability="Level 2 - Self-Aware Kernel",
            current_limitation="Forge can run and learn, but cannot update state automatically after runs.",
            gap="Run outcomes do not yet update current_state.md, capabilities.md, limitations.md, or test_health.md.",
            smallest_useful_improvement="Add a conservative state updater after successful and failed runs.",
            acceptance_criteria=(
                "Successful runs can record latest run and verified capabilities.",
                "Failed runs update limitations without claiming success.",
                "State updates remain readable markdown.",
                "Tests cover success and failure state updates.",
            ),
            risk_level="low",
            reason_for_priority="The Level 2 maturity model requires Forge to report and update its own state conservatively.",
        )

    if "gap" not in current:
        return GapAnalysis(
            target_capability="Gap-based self-improvement",
            current_limitation="Forge cannot yet compare state and horizon.",
            gap="No gap analyzer is implemented.",
            smallest_useful_improvement="Add a markdown-based gap analyzer.",
            acceptance_criteria=("Gap analysis identifies one small next task.", "Tests cover fixture markdown."),
            risk_level="low",
            reason_for_priority="Every improvement must point to a state/horizon gap.",
        )

    return GapAnalysis(
        target_capability="Conservative self-improvement",
        current_limitation="No obvious missing Level 1 capability was detected.",
        gap="Backlog needs review for the next small improvement.",
        smallest_useful_improvement="Review backlog and select the next low-risk task.",
        acceptance_criteria=("Selected task is small, testable, and aligned with the horizon.",),
        risk_level="low",
        reason_for_priority="Forge should continue improving through bounded tasks.",
    )
