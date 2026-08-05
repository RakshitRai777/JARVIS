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
        # Read Screen
        ########################################################

        vision_result = self.vision.read_screen()

        if not vision_result.success:

            return VerificationResult(

                success=False,

                error=vision_result.error,

                confidence=0.0,

            )

        ########################################################
        # OCR Text
        ########################################################

        screen_text = vision_result.cleaned_text.lower()

        expected = str(

            rule.expected

        ).lower()

        ########################################################
        # Verify
        ########################################################

        if expected in screen_text:

            return VerificationResult(

                success=True,

                message=f"Verified '{rule.expected}'.",

                confidence=1.0,

            )

        ########################################################

        return VerificationResult(

            success=False,

            error=f"'{rule.expected}' not found.",

            confidence=0.0,

        )