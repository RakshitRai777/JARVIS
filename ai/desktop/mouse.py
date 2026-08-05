from __future__ import annotations

from typing import Tuple

import pyautogui


class Mouse:
    """
    Low-level mouse controller.

    Responsibilities
    ----------------
    • Move cursor
    • Left click
    • Right click
    • Double click
    • Middle click
    • Drag
    • Scroll
    • Read cursor position

    This class contains ONLY desktop mouse operations.
    It knows nothing about Vision, AI, Actions or Workflows.
    """

    ############################################################

    def __init__(self):

        pyautogui.FAILSAFE = True

        pyautogui.PAUSE = 0.1

    ############################################################

    def position(
        self,
    ) -> Tuple[int, int]:

        return pyautogui.position()

    ############################################################

    def move(
        self,
        x: int,
        y: int,
        duration: float = 0.20,
    ) -> None:

        pyautogui.moveTo(

            x,

            y,

            duration=duration,

        )

    ############################################################

    def click(
        self,
        x: int | None = None,
        y: int | None = None,
        duration: float = 0.20,
    ) -> None:

        if x is not None and y is not None:

            self.move(

                x,

                y,

                duration,

            )

        pyautogui.click()

    ############################################################

    def right_click(
        self,
        x: int | None = None,
        y: int | None = None,
        duration: float = 0.20,
    ) -> None:

        if x is not None and y is not None:

            self.move(

                x,

                y,

                duration,

            )

        pyautogui.rightClick()

    ############################################################

    def double_click(
        self,
        x: int | None = None,
        y: int | None = None,
        duration: float = 0.20,
    ) -> None:

        if x is not None and y is not None:

            self.move(

                x,

                y,

                duration,

            )

        pyautogui.doubleClick()

    ############################################################

    def middle_click(
        self,
        x: int | None = None,
        y: int | None = None,
        duration: float = 0.20,
    ) -> None:

        if x is not None and y is not None:

            self.move(

                x,

                y,

                duration,

            )

        pyautogui.middleClick()

    ############################################################

    def drag(
        self,
        start_x: int,
        start_y: int,
        end_x: int,
        end_y: int,
        duration: float = 0.50,
    ) -> None:

        self.move(

            start_x,

            start_y,

            0,

        )

        pyautogui.dragTo(

            end_x,

            end_y,

            duration=duration,

            button="left",

        )

    ############################################################

    def scroll(
        self,
        clicks: int,
    ) -> None:

        pyautogui.scroll(

            clicks

        )