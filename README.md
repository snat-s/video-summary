# What is this?

Make a video summary with AI.

Thanks to Whisper from OpenAI you can have transcription of videos.
Now, we can use any summarization model synthesize the information.

# How does it work?

1. Download the video with `yt-dlp`
2. Let Whisper transcribe the video.
3. Summarize with distilbart
4. Output everything to a .txt file

# TODOs

- [X] Create a minimal frontend
- [ ] Add a lot more documentation
  - [ ] Documentation for the frontend
  - [ ] Documentation for the python_pypeline
- [ ] Add a requirements.txt
