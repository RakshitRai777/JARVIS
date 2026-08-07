from datetime import datetime

from ai.agent.agent_state import AgentState

from ai.memory.memory import Memory
from ai.memory.memory_context import MemoryContext
from ai.memory.memory_type import MemoryType

from ai.agent.goal import Goal
from ai.agent.goal_context import GoalContext
from ai.agent.goal_status import GoalStatus

from ai.project.project import Project
from ai.project.project_status import ProjectStatus
from ai.project.milestone import Milestone
from ai.project.task import Task
from ai.project.task_status import TaskStatus


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

        description="AI Operating System",

        status=ProjectStatus.ACTIVE,

        progress=75.0,

    )

    ########################################################
    # Active Task
    ########################################################

    task = Task(

        title="Implement ProjectManager",

        description="Create the ProjectManager class.",

        status=TaskStatus.ACTIVE,

        progress=50.0,

        priority=1,

    )

    ########################################################
    # Active Milestone
    ########################################################

    milestone = Milestone(

        title="Project Intelligence",

        description="Build the Project subsystem.",

    )

    milestone.add_task(

        Task(

            title="ProjectStatus",

            status=TaskStatus.COMPLETED,

            progress=100.0,

        )

    )

    milestone.add_task(

        Task(

            title="Project",

            status=TaskStatus.COMPLETED,

            progress=100.0,

        )

    )

    milestone.add_task(task)

    ########################################################
    # Agent State
    ########################################################

    state = AgentState(

        memory_context=memory_context,

        goal_context=goal_context,

        active_project=project,

        active_milestone=milestone,

        active_task=task,

    )

    ########################################################

    print("=" * 60)
    print("AGENT STATE")
    print("=" * 60)

    ########################################################
    # Memory
    ########################################################

    print()
    print("Memory Count")
    print(state.memory_context.count)

    ########################################################
    # Goal
    ########################################################

    print()
    print("Active Goal")

    if state.goal_context.current_goal:

        goal = state.goal_context.current_goal

        print(goal.title)
        print(goal.status.name)
        print(goal.progress)

    else:

        print("None")

    ########################################################
    # Project
    ########################################################

    print()
    print("Active Project")

    if state.active_project:

        print(state.active_project.name)
        print(state.active_project.status.name)
        print(state.active_project.progress)

    else:

        print("None")

    ########################################################
    # Milestone
    ########################################################

    print()
    print("Active Milestone")

    if state.active_milestone:

        print(state.active_milestone.title)
        print(state.active_milestone.progress)
        print(state.active_milestone.completed)

    else:

        print("None")

    ########################################################
    # Task
    ########################################################

    print()
    print("Active Task")

    if state.active_task:

        print(state.active_task.title)
        print(state.active_task.status.name)
        print(state.active_task.progress)

    else:

        print("None")

    ########################################################
    # Metadata
    ########################################################

    print()
    print("Metadata")
    print(state.metadata)


if __name__ == "__main__":

    main()