from ai.planner.execution_plan import ExecutionPlan
from ai.planner.execution_step import ExecutionStep
from ai.planner.planner_action import PlannerAction


class PlanBuilder:
    """
    Builds executable plans from planner decisions.

    The Planner decides WHAT should happen.

    The PlanBuilder decides HOW to execute it.
    """

    ############################################################

    def build(
        self,
        action: PlannerAction,
        message: str,
    ) -> ExecutionPlan:

        plan = ExecutionPlan()

        ########################################################
        # Tool
        ########################################################

        if action == PlannerAction.TOOL:

            plan.add_step(

                ExecutionStep(

                    action="tool",

                    parameters={

                        "command": message,

                    },

                    description="Execute tool command.",

                )

            )

        ########################################################
        # Memory
        ########################################################

        elif action == PlannerAction.MEMORY:

            plan.add_step(

                ExecutionStep(

                    action="memory",

                    parameters={

                        "query": message,

                    },

                    description="Query memory.",

                )

            )

        ########################################################
        # LLM
        ########################################################

        elif action == PlannerAction.LLM:

            plan.add_step(

                ExecutionStep(

                    action="llm",

                    parameters={

                        "query": message,

                    },

                    description="Generate LLM response.",

                )

            )

        ########################################################
        # System
        ########################################################

        elif action == PlannerAction.SYSTEM:

            plan.add_step(

                ExecutionStep(

                    action="system",

                    parameters={

                        "command": message,

                    },

                    description="Execute system command.",

                )

            )

        return plan