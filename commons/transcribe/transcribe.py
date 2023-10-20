import whisper


class Transcribe:
    def __init__(self) -> None:
        self.transcription_model = whisper.load_model("small", "cpu")

    def get_transcription(self, video_link):
        try:
            transcript = self.transcription_model.transcribe(video_link)["text"]
        except Exception as e:
            transcript = {"text": "Could not transcribe"}
            raise e
        return transcript
