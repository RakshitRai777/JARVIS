from dataclasses import dataclass, field
from ai.agent.goal_context import GoalContext
from ai.memory.memory_context import MemoryContext


@dataclass(slots=True)
class PlanningContext:
    """
    Context supplied to the planner.

    Contains the user's command together
    with any relevant memories.
    """

    ############################################################

    command: str = ""

    ############################################################

    memory_context: MemoryContext = field(

        default_factory=MemoryContext,

    )

    memory_summary: str = ""

    #############################################################

    goal_context: GoalContext = field(
        default_factory=GoalContext,
    )