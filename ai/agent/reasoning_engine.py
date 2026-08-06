from ai.agent.reasoning_context import ReasoningContext
from ai.agent.reasoning_result import ReasoningResult


class ReasoningEngine:
    """
    Performs high-level reasoning before planning.

    Version 2
    ---------
    Uses the user's command together with the
    retrieved memory summary to generate an
    intelligent conclusion.

    Future
    ------
    • LLM reasoning
    • Multi-step reasoning
    • Reflection
    • Strategy selection
    """

    ############################################################

    def reason(
        self,
        context: ReasoningContext,
    ) -> ReasoningResult:

        command = (
            context.planning_context.command
            .lower()
            .strip()
        )

        summary = (
            context.planning_context.memory_summary
        )

        ########################################################
        # Build reasoning
        ########################################################

        thought = (
            f"Objective: {context.objective}\n"
            f"Command: {context.planning_context.command}"
        )

        ########################################################
        # Continue existing work
        ########################################################

        if "continue" in command:

            if summary and summary != "No relevant memories.":

                conclusion = (
                    "Relevant memories found. "
                    "Continue the existing work."
                )

                confidence = 0.95

            else:

                conclusion = (
                    "No previous work found. "
                    "A new plan may be required."
                )

                confidence = 0.75

        ########################################################
        # Remember
        ########################################################

        elif "remember" in command:

            conclusion = (
                "Store the supplied information in memory."
            )

            confidence = 1.0

        ########################################################
        # Default
        ########################################################

        else:

            conclusion = (
                "Proceed with planning."
            )

            confidence = 0.85

        ########################################################

        return ReasoningResult(

            success=True,

            thought=thought,

            conclusion=conclusion,

            confidence=confidence,

        )