"""from pytubefix import YouTube

url="https://www.youtube.com/watch?v=cWzMWUXp63c"

YouTube(url=url).streams.first().download()
print("Download Successfully!")"""

import yt_dlp

url = "https://www.youtube.com/watch?v=BSJa1UytM8w&list=RDBSJa1UytM8w&start_radio=1"

ydl_opts = {}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(url, download=True)
    print(info["title"])
