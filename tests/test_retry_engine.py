from ai.execution.execution_result import ExecutionResult
from ai.execution.retry_engine import RetryEngine
from ai.execution.retry_policy import RetryPolicy


############################################################
# Test 1
############################################################

def always_success():

    return ExecutionResult(

        success=True,

        message="Success",

    )


############################################################
# Test 2
############################################################

failure_counter = 0


def succeed_after_three_attempts():

    global failure_counter

    failure_counter += 1

    if failure_counter < 3:

        return ExecutionResult(

            success=False,

            message=f"Failure {failure_counter}",

        )

    return ExecutionResult(

        success=True,

        message=f"Succeeded on attempt {failure_counter}",

    )


############################################################
# Test 3
############################################################

always_fail_counter = 0


def always_fail():

    global always_fail_counter

    always_fail_counter += 1

    return ExecutionResult(

        success=False,

        message=f"Failure {always_fail_counter}",

    )


############################################################

def main():

    engine = RetryEngine()

    ########################################################
    # Test 1
    ########################################################

    print("=" * 60)
    print("SUCCESS FIRST ATTEMPT")
    print("=" * 60)

    result = engine.execute(

        always_success,

        RetryPolicy(),

    )

    print(result)

    ########################################################
    # Test 2
    ########################################################

    print()
    print("=" * 60)
    print("SUCCESS AFTER RETRIES")
    print("=" * 60)

    global failure_counter

    failure_counter = 0

    result = engine.execute(

        succeed_after_three_attempts,

        RetryPolicy(

            max_attempts=5,

            delay_seconds=0,

        ),

    )

    print(result)

    print("Attempts :", failure_counter)

    ########################################################
    # Test 3
    ########################################################

    print()
    print("=" * 60)
    print("FAIL AFTER MAX ATTEMPTS")
    print("=" * 60)

    global always_fail_counter

    always_fail_counter = 0

    result = engine.execute(

        always_fail,

        RetryPolicy(

            max_attempts=3,

            delay_seconds=0,

        ),

    )

    print(result)

    print("Attempts :", always_fail_counter)

    ########################################################
    # Test 4
    ########################################################

    print()
    print("=" * 60)
    print("RETRY DISABLED")
    print("=" * 60)

    always_fail_counter = 0

    result = engine.execute(

        always_fail,

        RetryPolicy(

            enabled=False,

            max_attempts=5,

            delay_seconds=0,

        ),

    )

    print(result)

    print("Attempts :", always_fail_counter)


if __name__ == "__main__":

    main()