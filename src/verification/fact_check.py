# src/verification/fact_check.py

import requests

class FactCheckEngine:
    def __init__(self, api_key=None):
        self.api_key = api_key
        self.fact_check_api_url = "https://factchecktools.googleapis.com/v1alpha1/claims:search"
    
    def check_fact(self, text):
        """
        Checks the given text against a fact-checking service.
        :param text: Text to be fact-checked.
        :return: Fact-checking results.
        """
        if self.api_key:
            response = self.query_fact_check_api(text)
            if response:
                return self.process_response(response)
        return {"status": "No API key or fact-checking service unavailable."}

    def query_fact_check_api(self, query):
        """
        Queries the fact-checking API with the provided text.
        :param query: The text to be fact-checked.
        :return: API response in JSON format.
        """
        params = {
            'key': self.api_key,
            'query': query,
            'languageCode': 'en'
        }
        try:
            response = requests.get(self.fact_check_api_url, params=params)
            return response.json() if response.status_code == 200 else None
        except Exception as e:
            print(f"Error querying fact-checking API: {e}")
            return None

    def process_response(self, response):
        """
        Processes the fact-checking API response and extracts relevant information.
        :param response: API response from the fact-checking service.
        :return: Parsed fact-checking results.
        """
        claims = response.get("claims", [])
        results = []
        for claim in claims:
            claim_text = claim.get("text", "N/A")
            claimant = claim.get("claimant", "Unknown")
            claim_review = claim.get("claimReview", [])
            if claim_review:
                publisher = claim_review[0].get("publisher", {}).get("name", "Unknown")
                credibility_rating = claim_review[0].get("textualRating", "Unknown")
                results.append({
                    "claim": claim_text,
                    "claimant": claimant,
                    "publisher": publisher,
                    "rating": credibility_rating
                })
        return results
