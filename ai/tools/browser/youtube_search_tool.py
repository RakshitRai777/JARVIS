from ai.tools.tool import Tool
from ai.tools.tool_context import ToolContext
from ai.tools.tool_result import ToolResult

from ai.tools.browser.browser_manager import BrowserManager


class YouTubeSearchTool(Tool):
    """
    Performs YouTube searches.
    """

    ############################################################

    def __init__(self):

        self.manager = BrowserManager()

    ############################################################

    @property
    def name(self) -> str:

        return "YouTube Search"

    ############################################################

    @property
    def description(self) -> str:

        return "Searches YouTube."

    ############################################################

    def match_score(
        self,
        command: str,
    ) -> int:

        text = command.lower().strip()

        if text.startswith("search youtube for"):

            return 100

        if text.startswith("search youtube"):

            return 95

        if text.startswith("youtube"):

            return 90

        if text.startswith("search video for"):

            return 85

        if text.startswith("search video"):

            return 80

        if text.startswith("find video"):

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

            "search youtube for",

            "search youtube",

            "youtube",

            "search video for",

            "search video",

            "find video",

        ]

        for prefix in prefixes:

            if query.lower().startswith(prefix):

                query = query[len(prefix):].strip()

                break

        if not query:

            return ToolResult(

                success=False,

                message="Please provide something to search on YouTube.",

            )

        success = self.manager.youtube_search(query)

        if success:

            return ToolResult(

                success=True,

                message=f"Searching YouTube for '{query}'.",

            )

        return ToolResult(

            success=False,

            message="YouTube search failed.",

        )