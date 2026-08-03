from runtime.state import RuntimeState
from runtime.service_registry import ServiceRegistry


class Runtime:
    """
    Core runtime object.
    """

    def __init__(self):
        self.state = RuntimeState()
        self.services = ServiceRegistry()


runtime = Runtime()