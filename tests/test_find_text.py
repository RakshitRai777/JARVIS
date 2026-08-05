from ai.tools.vision.vision_manager import VisionManager


def main():

    vision = VisionManager()

    print()

    print("Finding ChatGPT...")

    print()

    element = vision.find_text(

        "ChatGPT"

    )

    if element:

        print(element)

    else:

        print("Not Found")


if __name__ == "__main__":

    main()