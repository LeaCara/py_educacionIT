# pip install git+https://github.com/openai/whisper
# pip install pytube
from unittest import result
import pytube
import whisper

youtubeVideoId = "https://www.youtube.com/shorts/a13ygtf2EpA"
model = whisper.load_model('small')

youtubeVideo = pytube.YouTube(youtubeVideoId)
audio = youtubeVideo.streams.get_audio_only()

audio.download(filename='tmp.mp4')

result = model.transcribe('tmp.mp4')

print(result["text"])