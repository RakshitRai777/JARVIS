from dataclasses import dataclass, field
from datetime import datetime

from ai.execution.execution_result import ExecutionResult


@dataclass(slots=True)
class RecoveryResult:
    """
    Represents the outcome of a recovery attempt.

    Responsibilities
    ----------------
    • Store failure information
    • Store recovery status
    • Store timestamp
    • Store execution result

    This class contains data only.
    The RecoveryEngine performs the
    actual recovery process.
    """

    ############################################################

    recovered: bool

    ############################################################

    workflow: str | None = None

    ############################################################

    step: str | None = None

    ############################################################

    error: str | None = None

    ############################################################

    execution_result: ExecutionResult | None = None

    ############################################################

    timestamp: datetime = field(
        default_factory=datetime.now,
    )