# src/app.py

from src.ingestion.text_handler import TextHandler
from src.ingestion.url_handler import URLHandler
from src.ingestion.image_handler import ImageHandler
from src.ingestion.video_handler import VideoHandler
from src.ingestion.audio_handler import AudioHandler

# Initialize the handlers
text_handler = TextHandler()
url_handler = URLHandler()
image_handler = ImageHandler()
video_handler = VideoHandler()
audio_handler = AudioHandler()

def main():
    # Example text input
    text_input = "Apple announces the new iPhone 15 today at the event in Cupertino."
    clean_text = text_handler.handle(text_input)
    print("Processed Text:", clean_text)

    # Example URL input
    url_input = "https://news.ycombinator.com/"
    url_content = url_handler.handle(url_input)
    print("Extracted URL Content:", url_content)

    # Example image input
    image_path = "/path/to/image.jpg"
    processed_image = image_handler.handle(image_path)
    print("Processed Image Shape:", processed_image.shape)

    # Example video input
    video_path = "/path/to/video.mp4"
    video_frames = video_handler.handle(video_path)
    print("Extracted Frames Count:", len(video_frames))

    # Example audio input
    audio_path = "/path/to/audio.wav"
    transcribed_text = audio_handler.handle(audio_path)
    print("Transcribed Audio:", transcribed_text)

if __name__ == "__main__":
    main()
