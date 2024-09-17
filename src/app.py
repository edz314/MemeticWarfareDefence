# src/app.py

from src.ingestion.text_handler import TextHandler
from src.ingestion.url_handler import URLHandler
from src.ingestion.image_handler import ImageHandler
from src.ingestion.video_handler import VideoHandler
from src.ingestion.audio_handler import AudioHandler

from src.parsing.text_parser import TextParser
from src.parsing.url_parser import URLParser
from src.parsing.image_parser import ImageParser
from src.parsing.video_parser import VideoParser
from src.parsing.audio_parser import AudioParser

# Initialize the handlers and parsers
text_handler = TextHandler()
url_handler = URLHandler()
image_handler = ImageHandler()
video_handler = VideoHandler()
audio_handler = AudioHandler()

text_parser = TextParser()
url_parser = URLParser()
image_parser = ImageParser()
video_parser = VideoParser()
audio_parser = AudioParser()

def main():
    # Example text input
    text_input = "Apple announces the new iPhone 15 today at the event in Cupertino."
    clean_text = text_handler.handle(text_input)
    parsed_text = text_parser.parse(clean_text)
    print("Parsed Text:", parsed_text)

    # Example URL input
    url_input = "https://news.ycombinator.com/"
    url_content = url_handler.handle(url_input)
    parsed_url_content = url_parser.parse(url_content)
    print("Parsed URL Content:", parsed_url_content)

    # Example image input
    image_path = "/path/to/image.jpg"
    processed_image = image_handler.handle(image_path)
    parsed_image = image_parser.parse(processed_image)
    print("Parsed Image:", parsed_image)

    # Example video input
    video_path = "/path/to/video.mp4"
    video_frames = video_handler.handle(video_path)
    parsed_video = video_parser.parse(video_frames)
    print("Parsed Video Frames:", parsed_video)

    # Example audio input
    audio_path = "/path/to/audio.wav"
    transcribed_text = audio_handler.handle(audio_path)
    parsed_audio = audio_parser.parse(transcribed_text)
    print("Parsed Audio:", parsed_audio)

if __name__ == "__main__":
    main()
