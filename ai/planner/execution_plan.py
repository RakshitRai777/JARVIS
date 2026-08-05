from dataclasses import dataclass, field

from ai.planner.execution_step import (
    ExecutionStep,
)


@dataclass
class ExecutionPlan:
    """
    Represents a sequence of executable
    steps.

    Future:
        • Conditional branches
        • Loops
        • Recovery
    """

    ############################################################

    steps: list[ExecutionStep] = field(

        default_factory=list

    )

    ############################################################

    def add_step(
        self,
        step: ExecutionStep,
    ):

        self.steps.append(step)

    ############################################################

    @property
    def is_empty(
        self,
    ) -> bool:

        return len(self.steps) == 0