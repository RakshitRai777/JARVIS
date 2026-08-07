from datetime import datetime

from ai.memory.memory import Memory
from ai.memory.memory_service import MemoryService
from ai.memory.memory_type import MemoryType

from ai.agent.goal_manager import GoalManager

from ai.project.project_manager import ProjectManager

from ai.planner.planning_engine import PlanningEngine


def main():

    ########################################################

    service = MemoryService()

    service.clear()

    ########################################################

    service.remember(

        Memory(

            memory_type=MemoryType.LONG_TERM,

            content="Current project is FitOS",

            created_at=datetime.now(),

        )

    )

    ########################################################
    # Goal
    ########################################################

    goal_manager = GoalManager()

    goal = goal_manager.create_goal(

        "Build FitOS",

        "Complete the FitOS project.",

    )

    goal_manager.activate(goal)

    goal.progress = 45.0

    ########################################################
    # Project
    ########################################################

    project_manager = ProjectManager()

    project = project_manager.create_project(

        "FitOS",

        "AI Operating System",

    )

    project_manager.activate(project)

    project.progress = 75.0

    ########################################################

    engine = PlanningEngine()

    ########################################################

    engine.goal_manager = goal_manager

    engine.project_manager = project_manager

    engine.advisor.goal_manager = goal_manager

    engine.advisor.project_manager = project_manager

    ########################################################

    print("=" * 60)

    print("GOAL-AWARE REASONING")

    print("=" * 60)

    ########################################################

    plan = engine.build_plan(

        "Continue FitOS",

    )

    ########################################################

    state = engine.advisor.project_manager.get_active_project()

    if state:

        print()

        print("Project")

        print(state.name)

        print()

        print("Status")

        print(state.status.name)

        print()

        print("Progress")

        print(state.progress)

    ########################################################

    print()

    print("Steps :", len(plan.steps))

    print()

    for index, step in enumerate(

        plan.steps,

        start=1,

    ):

        print(

            f"{index}.",

            step.description,

        )


if __name__ == "__main__":

    main()