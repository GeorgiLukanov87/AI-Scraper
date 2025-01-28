import unittest
from unittest.mock import patch
from core.process_article import process_article


class TestProcessArticle(unittest.TestCase):
    @patch("core.process_article.fetch_article")
    @patch("core.process_article.generate_summary_and_title")
    @patch("core.process_article.print_results")
    @patch("core.process_article.save_results_to_file")
    @patch("core.process_article.print_error")
    def test_process_article_success(
        self, mock_print_error, mock_save, mock_print, mock_generate, mock_fetch
    ):
        # Mock fetch_article
        mock_fetch.return_value = {"title": "Fetched Title", "content": "Fetched Content"}

        # Mock generate_summary_and_title
        mock_generate.return_value = {"title": "Generated Title", "summary": "Generated Summary"}

        process_article("https://example.com", "fake_api_key", "test_result.txt")

        mock_fetch.assert_called_once()
        mock_generate.assert_called_once()
        mock_print.assert_called_once_with("Fetched Title", "Generated Title", "Generated Summary")
        mock_save.assert_called_once()

    @patch("core.process_article.fetch_article")
    @patch("core.process_article.print_error")
    def test_process_article_fetch_failure(self, mock_print_error, mock_fetch):
        # Mock fetch_article failure
        mock_fetch.return_value = None

        process_article("https://example.com", "fake_api_key", "test_result.txt")
        mock_fetch.assert_called_once()
        mock_print_error.assert_called_once_with("Failed to fetch the article.")


if __name__ == "__main__":
    unittest.main()
