from ai.embeddings.chunk import Chunk
from ai.embeddings.embedding_model import EmbeddingModel


def run():

    chunk = Chunk(
        text="Python was created by Guido van Rossum."
    )

    EmbeddingModel.embed_chunk(chunk)

    print("=" * 60)
    print("EMBEDDING MODEL TEST")
    print("=" * 60)

    print()

    print("Text:")
    print(chunk.text)

    print()

    print("Embedding created:")
    print(chunk.embedding is not None)

    print()

    print("Embedding dimension:")
    print(len(chunk.embedding))


if __name__ == "__main__":
    run()