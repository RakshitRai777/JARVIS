from main import main

from tests.test_brain import run as brain_test


def run():

    print()

    print("Running JARVIS Smoke Tests...")

    print()

    # Initialize runtime
    main()

    # Run architecture tests
    brain_test()

    print()

    print("Smoke Tests Finished.")

    print()


if __name__ == "__main__":

    run()