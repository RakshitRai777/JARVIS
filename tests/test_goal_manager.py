from ai.agent.goal_manager import GoalManager


def main():

    manager = GoalManager()

    ########################################################

    goal = manager.create_goal(

        "Build FitOS",

        "Complete the FitOS project.",

    )

    ########################################################

    print("=" * 60)
    print("GOAL CREATED")
    print("=" * 60)

    print(goal)

    ########################################################

    manager.activate(

        goal,

    )

    print()

    print("Status :", goal.status.name)

    ########################################################

    manager.update_progress(

        goal,

        45,

    )

    print("Progress :", goal.progress)

    ########################################################

    manager.complete(

        goal,

    )

    print()

    print("Status :", goal.status.name)

    print("Progress :", goal.progress)

    print("Completed :", goal.completed_at is not None)

    ########################################################

    print()

    print("Total Goals :", len(manager.get_goals()))

    print()

    print("=" * 60)
    print("FIND GOAL")
    print("=" * 60)

    found = manager.find_goal("Build FitOS")

    print(found.title if found else "Not Found")

    print()

    print("=" * 60)
    print("ACTIVE GOAL")
    print("=" * 60)

    active = manager.get_active_goal()

    print(active.title if active else "None")

    print()

    print("=" * 60)
    print("REMOVE GOAL")
    print("=" * 60)

    removed = manager.remove_goal(goal)

    print("Removed :", removed)

    print("Remaining Goals :", len(manager.get_goals()))


if __name__ == "__main__":

    main()