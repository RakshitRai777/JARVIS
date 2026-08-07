from datetime import datetime

from ai.agent.agent_state import AgentState

from ai.agent.goal import Goal
from ai.agent.goal_context import GoalContext
from ai.agent.goal_status import GoalStatus

from ai.memory.memory import Memory
from ai.memory.memory_context import MemoryContext
from ai.memory.memory_type import MemoryType

from ai.project.project import Project
from ai.project.project_status import ProjectStatus

from ai.planner.planning_context import PlanningContext


def main():

    ########################################################
    # Memory
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
    # Goal
    ########################################################

    goal = Goal(

        title="Build FitOS",

        status=GoalStatus.ACTIVE,

        progress=45.0,

    )

    goal_context = GoalContext(

        current_goal=goal,

        all_goals=[goal],

    )

    ########################################################
    # Project
    ########################################################

    project = Project(

        name="FitOS",

        status=ProjectStatus.ACTIVE,

        progress=75.0,

    )

    ########################################################
    # Agent State
    ########################################################

    state = AgentState(

        memory_context=memory_context,

        goal_context=goal_context,

        active_project=project,

    )

    ########################################################

    context = PlanningContext(

        command="Continue FitOS",

        agent_state=state,

    )

    ########################################################

    print("=" * 60)
    print("PLANNING CONTEXT")
    print("=" * 60)

    print()

    print("Command")

    print(context.command)

    print()

    print("Memory Count")

    print(context.agent_state.memory_context.count)

    print()

    print("Goal")

    goal = context.agent_state.goal_context.current_goal

    print(goal.title)

    print(goal.progress)

    print()

    print("Project")

    print(context.agent_state.active_project.name)

    print(context.agent_state.active_project.progress)


if __name__ == "__main__":

    main()