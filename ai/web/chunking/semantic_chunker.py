import re

from ai.embeddings.chunk import Chunk

from ai.web.chunking.chunk_config import ChunkConfig
from ai.web.chunking.heading_detector import HeadingDetector
from ai.web.chunking.paragraph_merger import ParagraphMerger
from ai.web.chunking.overlap_builder import OverlapBuilder
from ai.web.chunking.oversized_splitter import OversizedSplitter

class SemanticChunker:
    """
    Production Semantic Chunker.

    Pipeline
    --------
    Raw Text
        ↓
    Paragraph Split
        ↓
    Heading Detection
        ↓
    Paragraph Merge
        ↓
    Overlap Builder
        ↓
    Chunk Objects
    """

    ##########################################################

    def __init__(self, config: ChunkConfig | None = None):

        self.config = config or ChunkConfig()

        self.heading_detector = HeadingDetector()

        self.merger = ParagraphMerger(self.config)

        self.overlap = OverlapBuilder(self.config)

        self.splitter = OversizedSplitter(self.config)

    ##########################################################

    def split_paragraphs(
        self,
        text: str
    ) -> list[str]:

        paragraphs = [

            p.strip()

            for p in re.split(r"\n\s*\n", text)

            if p.strip()

        ]

        return paragraphs

    ##########################################################

    def attach_headings(
        self,
        paragraphs: list[str]
    ) -> list[str]:

        if not self.config.preserve_headings:

            return paragraphs

        output = []

        current_section = []

        current_heading = ""

        for paragraph in paragraphs:

            first_line = paragraph.splitlines()[0].strip()

            if self.heading_detector.is_heading(first_line):

                if current_section:

                    output.append("\n\n".join(current_section))
                    current_section = []

                current_heading = first_line

                continue

            if current_heading and not current_section:

                current_section.append(current_heading)

            current_section.append(paragraph)

        if current_section:

            output.append("\n\n".join(current_section))

        return output

    ##########################################################

    def chunk(
        self,
        text: str
    ) -> list[Chunk]:

        ######################################################
        # Split
        ######################################################

        paragraphs = self.split_paragraphs(text)

        ######################################################
        # Preserve headings
        ######################################################

        paragraphs = self.attach_headings(paragraphs)

        ######################################################
        # Merge
        ######################################################

        merged = self.merger.merge(paragraphs)

        ######################################################
        # Split oversized semantic blocks
        ######################################################

        merged = self.splitter.split(merged)

        ######################################################
        # Overlap
        ######################################################

        merged = self.overlap.build(merged)

        ######################################################
        # Convert to Chunk objects
        ######################################################

        chunks = []

        for i, chunk_text in enumerate(merged):

            words = len(chunk_text.split())
            chars = len(chunk_text)
            print(
                f"[Chunk {i}] "
                f"{words} words | "
                f"{chars} chars"
            )

            chunks.append(

                Chunk(

                    text=chunk_text,

                    embedding=None,

                    score=0.0,

                    title="",

                    source="",

                    metadata={

                        "chunk_index": i

                    }

                )

            )

        return chunks