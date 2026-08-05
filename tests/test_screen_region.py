from ai.geometry.screen_region import ScreenRegion
from ai.desktop.screenshot import Screenshot


def main():

    screenshot = Screenshot()

    region = ScreenRegion(

        left=0,

        top=0,

        width=600,

        height=200,

    )

    path = screenshot.capture_region(region)

    print()

    print("Saved to:")

    print(path)


if __name__ == "__main__":

    main()