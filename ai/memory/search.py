import re


class MemorySearch:
    """
    Performs lightweight keyword extraction
    for memory retrieval.
    """

    STOP_WORDS = {
        "what",
        "who",
        "where",
        "when",
        "why",
        "how",
        "is",
        "are",
        "am",
        "was",
        "were",
        "the",
        "a",
        "an",
        "my",
        "your",
        "our",
        "their",
        "his",
        "her",
        "do",
        "does",
        "did",
        "i",
        "you",
        "me",
        "tell",
        "please",
        "remember",
        "about",
        "to",
        "of",
        "for",
        "and",
        "in",
        "on",
        "at",
        "with"
    }

    @classmethod
    def keywords(cls, text: str):

        words = re.findall(
            r"\b[a-zA-Z]+\b",
            text.lower()
        )

        return [
            word
            for word in words
            if word not in cls.STOP_WORDS
        ]