import unittest
from unittest.mock import patch, MagicMock

from core.summarizer import generate_summary_and_title


class TestSummarizer(unittest.TestCase):
    @patch("core.summarizer.OpenAI")
    def test_generate_summary_and_title_success(self, mock_openai):
        # Mock LLM response
        mock_llm = MagicMock()
        mock_llm.invoke.return_value = "Title: Test Title\nSummary: This is a test summary."
        mock_openai.return_value = mock_llm

        result = generate_summary_and_title("Test article content", "fake_api_key", 50)
        self.assertEqual(result["title"], "Test Title")
        self.assertEqual(result["summary"], "This is a test summary.")

    @patch("core.summarizer.OpenAI")
    def test_generate_summary_and_title_failure(self, mock_openai):
        # Mock LLM failure
        mock_openai.side_effect = Exception("API error")
        result = generate_summary_and_title("Test article content", "fake_api_key", 50)
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
