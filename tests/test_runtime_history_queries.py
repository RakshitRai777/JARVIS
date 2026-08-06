from ai.runtime.runtime import Runtime
from ai.workflow.workflow_step import WorkflowStep
from ai.execution.execution_result import ExecutionResult


def print_title(title: str):
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


def main():

    runtime = Runtime()

    runtime.set_workflow("Workflow A")

    ############################################################
    # Success
    ############################################################

    runtime.update_from_execution(

        WorkflowStep(

            action="tool",

            parameters={

                "command": "Open Notepad",

            },

            description="Open Notepad",

        ),

        ExecutionResult(

            success=True,

            message="Opened",

        ),

    )

    ############################################################
    # Failure
    ############################################################

    runtime.update_from_execution(

        WorkflowStep(

            action="focus_window",

            parameters={

                "application": "Chrome",

            },

            description="Focus Chrome",

        ),

        ExecutionResult(

            success=False,

            message="Window not found",

        ),

    )

    ############################################################
    # Success
    ############################################################

    runtime.update_from_execution(

        WorkflowStep(

            action="tool",

            parameters={

                "command": "Type Hello",

            },

            description="Type Hello",

        ),

        ExecutionResult(

            success=True,

            message="Typed",

        ),

    )

    ############################################################

    history = runtime.runtime_history

    print_title("ALL")

    print("Total :", len(history))

    ############################################################

    print_title("SUCCESS")

    print(

        len(

            history.successful()

        )

    )

    ############################################################

    print_title("FAILED")

    print(

        len(

            history.failed()

        )

    )

    ############################################################

    print_title("LAST SUCCESS")

    print(

        history.last_success().step

    )

    ############################################################

    print_title("LAST FAILURE")

    print(

        history.last_failure().step

    )

    ############################################################

    print_title("BY ACTION")

    print(

        len(

            history.by_action(

                "tool"

            )

        )

    )

    ############################################################

    print_title("BY WORKFLOW")

    print(

        len(

            history.by_workflow(

                "Workflow A"

            )

        )

    )


if __name__ == "__main__":

    main()