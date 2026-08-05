from pathlib import Path

from ai.tools.vision.template.template_manager import TemplateManager


def main():

    assets = Path(__file__).parent / "assets"

    manager = TemplateManager()

    result = manager.find(

        image=assets / "screenshot.png",

        template=assets / "chatgpt_logo.png",

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