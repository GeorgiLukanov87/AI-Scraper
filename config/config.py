# config/config.py

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API key for OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# List of urls for scrapping
config_url_list = [
    "https://en.wikipedia.org/wiki/Talk:Image",
    "https://www.bbc.com/news/world-us-canada-59703761",
    "https://en.wikipedia.org/wiki/Main_Page",
    "https://www.olx.bg/"
]

config_url = config_url_list[0]

# Default settings
RESULT_FILENAME = "result.txt"
LOG_FILENAME = "app.log"
