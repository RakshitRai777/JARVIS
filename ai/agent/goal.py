from dataclasses import dataclass, field
from datetime import datetime

from ai.agent.goal_status import GoalStatus


@dataclass(slots=True)
class Goal:
    """
    Represents a long-running objective
    managed by the agent.
    """

    ############################################################

    title: str = ""

    ############################################################

    description: str = ""

    ############################################################

    status: GoalStatus = GoalStatus.PENDING

    ############################################################

    progress: float = 0.0

    ############################################################

    created_at: datetime = field(

        default_factory=datetime.now,

    )

    ############################################################

    completed_at: datetime | None = None