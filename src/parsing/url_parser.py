# src/parsing/url_parser.py

from src.parsing.text_parser import TextParser

class URLParser:
    def __init__(self):
        self.text_parser = TextParser()

    def parse(self, url_content):
        """
        Parses the textual content extracted from a URL.
        :param url_content: Cleaned text from the URL.
        :return: Parsed text analysis including entities, keywords, etc.
        """
        return self.text_parser.parse(url_content)
