import os
from pathlib import Path

from dotenv import load_dotenv

# Load .env
load_dotenv()


class Settings:
    """
    Global configuration for JARVIS.

    Categories
    ----------
    • General
    • AI
    • Voice
    • Vision
    • Memory
    • Automation
    • Logging
    • Paths
    """

    ############################################################
    # General
    ############################################################

    APP_NAME = "JARVIS"

    VERSION = "3.0.0"

    DEBUG = os.getenv(
        "DEBUG",
        "False"
    ).lower() == "true"

    LOG_LEVEL = os.getenv(
        "LOG_LEVEL",
        "INFO"
    )

    ############################################################
    # AI
    ############################################################

    MODEL_NAME = os.getenv(
        "MODEL_NAME",
        "llama-3.3-70b-versatile"
    )

    GROQ_API_KEY = os.getenv(
        "GROQ_API_KEY"
    )

    ############################################################
    # Voice
    ############################################################

    VOICE_ENABLED = os.getenv(
        "VOICE_ENABLED",
        "True"
    ).lower() == "true"

    ############################################################
    # Vision
    ############################################################

    VISION_ENABLED = os.getenv(
        "VISION_ENABLED",
        "False"
    ).lower() == "true"

    VISION_PROFILING = os.getenv(
        "VISION_PROFILING",
        "True"
    ).lower() == "true"

    SAVE_SCREENSHOTS = os.getenv(
        "SAVE_SCREENSHOTS",
        "True"
    ).lower() == "true"

    OCR_DEBUG = os.getenv(
        "OCR_DEBUG",
        "False"
    ).lower() == "true"

    ############################################################
    # Memory
    ############################################################

    MEMORY_ENABLED = os.getenv(
        "MEMORY_ENABLED",
        "False"
    ).lower() == "true"

    ############################################################
    # Automation
    ############################################################

    DEFAULT_TIMEOUT = float(
        os.getenv(
            "DEFAULT_TIMEOUT",
            "10"
        )
    )

    MAX_RETRIES = int(
        os.getenv(
            "MAX_RETRIES",
            "1"
        )
    )

    ############################################################
    # Paths
    ############################################################

    BASE_DIR = Path(__file__).resolve().parent.parent

    LOG_DIR = BASE_DIR / "logs"

    SCREENSHOT_DIR = BASE_DIR / "screenshots"


settings = Settings()