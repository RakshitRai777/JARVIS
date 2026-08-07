from dataclasses import dataclass, field

from ai.agent.agent_state import AgentState


@dataclass(slots=True)
class ReasoningContext:
    """
    Context supplied to the reasoning engine.
    """

    ############################################################

    command: str = ""

    ############################################################

    agent_state: AgentState = field(
        default_factory=AgentState,
    )

    ############################################################

    objective: str = ""

    ############################################################

    previous_reasoning: str = ""