from ai.web.scraper.page_downloader import PageDownloader
from ai.web.scraper.html_parser import HTMLParser
from ai.web.scraper.content_cleaner import ContentCleaner
from ai.web.scraper.chunker import Chunker

from ai.embeddings.semantic_ranker import SemanticRanker


def run():

    downloader = PageDownloader()

    parser = HTMLParser()

    cleaner = ContentCleaner()

    chunker = Chunker()

    ranker = SemanticRanker()

    html = downloader.download(

        "https://en.wikipedia.org/wiki/Python_(programming_language)"

    )

    parsed = parser.parse(html)

    cleaned = cleaner.clean(parsed)

    chunks = chunker.chunk(cleaned)

    question = "Who created Python?"

    print("=" * 60)

    print(question)

    print("=" * 60)

    print()

    results = ranker.rank(

        question,

        chunks,

        top_results=3

    )

    for i, chunk in enumerate(results, 1):

        print(f"TOP {i}")

        print("-" * 40)

        print(chunk.text[:900])

        print()


if __name__ == "__main__":

    run()