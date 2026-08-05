import time

from ai.actions.action_manager import ActionManager

from ai.tools.tool_executor import ToolExecutor

from ai.workflow.workflow import Workflow
from ai.workflow.workflow_result import WorkflowResult


class WorkflowEngine:
    """
    Executes workflows.

    Responsibilities
    ----------------
    • Execute WorkflowStep objects
    • Delegate Action execution to ActionManager
    • Fall back to ToolExecutor for legacy actions
    • Return WorkflowResult

    Future versions will support:
        • Verification
        • Retry
        • Conditional execution
        • Parallel execution
    """

    ############################################################

    def __init__(self):

        ########################################################
        # Action Framework
        ########################################################

        self.action_manager = ActionManager()

        ########################################################
        # Legacy Tool Framework
        ########################################################

        self.executor = ToolExecutor()

    ############################################################

    def execute(
        self,
        workflow: Workflow,
    ) -> WorkflowResult:

        start_time = time.perf_counter()

        completed_steps = 0

        ########################################################

        for step in workflow:

            ####################################################
            # Try Action Framework first
            ####################################################

            result = self.action_manager.execute(

                workflow,

                step,

            )

            ####################################################
            # Action Found
            ####################################################

            if result.success:

                completed_steps += 1

                continue

            ####################################################
            # If ActionManager doesn't know this action,
            # fall back to the legacy Tool framework.
            ####################################################

            if (
                result.error
                and result.error.startswith(
                    "No action registered"
                )
            ):

                command = self._build_command(step)

                legacy_result = self.executor.execute(

                    command

                )

                if not legacy_result.success:

                    return WorkflowResult(

                        success=False,

                        completed_steps=completed_steps,

                        total_steps=len(workflow),

                        execution_time=(
                            time.perf_counter()
                            - start_time
                        ),

                        error=legacy_result.message,

                    )

                completed_steps += 1

                continue

            ####################################################
            # Action failed
            ####################################################

            return WorkflowResult(

                success=False,

                completed_steps=completed_steps,

                total_steps=len(workflow),

                execution_time=(
                    time.perf_counter()
                    - start_time
                ),

                error=result.message or result.error,

            )

        ########################################################

        return WorkflowResult(

            success=True,

            completed_steps=completed_steps,

            total_steps=len(workflow),

            execution_time=(
                time.perf_counter()
                - start_time
            ),

        )

    ############################################################

    def _build_command(
        self,
        step,
    ) -> str:
        """
        Temporary compatibility layer.

        Converts WorkflowStep into a natural-language
        command for the legacy ToolExecutor.

        This method will disappear once every action
        has been migrated to the Action Framework.
        """

        action = step.action.lower()

        params = step.parameters

        ########################################################

        if action == "click_text":

            return f"Click {params['target']}"

        ########################################################

        if action == "type_text":

            return f"Type {params['text']}"

        ########################################################

        if action == "press_key":

            return f"Press {params['key']}"

        ########################################################

        if action == "hotkey":

            keys = " ".join(

                params["keys"]

            )

            return f"Press {keys}"

        ########################################################

        if action == "open_url":

            return f"Open {params['url']}"

        ########################################################

        raise ValueError(

            f"Unknown workflow action: {action}"

        )