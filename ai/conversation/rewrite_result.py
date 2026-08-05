from dataclasses import dataclass


@dataclass
class RewriteResult:
    """
    Result of rewriting a query.
    """

    original_query: str

    rewritten_query: str

    changed: bool

    reason: str