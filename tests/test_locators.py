from pathlib import Path

from ai.locators.text_locator import TextLocator
from ai.locators.template_locator import TemplateLocator

from ai.tools.vision.vision_manager import VisionManager


def main():

    assets = Path(__file__).parent / "assets"

    vision = VisionManager()

    ########################################################

    text = TextLocator(

        "ChatGPT"

    )

    print()

    print("TEXT LOCATOR")

    result = text.locate(

        vision

    )

    print(result.success)

    ########################################################

    template = TemplateLocator(

        assets / "chatgpt_logo.png"

    )

    print()

    print("TEMPLATE LOCATOR")

    result = template.locate(

        vision

    )

    print(result.success)

    if result:

        print(result.value)


if __name__ == "__main__":

    main()