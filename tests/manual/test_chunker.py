from ai.web.scraper.page_downloader import PageDownloader
from ai.web.scraper.html_parser import HTMLParser
from ai.web.scraper.content_cleaner import ContentCleaner
from ai.web.scraper.chunker import Chunker


def run():

    downloader = PageDownloader()

    parser = HTMLParser()

    cleaner = ContentCleaner()

    chunker = Chunker()

    url = "https://en.wikipedia.org/wiki/Python_(programming_language)"

    print("=" * 60)
    print("CHUNKER TEST")
    print("=" * 60)

    html = downloader.download(url)

    parsed = parser.parse(html)

    cleaned = cleaner.clean(parsed)

    chunks = chunker.chunk(cleaned)

    print()

    print(f"Characters : {len(cleaned):,}")

    print(f"Chunks     : {len(chunks)}")

    print()

    for i, chunk in enumerate(chunks[:3], start=1):

        print("=" * 60)

        print(f"CHUNK {i}")

        print("=" * 60)

        print(chunk[:800])

        print()

    print("=" * 60)


if __name__ == "__main__":

    run()