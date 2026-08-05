from ai.tools.tool import Tool
from ai.tools.tool_context import ToolContext
from ai.tools.tool_result import ToolResult

from ai.tools.system.application_database import (
    ApplicationDatabase,
)

from ai.tools.system.application_manager import (
    ApplicationManager,
)


class CloseAppTool(Tool):
    """
    Closes desktop applications.
    """

    ############################################################

    def __init__(self):

        self.database = ApplicationDatabase()

        self.manager = ApplicationManager()

    ############################################################

    @property
    def name(self) -> str:

        return "Close Application"

    ############################################################

    @property
    def description(self) -> str:

        return "Closes running desktop applications."

    ############################################################

    def can_handle(
        self,
        command: str,
    ) -> bool:

        command = command.lower()

        return (

            command.startswith("close")

            or command.startswith("exit")

            or command.startswith("quit")

            or command.startswith("terminate")

            or command.startswith("kill")

        )

    ############################################################

    def execute(
        self,
        context: ToolContext,
    ) -> ToolResult:

        application = self.database.find(
            context.command
        )

        if application is None:

            return ToolResult(

                success=False,

                message="I couldn't identify the application to close.",

            )

        success = self.manager.close(
            application
        )

        if success:

            return ToolResult(

                success=True,

                message=f"Closing {application.name}.",

            )

        if application.process_name is None:

            return ToolResult(

                success=False,

                message=(
                    f"{application.name} cannot be closed safely "
                    "because it is part of Windows."
                ),

            )

        return ToolResult(

            success=False,

            message=f"Failed to close {application.name}.",

        )