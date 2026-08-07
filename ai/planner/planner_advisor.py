from ai.agent.goal_context import GoalContext
from ai.agent.goal_manager import GoalManager

from ai.planner.context_builder import ContextBuilder
from ai.planner.planning_context import PlanningContext


class PlannerAdvisor:
    """
    Enriches planning context before it reaches
    the Planner.

    Responsibilities
    ----------------
    • Build memory summary
    • Attach active goal information
    """

    ############################################################

    def __init__(self,goal_manager: GoalManager | None = None,):

        self.context_builder = ContextBuilder()

        self.goal_manager = goal_manager or GoalManager()

    ############################################################

    def advise(
        self,
        context: PlanningContext,
    ) -> PlanningContext:

        ########################################################
        # Build structured memory context
        ########################################################

        structured_context = self.context_builder.build(

            context.memory_context,

        )

        context.memory_summary = structured_context

        ########################################################
        # Attach active goal
        ########################################################

        active_goal = self.goal_manager.get_active_goal()

        context.goal_context = GoalContext(

            current_goal=active_goal,

            all_goals=self.goal_manager.get_goals(),

        )

        ########################################################

        return context