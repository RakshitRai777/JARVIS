from ai.embeddings.chunk import Chunk


class ContextBudget:
    """
    Limits the amount of context sent to the LLM.

    This prevents:

    • HTTP 413 errors
    • Excessive token usage
    • Slow responses

    The highest-ranked chunks are kept first.
    """

    ##########################################################

    MAX_CONTEXT_CHARS = 6000

    MAX_CHUNKS = 5

    ##########################################################

    def limit(
        self,
        chunks: list[Chunk],
    ) -> list[Chunk]:

        if not chunks:
            return []

        kept = []

        total_chars = 0

        ######################################################

        for chunk in chunks[: self.MAX_CHUNKS]:

            text = chunk.text or ""

            remaining = self.MAX_CONTEXT_CHARS - total_chars

            if remaining <= 0:
                break

            ##################################################
            # Entire chunk fits
            ##################################################

            if len(text) <= remaining:

                kept.append(chunk)

                total_chars += len(text)

                continue

            ##################################################
            # Trim the last chunk
            ##################################################

            shortened = Chunk(

                text=text[:remaining],

                embedding=None,

            )

            shortened.title = chunk.title

            shortened.source = chunk.source

            kept.append(shortened)

            total_chars += len(shortened.text)

            break

        ######################################################

        print()

        print(
            f"[ContextBudget] "
            f"{len(chunks)} -> {len(kept)} chunks | "
            f"{total_chars} chars"
        )

        print()

        return kept