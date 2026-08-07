from ai.planner.planner_action import PlannerAction

from ai.planner.planning_strategy import PlanningStrategy
from ai.planner.planning_strategy_type import (
    PlanningStrategyType,
)


class StrategyPlanner:
    """
    Converts a PlanningStrategy into a PlannerAction.

    Responsibilities
    ----------------
    • Interpret high-level planning strategy
    • Select the appropriate planner action
    """

    ############################################################

    def decide(
        self,
        strategy: PlanningStrategy,
    ) -> PlannerAction:

        ########################################################
        # Resume Goal
        ########################################################

        if strategy.strategy == PlanningStrategyType.RESUME_GOAL:

            return PlannerAction.LLM

        ########################################################
        # Store Memory
        ########################################################

        if strategy.strategy == PlanningStrategyType.STORE_MEMORY:

            return PlannerAction.MEMORY

        ########################################################
        # Execute Tool
        ########################################################

        if strategy.strategy == PlanningStrategyType.EXECUTE_TOOL:

            return PlannerAction.TOOL

        ########################################################
        # System Command
        ########################################################

        if strategy.strategy == PlanningStrategyType.SYSTEM_COMMAND:

            return PlannerAction.SYSTEM

        ########################################################
        # Default
        ########################################################

        return PlannerAction.LLM