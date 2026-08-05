from dataclasses import dataclass, field

from ai.workflow.workflow_step import WorkflowStep


@dataclass(slots=True)
class Workflow:
    """
    Represents an executable workflow.

    A workflow is simply an ordered collection
    of WorkflowStep objects.
    """

    ############################################################

    name: str = "Unnamed Workflow"

    ############################################################

    description: str = ""

    ############################################################

    steps: list[WorkflowStep] = field(

        default_factory=list

    )

    ############################################################

    metadata: dict = field(

        default_factory=dict

    )

    ############################################################

    def add_step(
        self,
        step: WorkflowStep,
    ):

        self.steps.append(step)

    ############################################################

    def extend(
        self,
        steps: list[WorkflowStep],
    ):

        self.steps.extend(steps)

    ############################################################

    def clear(
        self,
    ):

        self.steps.clear()

    ############################################################

    def __len__(
        self,
    ):

        return len(self.steps)

    ############################################################

    def __iter__(
        self,
    ):

        return iter(self.steps)

    ############################################################

    def __getitem__(
        self,
        index,
    ):

        return self.steps[index]

    ############################################################

    @property
    def empty(
        self,
    ) -> bool:

        return len(self.steps) == 0

    ############################################################

    def __str__(
        self,
    ):

        return (

            f"{self.name} "

            f"({len(self.steps)} steps)"

        )