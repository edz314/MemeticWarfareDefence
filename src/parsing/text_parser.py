# src/parsing/text_parser.py

import spacy

class TextParser:
    def __init__(self):
        # Load a basic NLP model for language processing
        self.nlp = spacy.load('en_core_web_sm')

    def parse(self, text):
        """
        Parses the given text input using NLP techniques.
        :param text: Cleaned text input.
        :return: Parsed text analysis including entities, keywords, etc.
        """
        doc = self.nlp(text)
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        keywords = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
        return {
            "entities": entities,
            "keywords": keywords
        }
