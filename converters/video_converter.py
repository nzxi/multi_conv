from pathlib import Path

from moviepy.editor import VideoFileClip


def convert_video(in_video, out_video):
    suffix = Path(out_video).suffix.lower()

    with VideoFileClip(in_video) as clip:
        if suffix == ".gif":
            clip.write_gif(out_video, fps=clip.fps or 24)
            return

        codec = None
        audio_codec = None
        if suffix in {".mp4", ".m4v"}:
            codec = "libx264"
            audio_codec = "aac"
        elif suffix == ".webm":
            codec = "libvpx"
            audio_codec = "libvorbis"

        clip.write_videofile(
            out_video,
            codec=codec,
            audio_codec=audio_codec,
            fps=clip.fps or 24,
        )
