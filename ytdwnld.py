from pytubefix import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)

print("Views: ", yt.views)

yd = yt.streams.get_highest_resolution()

print(yd)

yd.download(r"C:\Users\noeba\Downloads")