from ai.tools.desktop.desktop_manager import DesktopManager


def main():

    desktop = DesktopManager()

    path = desktop.take_region_screenshot(

        left=0,
        top=0,
        width=600,
        height=200,

    )

    print()

    print("Saved to:")

    print(path)


if __name__ == "__main__":

    main()