import time
import requests

from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


class PageDownloader:
    """
    Production-grade web page downloader.

    Features
    --------
    • Shared HTTP Session
    • Connection Pooling
    • Automatic Retries
    • Exponential Backoff
    • Browser-like Headers
    • Timeout Handling
    """

    ##########################################################

    MAX_RETRIES = 3

    BACKOFF_FACTOR = 1.0

    POOL_CONNECTIONS = 20

    POOL_MAXSIZE = 20

    ##########################################################

    _session = None

    ##########################################################

    def __init__(self, timeout: int = 15):

        self.timeout = timeout

    ##########################################################

    @classmethod
    def session(cls):
        """
        Returns the singleton HTTP session.
        """

        if cls._session is None:

            print("[Downloader] Creating HTTP session...")

            session = requests.Session()

            retry = Retry(

                total=cls.MAX_RETRIES,

                connect=cls.MAX_RETRIES,

                read=cls.MAX_RETRIES,

                backoff_factor=cls.BACKOFF_FACTOR,

                status_forcelist=[

                    429,
                    500,
                    502,
                    503,
                    504

                ],

                allowed_methods=[

                    "GET",
                    "HEAD"

                ]

            )

            adapter = HTTPAdapter(

                max_retries=retry,

                pool_connections=cls.POOL_CONNECTIONS,

                pool_maxsize=cls.POOL_MAXSIZE

            )

            session.mount(

                "http://",

                adapter

            )

            session.mount(

                "https://",

                adapter

            )

            session.headers.update(

                {

                    "User-Agent":
                        (
                            "Mozilla/5.0 "
                            "(Windows NT 10.0; Win64; x64) "
                            "AppleWebKit/537.36 "
                            "(KHTML, like Gecko) "
                            "Chrome/138.0 Safari/537.36"
                        ),

                    "Accept":
                        (
                            "text/html,"
                            "application/xhtml+xml,"
                            "application/xml;q=0.9,"
                            "*/*;q=0.8"
                        ),

                    "Accept-Language":
                        "en-US,en;q=0.9",

                    "Connection":
                        "keep-alive",

                    "Cache-Control":
                        "no-cache",

                }

            )

            cls._session = session

        return cls._session

    ##########################################################

    def download(self, url: str) -> str:

        try:

            response = self.session().get(

                url,

                timeout=self.timeout,

                allow_redirects=True

            )

            ##################################################

            if response.status_code in (401, 403):

                print(

                    f"[Downloader] Access denied ({response.status_code})"

                    f" -> {url}"

                )

                return ""

            ##################################################

            if response.status_code == 404:

                print(

                    f"[Downloader] Page not found -> {url}"

                )

                return ""

            ##################################################

            response.raise_for_status()

            ##################################################

            return response.text

        except requests.Timeout:

            print(

                f"[Downloader] Timeout -> {url}"

            )

            return ""

        except requests.ConnectionError:

            print(

                f"[Downloader] Connection error -> {url}"

            )

            return ""

        except requests.RequestException as e:

            print(

                f"[Downloader] Request failed -> {url}"

            )

            print(e)

            return ""

    ##########################################################

    @classmethod
    def close(cls):
        """
        Close the shared session.
        """

        if cls._session is not None:

            cls._session.close()

            cls._session = None