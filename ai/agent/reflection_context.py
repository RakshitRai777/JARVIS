from dataclasses import dataclass, field

from ai.execution.execution_result import ExecutionResult


@dataclass(slots=True)
class ReflectionContext:
    """
    Context supplied to the Reflection Engine.

    Contains everything required to evaluate
    a completed execution.
    """

    ############################################################

    execution_result: ExecutionResult = field(

        default_factory=ExecutionResult,

    )

    ############################################################

    objective: str = ""

    ############################################################

    workflow: str = ""