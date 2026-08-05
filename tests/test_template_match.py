from ai.geometry.screen_region import ScreenRegion
from ai.tools.vision.template.template_match import TemplateMatch


def main():

    match = TemplateMatch(

        region=ScreenRegion(

            left=100,

            top=200,

            width=40,

            height=30,

        ),

        confidence=0.973,

    )

    print()

    print(match)

    print()

    print("Center :", match.center)

    print("Left   :", match.left)

    print("Top    :", match.top)

    print("Width  :", match.width)

    print("Height :", match.height)


if __name__ == "__main__":

    main()