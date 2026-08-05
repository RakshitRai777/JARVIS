from enum import Enum


class FilesystemAction(str, Enum):
    """
    Supported filesystem actions.
    """

    ############################################################

    CREATE_FOLDER = "create_folder"

    CREATE_FILE = "create_file"

    DELETE = "delete"

    RENAME = "rename"

    COPY = "copy"

    MOVE = "move"

    LIST_DIRECTORY = "list_directory"

    OPEN_FILE = "open_file"

    OPEN_FOLDER = "open_folder"