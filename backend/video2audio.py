import sys
from moviepy.editor import VideoFileClip

def video2audio(videoName):
    video = VideoFileClip(videoName)
    audio = video.audio
    audio.write_audiofile(videoName+'.mp3')
    print("Done processing the file")
    return videoName + '.mp3'

if __name__ == '__main__':
    videoName = sys.argv[1]
    video2audio(videoName)
