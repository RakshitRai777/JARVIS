from dataclasses import dataclass


@dataclass
class ResolutionResult:
    """
    Result of conversational query resolution.
    """

    original_query: str

    resolved_query: str

    changed: bool

    reason: str