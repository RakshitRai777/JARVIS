from dataclasses import dataclass

from ai.geometry.screen_region import ScreenRegion


@dataclass(slots=True)
class VerificationRule:
    """
    Describes how an action should be verified.

    A verification rule tells the verification
    framework what success looks like.

    Examples
    --------

    • Text exists
    • Text does not exist
    • Image exists
    • Window exists

    Optional region-based verification allows
    OCR to operate on only part of the screen,
    dramatically improving performance.
    """

    ############################################################

    rule_type: str

    ############################################################

    expected: str

    ############################################################
    # Optional region
    ############################################################

    region: ScreenRegion | None = None

    ############################################################

    confidence: float = 0.80

    ############################################################

    ignore_case: bool = True

    ############################################################

    def __str__(self):

        if self.region is None:

            return (

                f"{self.rule_type}"

                f"('{self.expected}')"

            )

        return (

            f"{self.rule_type}"

            f"('{self.expected}', "

            f"{self.region})"

        )