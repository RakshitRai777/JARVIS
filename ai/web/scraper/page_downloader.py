import requests


class PageDownloader:
    """
    Downloads the raw HTML of a webpage.
    """

    def __init__(
        self,
        timeout: int = 15
    ):

        self.timeout = timeout

        self.headers = {

            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 "
                "(KHTML, like Gecko) "
                "Chrome/137.0 Safari/537.36"
            )

        }

    ##########################################################

    def download(
        self,
        url: str
    ) -> str:

        response = requests.get(
            url,
            headers=self.headers,
            timeout=self.timeout
        )

        response.raise_for_status()

        return response.text