# core/summarizer.py

from typing import Dict

from langchain_openai import OpenAI
import logging

from prompts.prompts import generate_prompt


def generate_summary_and_title(article_text: str, api_key: str, max_words_count: int) -> Dict:
    try:
        logging.info("Generating title and summary using OpenAI LLM.")
        llm = OpenAI(temperature=0.7, openai_api_key=api_key)

        prompt = generate_prompt(article_text, max_words_count)
        response = llm.invoke(prompt)

        lines = response.strip().split('\n')
        title = lines[0].replace("Title:", "").strip() if "Title:" in lines[0] else "No Title"
        summary = ' '.join(lines[1:]).replace("Summary:", "").strip() if "Summary:" in response else "No Summary"

        logging.info("Successfully generated title and summary.")
        return {"title": title, "summary": summary}

    except Exception as e:
        logging.error(f"Error with LLM: {e}")
        return None
