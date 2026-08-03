from ai.web.web_result import WebResult


def run():

    result = WebResult(
        success=True,
        title="Python",
        url="https://python.org",
        snippet="Official Python website",
        source="DuckDuckGo"
    )

    print("=" * 60)
    print("WEB RESULT TEST")
    print("=" * 60)

    print(result)


if __name__ == "__main__":
    run()