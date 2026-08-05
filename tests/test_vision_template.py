from pathlib import Path

from ai.tools.vision.vision_manager import VisionManager


def main():

    assets = Path(__file__).parent / "assets"

    vision = VisionManager()

    result = vision.find_template(

        template=assets / "chatgpt_logo.png",

        image_path=assets / "screenshot.png",

    )

    print()

    print(result)

    print()

    if result:

        print(result.best_match)

    else:

        print(result.error)


if __name__ == "__main__":

    main()