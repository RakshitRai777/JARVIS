from ai.verification.verifier import Verifier
from ai.verification.verification_rule import VerificationRule
from ai.verification.verification_result import VerificationResult
from ai.verification.ocr_verifier import OCRVerifier

class VerificationManager:
    """
    Central manager for verification.

    Responsibilities
    ----------------
    • Register verifiers
    • Resolve verifier
    • Execute verification

    Future Responsibilities
    -----------------------
    • Retry verification
    • Timeout handling
    • Confidence filtering
    • Logging
    """

    ############################################################

    def __init__(self):

        self._verifiers: dict[str, Verifier] = {}

        self.register(
            OCRVerifier()
        )

    ############################################################

    def register(
        self,
        verifier: Verifier,
    ):

        self._verifiers[

            verifier.name

        ] = verifier

    ############################################################

    def get(
        self,
        rule_type: str,
    ) -> Verifier | None:

        return self._verifiers.get(

            rule_type

        )

    ############################################################

    def verify(
        self,
        rule: VerificationRule,
    ) -> VerificationResult:

        verifier = self.get(

            rule.rule_type

        )

        if verifier is None:

            return VerificationResult(

                success=False,

                error=f"No verifier registered for '{rule.rule_type}'.",

            )

        return verifier.verify(

            rule

        )

    ############################################################

    def all(self):

        return list(

            self._verifiers.values()

        )