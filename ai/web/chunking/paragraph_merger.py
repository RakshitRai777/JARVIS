from ai.web.chunking.chunk_config import ChunkConfig


class ParagraphMerger:
    """
    Merge small paragraphs into semantic blocks.

    Goals
    -----
    • Avoid tiny chunks
    • Preserve paragraph boundaries
    • Keep chunks near target size
    """

    ##########################################################

    def __init__(self, config: ChunkConfig | None = None):

        self.config = config or ChunkConfig()

    ##########################################################

    @staticmethod
    def word_count(text: str) -> int:

        return len(text.split())

    ##########################################################

    def merge(self, paragraphs: list[str]) -> list[str]:

        if not paragraphs:
            return []

        merged = []

        current = []

        current_words = 0

        ######################################################

        for paragraph in paragraphs:

            paragraph = paragraph.strip()

            if not paragraph:
                continue

            words = self.word_count(paragraph)

            ##################################################
            # If adding this paragraph would exceed max size,
            # flush current chunk first.
            ##################################################

            if (
                current
                and current_words + words > self.config.max_words
            ):

                merged.append("\n\n".join(current))

                current = []

                current_words = 0

            ##################################################

            current.append(paragraph)

            current_words += words

            ##################################################
            # If we've reached target size, flush.
            ##################################################

            if current_words >= self.config.target_words:

                merged.append("\n\n".join(current))

                current = []

                current_words = 0

        ######################################################
        # Remaining text
        ######################################################

        if current:

            if (
                merged
                and current_words < self.config.min_words
            ):

                merged[-1] += "\n\n" + "\n\n".join(current)

            else:

                merged.append("\n\n".join(current))

        return merged