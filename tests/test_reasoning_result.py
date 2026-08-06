from ai.agent.reasoning_result import ReasoningResult


def main():

    print("=" * 60)
    print("DEFAULT")
    print("=" * 60)

    result = ReasoningResult()

    print(result)

    print()

    print("=" * 60)
    print("CUSTOM")
    print("=" * 60)

    result = ReasoningResult(

        success=True,

        thought="User wants to continue FitOS.",

        conclusion="Resume previous project.",

        confidence=0.94,

    )

    print(result)


if __name__ == "__main__":

    main()