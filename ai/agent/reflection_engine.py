from ai.agent.reflection_context import ReflectionContext
from ai.agent.reflection_result import ReflectionResult


class ReflectionEngine:
    """
    Reflects on completed executions.

    Responsibilities
    ----------------
    • Evaluate execution success
    • Produce learnings
    • Decide whether the learning
      should be stored in memory

    Future
    ------
    • LLM-based reflection
    • Failure analysis
    • Strategy improvement
    • Long-term learning
    """

    ############################################################

    def reflect(
        self,
        context: ReflectionContext,
    ) -> ReflectionResult:

        ########################################################
        # Successful execution
        ########################################################

        if context.execution_result.success:

            return ReflectionResult(

                success=True,

                reflection="Execution completed successfully.",

                learning=(
                    f"Workflow '{context.workflow}' "
                    f"completed successfully."
                ),

                should_store=True,

            )

        ########################################################
        # Failed execution
        ########################################################

        return ReflectionResult(

            success=False,

            reflection="Execution failed.",

            learning=(
                f"Workflow '{context.workflow}' "
                f"requires further investigation."
            ),

            should_store=False,

        )