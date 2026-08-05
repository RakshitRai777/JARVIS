from pathlib import Path

import pyautogui

from ai.tools.vision.vision_manager import VisionManager


class ClickTemplateTool:
    """
    Clicks on a template found on screen.

    Flow
    ----
    Screenshot
        ↓
    Template Matching
        ↓
    Mouse Move
        ↓
    Click
    """

    ############################################################

    def __init__(self):

        self.vision = VisionManager()

    ############################################################

    def click(
        self,
        template: str | Path,
        image_path: str | Path | None = None,
        threshold: float = 0.75,
        duration: float = 0.20,
    ) -> bool:

        ########################################################

        result = self.vision.find_template(

            template=template,

            image_path=image_path,

            threshold=threshold,

        )

        ########################################################

        if not result:

            return False

        ########################################################

        x, y = result.best_match.center

        pyautogui.moveTo(

            x,

            y,

            duration=duration,

        )

        pyautogui.click()

        ########################################################

        return True