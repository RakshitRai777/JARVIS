from ai.conversation.entity_extraction.entity_parser import EntityParser
from ai.conversation.entity_extraction.extraction_result import ExtractionResult
from ai.llm_manager import LLMManager


class EntityExtractor:
    """
    Uses the LLM to extract important entities
    from assistant responses.
    """

    ##########################################################

    def __init__(self):

        self.llm = LLMManager()

        self.parser = EntityParser()

    ##########################################################

    def extract(self, text: str) -> ExtractionResult:

        prompt = f"""
Extract only the important named entities from the text.

Allowed entity types:

PERSON
ORGANIZATION
COMPANY
PRODUCT
PROGRAMMING_LANGUAGE
COUNTRY
CITY
PLACE
BOOK
MOVIE
EVENT

Rules:

- One entity per line.
- Format exactly:

TYPE: Name

- Ignore dates.
- Ignore numbers.
- Ignore adjectives.
- Ignore duplicates.
- If there are no entities return exactly:

NONE

Text:

{text}
"""

        messages = [

            {
                "role": "system",
                "content": (
                    "You extract named entities."
                ),
            },

            {
                "role": "user",
                "content": prompt,
            },

        ]

        raw = self.llm.generate(messages).strip()

        ######################################################

        if raw.upper() == "NONE":

            return ExtractionResult(

                entities=[],

                raw_output=raw,

            )

        ######################################################

        entities = self.parser.parse(raw)

        ######################################################

        return ExtractionResult(

            entities=entities,

            raw_output=raw,

        )