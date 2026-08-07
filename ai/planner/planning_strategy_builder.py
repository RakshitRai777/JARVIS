from ai.agent.reasoning_result import ReasoningResult

from ai.planner.planning_strategy import PlanningStrategy
from ai.planner.planning_strategy_type import (
    PlanningStrategyType,
)


class PlanningStrategyBuilder:
    """
    Converts reasoning results into high-level
    planning strategies.
    """

    ############################################################

    def build(
        self,
        reasoning: ReasoningResult,
    ) -> PlanningStrategy:

        conclusion = reasoning.conclusion.lower()

        ########################################################
        # Resume Project
        ########################################################

        if "active project" in conclusion:

            return PlanningStrategy(

                strategy=PlanningStrategyType.RESUME_PROJECT,

                reason=reasoning.conclusion,

                confidence=reasoning.confidence,

            )

        ########################################################
        # Resume Goal
        ########################################################

        if "active goal" in conclusion:

            return PlanningStrategy(

                strategy=PlanningStrategyType.RESUME_GOAL,

                reason=reasoning.conclusion,

                confidence=reasoning.confidence,

            )

        ########################################################
        # Create Project
        ########################################################

        if "create project" in conclusion:

            return PlanningStrategy(

                strategy=PlanningStrategyType.CREATE_PROJECT,

                reason=reasoning.conclusion,

                confidence=reasoning.confidence,

            )

        ########################################################
        # Create Goal
        ########################################################

        if "create goal" in conclusion:

            return PlanningStrategy(

                strategy=PlanningStrategyType.CREATE_GOAL,

                reason=reasoning.conclusion,

                confidence=reasoning.confidence,

            )

        ########################################################
        # Store Memory
        ########################################################

        if "memory" in conclusion:

            return PlanningStrategy(

                strategy=PlanningStrategyType.STORE_MEMORY,

                reason=reasoning.conclusion,

                confidence=reasoning.confidence,

            )

        ########################################################
        # Execute Tool
        ########################################################

        if "tool" in conclusion:

            return PlanningStrategy(

                strategy=PlanningStrategyType.EXECUTE_TOOL,

                reason=reasoning.conclusion,

                confidence=reasoning.confidence,

            )

        ########################################################
        # System Command
        ########################################################

        if "system" in conclusion:

            return PlanningStrategy(

                strategy=PlanningStrategyType.SYSTEM_COMMAND,

                reason=reasoning.conclusion,

                confidence=reasoning.confidence,

            )

        ########################################################
        # Default
        ########################################################

        return PlanningStrategy(

            strategy=PlanningStrategyType.DEFAULT,

            reason=reasoning.conclusion,

            confidence=reasoning.confidence,

        )