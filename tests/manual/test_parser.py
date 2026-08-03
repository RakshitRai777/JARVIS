from ai.web.scraper.page_downloader import PageDownloader
from ai.web.scraper.html_parser import HTMLParser


def run():

    downloader = PageDownloader()

    parser = HTMLParser()

    url = "https://en.wikipedia.org/wiki/Python_(programming_language)"

    print("=" * 60)
    print("HTML PARSER TEST")
    print("=" * 60)

    print()

    print("Downloading page...")

    html = downloader.download(url)

    print(f"Downloaded {len(html):,} characters")

    print()

    print("Extracting content...")

    text = parser.parse(html)

    print(f"Extracted {len(text):,} characters")

    print()

    print("=" * 60)

    print(text[:3000])

    print()

    print("=" * 60)


if __name__ == "__main__":

    run()