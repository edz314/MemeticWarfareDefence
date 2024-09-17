# src/verification/source_basket.py

class SourceBasket:
    def __init__(self):
        self.sources = []

    def add_source(self, source_name, source_url):
        """
        Adds a trusted source to the source basket.
        :param source_name: The name of the source.
        :param source_url: The URL of the source.
        """
        self.sources.append({"name": source_name, "url": source_url})

    def verify_with_sources(self, text):
        """
        Verifies the text with trusted sources in the basket.
        :param text: The text to verify.
        :return: Verification status based on source comparison.
        """
        for source in self.sources:
            # Implement source comparison logic (could be expanded with actual APIs)
            if source["name"] in text or source["url"] in text:
                return f"Text matches a trusted source: {source['name']}"
        return "No matches found in trusted sources."
