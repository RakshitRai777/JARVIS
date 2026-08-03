from ai.planner.decision import Decision
from ai.planner.planner_action import PlannerAction


class Planner:
    """
    Decides what should happen with the user's request.
    """

    def decide(self, message: str) -> Decision:

        text = message.lower().strip()

        tool_keywords = [
            "open",
            "close",
            "shutdown",
            "restart",
            "search",
            "play"
        ]

        if any(text.startswith(word) for word in tool_keywords):

            return Decision(
                action=PlannerAction.TOOL,
                reason="Tool command detected."
            )

        if text.startswith("remember"):

            return Decision(
                action=PlannerAction.MEMORY,
                reason="Memory storage requested."
            )

        if text in [
            "stop",
            "exit",
            "quit"
        ]:

            return Decision(
                action=PlannerAction.SYSTEM,
                reason="System command."
            )

        return Decision(
            action=PlannerAction.LLM,
            reason="General conversation."
        )