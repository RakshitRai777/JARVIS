from ai.knowledge.knowledge_result import KnowledgeResult
from ai.knowledge.knowledge_source import KnowledgeSource


class KnowledgeRouter:
    """
    Determines where information should come from.

    It DOES NOT retrieve information.

    It only decides the source.
    """

    def route(
        self,
        message: str
    ) -> KnowledgeResult:

        text = message.lower().strip()

        # -------------------------
        # Memory Questions
        # -------------------------

        memory_prefixes = [
            "what is my",
            "what's my",
            "who am i",
            "where do i",
            "what do i"
        ]

        if any(text.startswith(prefix) for prefix in memory_prefixes):

            return KnowledgeResult(
                source=KnowledgeSource.MEMORY,
                reason="Personal information requested."
            )

        # -------------------------
        # Web Questions
        # -------------------------

        web_keywords = [
            "today",
            "latest",
            "current",
            "news",
            "weather",
            "stock",
            "price",
            "president",
            "prime minister",
            "chief minister",
            "live",
            "score"
        ]

        if any(keyword in text for keyword in web_keywords):

            return KnowledgeResult(
                source=KnowledgeSource.WEB,
                reason="Current information required."
            )

        # -------------------------
        # Default
        # -------------------------

        return KnowledgeResult(
            source=KnowledgeSource.LLM,
            reason="General knowledge."
        )