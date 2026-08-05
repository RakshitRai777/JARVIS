from dataclasses import dataclass


@dataclass
class RewriteResult:
    """
    Result returned by the Query Rewriter.

    Attributes
    ----------
    original_query : str
        User's original question.

    rewritten_query : str
        Query that should be sent to the search engine.

    changed : bool
        Whether the query was rewritten.

    reason : str
        Explanation of why it was rewritten.
    """

    original_query: str

    rewritten_query: str

    changed: bool = False

    reason: str = ""