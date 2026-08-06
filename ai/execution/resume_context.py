from dataclasses import dataclass

from ai.execution.execution_cursor import ExecutionCursor
from ai.execution.execution_engine import ExecutionEngine


@dataclass(slots=True)
class ResumeContext:
    """
    Context required to resume a workflow.

    Responsibilities
    ----------------
    • Provide the execution cursor
    • Provide the execution engine

    This class contains data only.
    """

    ############################################################

    cursor: ExecutionCursor

    ############################################################

    execution_engine: ExecutionEngine