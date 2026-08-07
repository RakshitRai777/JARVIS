from ai.agent.reasoning_context import ReasoningContext
from ai.agent.reasoning_engine import (ReasoningEngine as AgentReasoningEngine,)

from ai.memory.memory_retriever import MemoryRetriever

from ai.planner.execution_plan import ExecutionPlan
from ai.planner.goal_parser import GoalParser
from ai.planner.plan_builder import PlanBuilder
from ai.planner.planner import Planner
from ai.planner.planner_advisor import PlannerAdvisor
from ai.planner.planning_context import PlanningContext
from ai.planner.reasoning_engine import (ReasoningEngine as PlanReasoningEngine,)
from ai.agent.goal_manager import GoalManager
from ai.planner.planning_strategy_builder import (
    PlanningStrategyBuilder,
)

class PlanningEngine:
    """
    Orchestrates the complete planning pipeline.

    Responsibilities
    ----------------
    • Retrieve relevant memories
    • Build planning context
    • Enrich context
    • Perform reasoning
    • Parse goals
    • Ask Planner for decisions
    • Build execution steps
    • Improve the execution plan
    """

    ############################################################

    def __init__(self):

        self.goal_parser = GoalParser()

        self.planner = Planner()

        self.builder = PlanBuilder()

        self.memory_retriever = MemoryRetriever()

        self.goal_manager = GoalManager()

        self.advisor = PlannerAdvisor(goal_manager=self.goal_manager,)

        ########################################################
        # Agent reasoning (think before planning)
        ########################################################

        self.reasoning_engine = AgentReasoningEngine()

        ########################################################
        # Planner reasoning (improve execution plan)
        ########################################################

        self.plan_reasoning = PlanReasoningEngine()
        self.strategy_builder = PlanningStrategyBuilder()

    ############################################################

    def build_plan(
        self,
        request: str | PlanningContext,
    ) -> ExecutionPlan:

        ########################################################
        # Backward compatibility
        ########################################################

        if isinstance(request, str):

            context = PlanningContext(

                command=request,

                memory_context=self.memory_retriever.retrieve(

                    request,

                ),

            )

        else:

            context = request

        ########################################################
        # Enrich planning context
        ########################################################

        context = self.advisor.advise(

            context,

        )

        ########################################################
        # Perform reasoning
        ########################################################

        reasoning_context = ReasoningContext(

            planning_context=context,

            objective="Determine the best planning strategy",

        )

        reasoning = self.reasoning_engine.reason(

            reasoning_context,

        )

        ########################################################
        # Build planning strategy
        ########################################################

        strategy = self.strategy_builder.build(
            reasoning,
        )

        print()

        print("=" * 60)
        print("PLANNING STRATEGY")
        print("=" * 60)

        print("Strategy")

        print(strategy.strategy.name)

        print()

        print("Reason")

        print(strategy.reason)

        print()

        print("Confidence")

        print(strategy.confidence)

        print()

        ########################################################
        # Build execution plan
        ########################################################

        plan = ExecutionPlan()

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

            ####################################################

            for step in subplan.steps:

                plan.add_step(

                    step,

                )

        ########################################################
        # Improve execution plan
        ########################################################

        return self.plan_reasoning.improve(

            plan,

        )