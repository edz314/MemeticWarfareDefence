# tests/test_text_parser.py

import unittest
from src.parsing.text_parser import TextParser

class TestTextParser(unittest.TestCase):
    
    def setUp(self):
        self.text_parser = TextParser()

    def test_parse(self):
        input_text = "Apple announces the new iPhone."
        parsed_output = self.text_parser.parse(input_text)
        self.assertIn(('Apple', 'ORG'), parsed_output['entities'])
        self.assertIn('announce', parsed_output['keywords'])

if __name__ == "__main__":
    unittest.main()
