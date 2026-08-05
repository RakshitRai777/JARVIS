from __future__ import annotations

import pyperclip


class Clipboard:
    """
    Clipboard utility.

    Responsibilities
    ----------------
    • Read clipboard contents
    • Write clipboard contents

    This class is a low-level desktop utility.
    """

    ############################################################

    def get(self) -> str | None:
        """
        Read text from the system clipboard.
        """

        return pyperclip.paste()

    ############################################################

    def set(
        self,
        text: str,
    ) -> bool:
        """
        Write text to the system clipboard.
        """

        pyperclip.copy(text)

        return True