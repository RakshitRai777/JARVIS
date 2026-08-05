from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class WorkflowResult:
    """
    Result returned after executing a workflow.
    """

    ############################################################

    success: bool

    ############################################################

    completed_steps: int = 0

    ############################################################

    total_steps: int = 0

    ############################################################

    execution_time: float = 0.0

    ############################################################

    error: str | None = None

    ############################################################

    data: dict[str, Any] = field(

        default_factory=dict

    )

    ############################################################

    @property
    def progress(self) -> float:
        """
        Returns workflow completion percentage.
        """

        if self.total_steps == 0:

            return 0.0

        return (

            self.completed_steps

            / self.total_steps

        ) * 100

    ############################################################

    def __str__(self):

        if self.success:

            return (

                f"Workflow completed "

                f"({self.completed_steps}/"

                f"{self.total_steps} steps, "

                f"{self.execution_time:.2f}s)"

            )

        return (

            f"Workflow failed "

            f"({self.completed_steps}/"

            f"{self.total_steps} steps)"

        )