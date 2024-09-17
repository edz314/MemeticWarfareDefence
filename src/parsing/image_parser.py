# src/parsing/image_parser.py

import cv2
import pytesseract

class ImageParser:
    def __init__(self):
        # You can add initialization for any deep learning model here if needed
        pass

    def parse(self, image):
        """
        Parses the given image input using computer vision techniques.
        :param image: Pre-processed image.
        :return: Parsed data from the image (e.g., detected text or objects).
        """
        # Example: Use OCR to detect text in the image
        detected_text = self.extract_text_from_image(image)
        return {
            "detected_text": detected_text
        }

    def extract_text_from_image(self, image):
        """
        Uses OCR to extract text from the image.
        :param image: Pre-processed image.
        :return: Detected text as a string.
        """
        # Convert image to string using pytesseract
        text = pytesseract.image_to_string(image)
        return text.strip()
