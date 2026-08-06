import time
from collections.abc import Callable

from ai.execution.execution_result import ExecutionResult
from ai.execution.retry_policy import RetryPolicy


class RetryEngine:
    """
    Generic retry engine.

    Responsibilities
    ----------------
    • Execute an operation
    • Retry failed operations
    • Wait between retries
    • Return the final ExecutionResult

    The RetryEngine is intentionally unaware of
    workflows, actions, tools, or execution
    contexts. It simply retries any callable
    that returns an ExecutionResult.
    """

    ############################################################

    def __init__(
        self,
        sleep_function: Callable[[float], None] = time.sleep,
    ):

        self._sleep = sleep_function

    ############################################################

    def execute(
        self,
        operation: Callable[[], ExecutionResult],
        policy: RetryPolicy,
    ) -> ExecutionResult:

        """
        Execute an operation according to the
        supplied retry policy.
        """

        ########################################################
        # Retry disabled
        ########################################################

        if not policy.enabled:

            return operation()

        ########################################################

        last_result: ExecutionResult | None = None

        ########################################################

        for attempt in range(

            1,

            policy.max_attempts + 1,

        ):

            result = operation()

            ####################################################
            # Success
            ####################################################

            if result.success:

                return result

            ####################################################

            last_result = result

            ####################################################
            # Final attempt reached
            ####################################################

            if attempt == policy.max_attempts:

                break

            ####################################################
            # Wait before next retry
            ####################################################

            self._sleep(

                policy.delay_seconds,

            )

        ########################################################
        # Return the final failure
        ########################################################

        return last_result