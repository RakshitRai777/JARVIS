from bs4 import BeautifulSoup
from bs4.element import Tag


class HtmlParser:
    """
    Intelligent HTML parser.

    Responsibilities
    ----------------
    • Extract the main article
    • Remove navigation
    • Remove sidebars
    • Remove ads
    • Preserve headings and paragraphs
    """

    def parse(
        self,
        html: str
    ) -> str:

        if not html:
            return ""

        soup = BeautifulSoup(html, "lxml")

        ########################################################
        # Find the main content FIRST
        ########################################################

        root = (
            soup.find("main")
            or soup.find("article")
            or soup.find(attrs={"role": "main"})
            or soup.find(id="mw-content-text")
            or soup.find(id="content")
            or soup.body
            or soup
        )

        if root is None:
            return ""

        ########################################################
        # Remove useless HTML tags
        ########################################################

        remove_tags = [

            "script",
            "style",
            "noscript",
            "svg",
            "nav",
            "header",
            "footer",
            "aside",
            "iframe",
            "form",
            "button",
            "input",
            "figure",
            "figcaption"

        ]

        for tag in root.find_all(remove_tags):

            tag.decompose()

        ########################################################
        # Remove useless containers
        ########################################################

        remove_keywords = {

            "sidebar",
            "navigation",
            "navbar",
            "breadcrumb",
            "cookie",
            "footer",
            "header",
            "advert",
            "ads",
            "promo",
            "recommend",
            "related",
            "infobox",
            "navbox",
            "toc",
            "catlinks",
            "mw-navigation",
            "vector-header",
            "vector-sidebar",
            "printfooter",
            "metadata"

        }

        for element in list(root.find_all(True)):

            if not isinstance(element, Tag):
                continue

            attrs = getattr(element, "attrs", None)

            if not isinstance(attrs, dict):
                continue

            element_id = attrs.get("id", "") or ""

            classes = attrs.get("class", [])

            if classes is None:
                classes = []

            if isinstance(classes, str):
                classes = [classes]

            attr_string = (
                str(element_id)
                + " "
                + " ".join(classes)
            ).lower()

            if any(keyword in attr_string for keyword in remove_keywords):

                element.decompose()

        ########################################################
        # Extract semantic text
        ########################################################

        blocks = []

        for tag in root.find_all(

            [

                "h1",
                "h2",
                "h3",
                "h4",
                "p",
                "li",
                "pre",
                "code"

            ]

        ):

            text = tag.get_text(
                " ",
                strip=True
            )

            if len(text) < 20:
                continue

            blocks.append(text)

        ########################################################
        # Fallback
        ########################################################

        if not blocks:

            text = root.get_text(
                separator="\n\n",
                strip=True
            )

            return text

        ########################################################

        return "\n\n".join(blocks)