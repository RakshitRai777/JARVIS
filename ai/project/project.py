from dataclasses import dataclass, field
from datetime import datetime

from ai.project.project_status import ProjectStatus


@dataclass(slots=True)
class Project:
    """
    Represents a long-running project managed
    by the AI agent.
    """

    ############################################################

    name: str = ""

    ############################################################

    description: str = ""

    ############################################################

    status: ProjectStatus = ProjectStatus.PLANNING

    ############################################################

    progress: float = 0.0

    ############################################################

    created_at: datetime = field(

        default_factory=datetime.now,

    )

    ############################################################

    completed_at: datetime | None = None