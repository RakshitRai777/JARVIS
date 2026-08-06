from ai.memory.memory_retriever import MemoryRetriever
from ai.planner.execution_plan import ExecutionPlan
from ai.planner.goal_parser import GoalParser
from ai.planner.plan_builder import PlanBuilder
from ai.planner.planner import Planner
from ai.planner.planning_context import PlanningContext
from ai.planner.reasoning_engine import ReasoningEngine
from ai.planner.planner_advisor import PlannerAdvisor

class PlanningEngine:
    """
    Orchestrates the planning process.

    Responsibilities
    ----------------
    • Retrieve relevant memories
    • Parse goals
    • Ask Planner for a decision
    • Ask PlanBuilder to build steps
    • Return a complete ExecutionPlan
    """

    ############################################################

    def __init__(self):

        self.goal_parser = GoalParser()

        self.planner = Planner()

        self.builder = PlanBuilder()

        self.reasoning = ReasoningEngine()

        self.memory_retriever = MemoryRetriever()

        self.advisor = PlannerAdvisor()

    ############################################################

    def build_plan(

        self,

        request: str | PlanningContext,

    ) -> ExecutionPlan:

        ########################################################
        # Backward compatibility
        ########################################################

        if isinstance(

            request,

            str,

        ):

            context = PlanningContext(

                command=request,

                memory_context=self.memory_retriever.retrieve(

                    request,

                ),

            )

        else:

            context = request

        context = self.advisor.advise(
            context,
        )

        ########################################################

        plan = ExecutionPlan()

        ########################################################
        # Parse goals
        ########################################################

        goals = self.goal_parser.parse(

            context.command,

        )

        ########################################################

        for goal in goals:

            decision = self.planner.decide(

                goal,

            )

            subplan = self.builder.build(

                decision.action,

                goal,

            )

            for step in subplan.steps:

                plan.add_step(

                    step,

                )

        ########################################################
        # Future:
        # Planner will use context.memory_context
        ########################################################

        return self.reasoning.improve(

            plan,

        )