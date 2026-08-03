from ai.web.scraper.html_parser import HTMLParser


def test_parser_creation():

    parser = HTMLParser()

    assert parser is not None


def test_parse_html():

    parser = HTMLParser()

    html = """
    <html>

    <body>

        <h1>Hello</h1>

        <p>This is a test.</p>

    </body>

    </html>
    """

    text = parser.parse(html)

    assert "Hello" in text

    assert "This is a test." in text