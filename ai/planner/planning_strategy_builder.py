from ai.agent.reasoning_result import ReasoningResult

from ai.planner.planning_strategy import PlanningStrategy
from ai.planner.planning_strategy_type import (
    PlanningStrategyType,
)


class PlanningStrategyBuilder:
    """
    Converts a ReasoningResult into a PlanningStrategy.
    """

    ############################################################

    def build(
        self,
        reasoning: ReasoningResult,
    ) -> PlanningStrategy:

        conclusion = reasoning.conclusion.lower()

        ########################################################
        # Resume existing goal
        ########################################################

        if "active goal" in conclusion:

            strategy = PlanningStrategyType.RESUME_GOAL

        ########################################################
        # Store memory
        ########################################################

        elif "store" in conclusion:

            strategy = PlanningStrategyType.STORE_MEMORY

        ########################################################
        # Execute tool
        ########################################################

        elif "tool" in conclusion:

            strategy = PlanningStrategyType.EXECUTE_TOOL

        ########################################################
        # System command
        ########################################################

        elif "system" in conclusion:

            strategy = PlanningStrategyType.SYSTEM_COMMAND

        ########################################################
        # Default
        ########################################################

        else:

            strategy = PlanningStrategyType.DEFAULT

        ########################################################

        return PlanningStrategy(

            strategy=strategy,

            reason=reasoning.conclusion,

            confidence=reasoning.confidence,

        )