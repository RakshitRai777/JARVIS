from datetime import datetime

from ai.memory.memory import Memory
from ai.memory.memory_service import MemoryService
from ai.memory.memory_type import MemoryType

from ai.planner.planning_engine import PlanningEngine


def main():

    ########################################################

    service = MemoryService()

    service.clear()

    ########################################################

    service.remember(

        Memory(

            memory_type=MemoryType.LONG_TERM,

            content="Current project is FitOS",

            created_at=datetime.now(),

        )

    )

    ########################################################

    engine = PlanningEngine()

    ########################################################

    print("=" * 60)
    print("REASONING-DRIVEN PLANNING")
    print("=" * 60)

    plan = engine.build_plan(

        "Continue FitOS",

    )

    ########################################################

    print("Steps :", len(plan.steps))

    print()

    for index, step in enumerate(

        plan.steps,

        start=1,

    ):

        print(

            f"{index}.",

            step.description,

        )


if __name__ == "__main__":

    main()