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

    def match_score(
        self,
        command: str,
    ) -> int:

        text = command.lower().strip()

        ########################################################
        # Close application commands
        ########################################################

        prefixes = [

            "close",

            "exit",

            "quit",

            "terminate",

            "kill",

        ]

        if not any(text.startswith(prefix) for prefix in prefixes):

            return 0

        ########################################################
        # Known application?
        ########################################################

        application = self.database.find(command)

        if application is not None:

            return 100

        ########################################################

        return 25

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