from ai.geometry.screen_region import ScreenRegion

from ai.verification.ocr_verifier import OCRVerifier
from ai.verification.verification_rule import VerificationRule


def main():

    verifier = OCRVerifier()

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

    result = verifier.verify(

        rule

    )

    print()

    print("Success    :", result.success)

    print("Confidence :", result.confidence)

    print("Message    :", result.message)

    print("Error      :", result.error)


if __name__ == "__main__":

    main()