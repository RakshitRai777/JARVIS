from dataclasses import dataclass, field
from datetime import datetime

from ai.project.task_status import TaskStatus


@dataclass(slots=True)
class Task:
    """
    Represents an executable unit of work
    within a project.
    """

    ############################################################

    title: str = ""

    ############################################################

    description: str = ""

    ############################################################

    status: TaskStatus = TaskStatus.PENDING

    ############################################################

    progress: float = 0.0

    ############################################################

    priority: int = 0

    ############################################################

    created_at: datetime = field(

        default_factory=datetime.now,

    )

    ############################################################

    completed_at: datetime | None = None