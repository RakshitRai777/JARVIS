from dataclasses import dataclass

from ai.planner.planner_action import PlannerAction


@dataclass
class Decision:
    """
    Result returned by the Planner.
    """

    action: PlannerAction

    reason: str = ""