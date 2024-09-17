# src/ingestion/url_handler.py

import requests
from bs4 import BeautifulSoup

class URLHandler:
    def __init__(self):
        pass

    def handle(self, url):
        """
        Fetches and processes content from the given URL.
        :param url: The web URL to process.
        :return: Cleaned text content from the URL.
        """
        html_content = self.fetch_url_content(url)
        clean_content = self.extract_text_from_html(html_content)
        return clean_content

    def fetch_url_content(self, url):
        """
        Fetches the raw HTML content from the given URL.
        :param url: The web URL.
        :return: Raw HTML content.
        """
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return None

    def extract_text_from_html(self, html_content):
        """
        Extracts readable text from the HTML content.
        :param html_content: Raw HTML content.
        :return: Cleaned text from the web page.
        """
        soup = BeautifulSoup(html_content, 'html.parser')
        # Get the main text content from paragraphs
        paragraphs = soup.find_all('p')
        return ' '.join([p.get_text() for p in paragraphs])
