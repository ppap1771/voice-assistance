# Audio Processing Toolkit

This project is a toolkit for audio processing tasks. 

## Overview

The project provides functionalities for:

- **Speech to Text**: Convert audio files to text.
- **Text to Speech**: Generate speech audio from text.
- **Audio Input**: Capture audio input from various sources.

## Features

- Speech to text conversion with high accuracy.
- Text to speech generation with natural-sounding voices.
- Support for various audio input sources.

## Installation

This project utilizes a virtual environment for managing dependencies. To install, follow these steps:

1. **Create a virtual environment:**
   ```bash
   python3 -m venv .venv
   ```
2. **Activate the virtual environment:**
   - Linux/macOS:
     ```bash
     source .venv/bin/activate
     ```
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Speech to Text

```python
from utils import speech2text

audio_file = "data/output.wav"
text = speech2text(audio_file)

print(text)
```

### Text to Speech

```python
from utils import text2speech

text = "This is a test of the text to speech functionality."
audio_file = "data/output.wav"
text2speech(text, audio_file)
```

### Audio Input

```python
from utils import audio_in

# Capture audio from the default microphone
audio_data = audio_in()

# Process the audio data
# ...
```

## License

This project is licensed under the [License Name] license.
