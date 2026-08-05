from ai.web.chunking.chunk_config import ChunkConfig


class OverlapBuilder:
    """
    Adds word overlap between semantic chunks.
    """

    ##########################################################

    def __init__(self, config: ChunkConfig | None = None):

        self.config = config or ChunkConfig()

    ##########################################################

    def build(
        self,
        chunks: list[str],
    ) -> list[str]:

        if len(chunks) <= 1:
            return chunks

        result = [chunks[0]]

        overlap = self.config.overlap_words

        ######################################################

        for chunk in chunks[1:]:

            previous = result[-1]

            previous_words = previous.split()

            overlap_words = previous_words[-overlap:]

            merged = (
                " ".join(overlap_words)
                + "\n\n"
                + chunk
            )

            result.append(merged)

        ######################################################

        return result