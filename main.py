# main.py

from config.config import config_url, OPENAI_API_KEY, RESULT_FILENAME
from config.logger_setup import configure_logger
from core.process_article import process_article

if __name__ == "__main__":
    configure_logger()
    url = config_url[1]

    # url = "https://en.wikipedia.org/wiki/bulgaria"
    # '''    List of urls:
    #   0:  "https://en.wikipedia.org/wiki/england",
    #   1:  "https://www.bbc.com/news/world-us-canada-59703761",
    #   2:  "https://en.wikipedia.org/wiki/Main_Page",
    #   3:  "https://www.olx.bg/",
    #   4:  "https://georgilukanov87.pythonanywhere.com/",
    #   '''

    process_article(url, OPENAI_API_KEY, RESULT_FILENAME)
