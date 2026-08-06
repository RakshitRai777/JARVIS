from ai.planner.planning_engine import PlanningEngine


def main():

    engine = PlanningEngine()

    command = "Open Notepad then type Hello"

    print()

    print(command)

    print()

    plan = engine.build_plan(command)

    print("=" * 60)

    print("IMPROVED PLAN")

    print("=" * 60)

    for i, step in enumerate(plan.steps, start=1):

        print(f"Step {i}")

        print(step.action)

        print(step.parameters)

        print(step.description)

        print("-" * 60)


if __name__ == "__main__":

    main()