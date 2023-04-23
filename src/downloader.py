import os
import sys
from pathlib import Path

import yt_dlp

# Make sure ffmpeg is accessible on Windows
try:
    wd = sys._MEIPASS
except AttributeError:
    wd = os.getcwd()

FFMPEG_PATH = os.path.join(wd, "ffmpeg.exe")
if not os.path.exists(FFMPEG_PATH):
    FFMPEG_PATH = "ffmpeg"


def move_file(src: Path, dst: Path):
    src = src.resolve()
    dst = dst.resolve()
    if not dst.exists():
        if not dst.parent.exists():
            dst.parent.mkdir(parents=True)
        src.rename(dst)
    else:
        print("File already exists")


def download_video_as_mp3(url: str, output_dir: Path, downloading_hook=None):
    if type(output_dir) == str:
        output_dir = Path(output_dir)
    output_dir = output_dir.resolve()
    ydl_opts = {
        "format": "m4a/bestaudio/best",
        "postprocessors": [
            {  # Extract audio using ffmpeg
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
            }
        ],
    }

    video_path = download_video(url, output_dir, downloading_hook, ydl_opts, move=False)

    filepath = Path(str(video_path).replace(".m4a", ".mp3"))
    move_file(filepath, output_dir / filepath.name)


def download_video(
    url: str, output_dir: Path, downloading_hook=None, ydl_opts_extra=None, move=True
) -> Path:
    if type(output_dir) == str:
        output_dir = Path(output_dir)
    output_dir = output_dir.resolve()
    ydl_opts = {
        "ffmpeg_location": FFMPEG_PATH,
        "format": "mp4/bestvideo/best",
    }

    if ydl_opts_extra is not None:
        ydl_opts.update(ydl_opts_extra)

    if downloading_hook:
        ydl_opts["progress_hooks"] = [downloading_hook]

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url)
        filepath = Path(ydl.prepare_filename(info)).resolve()
        if move:
            move_file(filepath, output_dir / filepath.name)

    return filepath


if __name__ == "__main__":
    download_video_as_mp3(
        "https://www.youtube.com/watch?v=tyYcnFpk1c8", Path("./output")
    )
