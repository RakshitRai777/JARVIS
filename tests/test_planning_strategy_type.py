from ai.planner.planning_strategy_type import PlanningStrategyType


def main():

    print("=" * 60)
    print("PLANNING STRATEGY TYPE")
    print("=" * 60)

    for strategy in PlanningStrategyType:

        print(

            strategy.name,

            "=",

            strategy.value,

        )


if __name__ == "__main__":

    main()