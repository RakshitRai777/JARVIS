from ai.agent.reasoning_result import ReasoningResult

from ai.planner.planning_strategy_builder import (
    PlanningStrategyBuilder,
)


def main():

    builder = PlanningStrategyBuilder()

    ########################################################

    reasoning = ReasoningResult(

        success=True,

        thought="Continue FitOS",

        conclusion=(
            "Continue the active project "
            "'FitOS' from 75.0% progress."
        ),

        confidence=0.99,

    )

    ########################################################

    strategy = builder.build(

        reasoning,

    )

    ########################################################

    print("=" * 60)
    print("PLANNING STRATEGY BUILDER")
    print("=" * 60)

    print()

    print("Strategy")

    print(strategy.strategy.name)

    print()

    print("Reason")

    print(strategy.reason)

    print()

    print("Confidence")

    print(strategy.confidence)


if __name__ == "__main__":

    main()