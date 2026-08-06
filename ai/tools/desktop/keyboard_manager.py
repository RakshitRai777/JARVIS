import pyautogui


class KeyboardManager:
    """
    Central manager for keyboard operations.

    Responsibilities
    ----------------
    • Type text
    • Press keys
    • Hold keys
    • Release keys
    • Execute hotkeys

    Higher-level tools should use this class
    instead of calling pyautogui directly.
    """

    ############################################################

    def __init__(self):

        # Safety feature
        pyautogui.FAILSAFE = True

        # Small delay after each action
        pyautogui.PAUSE = 0.1

    ############################################################

    def type_text(
        self,
        text: str,
        interval: float = 0.02,
    ) -> bool:
        """
        Types text naturally.
        """

        try:

            pyautogui.write(

                text,

                interval=interval,

            )

            return True

        except Exception:

            return False

    ############################################################
    # Backward Compatibility
    ############################################################

    def type(
        self,
        text: str,
        interval: float = 0.02,
    ) -> bool:
        """
        Legacy alias for type_text().
        """

        return self.type_text(

            text,

            interval,

        )

    ############################################################

    def press(
        self,
        key: str,
    ) -> bool:
        """
        Press a single key.
        """

        try:

            pyautogui.press(

                key,

            )

            return True

        except Exception:

            return False

    ############################################################
    # Backward Compatibility
    ############################################################

    def press_key(
        self,
        key: str,
    ) -> bool:
        """
        Legacy alias for press().
        """

        return self.press(

            key,

        )

    ############################################################

    def key_down(
        self,
        key: str,
    ) -> bool:
        """
        Hold a key down.
        """

        try:

            pyautogui.keyDown(

                key,

            )

            return True

        except Exception:

            return False

    ############################################################

    def key_up(
        self,
        key: str,
    ) -> bool:
        """
        Release a held key.
        """

        try:

            pyautogui.keyUp(

                key,

            )

            return True

        except Exception:

            return False

    ############################################################

    def hotkey(
        self,
        *keys: str,
    ) -> bool:
        """
        Execute a keyboard shortcut.

        Example:

            hotkey("ctrl", "c")
        """

        try:

            pyautogui.hotkey(

                *keys,

            )

            return True

        except Exception:

            return False