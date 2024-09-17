# src/ingestion/text_handler.py

class TextHandler:
    def __init__(self):
        pass

    def handle(self, text_input):
        """
        Handles text input and prepares it for parsing.
        :param text_input: Raw text input from user or media stream.
        :return: Cleaned text ready for further analysis.
        """
        clean_text = self.clean_text(text_input)
        return clean_text

    def clean_text(self, text):
        """
        Cleans the input text by removing unnecessary characters, whitespace, etc.
        :param text: The raw text input.
        :return: Cleaned text.
        """
        return text.strip().lower()
