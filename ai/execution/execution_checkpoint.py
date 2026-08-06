from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4


@dataclass(slots=True)
class ExecutionCheckpoint:
    """
    Represents an execution checkpoint.
    """

    ############################################################

    checkpoint_id: str = field(

        default_factory=lambda: str(uuid4())

    )

    ############################################################

    workflow: str = ""

    ############################################################

    current_step: int = 0

    ############################################################

    total_steps: int = 0

    ############################################################

    timestamp: datetime = field(

        default_factory=datetime.now,

    )