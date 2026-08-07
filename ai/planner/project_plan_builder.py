from ai.planner.execution_plan import ExecutionPlan
from ai.planner.execution_step import ExecutionStep

from ai.project.task import Task


class ProjectPlanBuilder:
    """
    Builds execution plans for project tasks.
    """

    ############################################################

    def build(
        self,
        task: Task,
    ) -> ExecutionPlan:

        plan = ExecutionPlan()

        ########################################################
        # Analyze
        ########################################################

        plan.add_step(

            ExecutionStep(

                action="analyze",

                parameters={

                    "task": task.title,

                },

                description=f"Analyze task '{task.title}'.",

            )

        )

        ########################################################
        # Implement
        ########################################################

        plan.add_step(

            ExecutionStep(

                action="implement",

                parameters={

                    "task": task.title,

                },

                description=f"Implement '{task.title}'.",

            )

        )

        ########################################################
        # Test
        ########################################################

        plan.add_step(

            ExecutionStep(

                action="test",

                parameters={

                    "task": task.title,

                },

                description="Run project tests.",

            )

        )

        ########################################################
        # Reflect
        ########################################################

        plan.add_step(

            ExecutionStep(

                action="reflect",

                parameters={

                    "task": task.title,

                },

                description="Reflect on implementation.",

            )

        )

        ########################################################
        # Update Progress
        ########################################################

        plan.add_step(

            ExecutionStep(

                action="update_progress",

                parameters={

                    "task": task.title,

                },

                description="Update task progress.",

            )

        )

        ########################################################

        return plan