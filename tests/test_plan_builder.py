from ai.planner.plan_builder import PlanBuilder
from ai.planner.planner_action import PlannerAction


def print_plan(title, plan):

    print()
    print("=" * 60)
    print(title)
    print("=" * 60)

    for i, step in enumerate(plan.steps, start=1):

        print(f"Step {i}")
        print(f"Action      : {step.action}")
        print(f"Parameters  : {step.parameters}")
        print(f"Description : {step.description}")
        print("-" * 60)


def main():

    builder = PlanBuilder()

    ############################################################

    plan = builder.build_single(

        PlannerAction.TOOL,

        "Open Notepad",

    )

    print_plan("TOOL PLAN", plan)

    ############################################################

    plan = builder.build_single(

        PlannerAction.MEMORY,

        "Remember my name is Rakshit",

    )

    print_plan("MEMORY PLAN", plan)

    ############################################################

    plan = builder.build_single(

        PlannerAction.LLM,

        "Explain quantum computing",

    )

    print_plan("LLM PLAN", plan)

    ############################################################

    plan = builder.build_single(

        PlannerAction.SYSTEM,

        "exit",

    )

    print_plan("SYSTEM PLAN", plan)


if __name__ == "__main__":

    main()