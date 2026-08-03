from runtime.runtime import runtime
from runtime.base_service import BaseService

from ai.memory.memory_service import MemoryService
from utils.logger import logger


class LoggerService(BaseService):

    def __init__(self):
        super().__init__("Logger")


def on_ready():
    logger.info("EVENT -> System Ready")


_initialized = False


def initialize_runtime():
    """
    Initialize the complete JARVIS runtime.

    Safe to call multiple times.
    """

    global _initialized

    if _initialized:
        return

    runtime.state.start()
    runtime.state.initialize()

    logger_service = LoggerService()
    memory_service = MemoryService()

    runtime.services.register("logger", logger_service)
    runtime.services.register("memory", memory_service)

    runtime.lifecycle.register(logger_service)
    runtime.lifecycle.register(memory_service)

    runtime.health.register(logger_service)
    runtime.health.register(memory_service)

    runtime.events.subscribe(
        "system.ready",
        on_ready
    )

    runtime.lifecycle.initialize()
    runtime.lifecycle.start()

    logger.info("=" * 60)
    logger.info("Starting JARVIS")
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

    _initialized = True