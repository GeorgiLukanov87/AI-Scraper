# main.py

import logging

from config.config import config_url, OPENAI_API_KEY, RESULT_FILENAME
from config.logger_setup import configure_logger
from core.process_article import process_article


if __name__ == "__main__":
    configure_logger()
    logging.info("Program started.")

    url = config_url
    process_article(url, OPENAI_API_KEY, RESULT_FILENAME)

    logging.info("Program finished.\n")
