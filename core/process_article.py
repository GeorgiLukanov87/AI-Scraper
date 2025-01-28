# core/process_article.py

from core.article_fetcher import fetch_article
from core.file_manager import save_results_to_file
from core.summarizer import generate_summary_and_title
from utils.output_manager import print_results, print_error


def process_article(url: str, api_key: str, result_filename: str) -> None:
    article = fetch_article(url)

    if article:
        result = generate_summary_and_title(article["content"], api_key, max_words_count=50)

        if result:
            print_results(article["title"], result["title"], result["summary"])
            save_results_to_file(result["title"], result["summary"], url, filename=result_filename)
        else:
            print_error("Failed to generate title and summary.")
    else:
        print_error("Failed to fetch the article.")
