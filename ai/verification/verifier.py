from abc import ABC, abstractmethod

from ai.verification.verification_result import VerificationResult
from ai.verification.verification_rule import VerificationRule


class Verifier(ABC):
    """
    Base class for every verification strategy.

    Examples
    --------
    OCRVerifier
    WindowVerifier
    ClipboardVerifier
    FileVerifier
    """

    ############################################################

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Unique verifier name.

        Example:
            text_exists
            file_exists
            window_title
        """
        pass

    ############################################################

    @abstractmethod
    def verify(
        self,
        rule: VerificationRule,
    ) -> VerificationResult:
        """
        Execute verification.
        """
        pass