from ai.desktop.mouse import Mouse

from ai.tools.vision.vision_manager import VisionManager


class ClickTool:
    """
    Generic click tool.

    Works with any Locator implementation.
    """

    ############################################################

    def __init__(self):

        self.vision = VisionManager()

        self.mouse = Mouse()

    ############################################################

    def click(
        self,
        locator,
        duration: float = 0.20,
    ) -> bool:

        ########################################################
        # Locate target
        ########################################################

        result = locator.locate(

            self.vision

        )

        ########################################################

        if not result:

            return False

        ########################################################

        x, y = result.center

        ########################################################

        self.mouse.click(

            x,

            y,

            duration,

        )

        ########################################################

        return True