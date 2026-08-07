from dataclasses import dataclass, field
from datetime import datetime

from ai.project.project_status import ProjectStatus
from ai.project.milestone import Milestone


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
    # Project milestones
    ############################################################

    milestones: list[Milestone] = field(

        default_factory=list,

    )

    ############################################################

    created_at: datetime = field(

        default_factory=datetime.now,

    )

    ############################################################

    completed_at: datetime | None = None

    ############################################################
    