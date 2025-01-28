import unittest
from unittest.mock import patch, MagicMock

from core.article_fetcher import fetch_article


class TestArticleFetcher(unittest.TestCase):
    @patch("core.article_fetcher.requests.get")
    def test_fetch_article_success(self, mock_get):
        # Mock a successful response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = "<html><title>Test Title</title><p>Paragraph 1</p><p>Paragraph 2</p></html>"
        mock_get.return_value = mock_response

        result = fetch_article("https://example.com")
        self.assertEqual(result["title"], "Test Title")
        self.assertIn("Paragraph 1", result["content"])

    @patch("core.article_fetcher.requests.get")
    def test_fetch_article_failure(self, mock_get):
        # Mock a failed response
        mock_get.side_effect = Exception("Network error")
        result = fetch_article("https://example.com")
        self.assertIsNone(result)  # Ensure the function returns None when there's an error


if __name__ == "__main__":
    unittest.main()
