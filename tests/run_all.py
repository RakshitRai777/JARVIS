import subprocess
import sys


TESTS = [

    ############################################################
    # Planner
    ############################################################

    "tests.test_goal_parser",
    "tests.test_planning_engine",
    "tests.test_reasoning_engine",

    ############################################################
    # Runtime
    ############################################################

    "tests.test_runtime_state",
    "tests.test_runtime_history",
    "tests.test_runtime_history_queries",
    "tests.test_runtime_session",
    "tests.test_runtime_variables",

    ############################################################
    # Variable Resolution
    ############################################################

    "tests.test_variable_resolver",
    "tests.test_variable_resolution_execution",

    ############################################################
    # Conditional Execution
    ############################################################

    "tests.test_condition_evaluator",
    "tests.test_conditional_execution",

    ############################################################
    # Integration
    ############################################################

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

    failed_tests = []

    print()

    print("=" * 60)

    print("J.A.R.V.I.S. REGRESSION SUITE")

    print("=" * 60)

    for module in TESTS:

        if run_test(module):

            passed += 1

        else:

            failed += 1

            failed_tests.append(module)

    print()

    print("=" * 60)

    print("SUMMARY")

    print("=" * 60)

    print(f"Passed : {passed}")

    print(f"Failed : {failed}")

    if failed_tests:

        print()

        print("Failed Tests")

        print("-" * 40)

        for module in failed_tests:

            print(module)

    else:

        print()

        print("All regression tests passed.")


if __name__ == "__main__":

    main()