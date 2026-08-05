from dataclasses import dataclass


@dataclass(slots=True)
class ExecutionPolicy:
    """
    Controls how a workflow step should execute.

    Policies describe execution behaviour rather than
    the action itself.
    """

    ############################################################

    retries: int = 0

    ############################################################

    timeout: float = 5.0

    ############################################################

    verify: bool = False

    ############################################################

    continue_on_failure: bool = False

    ############################################################

    retry_delay: float = 0.5