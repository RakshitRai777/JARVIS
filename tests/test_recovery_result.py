from ai.execution.execution_result import ExecutionResult
from ai.execution.recovery_result import RecoveryResult


def main():

    ############################################################
    # Default Recovery
    ############################################################

    print("=" * 60)
    print("DEFAULT RECOVERY")
    print("=" * 60)

    recovery = RecoveryResult(

        recovered=False,

    )

    print("Recovered :", recovery.recovered)
    print("Workflow  :", recovery.workflow)
    print("Step      :", recovery.step)
    print("Error     :", recovery.error)
    print("Timestamp :", recovery.timestamp)

    ############################################################
    # Recovery With Execution Result
    ############################################################

    print()
    print("=" * 60)
    print("CUSTOM RECOVERY")
    print("=" * 60)

    execution = ExecutionResult(

        success=False,

        message="Open Chrome failed.",

        error="Application not found.",

    )

    recovery = RecoveryResult(

        recovered=False,

        workflow="Browser Workflow",

        step="Open Chrome",

        error="Application not found.",

        execution_result=execution,

    )

    print("Recovered :", recovery.recovered)
    print("Workflow  :", recovery.workflow)
    print("Step      :", recovery.step)
    print("Error     :", recovery.error)
    print("Execution :", recovery.execution_result)
    print("Timestamp :", recovery.timestamp)

    ############################################################
    # Successful Recovery
    ############################################################

    print()
    print("=" * 60)
    print("SUCCESSFUL RECOVERY")
    print("=" * 60)

    recovery = RecoveryResult(

        recovered=True,

        workflow="Browser Workflow",

        step="Open Chrome",

    )

    print("Recovered :", recovery.recovered)
    print("Workflow  :", recovery.workflow)
    print("Step      :", recovery.step)
    print("Timestamp :", recovery.timestamp)


if __name__ == "__main__":

    main()