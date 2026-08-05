import re

from ai.tools.intent.tool_intent import ToolIntent


class ToolIntentClassifier:
    """
    Classifies whether a user request is intended
    for the Tool System.

    It does NOT choose the exact tool.

    It only determines the tool category.

    Example
    -------

    "Calculate 5+5"
        -> CALCULATOR

    "Open Chrome"
        -> BROWSER

    "Take a screenshot"
        -> UTILITY
    """

    ############################################################

    SYSTEM_KEYWORDS = {

        "shutdown",
        "restart",
        "sleep",
        "lock",
        "log off",

    }

    ############################################################

    BROWSER_KEYWORDS = {

        "open",
        "browse",
        "search",
        "visit",
        "website",
        "google",
        "youtube",
        "url",
        ".com",
        ".org",
        ".net",
        ".io",
        ".dev",
        ".ai",


    }

    ############################################################

    FILE_KEYWORDS = {

        "create",
        "delete",
        "copy",
        "move",
        "rename",
        "folder",
        "file",

    }

    ############################################################

    MEDIA_KEYWORDS = {

        "play",
        "pause",
        "resume",
        "stop music",
        "volume",
        "mute",
        "unmute",
        "sound",
        "audio",

    }

    ############################################################

    DEVELOPMENT_KEYWORDS = {

        "vs code",
        "vscode",
        "visual studio",
        "pycharm",
        "terminal",
        "cmd",
        "powershell",

    }

    ############################################################

    UTILITY_KEYWORDS = {

        "screenshot",
        "capture",
        "clipboard",
        "camera",

    }

    ############################################################

    def classify(
        self,
        text: str,
    ) -> ToolIntent:

        text = text.lower().strip()

        ########################################################
        # Calculator
        ########################################################

        if self._is_math(text):

            return ToolIntent.CALCULATOR

        ########################################################
        # System
        ########################################################

        if any(
            word in text
            for word in self.SYSTEM_KEYWORDS
        ):

            return ToolIntent.SYSTEM

        ########################################################
        # Browser
        ########################################################

        if any(
            word in text
            for word in self.BROWSER_KEYWORDS
        ):

            return ToolIntent.BROWSER

        ########################################################
        # Files
        ########################################################

        if any(
            word in text
            for word in self.FILE_KEYWORDS
        ):

            return ToolIntent.FILESYSTEM

        ########################################################
        # Media
        ########################################################

        if any(
            word in text
            for word in self.MEDIA_KEYWORDS
        ):

            return ToolIntent.MEDIA

        ########################################################
        # Development
        ########################################################

        if any(
            word in text
            for word in self.DEVELOPMENT_KEYWORDS
        ):

            return ToolIntent.DEVELOPMENT

        ########################################################
        # Utility
        ########################################################

        if any(
            word in text
            for word in self.UTILITY_KEYWORDS
        ):

            return ToolIntent.UTILITY

        ########################################################

        return ToolIntent.NONE

    ############################################################

    def _is_math(
        self,
        text: str,
    ) -> bool:

        text = text.lower().strip()

        math_words = {

            "calculate",
            "solve",
            "compute",
            "evaluate",

        }

        if any(
            text.startswith(word)
            for word in math_words
        ):

            return True

        if re.fullmatch(
            r"[0-9\s\+\-\*/%\(\)\.]+",
            text,
        ):

            return True

        return False