from ai.agent.reflection_context import ReflectionContext
from ai.agent.reflection_engine import ReflectionEngine

from ai.execution.execution_result import ExecutionResult


def run(success):

    ########################################################

    result = ExecutionResult(

        success=success,

        message="Execution finished.",

    )

    ########################################################

    context = ReflectionContext(

        execution_result=result,

        objective="Continue FitOS",

        workflow="Planning Workflow",

    )

    ########################################################

    engine = ReflectionEngine()

    reflection = engine.reflect(

        context,

    )

    ########################################################

    print("=" * 60)

    print("SUCCESS =", success)

    print("=" * 60)

    print("Reflection")

    print(reflection.reflection)

    print()

    print("Learning")

    print(reflection.learning)

    print()

    print("Store")

    print(reflection.should_store)

    print()


def main():

    run(True)

    run(False)


if __name__ == "__main__":

    main()