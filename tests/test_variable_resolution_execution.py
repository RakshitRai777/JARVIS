from ai.execution.execution_context import ExecutionContext
from ai.execution.execution_engine import ExecutionEngine
from ai.execution.execution_policy import ExecutionPolicy

from ai.planner.execution_step import ExecutionStep
from ai.workflow.workflow import Workflow

from ai.runtime.runtime import Runtime


def main():

    runtime = Runtime()

    ############################################################

    runtime.runtime_variables.set(

        "name",

        "Rakshit",

    )

    ############################################################

    workflow = Workflow(

        name="Variable Resolution Test",

    )

    ############################################################

    step = ExecutionStep(

        action="tool",

        parameters={

            "command": "type ${name}",

        },

        description="Type runtime variable",

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

    result = engine.execute(

        context,

    )

    ############################################################

    print()

    print("=" * 60)

    print("EXECUTION RESULT")

    print("=" * 60)

    print(result)


if __name__ == "__main__":

    main()