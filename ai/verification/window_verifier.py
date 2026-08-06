from ai.desktop.window_manager import WindowManager

from ai.verification.verifier import Verifier
from ai.verification.verification_rule import VerificationRule
from ai.verification.verification_result import VerificationResult


class WindowVerifier(Verifier):
    """
    Verifies desktop windows.

    Supports:
        • window_exists
        • window_not_exists
    """

    ############################################################

    def __init__(self):

        self.manager = WindowManager()

    ############################################################

    @property
    def name(self) -> str:

        return "window_exists"

    ############################################################

    def verify(
        self,
        rule: VerificationRule,
    ) -> VerificationResult:

        ########################################################
        # Exists
        ########################################################

        if rule.rule_type == "window_exists":

            exists = self.manager.exists(

                rule.expected,

            )

            if exists:

                return VerificationResult(

                    success=True,

                    message=f"Verified window '{rule.expected}'.",

                    confidence=1.0,

                )

            return VerificationResult(

                success=False,

                error=f"Window '{rule.expected}' was not found.",

                confidence=0.0,

            )

        ########################################################
        # Not Exists
        ########################################################

        if rule.rule_type == "window_not_exists":

            exists = self.manager.exists(

                rule.expected,

            )

            if not exists:

                return VerificationResult(

                    success=True,

                    message=f"Verified '{rule.expected}' is absent.",

                    confidence=1.0,

                )

            return VerificationResult(

                success=False,

                error=f"Window '{rule.expected}' still exists.",

                confidence=0.0,

            )

        ########################################################

        return VerificationResult(

            success=False,

            error=f"Unsupported verification rule '{rule.rule_type}'.",

            confidence=0.0,

        )