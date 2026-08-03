from ai.embeddings.chunk import Chunk


class Chunker:
    """
    Splits text into semantic chunks.
    """

    def __init__(

        self,

        chunk_size=1200,

        overlap=200

    ):

        self.chunk_size = chunk_size

        self.overlap = overlap

    ##########################################################

    def chunk(
        self,
        text: str
    ) -> list[Chunk]:

        if not text:

            return []

        chunks = []

        start = 0

        length = len(text)

        while start < length:

            end = min(

                start + self.chunk_size,

                length

            )

            if end < length:

                split = text.rfind(

                    "\n\n",

                    start,

                    end

                )

                if split != -1:

                    end = split

            chunk_text = text[start:end].strip()

            if chunk_text:

                chunks.append(

                    Chunk(

                        text=chunk_text

                    )

                )

            if end >= length:

                break

            start = max(

                end - self.overlap,

                start + 1

            )

        return chunks