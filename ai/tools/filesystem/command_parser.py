import re

from ai.tools.filesystem.filesystem_command import (
    FilesystemCommand,
)

from ai.tools.filesystem.filesystem_action import (
    FilesystemAction,
)


class FilesystemCommandParser:
    """
    Parses natural language filesystem commands.

    This parser converts user text into a
    structured FilesystemCommand.

    Future versions can support much more
    natural language without changing the
    filesystem tools.
    """

    ############################################################

    def parse(
        self,
        command: str,
    ) -> FilesystemCommand | None:

        text = command.strip()

        lower = text.lower()

        ########################################################
        # CREATE FOLDER
        ########################################################

        patterns = [

            r"^create folder (.+)$",

            r"^make folder (.+)$",

            r"^new folder (.+)$",

            r"^create a folder called (.+)$",

            r"^create a folder named (.+)$",

            r"^make a folder called (.+)$",

            r"^make a folder named (.+)$",

        ]

        for pattern in patterns:

            match = re.match(pattern, lower)

            if match:

                return FilesystemCommand(

                    action=FilesystemAction.CREATE_FOLDER,

                    target=text[match.start(1):],

                )

        ########################################################
        # CREATE FILE
        ########################################################

        patterns = [

            r"^create file (.+)$",

            r"^new file (.+)$",

            r"^make file (.+)$",

            r"^create a file called (.+)$",

            r"^create a file named (.+)$",

        ]

        for pattern in patterns:

            match = re.match(pattern, lower)

            if match:

                return FilesystemCommand(

                    action=FilesystemAction.CREATE_FILE,

                    target=text[match.start(1):],

                )

        ########################################################
        # DELETE
        ########################################################

        patterns = [

            r"^delete (.+)$",

            r"^remove (.+)$",

            r"^delete file (.+)$",

            r"^delete folder (.+)$",

            r"^remove file (.+)$",

            r"^remove folder (.+)$",

        ]

        for pattern in patterns:

            match = re.match(pattern, lower)

            if match:

                return FilesystemCommand(

                    action=FilesystemAction.DELETE,

                    target=text[match.start(1):],

                )

        ########################################################
        # RENAME
        ########################################################

        match = re.match(

            r"^rename (.+) to (.+)$",

            lower,

        )

        if match:

            source = text[match.start(1):match.end(1)]

            destination = text[match.start(2):]

            return FilesystemCommand(

                action=FilesystemAction.RENAME,

                source=source,

                destination=destination,

            )

        ########################################################

        return None