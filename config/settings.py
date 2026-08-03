import os
from pathlib import Path

from dotenv import load_dotenv

# Load .env
load_dotenv()


class Settings:
    """
    Global configuration for JARVIS.
    """

    APP_NAME = "JARVIS"

    VERSION = "3.0.0"

    DEBUG = os.getenv("DEBUG", "False").lower() == "true"

    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

    MODEL_NAME = os.getenv(
        "MODEL_NAME",
        "llama-3.3-70b-versatile"
    )

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    VOICE_ENABLED = os.getenv(
        "VOICE_ENABLED",
        "True"
    ).lower() == "true"

    VISION_ENABLED = os.getenv(
        "VISION_ENABLED",
        "False"
    ).lower() == "true"

    MEMORY_ENABLED = os.getenv(
        "MEMORY_ENABLED",
        "False"
    ).lower() == "true"

    BASE_DIR = Path(__file__).resolve().parent.parent

    LOG_DIR = BASE_DIR / "logs"


settings = Settings()