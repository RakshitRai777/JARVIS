from dataclasses import dataclass


@dataclass(slots=True)
class RetryPolicy:
    """
    Defines how a workflow step should be retried.

    Responsibilities
    ----------------
    • Maximum retry attempts
    • Delay between retries
    • Whether retry is enabled

    This class contains configuration only.
    The RetryEngine performs the actual retry logic.
    """

    ############################################################

    enabled: bool = True

    ############################################################

    max_attempts: int = 3

    ############################################################

    delay_seconds: float = 1.0