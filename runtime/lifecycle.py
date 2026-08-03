from utils.logger import logger


class LifecycleManager:

    def __init__(self):
        self._services = []

    def register(self, service):
        self._services.append(service)

    def initialize(self):

        logger.info("Initializing services...")

        for service in self._services:
            service.initialize()
            logger.info(f"Initialized: {service.name}")

    def start(self):

        logger.info("Starting services...")

        for service in self._services:
            service.start()
            logger.info(f"Started: {service.name}")

    def stop(self):

        logger.info("Stopping services...")

        for service in reversed(self._services):
            service.stop()
            logger.info(f"Stopped: {service.name}")