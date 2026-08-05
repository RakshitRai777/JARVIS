from dataclasses import dataclass, field
from typing import Any

from ai.execution.execution_policy import ExecutionPolicy
from ai.workflow.workflow import Workflow
from ai.workflow.workflow_step import WorkflowStep


@dataclass(slots=True)
class ExecutionContext:
    """
    Context for executing a single workflow step.

    The ExecutionEngine owns this object and
    passes it throughout the execution pipeline.
    """

    ############################################################

    workflow: Workflow

    ############################################################

    step: WorkflowStep

    ############################################################

    policy: ExecutionPolicy

    ############################################################

    metadata: dict[str, Any] = field(

        default_factory=dict

    )

    ############################################################

    shared_data: dict[str, Any] = field(

        default_factory=dict

    )

    ############################################################

    attempt: int = 1