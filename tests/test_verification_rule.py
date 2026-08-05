from ai.geometry.screen_region import ScreenRegion
from ai.verification.verification_rule import VerificationRule


def main():

    rule = VerificationRule(

        rule_type="text_exists",

        expected="ChatGPT",

        region=ScreenRegion(

            left=0,

            top=0,

            width=600,

            height=200,

        ),

    )

    print()

    print(rule)

    print()

    print(rule.region)


if __name__ == "__main__":

    main()