from dataclasses import dataclass

from ai.conversation.entities.entity import ConversationEntity


@dataclass
class ExtractionResult:
    """
    Result returned by the entity extractor.
    """

    entities: list[ConversationEntity]

    raw_output: str