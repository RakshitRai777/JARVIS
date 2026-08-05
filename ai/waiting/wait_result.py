from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class WaitResult:
    """
    Result returned by the WaitManager.

    Indicates whether a wait condition
    completed successfully or timed out.
    """

    ############################################################

    success: bool

    ############################################################

    message: str = ""

    ############################################################

    timed_out: bool = False

    ############################################################

    elapsed_time: float = 0.0

    ############################################################

    error: str | None = None

    ############################################################

    data: dict[str, Any] | None = None

    ############################################################

    def __bool__(self):

        return self.success

    ############################################################

    def __str__(self):

        if self.success:

            return self.message

        return self.error or self.message