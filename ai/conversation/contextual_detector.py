import re


class ContextualDetector:
    """
    Detects whether a query depends on previous conversation.

    If False:
        Skip contextual rewriting.

    If True:
        Use ContextualQueryRewriter.
    """

    PRONOUNS = {
        "he",
        "she",
        "they",
        "them",
        "his",
        "her",
        "their",
        "it",
        "its",
        "this",
        "that",
        "these",
        "those",
        "there",
        "here",
        "former",
        "latter",
        "him",
    }

    def needs_context(self, query: str) -> bool:

        query = query.lower()

        words = re.findall(r"[a-zA-Z']+", query)

        if not words:
            return False

        ####################################################
        # Pronouns
        ####################################################

        if any(word in self.PRONOUNS for word in words):
            return True

        ####################################################
        # Context-dependent phrases
        ####################################################

        context_patterns = [
            "what about",
            "how about",
            "what happened next",
            "tell me more",
            "and then",
            "what else",
            "where was he",
            "where was she",
            "where was it",
            "when was he",
            "when was she",
            "when was it",
        ]

        lower_query = query.lower()

        for pattern in context_patterns:
            if lower_query.startswith(pattern):
                return True

        return False