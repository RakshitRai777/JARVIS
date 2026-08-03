from utils.logger import logger
from config.settings import settings
from runtime.runtime import runtime


class LoggerService:
    pass


def main():

    runtime.state.start()
    runtime.state.initialize()

    runtime.services.register("logger", LoggerService())

    logger.info("=" * 60)
    logger.info(f"Starting {settings.APP_NAME}")
    logger.info(f"Services : {list(runtime.services.all().keys())}")
    logger.info("=" * 60)


if __name__ == "__main__":
    main()