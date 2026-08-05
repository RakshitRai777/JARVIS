from dataclasses import dataclass, field
from typing import Any

from ai.workflow.workflow import Workflow
from ai.workflow.workflow_step import WorkflowStep


@dataclass(slots=True)
class ActionContext:
    """
    Context passed to every Action during execution.

    It provides all information an Action needs
    without coupling it to the WorkflowEngine.
    """

    ############################################################

    workflow: Workflow

    ############################################################

    step: WorkflowStep

    ############################################################

    metadata: dict[str, Any] = field(

        default_factory=dict

    )

    ############################################################

    shared_data: dict[str, Any] = field(

        default_factory=dict

    )