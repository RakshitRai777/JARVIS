from ai.planner.planner import Planner
from ai.planner.planner_action import PlannerAction


def test_tool_detection():

    planner = Planner()

    decision = planner.decide("Open Chrome")

    assert decision.action == PlannerAction.TOOL


def test_memory_detection():

    planner = Planner()

    decision = planner.decide(
        "Remember I live in Uttarakhand"
    )

    assert decision.action == PlannerAction.MEMORY


def test_llm_detection():

    planner = Planner()

    decision = planner.decide("Hello")

    assert decision.action == PlannerAction.LLM


def test_system_detection():

    planner = Planner()

    decision = planner.decide("exit")

    assert decision.action == PlannerAction.SYSTEM