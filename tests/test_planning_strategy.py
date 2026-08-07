from ai.planner.planning_strategy import PlanningStrategy
from ai.planner.planning_strategy_type import (
    PlanningStrategyType,
)


def main():

    ########################################################

    print("=" * 60)
    print("DEFAULT STRATEGY")
    print("=" * 60)

    strategy = PlanningStrategy()

    print(strategy)

    ########################################################

    print()

    print("=" * 60)
    print("CUSTOM STRATEGY")
    print("=" * 60)

    strategy = PlanningStrategy(

        strategy=PlanningStrategyType.RESUME_GOAL,

        reason="Continue the active goal.",

        confidence=0.98,

    )

    print("Strategy   :", strategy.strategy.name)

    print("Reason     :", strategy.reason)

    print("Confidence :", strategy.confidence)


if __name__ == "__main__":

    main()