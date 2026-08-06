from ai.execution.execution_context import ExecutionContext
from ai.execution.execution_engine import ExecutionEngine
from ai.execution.execution_policy import ExecutionPolicy

from ai.planner.condition import Condition
from ai.planner.execution_step import ExecutionStep

from ai.runtime.runtime import Runtime

from ai.workflow.workflow import Workflow


def execute_step(condition):

    runtime = Runtime()

    runtime.runtime_variables.set(

        "browser",

        "Chrome",

    )

    ############################################################

    workflow = Workflow(

        name="Conditional Execution Test",

    )

    ############################################################

    step = ExecutionStep(

        action="tool",

        parameters={

            "command": "type Hello",

        },

        description="Conditional typing",

        condition=condition,

    )

    ############################################################

    context = ExecutionContext(

        workflow=workflow,

        step=step,

        policy=ExecutionPolicy(),

        runtime=runtime,

        metadata={},

    )

    ############################################################

    engine = ExecutionEngine()

    return engine.execute(

        context,

    )


def main():

    ############################################################
    # TRUE
    ############################################################

    print("=" * 60)
    print("TRUE CONDITION")
    print("=" * 60)

    result = execute_step(

        Condition(

            left="browser",

            operator="==",

            right="Chrome",

        )

    )

    print(result)

    ############################################################
    # FALSE
    ############################################################

    print()
    print("=" * 60)
    print("FALSE CONDITION")
    print("=" * 60)

    result = execute_step(

        Condition(

            left="browser",

            operator="==",

            right="Edge",

        )

    )

    print(result)


if __name__ == "__main__":

    main()