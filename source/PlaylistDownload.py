from pytube import YouTube 
from pytube import Playlist
from pytube.exceptions import *
import os
from moviepy.editor import *

#playlist
parentDir = "C:"
link = input("Paste link: \n")
p = Playlist(link)
total = p.length
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
        filePath= f'{dir}\{ytTitle}.mp3'
        if os.path.isfile(filePath):
            print(f'File {ytTitle} already exists...')
            counter  += 1

        else:
            out_file = stream.download(dir,ytTitle+".mp4")
            video = VideoFileClip(f'{dir}/{ytTitle}.mp4')
            print(f'Downloading video: {ytTitle}')
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            video.audio.write_audiofile(new_file,bitrate='2560k')
            video.close()
            os.remove(out_file)
            counter  += 1
            percentage = counter/total *100
            print("Completed: " + str(percentage))

##https://www.youtube.com/playlist?list=PLPcvK8sxCmaI0hopDgtOCfr9oX6PmRO8Y