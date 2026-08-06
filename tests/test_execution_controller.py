from ai.execution.execution_controller import ExecutionController


def print_state(controller):

    print("State :", controller.state.name)


def main():

    controller = ExecutionController()

    print("=" * 60)
    print("INITIAL")
    print("=" * 60)

    print_state(controller)

    print()

    print("=" * 60)
    print("START")
    print("=" * 60)

    controller.start()

    print_state(controller)

    print()

    print("=" * 60)
    print("PAUSE")
    print("=" * 60)

    controller.pause()

    print_state(controller)

    print()

    print("=" * 60)
    print("RESUME")
    print("=" * 60)

    controller.resume()

    print_state(controller)

    print()

    print("=" * 60)
    print("COMPLETE")
    print("=" * 60)

    controller.complete()

    print_state(controller)

    print()

    print("=" * 60)
    print("RESET")
    print("=" * 60)

    controller.reset()

    print_state(controller)

    print()

    print("=" * 60)
    print("CANCEL")
    print("=" * 60)

    controller.cancel()

    print_state(controller)

    print()

    print("=" * 60)
    print("FAIL")
    print("=" * 60)

    controller.fail()

    print_state(controller)


if __name__ == "__main__":

    main()