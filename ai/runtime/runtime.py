from ai.runtime.runtime_state import RuntimeState


class Runtime:
    """
    Central runtime controller.

    Owns the live RuntimeState and provides
    methods for updating and resetting it.

    Future responsibilities
    -----------------------
    • Sessions
    • History
    • Variables
    • Recovery
    """

    ############################################################

    def __init__(self):

        self.state = RuntimeState()

    ############################################################

    def reset(self):

        """
        Reset runtime state.
        """

        self.state.clear()

    ############################################################

    def set_workflow(
        self,
        workflow: str,
    ):

        self.state.current_workflow = workflow

    ############################################################

    def set_step(
        self,
        step: str,
    ):

        self.state.current_step = step

    ############################################################

    def set_application(
        self,
        application: str,
    ):

        self.state.current_application = application

    ############################################################

    def set_window(
        self,
        window: str,
    ):

        self.state.current_window = window

    ############################################################

    def set_last_action(
        self,
        action: str,
    ):

        self.state.last_action = action

    ############################################################

    def set_last_tool(
        self,
        tool: str,
    ):

        self.state.last_tool = tool

    ############################################################

    def set_last_result(
        self,
        result,
    ):

        self.state.last_result = result

    ############################################################
    def update_from_execution(
            self,
            step,
            result,
        ):
            """
            Update runtime after a successful step execution.
            """
    
            self.state.last_action = step.action
    
            self.state.last_result = result
    
            ########################################################
            # Store original command
            ########################################################
    
            command = step.parameters.get(
    
                "command",
    
                None,
    
            )

            self.state.last_command = command
    
            self.state.last_tool = None
            