from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class RuntimeResult:
    """
    Final result returned by the Agent Runtime.

    Represents the outcome of executing an entire task
    or workflow.
    """

    ############################################################

    success: bool

    ############################################################

    message: str = ""

    ############################################################

    data: Any | None = None

    ############################################################

    error: str | None = None

    ############################################################

    completed_tasks: int = 0

    ############################################################

    failed_tasks: int = 0

    ############################################################

    execution_time: float = 0.0

    ############################################################

    metadata: dict[str, Any] = field(

        default_factory=dict

    )

    ############################################################

    def __bool__(self):

        return self.success