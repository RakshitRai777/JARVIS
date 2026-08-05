from dataclasses import dataclass


@dataclass
class VisionResult:
    """
    Result produced by the Vision system.
    """

    ############################################################

    success: bool

    ############################################################

    text: str = ""

    ############################################################

    screenshot_path: str = ""

    ############################################################

    error: str = ""