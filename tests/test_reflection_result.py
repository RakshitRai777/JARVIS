from ai.agent.reflection_result import ReflectionResult


def main():

    ########################################################

    print("=" * 60)
    print("DEFAULT")
    print("=" * 60)

    result = ReflectionResult()

    print(result)

    ########################################################

    print()
    print("=" * 60)
    print("CUSTOM")
    print("=" * 60)

    result = ReflectionResult(

        success=True,

        reflection="Execution completed successfully.",

        learning="Continue using this workflow.",

        should_store=True,

    )

    print(result)


if __name__ == "__main__":

    main()