import whisper
import sys

def transcribe(audio_file):
    # Change this if you do not have a potato for computer.
    model = whisper.load_model("tiny")
    result = model.transcribe(audio_file)

    #print(result["text"])

    with open(audio_file+".txt", "w") as f:
        f.write(result['text'])
    return audio_file+".txt"

if __name__ == "__main__":
    audio = sys.argv[1]
    transcribe(audio)
