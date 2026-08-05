from ai.geometry.screen_region import ScreenRegion

from ai.tools.vision.vision_manager import VisionManager


def main():

    vision = VisionManager()

    region = ScreenRegion(

        left=0,

        top=0,

        width=600,

        height=200,

    )

    print()

    print("Reading region...")

    print()

    result = vision.read_region(

        region

    )

    print()

    print(result.success)

    print()

    print(result.cleaned_text)


if __name__ == "__main__":

    main()