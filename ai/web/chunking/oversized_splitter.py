from ai.web.chunking.chunk_config import ChunkConfig
from ai.web.chunking.sentence_splitter import SentenceSplitter


class OversizedSplitter:
    """
    Splits oversized semantic blocks while preserving
    sentence boundaries whenever possible.
    """

    ##########################################################

    def __init__(self, config: ChunkConfig | None = None):

        self.config = config or ChunkConfig()

        self.sentence_splitter = SentenceSplitter()

    ##########################################################

    @staticmethod
    def word_count(text: str) -> int:

        return len(text.split())

    ##########################################################

    def split(
        self,
        blocks: list[str],
    ) -> list[str]:

        if not blocks:
            return []

        output = []

        ######################################################

        for block in blocks:

            ##################################################
            # Already fits
            ##################################################

            if self.word_count(block) <= self.config.max_words:

                output.append(block)

                continue

            ##################################################
            # Sentence-aware splitting
            ##################################################

            sentences = self.sentence_splitter.split(block)

            current = []
            current_words = 0

            for sentence in sentences:

                words = self.word_count(sentence)

                ################################################
                # Extremely long sentence
                ################################################

                if words > self.config.max_words:

                    if current:

                        output.append(" ".join(current))

                        current = []
                        current_words = 0

                    sentence_words = sentence.split()

                    start = 0

                    while start < len(sentence_words):

                        end = min(
                            start + self.config.target_words,
                            len(sentence_words)
                        )

                        output.append(
                            " ".join(sentence_words[start:end])
                        )

                        start = end

                    continue

                ################################################
                # Start a new chunk
                ################################################

                if current_words + words > self.config.target_words:

                    output.append(" ".join(current))

                    current = []
                    current_words = 0

                current.append(sentence)

                current_words += words

            ##################################################

            if current:

                output.append(" ".join(current))

        ######################################################

        return output