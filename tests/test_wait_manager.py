from ai.verification.verification_rule import VerificationRule

from ai.waiting.wait_condition import WaitCondition
from ai.waiting.wait_manager import WaitManager


def main():

    print()

    print("Make sure ChatGPT is visible.")

    input("Press Enter when ready...")

    print()

    manager = WaitManager()

    condition = WaitCondition(

        rule=VerificationRule(

            rule_type="text_exists",

            expected="ChatGPT",

        ),

        timeout=5,

        poll_interval=0.5,

    )

    result = manager.wait_until(

        condition

    )

    print()

    print(result)

    print()

    print(

        f"Elapsed: {result.elapsed_time:.2f}s"

    )


if __name__ == "__main__":

    main()