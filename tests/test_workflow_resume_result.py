from ai.execution.execution_checkpoint import ExecutionCheckpoint
from ai.execution.execution_result import ExecutionResult
from ai.execution.workflow_resume_result import WorkflowResumeResult


def main():

    ############################################################
    # Default Resume Result
    ############################################################

    print("=" * 60)
    print("DEFAULT RESUME")
    print("=" * 60)

    result = WorkflowResumeResult(

        resumed=False,

    )

    print("Resumed        :", result.resumed)
    print("Checkpoint     :", result.checkpoint)
    print("Execution      :", result.execution_result)
    print("Resumed Step   :", result.resumed_step)
    print("Completed      :", result.completed)
    print("Timestamp      :", result.timestamp)

    ############################################################
    # Resume With Checkpoint
    ############################################################

    checkpoint = ExecutionCheckpoint(

        workflow="Browser Workflow",

        current_step=3,

        total_steps=5,

    )

    execution = ExecutionResult(

        success=True,

        message="Workflow resumed successfully.",

    )

    print()
    print("=" * 60)
    print("CUSTOM RESUME")
    print("=" * 60)

    result = WorkflowResumeResult(

        resumed=True,

        checkpoint=checkpoint,

        execution_result=execution,

        resumed_step=3,

        completed=False,

    )

    print("Resumed        :", result.resumed)
    print("Workflow       :", result.checkpoint.workflow)
    print("Current Step   :", result.checkpoint.current_step)
    print("Total Steps    :", result.checkpoint.total_steps)
    print("Execution      :", result.execution_result)
    print("Resumed Step   :", result.resumed_step)
    print("Completed      :", result.completed)
    print("Timestamp      :", result.timestamp)

    ############################################################
    # Completed Workflow
    ############################################################

    print()
    print("=" * 60)
    print("WORKFLOW COMPLETED")
    print("=" * 60)

    result = WorkflowResumeResult(

        resumed=True,

        checkpoint=checkpoint,

        execution_result=execution,

        resumed_step=5,

        completed=True,

    )

    print("Resumed        :", result.resumed)
    print("Completed      :", result.completed)
    print("Resumed Step   :", result.resumed_step)
    print("Timestamp      :", result.timestamp)


if __name__ == "__main__":

    main()