from ai.planner.context_builder import ContextBuilder
from ai.planner.planning_context import PlanningContext


class PlannerAdvisor:
    """
    Enriches planning context before it reaches
    the Planner.
    """

    ############################################################

    def __init__(self):

        self.context_builder = ContextBuilder()

    ############################################################

    def advise(
        self,
        context: PlanningContext,
    ) -> PlanningContext:

        ########################################################
        # Build structured context
        ########################################################

        structured_context = self.context_builder.build(

            context.memory_context,

        )

        ########################################################
        # Store it for future planner / LLM use
        ########################################################

        context.memory_summary = structured_context

        ########################################################

        return context