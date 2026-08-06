from ai.execution.execution_checkpoint import ExecutionCheckpoint
from ai.execution.execution_resume_engine import ExecutionResumeEngine


def main():

    engine = ExecutionResumeEngine()

    ############################################################
    # No Checkpoint
    ############################################################

    print("=" * 60)
    print("NO CHECKPOINT")
    print("=" * 60)

    result = engine.resume()

    print("Resumed       :", result.resumed)
    print("Checkpoint    :", result.checkpoint)
    print("Execution     :", result.execution_result)
    print("Completed     :", result.completed)

    ############################################################
    # Save Checkpoint
    ############################################################

    checkpoint = ExecutionCheckpoint(

        workflow="Browser Workflow",

        current_step=3,

        total_steps=5,

    )

    engine.save_checkpoint(

        checkpoint,

    )

    ############################################################
    # Resume
    ############################################################

    print()
    print("=" * 60)
    print("RESUME")
    print("=" * 60)

    result = engine.resume()

    print("Resumed       :", result.resumed)
    print("Workflow      :", result.checkpoint.workflow)
    print("Current Step  :", result.checkpoint.current_step)
    print("Total Steps   :", result.checkpoint.total_steps)
    print("Resume Step   :", result.resumed_step)
    print("Completed     :", result.completed)
    print("Execution     :", result.execution_result)

    ############################################################
    # Completed Workflow
    ############################################################

    checkpoint = ExecutionCheckpoint(

        workflow="Completed Workflow",

        current_step=5,

        total_steps=5,

    )

    engine.save_checkpoint(

        checkpoint,

    )

    print()
    print("=" * 60)
    print("ALREADY COMPLETED")
    print("=" * 60)

    result = engine.resume()

    print("Resumed       :", result.resumed)
    print("Workflow      :", result.checkpoint.workflow)
    print("Resume Step   :", result.resumed_step)
    print("Completed     :", result.completed)


if __name__ == "__main__":

    main()