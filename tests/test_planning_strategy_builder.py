from ai.agent.reasoning_result import ReasoningResult

from ai.planner.planning_strategy_builder import (
    PlanningStrategyBuilder,
)


def main():

    builder = PlanningStrategyBuilder()

    ########################################################

    reasoning = ReasoningResult(

        success=True,

        conclusion=(
            "Continue the active goal "
            "'Build FitOS' from 45% progress."
        ),

        confidence=0.98,

    )

    ########################################################

    strategy = builder.build(

        reasoning,

    )

    ########################################################

    print("=" * 60)
    print("PLANNING STRATEGY BUILDER")
    print("=" * 60)

    print("Strategy   :", strategy.strategy.name)

    print("Reason     :", strategy.reason)

    print("Confidence :", strategy.confidence)


if __name__ == "__main__":

    main()