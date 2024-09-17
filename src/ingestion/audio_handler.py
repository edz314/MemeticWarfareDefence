# src/ingestion/audio_handler.py

import speech_recognition as sr

class AudioHandler:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def handle(self, audio_path):
        """
        Handles audio input by converting it to text.
        :param audio_path: Path to the audio file.
        :return: Transcribed text from the audio.
        """
        audio = self.load_audio(audio_path)
        text = self.transcribe_audio(audio)
        return text

    def load_audio(self, audio_path):
        """
        Loads the audio file for transcription.
        :param audio_path: Path to the audio file.
        :return: Audio data.
        """
        with sr.AudioFile(audio_path) as source:
            audio = self.recognizer.record(source)
        return audio

    def transcribe_audio(self, audio):
        """
        Converts the audio to text using speech recognition.
        :param audio: Audio data.
        :return: Transcribed text.
        """
        try:
            return self.recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return "Audio not clear or understandable."
        except sr.RequestError as e:
            return f"Could not request results; {e}"
