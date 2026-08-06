from ai.execution.execution_engine import ExecutionEngine
from ai.execution.execution_context import ExecutionContext
from ai.execution.execution_policy import ExecutionPolicy
from ai.execution.execution_result import ExecutionResult

from ai.planner.execution_step import ExecutionStep

from ai.runtime.runtime import Runtime


############################################################
# Fake Action Manager
############################################################

class FakeActionManager:

    def execute(
        self,
        context,
    ):

        return ExecutionResult(

            success=True,

            message="Fake execution succeeded.",

            data="Success",

        )


############################################################

def main():

    engine = ExecutionEngine()

    ########################################################
    # Replace ActionManager
    ########################################################

    engine.action_manager = FakeActionManager()

    ########################################################

    runtime = Runtime()

    ########################################################

    step = ExecutionStep(

        action="tool",

        parameters={

            "command": "Open Chrome",

        },

        description="Open Chrome",

    )

    ########################################################

    context = ExecutionContext(

        workflow="Checkpoint Workflow",

        step=step,

        runtime=runtime,

        policy=ExecutionPolicy(),

        shared_data={

            "total_steps": 5,

        },

        attempt=1,

    )

    ########################################################

    result = engine.execute(

        context,

    )

    ########################################################

    checkpoint = engine.resume_engine.get_checkpoint()

    ########################################################

    print("=" * 60)
    print("EXECUTION RESULT")
    print("=" * 60)

    print(result)

    ########################################################

    print()
    print("=" * 60)
    print("CHECKPOINT")
    print("=" * 60)

    print("Exists       :", checkpoint is not None)

    if checkpoint:

        print("Workflow     :", checkpoint.workflow)
        print("Current Step :", checkpoint.current_step)
        print("Total Steps  :", checkpoint.total_steps)
        print("CheckpointID :", checkpoint.checkpoint_id)
        print("Timestamp    :", checkpoint.timestamp)


if __name__ == "__main__":

    main()