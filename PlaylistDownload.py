
from pytube import YouTube 
from pytube import Playlist
from pytube.exceptions import *
from moviepy import *
import os

#playlist
parentDir = "/Users/leonardoramosrusso/developer/YT/YouTubeTools/source"
link = input("Paste link: \n")
p = Playlist(link)
total = len(p)
print(f'Downloading: {p.title} - Total number of videos: {total}')
counter =0

for url in p.video_urls:

    try:
        video = YouTube(url)
        stream = video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first() 
        print(stream.bitrate)
    except VideoUnavailable:
        print("Video not available: " + stream.title)
    except PytubeError:
        print("Unknown Error")
    except:
        print("Some error")    
    else:
        ytTitle = video.title.replace('/','')
        defaultName = stream.default_filename
        dir = f'{parentDir}\{p.title}'
        filePath= f'{dir}\{ytTitle}.mp4'
        if os.path.isfile(filePath):
            print(f'File {ytTitle} already exists...')
            counter  += 1

        else:
            out_file = stream.download(dir,ytTitle+".mp4")
            print(f'Downloading video: {ytTitle}')
            base, ext = os.path.splitext(out_file)
            counter  += 1
            percentage = counter/total *100
            print("Completed: " + str(percentage))
