import re

from ai.conversation.query_resolution.resolution_result import ResolutionResult


class ConversationResolver:
    """
    Resolves conversational references.

    Priority

    1. Entity Memory
    2. Regex fallback
    """

    ##########################################################

    PRONOUNS = {
        "he",
        "she",
        "him",
        "his",
        "her",
        "they",
        "them",
        "it",
        "its",
    }

    ##########################################################

    def resolve(
        self,
        query: str,
        conversation,
    ) -> ResolutionResult:

        lower = query.lower()

        ######################################################
        # No pronouns
        ######################################################

        if not any(
            p in lower.split()
            for p in self.PRONOUNS
        ):

            return ResolutionResult(
                original_query=query,
                resolved_query=query,
                changed=False,
                reason="No conversational reference."
            )

        ######################################################
        # NEW
        # Resolve using EntityMemory FIRST
        ######################################################

        entity_memory = conversation.entity_memory

        entity = None

        ######################################################
        # Person
        ######################################################

        if any(
            p in lower.split()
            for p in ("he", "him", "his", "she", "her")
        ):

            person = entity_memory.resolve_pronoun("he")

            if person is not None:

                entity = person.name

        ######################################################
        # Object / Language / Company / Product
        ######################################################

        elif any(
            p in lower.split()
            for p in ("it", "its")
        ):

            obj = entity_memory.resolve_pronoun("it")

            if obj is not None:

                entity = obj.name

        ######################################################
        # Plural
        ######################################################

        elif any(
            p in lower.split()
            for p in ("they", "them")
        ):

            obj = entity_memory.resolve_pronoun("they")

            if obj is not None:

                entity = obj.name

        ######################################################
        # Fallback to regex
        ######################################################

        if entity is None:

            history = conversation.history()

            for message in reversed(history):

                if message.role != "assistant":
                    continue

                match = re.search(
                    r"([A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)",
                    message.content
                )

                if match:

                    entity = match.group(1)

                    break

        ######################################################

        if entity is None:

            return ResolutionResult(
                original_query=query,
                resolved_query=query,
                changed=False,
                reason="No entity found."
            )

        ######################################################

        resolved = query

        for pronoun in self.PRONOUNS:

            resolved = re.sub(
                rf"\b{pronoun}\b",
                entity,
                resolved,
                flags=re.IGNORECASE,
            )

        ######################################################

        return ResolutionResult(
            original_query=query,
            resolved_query=resolved,
            changed=True,
            reason=f"Resolved reference to '{entity}'."
        )