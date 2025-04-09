# # core/summarizer.py

from typing import Dict, List

import logging
import tiktoken

from langchain_openai import OpenAI
from prompts.prompts import generate_prompt

TOKEN_LIMIT = 4096
CHUNK_SIZE = 3500
OVERLAP = 500


def split_text_sliding_window(text: str, model="gpt-3.5-turbo") -> List[str]:
    enc = tiktoken.encoding_for_model(model)
    tokens = enc.encode(text)

    chunks = []
    start = 0
    while start < len(tokens):
        end = start + CHUNK_SIZE
        chunk = tokens[start:end]
        chunks.append(enc.decode(chunk))
        start += CHUNK_SIZE - OVERLAP

    return chunks


def summarize_chunks(chunks: List[str], api_key: str, max_words_count: int) -> List[str]:
    logging.info("Generating summaries for text chunks...")
    llm = OpenAI(openai_api_key=api_key, model="gpt-3.5-turbo-instruct")

    summaries = []
    for chunk in chunks:
        prompt = generate_prompt(chunk, max_words_count)
        response = llm.invoke(prompt)
        summaries.append(response.strip())

    return summaries


def generate_final_summary(chunks: List[str], api_key: str, max_words_count: int) -> str:
    logging.info("Merging intermediate summaries into final summary chunks...")
    llm = OpenAI(openai_api_key=api_key, model="gpt-3.5-turbo-instruct")

    merged_parts = []
    for chunk in chunks:
        prompt = generate_prompt(chunk, max_words_count)
        response = llm.invoke(prompt)
        merged_parts.append(response.strip())

    return " ".join(merged_parts)


def final_summary(summaries: List[str], api_key: str, max_words_count: int) -> Dict:
    combined_text = " ".join(summaries)
    combined_chunks = split_text_sliding_window(combined_text)
    merged_summary = generate_final_summary(combined_chunks, api_key, max_words_count)

    final_prompt = generate_prompt(merged_summary, max_words_count)
    llm = OpenAI(openai_api_key=api_key, model="gpt-3.5-turbo-instruct")
    final_response = llm.invoke(final_prompt)

    lines = final_response.strip().split("\n")
    title = lines[0].replace("Title:", "").strip() if "Title:" in lines[0] else "No Title"
    summary = ' '.join(lines[1:]).replace("Summary:", "").strip() if "Summary:" in final_response else "No Summary"

    return {"title": title, "summary": summary}


def generate_summary_and_title(article_text: str, api_key: str, max_words_count: int) -> Dict:
    try:
        logging.info("Processing article text for summarization...")
        chunks = split_text_sliding_window(article_text)
        summaries = summarize_chunks(chunks, api_key, max_words_count)
        result = final_summary(summaries, api_key, max_words_count)

        logging.info("Successfully generated title and summary.")
        return result

    except Exception as e:
        logging.error(f"Error with LLM: {e}")
        return None
