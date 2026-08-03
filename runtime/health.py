from dataclasses import dataclass
from datetime import datetime


@dataclass
class HealthStatus:
    service: str
    healthy: bool
    running: bool
    initialized: bool
    timestamp: datetime


class HealthMonitor:

    def __init__(self):
        self._services = []

    def register(self, service):
        self._services.append(service)

    def check_all(self):

        reports = []

        for service in self._services:

            report = HealthStatus(
                service=service.name,
                healthy=service.health_check(),
                running=service.running,
                initialized=service.initialized,
                timestamp=datetime.now()
            )

            reports.append(report)

        return reports