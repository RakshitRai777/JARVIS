from ai.conversation.entities.entity import ConversationEntity
from ai.conversation.entities.entity_type import EntityType


class EntityParser:
    """
    Converts LLM output into ConversationEntity objects.

    Expected format:

    PERSON: Guido van Rossum
    PROGRAMMING_LANGUAGE: Python
    ORGANIZATION: CWI
    """

    ##########################################################

    def parse(self, text: str):

        entities = []

        for line in text.splitlines():

            line = line.strip()

            if not line:

                continue

            if ":" not in line:

                continue

            entity_type, name = line.split(":", 1)

            entity_type = entity_type.strip().upper()

            name = name.strip()

            try:

                entity_enum = EntityType[entity_type]

            except KeyError:

                entity_enum = EntityType.UNKNOWN

            entities.append(

                ConversationEntity(

                    name=name,

                    entity_type=entity_enum

                )

            )

        return entities