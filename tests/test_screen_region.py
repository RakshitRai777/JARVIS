from ai.geometry.screen_region import ScreenRegion
from ai.tools.desktop.desktop_manager import DesktopManager


def main():

    desktop = DesktopManager()

    region = ScreenRegion(

        left=0,

        top=0,

        width=600,

        height=200,

    )

    path = desktop.take_region_screenshot(

        region

    )

    print()

    print("Saved to:")

    print(path)


if __name__ == "__main__":

    main()