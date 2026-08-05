from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class VerificationResult:
    """
    Result returned after verifying an action.
    """

    ############################################################

    success: bool

    ############################################################

    message: str = ""

    ############################################################

    error: str | None = None

    ############################################################

    confidence: float = 1.0

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