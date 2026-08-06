from datetime import datetime

from ai.memory.memory import Memory
from ai.memory.memory_service import MemoryService
from ai.memory.memory_type import MemoryType

from ai.planner.planning_engine import PlanningEngine


def main():

    ########################################################
    # Setup
    ########################################################

    service = MemoryService()

    service.clear()

    ########################################################
    # Store memories
    ########################################################

    service.remember(

        Memory(

            memory_type=MemoryType.LONG_TERM,

            content="Current project is FitOS",

            created_at=datetime.now(),

        )

    )

    service.remember(

        Memory(

            memory_type=MemoryType.GOAL,

            content="Build an AI Operating System",

            created_at=datetime.now(),

        )

    )

    ########################################################
    # Planning
    ########################################################

    engine = PlanningEngine()

    print("=" * 60)
    print("MEMORY AWARE PLANNING")
    print("=" * 60)

    plan = engine.build_plan(

        "Continue FitOS"

    )

    ########################################################
    # Output
    ########################################################

    print("Steps :", len(plan.steps))

    print()

    for index, step in enumerate(

        plan.steps,

        start=1,

    ):

        print(f"Step {index}")

        print("Action      :", step.action)

        print("Description :", step.description)

        print("-" * 60)


if __name__ == "__main__":

    main()