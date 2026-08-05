from ai.events.event import Event
from ai.events.event_type import EventType


class EventManager:
    """
    Central gateway for all events entering JARVIS.

    Responsibilities
    ----------------
    • Validate incoming events
    • Dispatch events to the Brain
    • (Future)
        - Logging
        - Event Queue
        - Event Bus
        - Background Tasks
        - Scheduling
    """

    ############################################################

    def __init__(self):

        self._brain = None

    ############################################################

    def set_brain(
        self,
        brain,
    ):

        """
        Registers the Brain.

        We avoid circular imports by injecting
        the Brain after construction.
        """

        self._brain = brain

    ############################################################

    def process(
        self,
        event: Event,
    ):

        """
        Processes an incoming event.
        """

        if self._brain is None:

            raise RuntimeError(

                "Brain has not been registered."

            )

        ########################################################
        # User Input
        ########################################################

        if event.event_type == EventType.USER_INPUT:

            return self._brain.handle_input(

                event.payload

            )

        ########################################################

        raise NotImplementedError(

            f"No handler for event type "

            f"{event.event_type.value}"

        )