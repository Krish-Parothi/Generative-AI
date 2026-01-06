import os
from dotenv import load_dotenv
load_dotenv()
from youtube_transcript_api import YouTubeTranscriptApi

video_id = "NepC0s_vZhimJJMe"

try:
    transcript_list = YouTubeTranscriptApi.fetch(video_id, languages=["en"])
    transcript = " ".join(chunk["text"] for chunk in transcript_list)
    print(transcript)

except:
    print("No Captions Available for this Video")