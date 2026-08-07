from dataclasses import dataclass, field

from ai.agent.agent_state import AgentState


@dataclass(slots=True)
class PlanningContext:
    """
    Context supplied to the planning engine.
    """

    ############################################################

    command: str = ""

    ############################################################

    agent_state: AgentState = field(
        default_factory=AgentState,
    )

    ############################################################

    memory_summary: str = ""