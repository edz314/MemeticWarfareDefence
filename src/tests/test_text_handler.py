# tests/test_text_handler.py

import unittest
from src.ingestion.text_handler import TextHandler

class TestTextHandler(unittest.TestCase):
    
    def setUp(self):
        self.text_handler = TextHandler()

    def test_clean_text(self):
        input_text = "  Hello World!  "
        expected_output = "hello world!"
        self.assertEqual(self.text_handler.clean_text(input_text), expected_output)

if __name__ == "__main__":
    unittest.main()
