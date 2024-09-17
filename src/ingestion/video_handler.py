# src/ingestion/video_handler.py

import cv2

class VideoHandler:
    def __init__(self):
        pass

    def handle(self, video_path):
        """
        Handles video input by extracting key frames for analysis.
        :param video_path: Path to the video file.
        :return: List of extracted frames.
        """
        video = self.load_video(video_path)
        frames = self.extract_frames(video)
        return frames

    def load_video(self, video_path):
        """
        Loads the video from the file system.
        :param video_path: Path to the video file.
        :return: VideoCapture object.
        """
        return cv2.VideoCapture(video_path)

    def extract_frames(self, video):
        """
        Extracts key frames from the video.
        :param video: VideoCapture object.
        :return: List of extracted frames.
        """
        frames = []
        success, frame = video.read()
        while success:
            frames.append(frame)
            success, frame = video.read()
        return frames
