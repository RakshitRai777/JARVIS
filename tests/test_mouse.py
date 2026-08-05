from ai.desktop.mouse import Mouse


def main():

    mouse = Mouse()

    print()

    print("Current Position")

    print(

        mouse.position()

    )

    print()

    input(

        "Press Enter to move the mouse..."

    )

    mouse.move(

        500,

        500,

    )

    print()

    print("Done.")


if __name__ == "__main__":

    main()