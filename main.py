from __future__ import unicode_literals
import youtube_dl

ydl_opts = {}
input_url = input('Link: ')

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([input_url])
    