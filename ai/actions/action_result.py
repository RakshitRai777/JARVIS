from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class ActionResult:
    """
    Result returned by an Action.

    Every Action returns one ActionResult,
    regardless of what it does.
    """

    ############################################################

    success: bool

    ############################################################

    message: str = ""

    ############################################################

    error: str | None = None

    ############################################################

    data: dict[str, Any] = field(

        default_factory=dict

    )

    ############################################################

    def __bool__(self):

        return self.success

    ############################################################

    def __str__(self):

        if self.success:

            return self.message

        return self.error or self.message