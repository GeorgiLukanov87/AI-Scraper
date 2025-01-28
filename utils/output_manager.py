# utils/output_manager.py

def print_results(article_title: str, generated_title: str, generated_summary: str) -> None:
    print("Original Title:\n", article_title)
    print("Generated Title:\n", generated_title)
    print("Generated Summary:\n", generated_summary)


def print_error(message: str) -> None:
    print("\nError:", message)
