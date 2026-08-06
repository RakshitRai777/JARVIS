from ai.runtime.runtime_state import RuntimeState


def main():

    state = RuntimeState()

    state.current_application = "Notepad"
    state.current_window = "Untitled - Notepad"
    state.last_action = "OpenAppTool"

    print("Current App :", state.current_application)
    print("Current Window :", state.current_window)
    print("Last Action :", state.last_action)

    state.clear()

    print("\nAfter Clear")
    print(state)


if __name__ == "__main__":
    main()