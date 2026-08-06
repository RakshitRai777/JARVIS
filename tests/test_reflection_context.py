from ai.agent.reflection_context import ReflectionContext

from ai.execution.execution_result import ExecutionResult


def main():

    ########################################################

    result = ExecutionResult(

        success=True,

        message="Execution completed successfully.",

    )

    ########################################################

    context = ReflectionContext(

        execution_result=result,

        objective="Continue FitOS",

        workflow="Planning Workflow",

    )

    ########################################################

    print("=" * 60)
    print("REFLECTION CONTEXT")
    print("=" * 60)

    print("Success   :", context.execution_result.success)

    print("Message   :", context.execution_result.message)

    print("Objective :", context.objective)

    print("Workflow  :", context.workflow)


if __name__ == "__main__":

    main()