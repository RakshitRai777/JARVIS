from ai.execution.execution_checkpoint import ExecutionCheckpoint
import time

def main():

    ############################################################
    # First Checkpoint
    ############################################################

    print("=" * 60)
    print("CHECKPOINT 1")
    print("=" * 60)

    checkpoint = ExecutionCheckpoint(

        workflow="Browser Workflow",

        current_step=2,

        total_steps=5,

    )

    print("Workflow     :", checkpoint.workflow)
    print("Current Step :", checkpoint.current_step)
    print("Total Steps  :", checkpoint.total_steps)
    print("Timestamp    :", checkpoint.timestamp)
    time.sleep(0.05)

    ############################################################
    # Second Checkpoint
    ############################################################

    print()
    print("=" * 60)
    print("CHECKPOINT 2")
    print("=" * 60)

    checkpoint = ExecutionCheckpoint(

        workflow="Login Workflow",

        current_step=4,

        total_steps=8,

    )

    print("Workflow     :", checkpoint.workflow)
    print("Current Step :", checkpoint.current_step)
    print("Total Steps  :", checkpoint.total_steps)
    print("Timestamp    :", checkpoint.timestamp)
    time.sleep(0.05)

    ############################################################
    # Final Step
    ############################################################

    print()
    print("=" * 60)
    print("FINAL STEP")
    print("=" * 60)

    checkpoint = ExecutionCheckpoint(

        workflow="Installation",

        current_step=10,

        total_steps=10,

    )

    print("Workflow     :", checkpoint.workflow)
    print("Current Step :", checkpoint.current_step)
    print("Total Steps  :", checkpoint.total_steps)
    print("Completed    :", checkpoint.current_step == checkpoint.total_steps)
    print("Timestamp    :", checkpoint.timestamp)


if __name__ == "__main__":

    main()