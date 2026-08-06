from ai.execution.execution_cursor import ExecutionCursor
from ai.planner.execution_step import ExecutionStep


def make_step(name: str) -> ExecutionStep:

    return ExecutionStep(

        action="tool",

        parameters={

            "command": name,

        },

        description=name,

    )


def main():

    ############################################################
    # Build execution plan
    ############################################################

    steps = [

        make_step("Open Chrome"),

        make_step("Search Google"),

        make_step("Click First Result"),

        make_step("Type Hello"),

    ]

    ############################################################

    cursor = ExecutionCursor(

        steps,

    )

    ############################################################
    # Simulate PlanExecutor
    ############################################################

    print("=" * 60)
    print("PLAN EXECUTION")
    print("=" * 60)

    executed = 0

    while cursor.has_next():

        step = cursor.current()

        print(

            f"Step {cursor.index + 1}/{cursor.total_steps}"

        )

        print(

            "Action      :", step.action

        )

        print(

            "Description :", step.description

        )

        print("-" * 60)

        executed += 1

        cursor.next()

    ############################################################
    # Final Cursor State
    ############################################################

    print()
    print("=" * 60)
    print("FINAL CURSOR STATE")
    print("=" * 60)

    print("Executed     :", executed)
    print("Cursor Index :", cursor.index)
    print("Total Steps  :", cursor.total_steps)
    print("Has Next     :", cursor.has_next())
    print("Current Step :", cursor.current())


if __name__ == "__main__":

    main()