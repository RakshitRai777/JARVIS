import re

from ai.conversation.entities.entity import ConversationEntity


class EntityMatcher:
    """
    Computes an entity relevance score for a chunk.

    Higher score means the chunk talks more about
    the important entities from the user's query.
    """

    ##########################################################

    def score(
        self,
        entities: list[ConversationEntity],
        text: str,
    ) -> float:

        if not entities:
            return 0.0

        lower = text.lower()

        matches = 0

        for entity in entities:

            pattern = re.escape(entity.name.lower())

            if re.search(rf"\b{pattern}\b", lower):

                matches += 1

        return matches / len(entities)