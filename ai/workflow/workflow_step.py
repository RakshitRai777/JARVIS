from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class WorkflowStep:
    """
    Represents a single executable workflow step.

    Example
    -------

    ClickText

    TypeText

    PressKey

    Wait

    OpenURL
    """

    ############################################################

    action: str

    ############################################################

    parameters: dict[str, Any] = field(

        default_factory=dict

    )

    ############################################################

    description: str = ""

    ############################################################

    verify: bool = True

    ############################################################

    timeout: float = 10.0

    ############################################################

    retry_count: int = 1

    ############################################################

    def __str__(self):

        return (

            f"{self.action}"

            f"({self.parameters})"

        )