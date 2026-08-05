import pygetwindow as gw

from ai.desktop.window import Window


def main():

    windows = []

    for w in gw.getAllWindows():

        if w.title.strip():

            windows.append(w)

    if not windows:

        print("No visible windows found.")

        return

    print()

    print("Available Windows")

    print("-" * 50)

    for i, w in enumerate(windows):

        print(f"{i}: {w.title}")

    print()

    choice = int(input("Select index: "))

    window = Window(

        windows[choice]

    )

    print()

    print(window)

    print()

    print("Title :", window.title)

    print("Rect  :", window.rect)


if __name__ == "__main__":

    main()