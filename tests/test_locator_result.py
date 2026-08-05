from ai.geometry.screen_region import ScreenRegion

from ai.locators.locator_result import LocatorResult


def main():

    result = LocatorResult(

        success=True,

        center=(500, 300),

        region=ScreenRegion(

            450,

            250,

            100,

            100,

        ),

        confidence=0.98,

        value="ChatGPT",

    )

    print()

    print(result)

    print()

    print(bool(result))


if __name__ == "__main__":

    main()