from ai.desktop.window_manager import WindowManager


def main():

    manager = WindowManager()

    print()

    print("All Visible Windows")

    print("-" * 60)

    windows = manager.list()

    for window in windows:

        print(window.title)

    print()

    print("Find Brave")

    print(

        manager.find("Brave")

    )

    print()

    print("Exists VS Code")

    print(

        manager.exists("Visual Studio Code")

    )

    print()

    print("Active Window")

    print(

        manager.active()

    )


if __name__ == "__main__":

    main()