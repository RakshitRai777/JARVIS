from ai.execution.execution_result import ExecutionResult
from ai.execution.recovery_engine import RecoveryEngine


def main():

    engine = RecoveryEngine()

    ############################################################
    # Failed Execution
    ############################################################

    print("=" * 60)
    print("FAILED EXECUTION")
    print("=" * 60)

    execution = ExecutionResult(

        success=False,

        message="Open Chrome failed.",

        error="Application not found.",

    )

    recovery = engine.recover(

        workflow="Browser Workflow",

        step="Open Chrome",

        execution_result=execution,

    )

    print("Recovered :", recovery.recovered)
    print("Workflow  :", recovery.workflow)
    print("Step      :", recovery.step)
    print("Error     :", recovery.error)
    print("Execution :", recovery.execution_result)

    ############################################################
    # Another Failure
    ############################################################

    print()
    print("=" * 60)
    print("SECOND FAILURE")
    print("=" * 60)

    execution = ExecutionResult(

        success=False,

        message="Click Button failed.",

        error="Button not found.",

    )

    recovery = engine.recover(

        workflow="Login Workflow",

        step="Click Login",

        execution_result=execution,

    )

    print("Recovered :", recovery.recovered)
    print("Workflow  :", recovery.workflow)
    print("Step      :", recovery.step)
    print("Error     :", recovery.error)
    print("Execution :", recovery.execution_result)

    ############################################################
    # Successful Execution
    ############################################################

    print()
    print("=" * 60)
    print("SUCCESSFUL EXECUTION")
    print("=" * 60)

    execution = ExecutionResult(

        success=True,

        message="Completed successfully.",

    )

    recovery = engine.recover(

        workflow="Success Workflow",

        step="Finished",

        execution_result=execution,

    )

    print("Recovered :", recovery.recovered)
    print("Workflow  :", recovery.workflow)
    print("Step      :", recovery.step)
    print("Error     :", recovery.error)
    print("Execution :", recovery.execution_result)


if __name__ == "__main__":

    main()