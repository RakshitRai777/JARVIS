from abc import ABC


class BaseService(ABC):
    """
    Base class for every JARVIS service.
    """

    def __init__(self, name: str):
        self.name = name
        self.initialized = False
        self.running = False

    def initialize(self):
        """
        Prepare the service.
        """
        self.initialized = True

    def start(self):
        """
        Start the service.
        """
        self.running = True

    def stop(self):
        """
        Stop the service.
        """
        self.running = False

    def health_check(self) -> bool:
        """
        Return True if service is healthy.
        """
        return self.running