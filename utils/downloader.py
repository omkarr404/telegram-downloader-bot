import yt_dlp
import os

async def download_media(link, quality):
    folder = "downloads"
    os.makedirs(folder, exist_ok=True)

    formats = {
        "360p": "bestvideo[height<=360]+bestaudio/best",
        "720p": "bestvideo[height<=720]+bestaudio/best",
        "1080p": "bestvideo[height<=1080]+bestaudio/best",
        "Audio": "bestaudio/best"
    }

    ydl_opts = {
        "format": formats.get(quality, "best"),
        "outtmpl": f"{folder}/%(title)s.%(ext)s",
        "merge_output_format": "mp4",
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(link, download=True)
        filename = ydl.prepare_filename(info)

    return filename
