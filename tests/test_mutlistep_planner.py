from ai.planner.plan_builder import PlanBuilder


def main():

    builder = PlanBuilder()

    plan = builder.build(

        "Open Notepad then type Hello"

    )

    print()

    print("Execution Plan")

    print("-" * 40)

    for i, step in enumerate(plan.steps, start=1):

        print(f"Step {i}")

        print(step.action)

        print(step.parameters)

        print()


if __name__ == "__main__":

    main()