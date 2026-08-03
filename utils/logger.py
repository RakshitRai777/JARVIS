import logging
from pathlib import Path

# --------------------------------------------------
# Logs Directory
# --------------------------------------------------

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "jarvis.log"

# --------------------------------------------------
# Global Logger
# --------------------------------------------------

logger = logging.getLogger("JARVIS")

logger.setLevel(logging.INFO)

# Prevent duplicate messages from propagating
logger.propagate = False

# --------------------------------------------------
# Configure only once
# --------------------------------------------------

if not logger.handlers:

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
    )

    file_handler = logging.FileHandler(
        LOG_FILE,
        encoding="utf-8"
    )

    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()

    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)