from ai.tools.tool import Tool
from ai.tools.tool_context import ToolContext
from ai.tools.tool_result import ToolResult

from ai.tools.browser.browser_manager import BrowserManager


class OpenURLTool(Tool):
    """
    Opens websites in the default browser.
    """

    ############################################################

    def __init__(self):

        self.manager = BrowserManager()

    ############################################################

    @property
    def name(self):

        return "Open URL"

    ############################################################

    @property
    def description(self):

        return "Opens websites."

    ############################################################

    def match_score(
        self,
        command: str,
    ) -> int:

        text = command.lower().strip()

        indicators = [

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

        if any(indicator in text for indicator in indicators):

            return 100

        return 0

    ############################################################

    def execute(
        self,
        context: ToolContext,
    ) -> ToolResult:

        command = context.command.strip()

        ########################################################
        # Remove the "open" keyword safely
        ########################################################

        parts = command.split(maxsplit=1)

        if len(parts) > 1:

            url = parts[1].strip()

        else:

            url = command.strip()

        ########################################################

        if not url.startswith(

            (

                "http://",

                "https://",

            )

        ):

            url = "https://" + url

        success = self.manager.open_url(url)

        if success:

            return ToolResult(

                success=True,

                message=f"Opening {url}.",

            )

        return ToolResult(

            success=False,

            message=f"Failed to open {url}.",

        )