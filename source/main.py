from youtube_downloader import YouTubeDownloader
from  moviepy.editor import *

answer = 'a'
folder_name = input("Set a folder name: \n")
arrClips = []
links =''

while answer != 'n':
    answer = input("Paste more links or type n to go next \n")
    if answer != 'n': links = links + answer + ','

links = links[:-1]
arrLinks = links.split(sep=',')


if __name__ == "__main__":
    for link in arrLinks:
        downloader = YouTubeDownloader(link, folder_name)
        fileName = downloader.download_video().default_filename
        clipFile = VideoFileClip(f'{folder_name}/{fileName}')
        print(clipFile)
        arrClips.append(clipFile)

qJoinVideos = input("Would you like to join this videos? \n")
if qJoinVideos == 'y':
    finalClip = concatenate_videoclips(arrClips)
    finalClip.write_videofile("gatheredVideo.mp4")