from __future__ import annotations

from ai.core.service_container import ServiceContainer

from ai.desktop.mouse import Mouse
from ai.desktop.window_manager import WindowManager

from ai.tools.vision.vision_manager import VisionManager


class Bootstrap:
    """
    Builds and wires the JARVIS application.

    This is the Composition Root.

    Every shared service is created exactly once
    and registered in the ServiceContainer.
    """

    ############################################################

    def __init__(self):

        self.container = ServiceContainer()

    ############################################################

    def build(self) -> ServiceContainer:

        ########################################################
        # Desktop
        ########################################################

        mouse = Mouse()

        window_manager = WindowManager()

        ########################################################
        # Vision
        ########################################################

        vision = VisionManager()

        ########################################################
        # Register Services
        ########################################################

        self.container.register(mouse)

        self.container.register(window_manager)

        self.container.register(vision)

        ########################################################

        return self.container