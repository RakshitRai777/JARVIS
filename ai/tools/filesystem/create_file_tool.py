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


class CreateFileTool(Tool):
    """
    Creates files on the filesystem.

    This tool relies on the
    FilesystemCommandParser for parsing.
    """

    ############################################################

    def __init__(self):

        self.manager = FileManager()

        self.parser = FilesystemCommandParser()

    ############################################################

    @property
    def name(self) -> str:

        return "Create File"

    ############################################################

    @property
    def description(self) -> str:

        return "Creates a new file."

    ############################################################

    def match_score(
        self,
        command: str,
    ) -> int:

        parsed = self.parser.parse(command)

        if parsed is None:

            return 0

        if parsed.action == FilesystemAction.CREATE_FILE:

            return 100

        return 0

    ############################################################

    def execute(
        self,
        context: ToolContext,
    ) -> ToolResult:

        parsed = self.parser.parse(context.command)

        if parsed is None:

            return ToolResult(

                success=False,

                message="I couldn't understand the file creation request.",

            )

        file_path = PathUtils.to_absolute(parsed.target)

        success = self.manager.create_file(file_path)

        if success:

            return ToolResult(

                success=True,

                message=f"File created:\n{file_path}",

                data=file_path,

            )

        return ToolResult(

            success=False,

            message=f"Failed to create file:\n{file_path}",

        )