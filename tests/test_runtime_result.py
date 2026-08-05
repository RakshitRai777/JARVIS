from ai.runtime.runtime_result import RuntimeResult


def main():

    result = RuntimeResult(

        success=True,

        message="Workflow completed.",

        completed_tasks=5,

        failed_tasks=0,

        execution_time=3.28,

    )

    print()

    print(result)

    print()

    print(bool(result))


if __name__ == "__main__":

    main()