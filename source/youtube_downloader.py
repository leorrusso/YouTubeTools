from pytube import YouTube

class YouTubeDownloader:
    def __init__(self, link, folder_name):
        self.link = link
        self.folder_name = folder_name

    def download_video(self):
        try:
            yt = YouTube(self.link)
            self.stream = yt.streams.get_highest_resolution()
            print(f'Downloading { self.stream.title}, size: { self.stream.filesize_mb}mb')
            yt_downloaded =  self.stream.download(self.folder_name,  self.stream.default_filename)
            print(f'{yt_downloaded} has been downloaded successfully!')
            return self.stream
        except Exception as e:
            print(f'Error: {e}')


