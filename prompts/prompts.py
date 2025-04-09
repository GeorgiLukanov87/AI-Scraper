# prompts/prompts.py

def generate_prompt(article_text: str, max_words_count: int) -> str:
    return (f"Analyze the following article and "
            f" a title and a short summary "
            f"(around +- {max_words_count} words)"
            f"about the most important in the article."
            f" Article: {article_text}.")
