from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from ai.execution.execution_result import ExecutionResult


@dataclass
class RuntimeHistoryEntry:
    """
    Represents one completed execution step.

    RuntimeHistory is simply a list of these.
    """

    ############################################################

    timestamp: datetime

    ############################################################

    workflow: str

    ############################################################

    step: str

    ############################################################

    action: str

    ############################################################

    command: str | None

    ############################################################

    result: ExecutionResult