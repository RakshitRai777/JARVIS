from ai.planner.planning_engine import PlanningEngine


def main():

    planner = PlanningEngine()

    plan = planner.build_plan(

        "Open Notepad then type Hello"

    )

    print()

    print("=" * 60)

    print("PLAN")

    print("=" * 60)

    for i, step in enumerate(plan.steps, start=1):

        print()

        print(f"Step {i}")

        print("Action :", step.action)

        print("Parameters :", step.parameters)

        if step.verification_rule:

            print(

                "Verification :",

                step.verification_rule,

            )

        else:

            print(

                "Verification : None",

            )


if __name__ == "__main__":

    main()