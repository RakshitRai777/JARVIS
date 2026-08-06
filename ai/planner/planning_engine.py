from ai.planner.execution_plan import ExecutionPlan
from ai.planner.goal_parser import GoalParser
from ai.planner.plan_builder import PlanBuilder
from ai.planner.planner import Planner
from ai.planner.reasoning_engine import ReasoningEngine

class PlanningEngine:
    """
    Orchestrates the planning process.

    Responsibilities
    ----------------
    • Parse goals
    • Ask Planner for a decision
    • Ask PlanBuilder to build steps
    • Return a complete ExecutionPlan
    """

    def __init__(self):

        self.goal_parser = GoalParser()
        self.planner = Planner()
        self.builder = PlanBuilder()
        self.reasoning = ReasoningEngine()

    ############################################################

    def build_plan(
        self,
        message: str,
    ) -> ExecutionPlan:

        plan = ExecutionPlan()

        goals = self.goal_parser.parse(message)

        for goal in goals:

            decision = self.planner.decide(goal)

            subplan = self.builder.build(

                decision.action,

                goal,

            )

            for step in subplan.steps:

                plan.add_step(step)

        return self.reasoning.improve(plan)