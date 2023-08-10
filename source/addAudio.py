from moviepy.editor import *

class VideoAudioEditor:
    def __init__(self, video_file, audio_file, output_file, loopNumber):
        self.video_file = video_file
        self.audio_file = audio_file
        self.output_file = output_file
        self.loopNumber = loopNumber

    def edit_audio(self):
        videoclip = VideoFileClip(self.video_file)
        videoclip = vfx.loop(videoclip, duration = self.loopNumber)
        audioclip = AudioFileClip(self.audio_file)
        audioclip = vfx.loop(audioclip, duration = self.loopNumber)
        new_audioclip = CompositeAudioClip([audioclip])
        videoclip.audio = new_audioclip
        videoclip.write_videofile(self.output_file)

# Example usage:
if __name__ == "__main__":
    video_file = input("Type video file name \n")
    audio_file = input("Type audio \n")
    output_file = input("Type output file name \n")
    loopNumber = input("Type loop duration\n")

    editor = VideoAudioEditor(video_file, audio_file, output_file, loopNumber)
    editor.edit_audio()
