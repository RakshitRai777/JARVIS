from ai.tools.vision.template.template_matcher import TemplateMatcher


def main():

    matcher = TemplateMatcher()

    result = matcher.find(

        image="tests/assets/screenshot.png",

        template="tests/assets/chatgpt_logo.png",

        threshold=0.75,

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