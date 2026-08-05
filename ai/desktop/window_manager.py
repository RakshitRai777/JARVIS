from __future__ import annotations

from typing import List

import pygetwindow as gw

from ai.desktop.window import Window


class WindowManager:
    """
    Discovers desktop windows.

    Responsibilities
    ----------------
    • List windows
    • Find windows
    • Active window
    • Check existence

    Does NOT manipulate windows.
    That is the responsibility of Window.
    """

    ############################################################

    def list(
        self,
        include_hidden: bool = False,
    ) -> List[Window]:

        windows = []

        for native in gw.getAllWindows():

            if not include_hidden:

                if not native.title.strip():

                    continue

            windows.append(

                Window(native)

            )

        return windows

    ############################################################

    def find(
        self,
        title: str,
    ) -> Window | None:

        target = title.lower()

        for window in self.list():

            if target in window.title.lower():

                return window

        return None

    ############################################################

    def exists(
        self,
        title: str,
    ) -> bool:

        return self.find(title) is not None

    ############################################################

    def active(
        self,
    ) -> Window | None:

        native = gw.getActiveWindow()

        if native is None:

            return None

        return Window(native)