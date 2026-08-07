from datetime import datetime

from ai.agent.goal import Goal
from ai.agent.goal_status import GoalStatus

from ai.memory.memory import Memory
from ai.memory.memory_service import MemoryService
from ai.memory.memory_type import MemoryType

from ai.planner.planning_engine import PlanningEngine


def main():

    ########################################################
    # Reset memory
    ########################################################

    service = MemoryService()

    service.clear()

    ########################################################
    # Store long-term memory
    ########################################################

    service.remember(

        Memory(

            memory_type=MemoryType.LONG_TERM,

            content="Current project is FitOS",

            created_at=datetime.now(),

        )

    )

    ########################################################
    # Create planning engine
    ########################################################

    engine = PlanningEngine()

    ########################################################
    # Create active goal
    ########################################################

    goal = engine.goal_manager.create_goal(

        title="Build FitOS",

        description="Complete the FitOS project.",

    )

    engine.goal_manager.activate(

        goal,

    )

    engine.goal_manager.update_progress(

        goal,

        45.0,

    )

    ########################################################
    # Execute planning
    ########################################################

    print("=" * 60)
    print("GOAL-AWARE REASONING")
    print("=" * 60)

    plan = engine.build_plan(

        "Continue FitOS",

    )

    ########################################################
    # Display active goal
    ########################################################

    print()

    print("=" * 60)
    print("ACTIVE GOAL")
    print("=" * 60)

    print("Title      :", goal.title)

    print("Status     :", goal.status.name)

    print("Progress   :", goal.progress)

    ########################################################
    # Display execution plan
    ########################################################

    print()

    print("=" * 60)
    print("EXECUTION PLAN")
    print("=" * 60)

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