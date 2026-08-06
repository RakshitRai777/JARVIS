from ai.execution.execution_cursor import ExecutionCursor
from ai.execution.execution_engine import ExecutionEngine
from ai.execution.resume_context import ResumeContext
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
    # Create execution plan
    ############################################################

    steps = [

        make_step("Open Chrome"),

        make_step("Search Google"),

        make_step("Click First Result"),

    ]

    ############################################################

    cursor = ExecutionCursor(

        steps,

    )

    ############################################################

    engine = ExecutionEngine()

    ############################################################

    context = ResumeContext(

        cursor=cursor,

        execution_engine=engine,

    )

    ############################################################

    print("=" * 60)
    print("RESUME CONTEXT")
    print("=" * 60)

    print("Cursor Index :", context.cursor.index)

    print("Total Steps  :", context.cursor.total_steps)

    print("Has Next     :", context.cursor.has_next())

    print("Current Step :", context.cursor.current().description)

    print()

    print(

        "Execution Engine :",

        type(context.execution_engine).__name__,

    )


if __name__ == "__main__":

    main()