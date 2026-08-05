from pathlib import Path

from ai.actions.click_template_action import ClickTemplateAction


def main():

    assets = Path(__file__).parent / "assets"

    action = ClickTemplateAction()

    print()

    print("The mouse will click the ChatGPT template.")

    input("Press Enter when ready...")

    print()

    result = action.execute(

        template=assets / "chatgpt_logo.png",

        image_path=assets / "screenshot.png",

    )

    print(result.message)


if __name__ == "__main__":

    main()