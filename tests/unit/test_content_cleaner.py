from ai.web.scraper.content_cleaner import ContentCleaner


def test_cleaner_creation():

    cleaner = ContentCleaner()

    assert cleaner is not None


def test_clean_text():

    cleaner = ContentCleaner()

    dirty = """
Python [1]

[edit]

| Table |

Hello World

[citation needed]
"""

    cleaned = cleaner.clean(dirty)

    assert "[1]" not in cleaned

    assert "[edit]" not in cleaned

    assert "|" not in cleaned

    assert "Hello World" in cleaned