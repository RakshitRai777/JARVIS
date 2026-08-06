from ai.execution.execution_context import ExecutionContext
from ai.execution.execution_engine import ExecutionEngine
from ai.execution.execution_policy import ExecutionPolicy

from ai.planner.execution_step import ExecutionStep
from ai.workflow.workflow import Workflow
from ai.runtime.runtime import Runtime


def main():

    ########################################################

    workflow = Workflow(

        name="Learning Workflow",

    )

    ########################################################

    step = ExecutionStep(

        action="tool",

        description="Open Chrome",

        parameters={

            "command": "Open Chrome",

        },

    )

    ########################################################

    context = ExecutionContext(

        workflow=workflow,

        step=step,

        policy=ExecutionPolicy(),

        runtime=Runtime(),

    )

    ########################################################

    engine = ExecutionEngine()

    ########################################################

    print("=" * 60)
    print("EXECUTION LEARNING PIPELINE")
    print("=" * 60)

    result = engine.execute(

        context,

    )

    ########################################################

    print()

    print("Execution Success")

    print(result.success)

    print()

    print("Execution Message")

    print(result.message)


if __name__ == "__main__":

    main()