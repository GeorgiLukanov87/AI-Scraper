# config/logger_setup.py

import logging
from config.config import LOG_FILENAME


def configure_logger(log_file: str = LOG_FILENAME) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
