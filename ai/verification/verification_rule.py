from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class VerificationRule:
    """
    Describes what should be verified after
    executing an action.
    """

    ############################################################

    rule_type: str

    ############################################################

    expected: Any

    ############################################################

    timeout: float = 5.0

    ############################################################

    confidence_threshold: float = 0.80

    ############################################################

    metadata: dict[str, Any] = field(

        default_factory=dict

    )

    ############################################################

    def __str__(self):

        return (

            f"{self.rule_type}"

            f"({self.expected})"

        )