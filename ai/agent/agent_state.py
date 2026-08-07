from dataclasses import dataclass, field

from ai.memory.memory_context import MemoryContext

from ai.agent.goal_context import GoalContext

from ai.project.project import Project
from ai.project.milestone import Milestone
from ai.project.task import Task


@dataclass(slots=True)
class AgentState:
    """
    Represents the complete runtime state
    of the AI agent.
    """

    ############################################################

    memory_context: MemoryContext = field(
        default_factory=MemoryContext,
    )

    ############################################################

    goal_context: GoalContext = field(
        default_factory=GoalContext,
    )

    ############################################################

    active_project: Project | None = None

    ############################################################

    active_milestone: Milestone | None = None

    ############################################################

    active_task: Task | None = None

    ############################################################

    metadata: dict = field(
        default_factory=dict,
    )