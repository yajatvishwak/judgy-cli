import ffmpeg


class VideoUtils:
    def __init__(self) -> None:
        pass

    def get_video_length(self, video_link):
        try:
            dd = ffmpeg.probe(video_link)["format"]["duration"]
            m, s = divmod(float(dd), 60)
            duration = "{:.2f} minutes and {:.2f} seconds".format(m, s)
            if not dd:
                duration = "0 minutes"
        except Exception as e:
            duration = "0 minutes"
        return duration
