from datetime import datetime

from ai.memory.memory import Memory
from ai.memory.memory_context import MemoryContext
from ai.memory.memory_type import MemoryType

from ai.agent.goal import Goal
from ai.agent.goal_context import GoalContext
from ai.agent.goal_status import GoalStatus

from ai.planner.planning_context import PlanningContext


def main():

    ########################################################
    # Memory Context
    ########################################################

    memory_context = MemoryContext(

        query="Continue FitOS",

    )

    memory_context.add(

        Memory(

            memory_type=MemoryType.LONG_TERM,

            content="Current project is FitOS",

            created_at=datetime.now(),

        )

    )

    ########################################################
    # Goal Context
    ########################################################

    goal = Goal(

        title="Build FitOS",

        description="Complete the FitOS project.",

        status=GoalStatus.ACTIVE,

        progress=45.0,

    )

    goal_context = GoalContext(

        current_goal=goal,

        all_goals=[goal],

    )

    ########################################################
    # Planning Context
    ########################################################

    context = PlanningContext(

        command="Continue FitOS",

        memory_context=memory_context,

        goal_context=goal_context,

    )

    ########################################################

    print("=" * 60)
    print("PLANNING CONTEXT")
    print("=" * 60)

    print("Command :", context.command)

    print("Memory Count :", context.memory_context.count)

    print()

    print("Relevant Memories")
    print("-" * 60)

    for memory in context.memory_context.memories:

        print("-", memory.content)

    print()

    print("Goal")
    print("-" * 60)

    if context.goal_context.current_goal is not None:

        print("Title    :", context.goal_context.current_goal.title)

        print("Status   :", context.goal_context.current_goal.status.name)

        print("Progress :", context.goal_context.current_goal.progress)

    else:

        print("No active goal")


if __name__ == "__main__":

    main()