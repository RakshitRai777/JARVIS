from dataclasses import dataclass, field
from datetime import datetime

from ai.execution.execution_checkpoint import ExecutionCheckpoint
from ai.execution.execution_result import ExecutionResult


@dataclass(slots=True)
class WorkflowResumeResult:
    """
    Represents the outcome of a workflow resume attempt.

    Responsibilities
    ----------------
    • Indicate whether resume succeeded
    • Store the checkpoint used
    • Store the execution result
    • Store the resumed step
    • Indicate whether the workflow completed

    This class contains data only.
    """

    ############################################################

    resumed: bool

    ############################################################

    checkpoint: ExecutionCheckpoint | None = None

    ############################################################

    execution_result: ExecutionResult | None = None

    ############################################################

    resumed_step: int = 0

    ############################################################

    completed: bool = False

    ############################################################

    timestamp: datetime = field(

        default_factory=datetime.now,

    )