import pyautogui


class MouseManager:
    """
    Central manager for mouse operations.

    Responsibilities
    ----------------
    • Move cursor
    • Left click
    • Right click
    • Double click
    • Drag
    • Scroll
    • Get cursor position

    Higher-level tools should use this class
    instead of calling pyautogui directly.
    """

    ############################################################

    def __init__(self):

        # Safety feature:
        # Moving the mouse to the top-left corner
        # immediately aborts automation.
        pyautogui.FAILSAFE = True

        # Small delay after each action.
        pyautogui.PAUSE = 0.1

    ############################################################

    def move_to(
        self,
        x: int,
        y: int,
        duration: float = 0.2,
    ) -> bool:
        """
        Move mouse to screen coordinates.
        """

        try:

            pyautogui.moveTo(

                x,

                y,

                duration=duration,

            )

            return True

        except Exception:

            return False

    ############################################################

    def left_click(
        self,
        x: int | None = None,
        y: int | None = None,
    ) -> bool:
        """
        Left mouse click.
        """

        try:

            if x is not None and y is not None:

                pyautogui.click(

                    x,

                    y,

                    button="left",

                )

            else:

                pyautogui.click(

                    button="left",

                )

            return True

        except Exception:

            return False

    ############################################################

    def right_click(
        self,
        x: int | None = None,
        y: int | None = None,
    ) -> bool:
        """
        Right mouse click.
        """

        try:

            if x is not None and y is not None:

                pyautogui.rightClick(

                    x,

                    y,

                )

            else:

                pyautogui.rightClick()

            return True

        except Exception:

            return False

    ############################################################

    def double_click(
        self,
        x: int | None = None,
        y: int | None = None,
    ) -> bool:
        """
        Double left click.
        """

        try:

            if x is not None and y is not None:

                pyautogui.doubleClick(

                    x,

                    y,

                )

            else:

                pyautogui.doubleClick()

            return True

        except Exception:

            return False

    ############################################################

    def drag(
        self,
        start_x: int,
        start_y: int,
        end_x: int,
        end_y: int,
        duration: float = 0.5,
    ) -> bool:
        """
        Drag from one point to another.
        """

        try:

            pyautogui.moveTo(

                start_x,

                start_y,

            )

            pyautogui.dragTo(

                end_x,

                end_y,

                duration=duration,

                button="left",

            )

            return True

        except Exception:

            return False

    ############################################################

    def scroll(
        self,
        amount: int,
    ) -> bool:
        """
        Scroll vertically.

        Positive = up
        Negative = down
        """

        try:

            pyautogui.scroll(

                amount

            )

            return True

        except Exception:

            return False

    ############################################################

    def position(
        self,
    ) -> tuple[int, int]:
        """
        Returns current cursor position.
        """

        return pyautogui.position()