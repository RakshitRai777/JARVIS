from __future__ import annotations

import ctypes


class LockScreen:
    """
    Windows lock screen utility.

    Responsibilities
    ----------------
    • Lock the current workstation
    """

    ############################################################

    def lock(self) -> bool:

        ctypes.windll.user32.LockWorkStation()

        return True