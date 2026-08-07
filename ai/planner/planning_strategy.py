from dataclasses import dataclass

from ai.planner.planning_strategy_type import (
    PlanningStrategyType,
)


@dataclass(slots=True)
class PlanningStrategy:
    """
    Represents the high-level strategy chosen
    by the reasoning engine before planning.
    """

    ############################################################

    strategy: PlanningStrategyType = (
        PlanningStrategyType.DEFAULT
    )

    ############################################################

    reason: str = ""

    ############################################################

    confidence: float = 0.0