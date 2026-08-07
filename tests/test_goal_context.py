from ai.agent.goal import Goal
from ai.agent.goal_context import GoalContext
from ai.agent.goal_status import GoalStatus


def main():

    goal = Goal(

        title="Build FitOS",

        description="Complete the FitOS project.",

        status=GoalStatus.ACTIVE,

        progress=45.0,

    )

    context = GoalContext(

        current_goal=goal,

        all_goals=[goal],

    )

    print("=" * 60)
    print("GOAL CONTEXT")
    print("=" * 60)

    print("Current Goal :", context.current_goal.title)

    print("Status       :", context.current_goal.status.name)

    print("Progress     :", context.current_goal.progress)

    print("Total Goals  :", len(context.all_goals))


if __name__ == "__main__":

    main()