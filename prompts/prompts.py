# prompts/prompts.py

def generate_prompt(article_text: str, max_words_count: int) -> str:
    return f"""
    Analyze the following article and generate a title and a short summary 
    (max {max_words_count} words) about the most important in the article:

    Article: {article_text}
    """
