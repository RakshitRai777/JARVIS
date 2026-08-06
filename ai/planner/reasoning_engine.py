from ai.planner.execution_plan import ExecutionPlan
from ai.planner.execution_step import ExecutionStep

from ai.verification.verification_rule import VerificationRule


class ReasoningEngine:
    """
    Improves an ExecutionPlan before execution.

    Responsibilities
    ----------------
    • Expand plans
    • Insert wait steps
    • Insert verification rules
    • Insert focus steps

    It NEVER executes anything.
    """

    ############################################################

    def improve(
        self,
        plan: ExecutionPlan,
    ) -> ExecutionPlan:

        improved = ExecutionPlan()

        ########################################################

        for step in plan.steps:

            ####################################################
            # Keep original step
            ####################################################

            improved.add_step(step)

            ####################################################
            # Only improve application launch steps
            ####################################################

            if not self._is_open_application(step):

                continue

            ####################################################
            # Extract application name
            ####################################################

            command = step.parameters.get(

                "command",

                "",

            )

            app = self._extract_application_name(

                command,

            )

            ####################################################
            # Attach verification
            ####################################################

            step.verification_rule = VerificationRule(

                rule_type="window_exists",

                expected=app,

            )

            ####################################################
            # Wait for application
            ####################################################

            improved.add_step(

                ExecutionStep(

                    action="wait",

                    parameters={

                        "seconds": 2,

                    },

                    description="Wait for application to open.",

                )

            )

            ####################################################
            # Focus application
            ####################################################

            improved.add_step(

                ExecutionStep(

                    action="focus_window",

                    parameters={

                        "application": app,

                    },

                    description="Focus application window.",

                )

            )

        ########################################################

        return improved

    ############################################################

    def _is_open_application(
        self,
        step: ExecutionStep,
    ) -> bool:

        if step.action != "tool":

            return False

        command = step.parameters.get(

            "command",

            "",

        ).lower()

        prefixes = (

            "open ",
            "launch ",
            "start ",
            "run ",

        )

        return command.startswith(

            prefixes,

        )

    ############################################################

    def _extract_application_name(
        self,
        command: str,
    ) -> str:
        """
        Extracts the application name from a
        launch command.

        Examples
        --------
        Open Notepad     -> Notepad
        Launch Chrome    -> Chrome
        Start VS Code    -> VS Code
        Run Calculator   -> Calculator
        """

        text = command.strip()

        lower = text.lower()

        prefixes = (

            "open ",
            "launch ",
            "start ",
            "run ",

        )

        for prefix in prefixes:

            if lower.startswith(prefix):

                return text[len(prefix):].strip()

        return text