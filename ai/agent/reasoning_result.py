from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True)
class ReasoningResult:
    """
    Represents the result of an AI reasoning step.
    """

    ############################################################

    success: bool = False

    ############################################################

    thought: str = ""

    ############################################################

    conclusion: str = ""

    ############################################################

    confidence: float = 0.0

    ############################################################

    timestamp: datetime = field(

        default_factory=datetime.now,

    )