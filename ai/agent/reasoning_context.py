from dataclasses import dataclass, field

from ai.planner.planning_context import PlanningContext


@dataclass(slots=True)
class ReasoningContext:
    """
    Context supplied to the reasoning engine.
    """

    ############################################################

    planning_context: PlanningContext = field(

        default_factory=PlanningContext,

    )

    ############################################################

    objective: str = ""

    ############################################################

    previous_reasoning: str = ""