# src/parsing/audio_parser.py

from src.parsing.text_parser import TextParser

class AudioParser:
    def __init__(self):
        self.text_parser = TextParser()

    def parse(self, transcribed_text):
        """
        Parses the transcribed text from audio input using NLP.
        :param transcribed_text: Text transcribed from audio.
        :return: Parsed text analysis including entities, keywords, etc.
        """
        return self.text_parser.parse(transcribed_text)
