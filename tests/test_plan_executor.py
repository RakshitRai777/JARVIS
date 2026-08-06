from ai.execution.plan_executor import PlanExecutor
from ai.planner.planning_engine import PlanningEngine


def main():

    planner = PlanningEngine()

    executor = PlanExecutor()

    command = "Open Notepad then type Hello"

    print()

    print("Command:")

    print(command)

    print()

    ########################################################

    plan = planner.build_plan(

        command,

    )

    ########################################################

    result = executor.execute(

        plan,

    )

    ########################################################

    print()

    print(result)


if __name__ == "__main__":

    main()