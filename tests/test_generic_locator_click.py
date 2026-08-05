from pathlib import Path

from ai.actions.click_action import ClickAction
from ai.locators.template_locator import TemplateLocator


def main():

    assets = Path(__file__).parent / "assets"

    action = ClickAction()

    locator = TemplateLocator(

        template=assets / "chatgpt_logo.png",

        image_path=assets / "screenshot.png",

    )

    print()

    print("Generic ClickAction Test")

    input("Press Enter when ready...")

    print()

    result = action.execute(

        locator

    )

    print(result)


if __name__ == "__main__":

    main()