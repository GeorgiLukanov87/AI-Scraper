# core/file_manager.py

import os
import logging
from datetime import datetime

from config.config import RESULT_FILENAME


def increment_records_count(filename: str) -> int:
    # Read the current count from the file if it exists
    records_count = 0
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith("Record"):
                    records_count += 1

    # Increment the count for the new record
    records_count += 1
    return records_count


def save_results_to_file(title: str, summary: str, url: str, filename: str = RESULT_FILENAME) -> None:
    try:
        # Get current timestamp
        timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        records_count = increment_records_count(filename=RESULT_FILENAME)

        # Append the new record to the file
        with open(filename, "a", encoding="utf-8") as file:
            file.write(f"Record {records_count}\n")
            file.write(f"Generated on: {timestamp}\n")
            file.write(f"Url: {url}\n")
            file.write(f"Generated Title:\n{title}\n")
            file.write(f"Generated Summary:\n{summary}\n")
            file.write("=" * 100 + "\n")

        logging.info(f"Results saved to file: {filename} (Record {records_count})")
    except Exception as e:
        logging.error(f"Error saving results to file: {e}")
