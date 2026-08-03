from ai.web.scraper.chunker import Chunker
from ai.embeddings.chunk import Chunk


def test_chunker_creation():

    chunker = Chunker()

    assert chunker is not None


def test_small_text():

    chunker = Chunker()

    text = "Hello World"

    chunks = chunker.chunk(text)

    assert len(chunks) == 1

    assert isinstance(chunks[0], Chunk)

    assert chunks[0].text == "Hello World"

    assert chunks[0].embedding is None

    assert chunks[0].score == 0


def test_large_text():

    chunker = Chunker(
        chunk_size=100,
        overlap=20
    )

    text = "A" * 1000

    chunks = chunker.chunk(text)

    assert len(chunks) > 1

    for chunk in chunks:

        assert isinstance(chunk, Chunk)

        assert len(chunk.text) > 0