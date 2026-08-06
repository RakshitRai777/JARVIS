from ai.planner.condition import Condition
from ai.planner.condition_evaluator import ConditionEvaluator
from ai.runtime.runtime_variables import RuntimeVariables


def main():

    variables = RuntimeVariables()

    ############################################################

    variables.set(

        "browser",

        "Chrome",

    )

    variables.set(

        "window",

        "Notepad",

    )

    ############################################################

    evaluator = ConditionEvaluator(

        variables,

    )

    ############################################################
    # Test 1
    ############################################################

    print("=" * 60)
    print("TEST 1")
    print("=" * 60)

    condition = Condition(

        left="browser",

        operator="==",

        right="Chrome",

    )

    print(

        evaluator.evaluate(

            condition,

        )

    )

    ############################################################
    # Test 2
    ############################################################

    print()
    print("=" * 60)
    print("TEST 2")
    print("=" * 60)

    condition = Condition(

        left="browser",

        operator="!=",

        right="Edge",

    )

    print(

        evaluator.evaluate(

            condition,

        )

    )

    ############################################################
    # Test 3
    ############################################################

    print()
    print("=" * 60)
    print("TEST 3")
    print("=" * 60)

    condition = Condition(

        left="window",

        operator="==",

        right="Chrome",

    )

    print(

        evaluator.evaluate(

            condition,

        )

    )

    ############################################################
    # Test 4
    ############################################################

    print()
    print("=" * 60)
    print("TEST 4")
    print("=" * 60)

    condition = Condition(

        left="window",

        operator="!=",

        right="Chrome",

    )

    print(

        evaluator.evaluate(

            condition,

        )

    )

    ############################################################
    # Test 5
    ############################################################

    print()
    print("=" * 60)
    print("TEST 5")
    print("=" * 60)

    try:

        condition = Condition(

            left="browser",

            operator="contains",

            right="Chrome",

        )

        evaluator.evaluate(

            condition,

        )

    except Exception as ex:

        print(type(ex).__name__)

        print(ex)


if __name__ == "__main__":

    main()