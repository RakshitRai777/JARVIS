class ServiceRegistry:
    """
    Registers and provides access to application services.
    """

    def __init__(self):
        self._services = {}

    def register(self, name: str, service):
        if name in self._services:
            raise ValueError(f"Service '{name}' already registered.")

        self._services[name] = service

    def get(self, name: str):
        if name not in self._services:
            raise KeyError(f"Service '{name}' not found.")

        return self._services[name]

    def exists(self, name: str) -> bool:
        return name in self._services

    def all(self):
        return self._services