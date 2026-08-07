from ai.planner.planner_action import PlannerAction

from ai.planner.planning_strategy import PlanningStrategy
from ai.planner.planning_strategy_type import (
    PlanningStrategyType,
)

from ai.planner.strategy_planner import StrategyPlanner


def main():

    planner = StrategyPlanner()

    ########################################################

    strategy = PlanningStrategy(

        strategy=PlanningStrategyType.RESUME_GOAL,

        reason="Continue Build FitOS",

        confidence=0.98,

    )

    ########################################################

    action = planner.decide(

        strategy,

    )

    ########################################################

    print("=" * 60)
    print("STRATEGY PLANNER")
    print("=" * 60)

    print("Strategy")

    print(strategy.strategy.name)

    print()

    print("Planner Action")

    print(action.name)


if __name__ == "__main__":

    main()