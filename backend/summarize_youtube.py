import sys
from video2audio import video2audio
from whisper_processing import transcribe
from summarize import summarize

def process_all_video(video_name):
    audio_name = video2audio(video_name)
    print("Finished processing the video")
    print(audio_name)
    text = transcribe(audio_name)
    print("Finished transcribing")
    print(text)
    summary = summarize(text)
    with open(text+'_summary.txt', "w") as f:
        for line in summary:
            f.write(line+'\n')
    print(summary)
    print("Finished")
    return "Done"

if __name__ == '__main__':
    video_name = sys.argv[1]
    process_all_video(video_name)
