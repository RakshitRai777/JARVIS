from ai.web.pipeline.web_pipeline import WebPipeline


def main():

    pipeline = WebPipeline()

    chunks = pipeline.retrieve(

        "Who created Python?"

    )

    print("=" * 70)

    print("WEB PIPELINE TEST")

    print("=" * 70)

    print()

    print("Chunks Returned :", len(chunks))

    print()

    for i, chunk in enumerate(chunks, start=1):

        print("=" * 70)

        print(f"CHUNK {i}")

        print("=" * 70)

        print("TITLE :", chunk.title)

        print("SOURCE:", chunk.source)

        print("SCORE :", round(chunk.score, 3))

        print()

        print(chunk.text[:800])

        print()


if __name__ == "__main__":

    main()