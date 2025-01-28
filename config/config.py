# config/config.py

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API key for OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

config_url = "https://en.wikipedia.org/wiki/Talk:Image"
# config_url = "https://www.bbc.com/news/world-us-canada-59703761"
# config_url = "https://en.wikipedia.org/wiki/Main_Page"

# Default settings
RESULT_FILENAME = "result.txt"
LOG_FILENAME = "app.log"
