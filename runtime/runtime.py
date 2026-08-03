from runtime.state import RuntimeState
from runtime.service_registry import ServiceRegistry
from runtime.event_bus import EventBus
from runtime.lifecycle import LifecycleManager
from runtime.health import HealthMonitor


class Runtime:

    def __init__(self):

        self.state = RuntimeState()

        self.services = ServiceRegistry()

        self.events = EventBus()

        self.lifecycle = LifecycleManager()

        self.health = HealthMonitor()


runtime = Runtime()