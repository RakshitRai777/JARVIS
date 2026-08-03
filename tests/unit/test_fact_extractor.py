from ai.memory.extraction.fact_extractor import FactExtractor


def test_extract_fact():

    extractor = FactExtractor()

    fact = extractor.extract(
        "My favourite colour is blue"
    )

    assert fact is not None

    assert "blue" in fact.content.lower()


def test_ignore_normal_sentence():

    extractor = FactExtractor()

    fact = extractor.extract(
        "How is the weather today?"
    )

    assert fact is None