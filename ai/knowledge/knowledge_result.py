from dataclasses import dataclass

from ai.knowledge.knowledge_source import KnowledgeSource


@dataclass
class KnowledgeResult:
    """
    Result returned by the Knowledge Router.
    """

    source: KnowledgeSource

    reason: str = ""