from ai.web.scraper.page_downloader import PageDownloader
from ai.web.scraper.html_parser import HTMLParser
from ai.web.scraper.content_cleaner import ContentCleaner
from ai.web.scraper.chunker import Chunker


def run():

    downloader = PageDownloader()

    parser = HTMLParser()

    cleaner = ContentCleaner()

    chunker = Chunker()

    print("=" * 60)
    print("SCRAPER PIPELINE TEST")
    print("=" * 60)

    html = downloader.download(
        "https://www.python.org"
    )

    parsed = parser.parse(html)

    cleaned = cleaner.clean(parsed)

    chunks = chunker.chunk(cleaned)

    print()

    print("HTML Length :", len(html))
    print("Parsed      :", len(parsed))
    print("Cleaned     :", len(cleaned))
    print("Chunks      :", len(chunks))

    print()

    print("=" * 60)
    print("FIRST CHUNK")
    print("=" * 60)

    print(chunks[0].text[:1000])


if __name__ == "__main__":
    run()