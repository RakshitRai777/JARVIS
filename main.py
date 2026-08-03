from config.settings import settings

from runtime.runtime import runtime
from runtime.base_service import BaseService

from utils.logger import logger

from ai.memory.memory_service import MemoryService


class LoggerService(BaseService):

    def __init__(self):
        super().__init__("Logger")


def on_ready():
    logger.info("EVENT -> System Ready")


def main():

    runtime.state.start()
    runtime.state.initialize()

    logger_service = LoggerService()
    memory_service = MemoryService()

    # Register services
    runtime.services.register(
        "logger",
        logger_service
    )

    runtime.services.register(
        "memory",
        memory_service
    )

    # Lifecycle
    runtime.lifecycle.register(logger_service)
    runtime.lifecycle.register(memory_service)

    # Health
    runtime.health.register(logger_service)
    runtime.health.register(memory_service)

    runtime.events.subscribe(
        "system.ready",
        on_ready
    )

    logger.info("Initializing services...")
    runtime.lifecycle.initialize()

    logger.info("Starting services...")
    runtime.lifecycle.start()

    logger.info("=" * 60)
    logger.info(f"Starting {settings.APP_NAME}")
    logger.info(f"Services : {list(runtime.services.all().keys())}")

    runtime.events.publish("system.ready")

    logger.info("Health Report")

    for report in runtime.health.check_all():

        logger.info(
            f"{report.service} | "
            f"Healthy={report.healthy} | "
            f"Running={report.running} | "
            f"Initialized={report.initialized}"
        )

    logger.info("=" * 60)


if __name__ == "__main__":
    main()