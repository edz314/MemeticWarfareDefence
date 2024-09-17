# src/parsing/video_parser.py

from src.parsing.image_parser import ImageParser

class VideoParser:
    def __init__(self):
        self.image_parser = ImageParser()

    def parse(self, frames):
        """
        Parses the given video input by analyzing each frame.
        :param frames: List of frames extracted from the video.
        :return: Parsed data from the video frames.
        """
        parsed_frames = []
        for frame in frames:
            parsed_data = self.image_parser.parse(frame)
            parsed_frames.append(parsed_data)
        return parsed_frames
