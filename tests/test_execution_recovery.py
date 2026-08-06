from ai.execution.execution_engine import ExecutionEngine
from ai.execution.execution_context import ExecutionContext
from ai.execution.execution_policy import ExecutionPolicy
from ai.planner.execution_step import ExecutionStep
from ai.execution.execution_result import ExecutionResult
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

            success=False,

            message="Fake execution failure.",

            error="Simulated failure.",

        )


############################################################

def main():

    engine = ExecutionEngine()

    ########################################################
    # Replace real ActionManager
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

        workflow="Recovery Workflow",

        step=step,

        runtime=runtime,

        policy=ExecutionPolicy(),

    )

    ########################################################

    result = engine.execute(

        context,

    )

    ########################################################

    print("=" * 60)

    print("EXECUTION RESULT")

    print("=" * 60)

    print(result)

    ########################################################

    print()

    print("=" * 60)

    print("RECOVERY RESULT")

    print("=" * 60)

    print(result.data)


if __name__ == "__main__":

    main()