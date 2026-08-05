from __future__ import annotations

import pyautogui


class Keyboard:
    """
    Low-level keyboard controller.

    Responsibilities
    ----------------
    • Type text
    • Press keys
    • Hold keys
    • Release keys
    • Execute hotkeys

    This class contains ONLY keyboard operations.
    """

    ############################################################

    def __init__(self):

        pyautogui.FAILSAFE = True

        pyautogui.PAUSE = 0.1

    ############################################################

    def type(
        self,
        text: str,
        interval: float = 0.02,
    ) -> None:

        pyautogui.write(

            text,

            interval=interval,

        )

    ############################################################

    def press(
        self,
        key: str,
    ) -> None:

        pyautogui.press(

            key,

        )

    ############################################################

    def key_down(
        self,
        key: str,
    ) -> None:

        pyautogui.keyDown(

            key,

        )

    ############################################################

    def key_up(
        self,
        key: str,
    ) -> None:

        pyautogui.keyUp(

            key,

        )

    ############################################################

    def hotkey(
        self,
        *keys: str,
    ) -> None:

        pyautogui.hotkey(

            *keys,

        )