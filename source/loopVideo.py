from moviepy.editor import *

class LoopVideo:
    def __init__(self, video_file, output_file, loopNumber:int):
        self.video_file = video_file
        self.output_file = output_file
        self.loopNumber = loopNumber

    def createLoop(self):
        videoclip = VideoFileClip(self.video_file)
        videoclip = vfx.loop(videoclip, duration=self.loopNumber)
        videoclip.write_videofile(self.output_file)

# Example usage:
if __name__ == "__main__":
    video_file = input("Type video file name \n")
    output_file = input("Type output file name \n")
    loopNumber = input("Type loop: \n")

    editor = LoopVideo(video_file, output_file, loopNumber)
    editor.createLoop()
