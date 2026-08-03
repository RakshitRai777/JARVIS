from ai.web.scraper.page_downloader import PageDownloader
from ai.web.scraper.html_parser import HTMLParser
from ai.web.scraper.content_cleaner import ContentCleaner


def run():

    downloader = PageDownloader()

    parser = HTMLParser()

    cleaner = ContentCleaner()

    url = "https://en.wikipedia.org/wiki/Python_(programming_language)"

    print("=" * 60)
    print("CONTENT CLEANER TEST")
    print("=" * 60)

    html = downloader.download(url)

    parsed = parser.parse(html)

    cleaned = cleaner.clean(parsed)

    print()

    print("Parsed Length :", len(parsed))

    print("Clean Length  :", len(cleaned))

    print()

    print("=" * 60)

    print(cleaned[:3000])

    print()

    print("=" * 60)


if __name__ == "__main__":

    run()