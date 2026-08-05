from ai.verification.verifier import Verifier
from ai.verification.verification_rule import VerificationRule
from ai.verification.verification_result import VerificationResult

from ai.tools.vision.vision_manager import VisionManager


class OCRVerifier(Verifier):
    """
    Verifies screen content using OCR.

    Supports:
        • text_exists
        • text_not_exists

    Automatically performs region OCR when a
    ScreenRegion is supplied in the VerificationRule.
    """

    ############################################################

    def __init__(self):

        self.vision = VisionManager()

    ############################################################

    @property
    def name(self) -> str:

        return "text_exists"

    ############################################################

    def verify(
        self,
        rule: VerificationRule,
    ) -> VerificationResult:

        ########################################################
        # Read Screen or Region
        ########################################################

        if rule.region is None:

            vision_result = self.vision.read_screen()

        else:

            vision_result = self.vision.read_region(

                rule.region

            )

        ########################################################

        if not vision_result.success:

            return VerificationResult(

                success=False,

                error=vision_result.error,

                confidence=0.0,

            )

        ########################################################
        # OCR Text
        ########################################################

        screen_text = vision_result.cleaned_text

        expected = str(

            rule.expected

        )

        ########################################################
        # Ignore Case
        ########################################################

        if rule.ignore_case:

            screen_text = screen_text.lower()

            expected = expected.lower()

        ########################################################
        # Verify
        ########################################################

        if rule.rule_type == "text_exists":

            if expected in screen_text:

                return VerificationResult(

                    success=True,

                    message=f"Verified '{rule.expected}'.",

                    confidence=1.0,

                )

            return VerificationResult(

                success=False,

                error=f"'{rule.expected}' not found.",

                confidence=0.0,

            )

        ########################################################

        if rule.rule_type == "text_not_exists":

            if expected not in screen_text:

                return VerificationResult(

                    success=True,

                    message=f"Verified '{rule.expected}' is absent.",

                    confidence=1.0,

                )

            return VerificationResult(

                success=False,

                error=f"'{rule.expected}' was found.",

                confidence=0.0,

            )

        ########################################################

        return VerificationResult(

            success=False,

            error=f"Unsupported verification rule '{rule.rule_type}'.",

            confidence=0.0,

        )