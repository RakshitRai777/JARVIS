from ai.execution.execution_state import ExecutionState


def main():

    print("=" * 60)
    print("EXECUTION STATES")
    print("=" * 60)

    for state in ExecutionState:

        print(state.name, "=", state.value)

    print()

    print("=" * 60)
    print("COMPARISON")
    print("=" * 60)

    print(

        ExecutionState.RUNNING == ExecutionState.RUNNING

    )

    print(

        ExecutionState.RUNNING == ExecutionState.PAUSED

    )


if __name__ == "__main__":

    main()