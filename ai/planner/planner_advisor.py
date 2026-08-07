from ai.agent.goal_context import GoalContext
from ai.agent.goal_manager import GoalManager

from ai.project.project_manager import ProjectManager

from ai.planner.context_builder import ContextBuilder
from ai.planner.planning_context import PlanningContext


class PlannerAdvisor:
    """
    Enriches the planning context before it
    reaches the Planner.

    Responsibilities
    ----------------
    • Build memory summary
    • Attach active goal
    • Attach active project
    """

    ############################################################

    def __init__(
        self,
        goal_manager: GoalManager | None = None,
        project_manager: ProjectManager | None = None,
    ):

        self.context_builder = ContextBuilder()

        self.goal_manager = goal_manager or GoalManager()

        self.project_manager = project_manager or ProjectManager()

    ############################################################

    def advise(
        self,
        context: PlanningContext,
    ) -> PlanningContext:

        ########################################################
        # Memory Summary
        ########################################################

        context.memory_summary = self.context_builder.build(

            context.agent_state.memory_context,

        )

        ########################################################
        # Goal
        ########################################################

        context.agent_state.goal_context = GoalContext(

            current_goal=self.goal_manager.get_active_goal(),

            all_goals=self.goal_manager.get_goals(),

        )

        ########################################################
        # Project
        ########################################################

        context.agent_state.active_project = (

            self.project_manager.get_active_project()

        )

        ########################################################

        return context