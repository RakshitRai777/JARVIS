from dataclasses import dataclass, field


@dataclass
class ExpandedQuery:
    """
    Represents a set of search queries generated
    from a single user question.
    """

    original_query: str

    queries: list[str] = field(default_factory=list)

    reason: str = ""