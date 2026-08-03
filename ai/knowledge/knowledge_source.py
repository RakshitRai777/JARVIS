from enum import Enum


class KnowledgeSource(Enum):
    """
    Possible knowledge sources for answering a request.
    """

    MEMORY = "MEMORY"

    WEB = "WEB"

    LLM = "LLM"

    NONE = "NONE"