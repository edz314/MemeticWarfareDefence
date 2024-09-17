# src/ingestion/image_handler.py

import cv2

class ImageHandler:
    def __init__(self):
        pass

    def handle(self, image_path):
        """
        Handles an image input by pre-processing it.
        :param image_path: Path to the image file.
        :return: Pre-processed image ready for analysis.
        """
        image = self.load_image(image_path)
        preprocessed_image = self.preprocess_image(image)
        return preprocessed_image

    def load_image(self, image_path):
        """
        Loads the image from the file system.
        :param image_path: Path to the image file.
        :return: Loaded image.
        """
        return cv2.imread(image_path)

    def preprocess_image(self, image):
        """
        Pre-processes the image by resizing, normalizing, etc.
        :param image: The loaded image.
        :return: Pre-processed image.
        """
        # Example: Convert to grayscale and resize
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        resized_image = cv2.resize(gray_image, (256, 256))
        return resized_image
