from ai.web.scraper.page_downloader import PageDownloader


def run():

    downloader = PageDownloader()

    urls = [

        "https://www.python.org",

        "https://en.wikipedia.org/wiki/Python_(programming_language)",

        "https://www.geeksforgeeks.org/python-programming-language-tutorial/"

    ]

    print("=" * 60)
    print("PAGE DOWNLOADER TEST")
    print("=" * 60)

    for url in urls:

        print()

        print(f"Downloading:\n{url}")

        html = downloader.download(url)

        if html is None:

            print("FAILED")

        else:

            print("SUCCESS")

            print(f"Downloaded {len(html):,} characters")


if __name__ == "__main__":

    run()