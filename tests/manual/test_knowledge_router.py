from ai.knowledge.knowledge_router import KnowledgeRouter


def run():

    router = KnowledgeRouter()

    questions = [
        "What is my favourite colour?",
        "Who is the Chief Minister of Uttarakhand?",
        "What's the weather today?",
        "Tell me a joke.",
        "Explain recursion."
    ]

    print("=" * 60)
    print("KNOWLEDGE ROUTER TEST")
    print("=" * 60)

    for question in questions:

        result = router.route(question)

        print()
        print(f"QUESTION : {question}")
        print(f"SOURCE   : {result.source.value}")
        print(f"REASON   : {result.reason}")


if __name__ == "__main__":
    run()