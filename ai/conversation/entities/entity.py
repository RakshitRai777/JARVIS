from dataclasses import dataclass

from ai.conversation.entities.entity_type import EntityType


@dataclass
class ConversationEntity:
    """
    Represents one entity mentioned
    during the conversation.
    """

    name: str

    entity_type: EntityType

    mentions: int = 1

    last_turn: int = 0