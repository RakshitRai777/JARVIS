import webbrowser
from urllib.parse import quote_plus


class BrowserManager:
    """
    Handles browser-related operations.

    Responsibilities
    ----------------
    • Open URLs
    • Perform Google searches
    • Perform YouTube searches

    Future
    ------
    • Open GitHub
    • Open Stack Overflow
    • Open Documentation
    """

    ############################################################

    def open_url(
        self,
        url: str,
    ) -> bool:

        try:

            webbrowser.open(url)

            return True

        except Exception as e:

            print()

            print("[BrowserManager]")

            print(e)

            print()

            return False

    ############################################################

    def google_search(
        self,
        query: str,
    ) -> bool:

        url = (

            "https://www.google.com/search?q="

            + quote_plus(query)

        )

        return self.open_url(url)

    ############################################################

    def youtube_search(
        self,
        query: str,
    ) -> bool:

        url = (

            "https://www.youtube.com/results?search_query="

            + quote_plus(query)

        )

        return self.open_url(url)