from ai.tools.tool import Tool
from ai.tools.tool_context import ToolContext
from ai.tools.tool_result import ToolResult

from ai.tools.system.application_database import (
    ApplicationDatabase,
)

from ai.tools.system.application_manager import (
    ApplicationManager,
)


class OpenAppTool(Tool):
    """
    Opens desktop applications.
    """

    ############################################################

    def __init__(self):

        self.database = ApplicationDatabase()

        self.manager = ApplicationManager()

    ############################################################

    @property
    def name(self) -> str:

        return "Open Application"

    ############################################################

    @property
    def description(self) -> str:

        return "Launches desktop applications."

    ############################################################

    def match_score(
        self,
        command: str,
    ) -> int:

        text = command.lower().strip()

        ########################################################
        # Must begin with "open"
        ########################################################

        if not text.startswith("open"):

            return 0

        ########################################################
        # URLs belong to OpenURLTool
        ########################################################

        url_indicators = [

            ".com",
            ".org",
            ".net",
            ".io",
            ".dev",
            ".ai",
            "http://",
            "https://",
            "www.",

        ]

        if any(indicator in text for indicator in url_indicators):

            return 5

        ########################################################
        # Is it a known application?
        ########################################################

        application = self.database.find(command)

        if application is not None:

            return 100

        ########################################################

        return 10

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

                message="I couldn't identify the application.",

            )

        success = self.manager.launch(

            application

        )

        if success:

            return ToolResult(

                success=True,

                message=f"Opening {application.name}.",

            )

        return ToolResult(

            success=False,

            message=f"Failed to open {application.name}.",

        )