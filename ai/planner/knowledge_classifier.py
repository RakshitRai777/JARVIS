from enum import Enum


class KnowledgeSource(Enum):
    """
    Possible knowledge sources.
    """

    MEMORY = "memory"

    WEB = "web"

    LLM = "llm"


class KnowledgeClassifier:
    """
    Decides where a question should be answered from.

    Priority
    --------
    1. Memory
    2. Web
    3. LLM

    This classifier is intentionally lightweight and fast.
    """

    ############################################################

    MEMORY_WORDS = {

        "remember",
        "memory",
        "my",
        "mine",
        "our",
        "previous",
        "previously",
        "earlier",
        "last time",
        "history",
        "saved",
        "profile",

    }

    ############################################################

    WEB_WORDS = {

        # comparisons
        "compare",
        "comparison",
        "vs",
        "versus",

        # shopping
        "buy",
        "price",
        "cost",
        "review",
        "reviews",
        "best",
        "recommend",
        "recommendation",
        "spec",
        "specs",
        "specification",
        "benchmark",
        "performance",

        # factual
        "who",
        "where",
        "when",
        "what is",
        "created",
        "invented",
        "founder",
        "ceo",
        "owner",
        "born",
        "died",
        "capital",

        # documentation
        "documentation",
        "docs",
        "tutorial",
        "guide",

        # freshness
        "latest",
        "today",
        "current",
        "news",
        "released",
        "release",
        "update",

    }

    ############################################################

    def classify(
        self,
        question: str,
    ) -> KnowledgeSource:

        if not question:

            return KnowledgeSource.LLM

        q = question.lower().strip()

        ########################################################
        # Memory
        ########################################################

        for word in self.MEMORY_WORDS:

            if word in q:

                return KnowledgeSource.MEMORY

        ########################################################
        # Web
        ########################################################

        for word in self.WEB_WORDS:

            if word in q:

                return KnowledgeSource.WEB

        ########################################################
        # Default
        ########################################################

        return KnowledgeSource.LLM