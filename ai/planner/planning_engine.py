from ai.agent.agent_state import AgentState
from ai.agent.goal_manager import GoalManager
from ai.agent.reasoning_context import ReasoningContext
from ai.agent.reasoning_engine import (
    ReasoningEngine as AgentReasoningEngine,
)

from ai.memory.memory_retriever import MemoryRetriever

from ai.project.project_manager import ProjectManager

from ai.planner.execution_plan import ExecutionPlan
from ai.planner.goal_parser import GoalParser
from ai.planner.plan_builder import PlanBuilder
from ai.planner.planner import Planner
from ai.planner.planner_advisor import PlannerAdvisor
from ai.planner.planning_context import PlanningContext
from ai.planner.planning_strategy_builder import (
    PlanningStrategyBuilder,
)
from ai.planner.project_plan_builder import (
    ProjectPlanBuilder,
)
from ai.planner.reasoning_engine import (
    ReasoningEngine as PlanReasoningEngine,
)


class PlanningEngine:
    """
    Orchestrates the complete planning pipeline.

    Responsibilities
    ----------------
    • Retrieve relevant memories
    • Build AgentState
    • Build PlanningContext
    • Enrich planning context
    • Perform reasoning
    • Build planning strategy
    • Build execution plans
    • Improve execution plans
    """

    ############################################################

    def __init__(self):

        self.goal_parser = GoalParser()

        self.planner = Planner()

        self.builder = PlanBuilder()

        self.project_builder = ProjectPlanBuilder()

        self.memory_retriever = MemoryRetriever()

        self.goal_manager = GoalManager()

        self.project_manager = ProjectManager()

        self.advisor = PlannerAdvisor(

            goal_manager=self.goal_manager,

            project_manager=self.project_manager,

        )

        ########################################################
        # Agent reasoning
        ########################################################

        self.reasoning_engine = AgentReasoningEngine()

        ########################################################
        # Planner reasoning
        ########################################################

        self.plan_reasoning = PlanReasoningEngine()

        ########################################################

        self.strategy_builder = PlanningStrategyBuilder()

    ############################################################

    def build_plan(
        self,
        request: str | PlanningContext,
    ) -> ExecutionPlan:

        ########################################################
        # Build Planning Context
        ########################################################

        if isinstance(request, str):

            memory_context = self.memory_retriever.retrieve(

                request,

            )

            agent_state = AgentState(

                memory_context=memory_context,

            )

            context = PlanningContext(

                command=request,

                agent_state=agent_state,

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

            command=context.command,

            agent_state=context.agent_state,

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

        ########################################################
        # Temporary Debug
        ########################################################

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
        # Project-aware planning
        ########################################################

        if strategy.strategy.name == "RESUME_PROJECT":

            ####################################################
            # Ask ProjectManager for the active project
            ####################################################

            project = self.project_manager.get_active_project()

            if project is not None:

                ################################################
                # Ask ProjectManager for the next task
                ################################################

                task = self.project_manager.get_active_task(

                    project,

                )

                ################################################

                if task is not None:

                    plan = self.project_builder.build(

                        task,

                    )

                    return self.plan_reasoning.improve(

                        plan,

                    )

        ########################################################
        # Default planning
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