from sentence_transformers import SentenceTransformer

from ai.embeddings.chunk import Chunk


class EmbeddingModel:
    """
    Singleton wrapper around the embedding model.

    The model is loaded only once during the
    lifetime of JARVIS.
    """

    _model = None

    ##########################################################

    @classmethod
    def model(cls):
        """
        Returns the singleton embedding model.
        """

        if cls._model is None:

            print("[Embedding] Loading embedding model...")

            cls._model = SentenceTransformer(
                "BAAI/bge-small-en-v1.5"
            )

            print("[Embedding] Embedding model loaded.")

        return cls._model

    ##########################################################

    @classmethod
    def encode(cls, text: str):
        """
        Encode a single text.
        """

        return cls.model().encode(
            text,
            normalize_embeddings=True
        )

    ##########################################################

    @classmethod
    def encode_many(cls, texts: list[str]):
        """
        Encode multiple texts.
        """

        if not texts:
            return []

        return cls.model().encode(
            texts,
            normalize_embeddings=True
        )

    ##########################################################

    @classmethod
    def embed_chunk(cls, chunk: Chunk):
        """
        Embed one Chunk object.
        """

        if chunk.embedding is None:

            chunk.embedding = cls.encode(
                chunk.text
            )

        return chunk

    ##########################################################

    @classmethod
    def embed_chunks(cls, chunks: list[Chunk]):
        """
        Embed a list of Chunk objects.

        Only chunks without an embedding are encoded.
        """

        if not chunks:
            return chunks

        pending = [
            chunk
            for chunk in chunks
            if chunk.embedding is None
        ]

        if not pending:
            return chunks

        vectors = cls.encode_many(
            [chunk.text for chunk in pending]
        )

        for chunk, vector in zip(
            pending,
            vectors
        ):
            chunk.embedding = vector

        return chunks

    ##########################################################

    @classmethod
    def clear(cls):
        """
        Unload the embedding model.

        Mainly useful for testing.
        """

        cls._model = None