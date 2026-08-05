from ai.tools.tool import Tool
from ai.tools.tool_context import ToolContext
from ai.tools.tool_result import ToolResult

from ai.tools.browser.browser_manager import BrowserManager


class GoogleSearchTool(Tool):
    """
    Performs Google searches.
    """

    ############################################################

    def __init__(self):

        self.manager = BrowserManager()

    ############################################################

    @property
    def name(self) -> str:

        return "Google Search"

    ############################################################

    @property
    def description(self) -> str:

        return "Searches Google."

    ############################################################

    def match_score(
        self,
        command: str,
    ) -> int:

        text = command.lower().strip()

        if text.startswith("search google for"):

            return 100

        if text.startswith("search google"):

            return 95

        if text.startswith("google"):

            return 90

        if text.startswith("search for"):

            return 75

        return 0

    ############################################################

    def execute(
        self,
        context: ToolContext,
    ) -> ToolResult:

        command = context.command.strip()

        query = command

        prefixes = [

            "search google for",

            "search google",

            "google",

            "search for",

        ]

        for prefix in prefixes:

            if query.lower().startswith(prefix):

                query = query[len(prefix):].strip()

                break

        if not query:

            return ToolResult(

                success=False,

                message="Please provide something to search for.",

            )

        success = self.manager.google_search(query)

        if success:

            return ToolResult(

                success=True,

                message=f"Searching Google for '{query}'.",

            )

        return ToolResult(

            success=False,

            message="Google search failed.",

        )