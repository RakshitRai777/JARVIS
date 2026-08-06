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
    # Build Execution Plan
    ############################################################

    steps = [

        make_step("Open Chrome"),

        make_step("Search Google"),

        make_step("Click First Result"),

    ]

    cursor = ExecutionCursor(steps)

    ############################################################
    # Initial State
    ############################################################

    print("=" * 60)
    print("INITIAL")
    print("=" * 60)

    print("Index       :", cursor.index)
    print("Total Steps :", cursor.total_steps)
    print("Has Next    :", cursor.has_next())
    print("Current     :", cursor.current().description)

    ############################################################
    # Next
    ############################################################

    cursor.next()

    print()
    print("=" * 60)
    print("AFTER NEXT")
    print("=" * 60)

    print("Index       :", cursor.index)
    print("Current     :", cursor.current().description)

    ############################################################
    # Previous
    ############################################################

    cursor.previous()

    print()
    print("=" * 60)
    print("AFTER PREVIOUS")
    print("=" * 60)

    print("Index       :", cursor.index)
    print("Current     :", cursor.current().description)

    ############################################################
    # Goto
    ############################################################

    cursor.goto(2)

    print()
    print("=" * 60)
    print("AFTER GOTO")
    print("=" * 60)

    print("Index       :", cursor.index)
    print("Current     :", cursor.current().description)

    ############################################################
    # Reset
    ############################################################

    cursor.reset()

    print()
    print("=" * 60)
    print("AFTER RESET")
    print("=" * 60)

    print("Index       :", cursor.index)
    print("Current     :", cursor.current().description)

    ############################################################
    # End of Plan
    ############################################################

    cursor.goto(cursor.total_steps)

    print()
    print("=" * 60)
    print("END OF PLAN")
    print("=" * 60)

    print("Index       :", cursor.index)
    print("Has Next    :", cursor.has_next())
    print("Current     :", cursor.current())

    ############################################################
    # Empty Plan
    ############################################################

    empty = ExecutionCursor([])

    print()
    print("=" * 60)
    print("EMPTY PLAN")
    print("=" * 60)

    print("Index       :", empty.index)
    print("Total Steps :", empty.total_steps)
    print("Has Next    :", empty.has_next())
    print("Current     :", empty.current())


if __name__ == "__main__":

    main()