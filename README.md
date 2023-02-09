# What is this?

Make a video summary with AI.

Thanks to Whisper from OpenAI you can have transcription of videos.
Now, we can use any summarization model synthesize the information.

A video to show how the interface works:


https://user-images.githubusercontent.com/65375294/217711577-ccdaae43-8e50-4fac-9dfe-f56126b9d4f5.mp4



# How does it work?

1. Download the video with `yt-dlp`
2. Let Whisper transcribe the video.
3. Summarize with distilbart
4. Output everything to a .txt file

# TODOs

- [x] Create a minimal frontend
- [ ] Add a lot more documentation
  - [ ] Documentation for the frontend
  - [ ] Documentation for the python_pypeline
- [x] Add a requirements.txt
