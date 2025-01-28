# core/article_fetcher.py

import requests
from bs4 import BeautifulSoup
import logging


def fetch_article(url):
    try:
        logging.info(f"Fetching article from URL: {url}")
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('title').get_text(strip=True)
        paragraphs = soup.find_all('p')
        content = ' '.join([p.get_text(strip=True) for p in paragraphs])

        print(f'Scrapped data: \n{content}\n')
        logging.info(f"Successfully fetched article: {title}")
        return {"title": title, "content": content}

    except Exception as e:
        logging.error(f"Error fetching the page: {e}")
        return None
