from ai.agent.reasoning_context import ReasoningContext
from ai.agent.reasoning_engine import ReasoningEngine

from ai.memory.memory_context import MemoryContext

from ai.planner.planning_context import PlanningContext


def run(command, summary):

    planning = PlanningContext(

        command=command,

        memory_context=MemoryContext(),

        memory_summary=summary,

    )

    context = ReasoningContext(

        planning_context=planning,

        objective="Understand user request",

    )

    engine = ReasoningEngine()

    result = engine.reason(

        context,

    )

    print("=" * 60)

    print(command)

    print("=" * 60)

    print("Thought")

    print(result.thought)

    print()

    print("Conclusion")

    print(result.conclusion)

    print()

    print("Confidence")

    print(result.confidence)

    print()


def main():

    run(

        "Continue FitOS",

        "Relevant Memories:\n- Current project is FitOS",

    )

    run(

        "Continue Unknown Project",

        "No relevant memories.",

    )

    run(

        "Remember that my favourite editor is VS Code",

        "No relevant memories.",

    )

    run(

        "Open Chrome",

        "No relevant memories.",

    )


if __name__ == "__main__":

    main()