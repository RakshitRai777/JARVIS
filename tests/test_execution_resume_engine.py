from ai.execution.execution_checkpoint import ExecutionCheckpoint
from ai.execution.execution_resume_engine import ExecutionResumeEngine


def main():

    engine = ExecutionResumeEngine()

    ############################################################
    # Initial State
    ############################################################

    print("=" * 60)
    print("INITIAL STATE")
    print("=" * 60)

    print("Has Checkpoint :", engine.has_checkpoint())
    print("Checkpoint     :", engine.get_checkpoint())

    ############################################################
    # Save First Checkpoint
    ############################################################

    checkpoint = ExecutionCheckpoint(

        workflow="Browser Workflow",

        current_step=2,

        total_steps=5,

    )

    engine.save_checkpoint(

        checkpoint,

    )

    print()
    print("=" * 60)
    print("AFTER SAVE")
    print("=" * 60)

    print("Has Checkpoint :", engine.has_checkpoint())

    saved = engine.get_checkpoint()

    print("Workflow       :", saved.workflow)
    print("Current Step   :", saved.current_step)
    print("Total Steps    :", saved.total_steps)

    ############################################################
    # Replace Checkpoint
    ############################################################

    checkpoint = ExecutionCheckpoint(

        workflow="Login Workflow",

        current_step=4,

        total_steps=8,

    )

    engine.save_checkpoint(

        checkpoint,

    )

    print()
    print("=" * 60)
    print("AFTER REPLACE")
    print("=" * 60)

    saved = engine.get_checkpoint()

    print("Workflow       :", saved.workflow)
    print("Current Step   :", saved.current_step)
    print("Total Steps    :", saved.total_steps)

    ############################################################
    # Clear Checkpoint
    ############################################################

    engine.clear_checkpoint()

    print()
    print("=" * 60)
    print("AFTER CLEAR")
    print("=" * 60)

    print("Has Checkpoint :", engine.has_checkpoint())
    print("Checkpoint     :", engine.get_checkpoint())


if __name__ == "__main__":

    main()