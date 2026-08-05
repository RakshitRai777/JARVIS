from dataclasses import dataclass

from ai.tools.filesystem.filesystem_action import FilesystemAction


@dataclass(slots=True)
class FilesystemCommand:
    """
    Represents a parsed filesystem command.
    """

    action: FilesystemAction

    target: str | None = None

    source: str | None = None

    destination: str | None = None