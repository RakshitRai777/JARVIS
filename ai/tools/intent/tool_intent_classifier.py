import re

from ai.tools.intent.tool_intent import ToolIntent


class ToolIntentClassifier:
    """
    Classifies a user's command into a high-level
    tool category.

    The ToolResolver later selects the best tool
    within that category.
    """

    ############################################################
    # Keyword Groups
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

        "open website",
        "browse",
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

    DESKTOP_KEYWORDS = {

        "screenshot",
        "capture",
        "clipboard",
        "camera",

    }

    ############################################################

    VISION_PREFIXES = (

        "click ",
        "click on ",
        "press ",
        "select ",
        "find ",
        "locate ",
        "where is ",
        "read screen",
        "explain screen",
        "describe screen",
        "summarize screen",

    )

    ############################################################

    VISION_KEYWORDS = {

        "screen",
        "ocr",
        "extract text",
        "scan screen",
        "understand screen",
        "what am i looking at",

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
        # Vision / Desktop Automation
        ########################################################

        if text.startswith(self.VISION_PREFIXES):

            return ToolIntent.VISION

        if any(
            keyword in text
            for keyword in self.VISION_KEYWORDS
        ):

            return ToolIntent.VISION

        ########################################################
        # System
        ########################################################

        if any(
            keyword in text
            for keyword in self.SYSTEM_KEYWORDS
        ):

            return ToolIntent.SYSTEM

        ########################################################
        # Browser
        ########################################################

        if any(
            keyword in text
            for keyword in self.BROWSER_KEYWORDS
        ):

            return ToolIntent.BROWSER

        ########################################################
        # Filesystem
        ########################################################

        if any(
            keyword in text
            for keyword in self.FILE_KEYWORDS
        ):

            return ToolIntent.FILESYSTEM

        ########################################################
        # Desktop
        ########################################################

        if any(
            keyword in text
            for keyword in self.DESKTOP_KEYWORDS
        ):

            return ToolIntent.DESKTOP

        ########################################################
        # Media
        ########################################################

        if any(
            keyword in text
            for keyword in self.MEDIA_KEYWORDS
        ):

            return ToolIntent.MEDIA

        ########################################################
        # Development
        ########################################################

        if any(
            keyword in text
            for keyword in self.DEVELOPMENT_KEYWORDS
        ):

            return ToolIntent.DEVELOPMENT

        ########################################################

        return ToolIntent.NONE

    ############################################################

    def _is_math(
        self,
        text: str,
    ) -> bool:

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
            r"[0-9\s+\-*/%.()]+",
            text,
        ):

            return True

        return False