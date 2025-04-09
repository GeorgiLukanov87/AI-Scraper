# prompts/prompts.py

def generate_prompt(article_text: str, max_words_count: int) -> str:
    return (f"Analyze the following article and generate a title and a short summary (around +- {max_words_count} words) "
            f"about the most important in the article. Article: {article_text}.")
