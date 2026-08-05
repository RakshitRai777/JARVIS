from dataclasses import dataclass, field
from typing import Any

from ai.execution.execution_policy import ExecutionPolicy
from ai.verification.verification_rule import VerificationRule


@dataclass(slots=True)
class WorkflowStep:
    """
    Represents one executable workflow step.

    A WorkflowStep describes:

    • What to execute
    • How to execute it
    • How to verify success
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
    # NEW
    ############################################################

    policy: ExecutionPolicy = field(

        default_factory=ExecutionPolicy

    )

    ############################################################
    # NEW
    ############################################################

    verification_rule: VerificationRule | None = None

    ############################################################

    def __str__(self):

        return (

            f"{self.action}"

            f"({self.parameters})"

        )