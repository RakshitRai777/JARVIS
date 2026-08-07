from datetime import datetime

from ai.agent.agent_state import AgentState

from ai.memory.memory import Memory
from ai.memory.memory_context import MemoryContext
from ai.memory.memory_type import MemoryType

from ai.planner.planner_advisor import PlannerAdvisor
from ai.planner.planning_context import PlanningContext


def main():

    ########################################################
    # Memory Context
    ########################################################

    memory_context = MemoryContext(

        query="Continue FitOS",

    )

    memory_context.add(

        Memory(

            memory_type=MemoryType.LONG_TERM,

            content="Current project is FitOS",

            created_at=datetime.now(),

        )

    )

    ########################################################
    # Agent State
    ########################################################

    state = AgentState(

        memory_context=memory_context,

    )

    ########################################################
    # Planning Context
    ########################################################

    context = PlanningContext(

        command="Continue FitOS",

        agent_state=state,

    )

    ########################################################

    print("=" * 60)
    print("RAW MEMORY CONTEXT")
    print("=" * 60)

    for memory in context.agent_state.memory_context.memories:

        print(memory.content)

    print()

    ########################################################

    advisor = PlannerAdvisor()

    enriched = advisor.advise(

        context,

    )

    ########################################################

    print("=" * 60)
    print("PLANNER ADVISOR")
    print("=" * 60)

    print("Command :", enriched.command)

    print(
        "Memory Count :",
        enriched.agent_state.memory_context.count,
    )

    print()

    print("Summary")

    print("-" * 60)

    print(enriched.memory_summary)


if __name__ == "__main__":

    main()