from typing import List

from ai.embeddings.chunk import Chunk


class WebContextBuilder:
    """
    Builds a concise context from retrieved web chunks.

    Responsibilities
    ----------------
    - Remove duplicate chunks
    - Preserve ranking order
    - Limit total context size
    - Include source information
    """

    def __init__(
        self,
        max_characters: int = 2500
    ):

        self.max_characters = max_characters

    ##################################################################

    def build(
        self,
        chunks: List[Chunk]
    ) -> str:

        if not chunks:
            return ""

        context = []

        seen = set()

        current_length = 0

        ##############################################################

        for chunk in chunks:

            text = chunk.text.strip()

            if not text:
                continue

            # Remove exact duplicate chunks
            if text in seen:
                continue

            seen.add(text)

            block = (
                f"Source: {chunk.title}\n"
                f"URL: {chunk.source}\n\n"
                f"{text}\n"
            )

            block_length = len(block)

            if current_length + block_length > self.max_characters:
                break

            context.append(block)

            current_length += block_length

        ##############################################################

        return "\n\n-----------------------------\n\n".join(context)