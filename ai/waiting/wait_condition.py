from dataclasses import dataclass

from ai.verification.verification_rule import VerificationRule


@dataclass(slots=True)
class WaitCondition:
    """
    Describes a condition that must become true
    before execution can continue.

    The WaitManager repeatedly evaluates the
    verification rule until it succeeds or
    the timeout expires.
    """

    ############################################################

    rule: VerificationRule

    ############################################################

    timeout: float = 10.0

    ############################################################

    poll_interval: float = 0.2

    ############################################################

    def __str__(self):

        return (

            f"WaitUntil("

            f"{self.rule}"

            f")"

        )
    