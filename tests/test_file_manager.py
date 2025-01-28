import unittest
import os
from core.file_manager import save_results_to_file


class TestFileManager(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_result.txt"

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_save_results_to_file(self):
        save_results_to_file("Test Title", "Test Summary", "https://example.com", filename=self.test_file)

        with open(self.test_file, "r", encoding="utf-8") as file:
            content = file.read()
            self.assertIn("Test Title", content)
            self.assertIn("Test Summary", content)
            self.assertIn("https://example.com", content)


if __name__ == "__main__":
    unittest.main()
