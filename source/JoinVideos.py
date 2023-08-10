from moviepy.editor import *
from moviepy.editor import VideoFileClip, concatenate_videoclips
from FileHandler import FolderFileScanner

class JoinVideos:
    def __init__(self, folderPath, fileName):
            self.folderPath = folderPath
            self.fileName = fileName
            
    def Join(self):
          arrClips = []
          scanner = FolderFileScanner(self.folderPath)
          for file in  scanner.get_file_paths():
                video = VideoFileClip(file)
                arrClips.append(video)

          finalClip = concatenate_videoclips(arrClips, method="compose")
          finalClip.write_videofile(self.fileName, fps=30)


_folderPath = input("Type folder path: \n")
_fileName = input("Type joined file name: \n")

instJoinVideos = JoinVideos(_folderPath, _fileName)
instJoinVideos.Join()

        
    