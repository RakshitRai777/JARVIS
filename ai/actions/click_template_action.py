from pathlib import Path

from ai.actions.action import Action
from ai.execution.execution_result import ExecutionResult
from ai.tools.desktop.click_template_tool import ClickTemplateTool


class ClickTemplateAction(Action):
    """
    Action that clicks on a template.
    """

    ############################################################

    def __init__(self):

        self.tool = ClickTemplateTool()

    ############################################################

    @property
    def name(self) -> str:

        return "click_template"

    ############################################################

    def execute(
        self,
        template: str | Path,
        image_path: str | Path | None = None,
        threshold: float = 0.75,
    ) -> ExecutionResult:

        success = self.tool.click(

            template=template,

            image_path=image_path,

            threshold=threshold,

        )

        if success:

            return ExecutionResult(

                success=True,

                message="Template clicked.",

            )

        return ExecutionResult(

            success=False,

            message="Template not found.",

        )