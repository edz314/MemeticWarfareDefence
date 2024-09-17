# src/app.py

from src.ingestion.text_handler import TextHandler
from src.parsing.text_parser import TextParser

# Initialize the components
text_handler = TextHandler()
text_parser = TextParser()

def main():
    # Simulate text input (could be from any source)
    text_input = "Apple announces the new iPhone 15 today at the event in Cupertino."
    
    # Handle and clean the text
    clean_text = text_handler.handle(text_input)
    
    # Parse the text for entities and keywords
    parsed_text = text_parser.parse(clean_text)
    
    print("Parsed Entities and Keywords:", parsed_text)

if __name__ == "__main__":
    main()
