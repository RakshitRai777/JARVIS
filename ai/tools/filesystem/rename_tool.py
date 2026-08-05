from ai.tools.tool import Tool
from ai.tools.tool_context import ToolContext
from ai.tools.tool_result import ToolResult

from ai.tools.filesystem.file_manager import FileManager
from ai.tools.filesystem.path_utils import PathUtils

from ai.tools.filesystem.command_parser import (
    FilesystemCommandParser,
)

from ai.tools.filesystem.filesystem_action import (
    FilesystemAction,
)


class RenameTool(Tool):
    """
    Renames files and folders.
    """

    ############################################################

    def __init__(self):

        self.manager = FileManager()

        self.parser = FilesystemCommandParser()

    ############################################################

    @property
    def name(self) -> str:

        return "Rename"

    ############################################################

    @property
    def description(self) -> str:

        return "Renames files and folders."

    ############################################################

    def match_score(
        self,
        command: str,
    ) -> int:

        parsed = self.parser.parse(command)

        if parsed is None:

            return 0

        if parsed.action == FilesystemAction.RENAME:

            return 100

        return 0

    ############################################################

    def execute(
        self,
        context: ToolContext,
    ) -> ToolResult:

        parsed = self.parser.parse(

            context.command

        )

        if parsed is None:

            return ToolResult(

                success=False,

                message="I couldn't understand the rename request.",

            )

        source = PathUtils.to_absolute(

            parsed.source

        )

        destination = PathUtils.to_absolute(

            parsed.destination

        )

        ########################################################

        if not self.manager.exists(source):

            return ToolResult(

                success=False,

                message=f"'{parsed.source}' does not exist.",

            )

        ########################################################

        success = self.manager.rename(

            source,

            destination,

        )

        if success:

            return ToolResult(

                success=True,

                message=f"Renamed '{parsed.source}' to '{parsed.destination}'.",

            )

        return ToolResult(

            success=False,

            message="Rename failed.",

        )