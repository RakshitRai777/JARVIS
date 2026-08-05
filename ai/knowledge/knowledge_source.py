from enum import Enum


class KnowledgeSource(Enum):
    """
    Available knowledge sources.

    The KnowledgeRouter decides which source(s)
    should be used for a given user request.
    """

    MEMORY = "memory"

    WEB = "web"

    LLM = "llm"

    HYBRID = "hybrid"