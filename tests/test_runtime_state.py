from ai.runtime.runtime_state import RuntimeState


def main():

    state = RuntimeState.RUNNING

    print()

    print(state)

    print()

    print(state.value)

    print()

    print(state == RuntimeState.RUNNING)

    print()

    print(list(RuntimeState))


if __name__ == "__main__":

    main()