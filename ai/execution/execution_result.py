from dataclasses import dataclass
from typing import Any


@dataclass
class ExecutionResult:
    success: bool
    message: str
    data: Any = None
    error: str | None = None
    execution_time: float = 0.0