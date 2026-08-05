from dataclasses import dataclass


@dataclass(frozen=True)
class ChunkConfig:
    """
    Configuration for semantic chunking.
    """

    target_words: int = 220

    max_words: int = 320

    min_words: int = 80

    overlap_words: int = 40

    preserve_headings: bool = True