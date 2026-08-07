from ai.agent.goal import Goal
from ai.agent.goal_status import GoalStatus


def main():

    ########################################################

    print("=" * 60)
    print("DEFAULT GOAL")
    print("=" * 60)

    goal = Goal()

    print(goal)

    ########################################################

    print()

    print("=" * 60)
    print("CUSTOM GOAL")
    print("=" * 60)

    goal = Goal(

        title="Build FitOS",

        description="Complete the FitOS project.",

        status=GoalStatus.ACTIVE,

        progress=35.0,

    )

    print("Title      :", goal.title)

    print("Description:", goal.description)

    print("Status     :", goal.status.name)

    print("Progress   :", goal.progress)

    print("Created    :", goal.created_at)

    print("Completed  :", goal.completed_at)


if __name__ == "__main__":

    main()