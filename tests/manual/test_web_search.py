from ai.web.providers.duckduckgo_provider import DuckDuckGoProvider


def run():

    provider = DuckDuckGoProvider()

    print("=" * 60)
    print("WEB SEARCH TEST")
    print("=" * 60)

    questions = [

        "Who is the Chief Minister of Uttarakhand?",

        "Latest AI News",

        "Python programming"

    ]

    for question in questions:

        print()

        print("QUESTION :", question)

        results = provider.search(question)

        if not results:

            print("No results.")
            continue

        if not results[0].success:

            print(results[0].error)
            continue

        print()

        for i, result in enumerate(results, start=1):

            print(f"{i}. {result.title}")

            print(result.snippet)

            print(result.url)

            print()

        print("-" * 60)


if __name__ == "__main__":
    run()