from dataclasses import dataclass, field
from typing import Any


@dataclass
class RuntimeState:
    """
    Represents the live runtime state of J.A.R.V.I.S.

    This object is updated continuously while
    workflows are executing.
    """

    ############################################################
    # Current execution
    ############################################################

    current_workflow: str | None = None

    current_step: str | None = None

    ############################################################
    # Desktop state
    ############################################################

    current_application: str | None = None

    current_window: str | None = None

    ############################################################
    # Last execution
    ############################################################

    last_action: str | None = None

    last_tool: str | None = None

    last_result: Any = None

    last_command: str | None = None

    ############################################################
    # Vision
    ############################################################

    last_screenshot: Any = None

    last_ocr: Any = None

    ############################################################
    # Variables
    ############################################################

    variables: dict[str, Any] = field(default_factory=dict)

    ############################################################

    def clear(self) -> None:
        """
        Reset the runtime state.
        """
        self.current_workflow = None
        self.current_step = None
        self.current_application = None
        self.current_window = None
        self.last_action = None
        self.last_command = None 
        self.last_tool = None
        self.last_result = None
        self.last_screenshot = None
        self.last_ocr = None
        self.variables.clear()