from ai.runtime.runtime import Runtime
from ai.workflow.workflow_step import WorkflowStep
from ai.execution.execution_result import ExecutionResult


def main():

    runtime = Runtime()

    ############################################################
    # Initial State
    ############################################################

    print("=" * 60)
    print("INITIAL HISTORY")
    print("=" * 60)

    print("History Size :", len(runtime.runtime_history))

    ############################################################
    # Simulate Workflow
    ############################################################

    runtime.set_workflow(

        "Test Workflow",

    )

    ############################################################

    step = WorkflowStep(

        action="tool",

        parameters={

            "command": "Open Notepad",

        },

        description="Open Notepad",

    )

    ############################################################

    result = ExecutionResult(

        success=True,

        message="Application opened.",

    )

    ############################################################

    runtime.update_from_execution(

        step,

        result,

    )

    ############################################################
    # Verify
    ############################################################

    print()
    print("=" * 60)
    print("AFTER EXECUTION")
    print("=" * 60)

    print("History Size :", len(runtime.runtime_history))

    entry = runtime.runtime_history.last()

    print()

    print("Workflow :", entry.workflow)

    print("Step :", entry.step)

    print("Action :", entry.action)

    print("Command :", entry.command)

    print("Success :", entry.result.success)

    ############################################################
    # Reset
    ############################################################

    runtime.reset()

    print()
    print("=" * 60)
    print("AFTER RESET")
    print("=" * 60)

    print(

        "History Size :",

        len(runtime.runtime_history),

    )


if __name__ == "__main__":

    main()