import os, sys, datetime
from utils.audio_in import record_audio
from utils.speech2text import textgen
from utils.llm import get_response
from utils.text2speech import audiogen

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
    def __init__(self):
        pass

    def play(audio_path) -> None:
        """
        code to play .wav file given as arg
        """
        os.system(f"aplay {audio_path}")

    def run(self):
        path = record_audio()
        text = textgen(path)
        response = get_response(text)
        out = audiogen(response)
        self.play(out)

        # additionally remove the contents of data and store a log file for output.
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(f'./logs/log_{timestamp}.txt', 'a') as f:
            f.write(f"{timestamp} - Processed audio: {path}\n")
            f.write(f"Generated output = {response}")
            f.write(f"{timestamp} - Generated speech: {out}\n")

        os.remove(path)
        os.remove(out)

if __name__ == "__main__":
    runner = Runner()
    runner.run()