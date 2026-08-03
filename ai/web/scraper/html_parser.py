from bs4 import BeautifulSoup


class HTMLParser:
    """
    Converts HTML into readable text.
    """

    ##########################################################

    def parse(
        self,
        html: str
    ) -> str:

        soup = BeautifulSoup(
            html,
            "lxml"
        )

        # Remove unwanted tags
        for tag in soup(

            [

                "script",
                "style",
                "noscript",
                "svg",
                "footer",
                "header",
                "nav",
                "form",
                "iframe"

            ]

        ):

            tag.decompose()

        text = soup.get_text(
            separator="\n"
        )

        return text