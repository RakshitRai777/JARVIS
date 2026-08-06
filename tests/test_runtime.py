from ai.runtime.runtime import Runtime


def main():

    runtime = Runtime()

    runtime.set_workflow(

        "Notepad Workflow"

    )

    runtime.set_application(

        "Notepad"

    )

    runtime.set_window(

        "Untitled - Notepad"

    )

    runtime.set_last_action(

        "OpenAppTool"

    )

    print(runtime.state)

    runtime.reset()

    print()

    print("After reset")

    print(runtime.state)


if __name__ == "__main__":

    main()