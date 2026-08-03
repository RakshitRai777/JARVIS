from ai.web.scraper.page_downloader import PageDownloader


def test_downloader_creation():

    downloader = PageDownloader()

    assert downloader is not None


def test_download_python():

    downloader = PageDownloader()

    html = downloader.download(
        "https://www.python.org/"
    )

    assert html is not None

    assert "<html" in html.lower()