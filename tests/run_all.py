import subprocess
import sys


TESTS = [

    "tests.test_goal_parser",
    "tests.test_planning_engine",
    "tests.test_reasoning_engine",
    "tests.test_runtime_state",
    "tests.test_runtime_plan_executor",

]


def run_test(module: str):

    print()

    print("=" * 60)

    print(module)

    print("=" * 60)

    result = subprocess.run(

        [

            sys.executable,

            "-m",

            module,

        ]

    )

    return result.returncode == 0


def main():

    passed = 0

    failed = 0

    print()

    print("=" * 60)

    print("J.A.R.V.I.S. REGRESSION SUITE")

    print("=" * 60)

    for module in TESTS:

        if run_test(module):

            passed += 1

        else:

            failed += 1

    print()

    print("=" * 60)

    print("SUMMARY")

    print("=" * 60)

    print(f"Passed : {passed}")

    print(f"Failed : {failed}")


if __name__ == "__main__":

    main()