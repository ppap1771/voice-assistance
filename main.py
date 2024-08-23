import os, sys


"""
    1. RUN: audio_in
       GET: AUDIO
    2. Speech To Text Model: 
       Gets, audio then generates text from audio
    3. The text goes into LLM generates answer buffer
    4. The answer buffer is sent to Text to Speech
    5. Then the audio_out.mp3/.wav file is deleted.
"""

class Runner:
    def __init__(self, audio_in: str):
        self.audio_in = audio_in
