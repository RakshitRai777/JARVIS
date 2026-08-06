from ai.agent.reasoning_context import ReasoningContext
from ai.planner.planning_context import PlanningContext


def main():

    context = ReasoningContext(

        planning_context=PlanningContext(

            command="Continue FitOS",

        ),

        objective="Continue existing project",

    )

    print("=" * 60)
    print("REASONING CONTEXT")
    print("=" * 60)

    print("Command   :", context.planning_context.command)
    print("Objective :", context.objective)
    print("Previous  :", context.previous_reasoning)


if __name__ == "__main__":

    main()