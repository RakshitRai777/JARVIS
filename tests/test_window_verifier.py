import subprocess
import time

from ai.verification.verification_manager import VerificationManager
from ai.verification.verification_rule import VerificationRule


def main():

    ############################################################
    # Launch Notepad
    ############################################################

    subprocess.Popen("notepad.exe")

    time.sleep(2)

    ############################################################

    manager = VerificationManager()

    rule = VerificationRule(

        rule_type="window_exists",

        expected="Notepad",

    )

    ############################################################

    result = manager.verify(

        rule,

    )

    ############################################################

    print()

    print(result)

    print()

    print("Success :", result.success)

    print("Confidence :", result.confidence)


if __name__ == "__main__":

    main()