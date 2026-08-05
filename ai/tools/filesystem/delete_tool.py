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


class DeleteTool(Tool):
    """
    Deletes files and folders.
    """

    ############################################################

    def __init__(self):

        self.manager = FileManager()

        self.parser = FilesystemCommandParser()

    ############################################################

    @property
    def name(self) -> str:

        return "Delete"

    ############################################################

    @property
    def description(self) -> str:

        return "Deletes files and folders."

    ############################################################

    def match_score(
        self,
        command: str,
    ) -> int:

        parsed = self.parser.parse(command)

        if parsed is None:

            return 0

        if parsed.action == FilesystemAction.DELETE:

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

                message="I couldn't understand the delete request.",

            )

        target = PathUtils.to_absolute(

            parsed.target

        )

        ########################################################

        if not self.manager.exists(target):

            return ToolResult(

                success=False,

                message=f"'{parsed.target}' does not exist.",

            )

        ########################################################

        success = self.manager.delete(

            target

        )

        if success:

            return ToolResult(

                success=True,

                message=f"Deleted '{parsed.target}'.",

            )

        return ToolResult(

            success=False,

            message="Delete failed.",

        )