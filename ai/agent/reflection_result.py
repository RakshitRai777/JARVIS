from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True)
class ReflectionResult:
    """
    Represents the result of reflecting on an execution.
    """

    ############################################################

    success: bool = False

    ############################################################

    reflection: str = ""

    ############################################################

    learning: str = ""

    ############################################################

    should_store: bool = False

    ############################################################

    timestamp: datetime = field(

        default_factory=datetime.now,

    )