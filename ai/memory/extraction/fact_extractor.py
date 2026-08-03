from dataclasses import dataclass


@dataclass
class ExtractedFact:

    content: str

    confidence: float


class FactExtractor:
    """
    Extract personal facts from user messages.

    Later this will use the LLM.
    """

    PATTERNS = [

        "my",

        "i am",

        "i'm",

        "i live",

        "i study",

        "i work",

        "i like",

        "i prefer",

        "my favourite",

        "my favorite",

        "my name"

    ]

    def extract(self, text: str):

        lower = text.lower()

        for pattern in self.PATTERNS:

            if pattern in lower:

                return ExtractedFact(

                    content=text,

                    confidence=0.90

                )

        return None