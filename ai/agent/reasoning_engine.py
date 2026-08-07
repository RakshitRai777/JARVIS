from ai.agent.reasoning_context import ReasoningContext
from ai.agent.reasoning_result import ReasoningResult


class ReasoningEngine:
    """
    Performs high-level reasoning before planning.

    Version 3
    ---------
    Uses the AgentState to reason about the user's
    current situation before planning.

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

        command = context.command.lower().strip()

        ########################################################
        # Memory summary
        ########################################################

        memories = context.agent_state.memory_context

        if memories.count:

            summary = "\n".join(

                memory.content

                for memory in memories.memories

            )

        else:

            summary = "No relevant memories."

        ########################################################
        # Goal information
        ########################################################

        goal = context.agent_state.goal_context.current_goal

        ########################################################
        # Project information
        ########################################################

        project = context.agent_state.active_project

        ########################################################
        # Build reasoning thought
        ########################################################

        thought = (
            f"Objective: {context.objective}\n"
            f"Command: {context.command}"
        )

        if goal is not None:

            thought += (
                f"\nActive Goal: {goal.title}"
                f"\nGoal Status: {goal.status.name}"
                f"\nProgress: {goal.progress}%"
            )

        if project is not None:

            thought += (
                f"\nActive Project: {project.name}"
                f"\nProject Status: {project.status.name}"
                f"\nProject Progress: {project.progress}%"
            )

        ########################################################
        # Continue existing work
        ########################################################

        if "continue" in command:

            if project is not None:

                conclusion = (
                    f"Continue the active project "
                    f"'{project.name}' "
                    f"from {project.progress}% progress."
                )

                confidence = 0.99

            elif goal is not None:

                conclusion = (
                    f"Continue the active goal "
                    f"'{goal.title}' "
                    f"from {goal.progress}% progress."
                )

                confidence = 0.98

            elif summary != "No relevant memories.":

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