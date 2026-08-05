from ai.geometry.screen_region import ScreenRegion

from ai.tools.vision.template.template_match import TemplateMatch
from ai.tools.vision.template.template_result import TemplateResult


def main():

    match = TemplateMatch(

        region=ScreenRegion(

            left=100,

            top=200,

            width=40,

            height=30,

        ),

        confidence=0.982,

    )

    result = TemplateResult(

        success=True,

        best_match=match,

        matches=[match],

        execution_time=0.014,

    )

    print()

    print(result)

    print()

    print("Success     :", result.success)

    print("Confidence  :", result.confidence)

    print("Matches     :", result.match_count)

    print("Best Match  :", result.best_match)

    print("Time        :", result.execution_time)


if __name__ == "__main__":

    main()