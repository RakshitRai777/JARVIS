from dataclasses import dataclass

from ai.planner.condition import Condition
from ai.verification.verification_rule import VerificationRule


@dataclass
class ExecutionStep:
    """
    Represents one executable step
    produced by the Planner.
    """

    ############################################################

    action: str

    ############################################################

    parameters: dict

    ############################################################

    description: str

    ############################################################

    condition: Condition | None = None

    ############################################################
    # Optional verification
    ############################################################

    verification_rule: VerificationRule | None = None