from ai.planner.planning_engine import PlanningEngine


def print_plan(plan):

    print()

    print("=" * 60)

    print("EXECUTION PLAN")

    print("=" * 60)

    for i, step in enumerate(plan.steps, start=1):

        print(f"Step {i}")

        print(f"Action      : {step.action}")

        print(f"Parameters  : {step.parameters}")

        print(f"Description : {step.description}")

        print("-" * 60)


def main():

    planner = PlanningEngine()

    ############################################################

    command = "Open Notepad then type Hello"

    print()

    print("Command:")

    print(command)

    ############################################################

    plan = planner.build_plan(command)

    ############################################################

    print_plan(plan)


if __name__ == "__main__":

    main()