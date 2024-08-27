from transformers import pipeline
import scipy


def audiogen(text) -> str: 
    synthesiser = pipeline("text-to-speech", "suno/bark")

    speech = synthesiser(text, forward_params={"do_sample": True})
    audio_data = speech[0]  

    sampling_rate = audio_data.get("sampling_rate", 16000)  
    audio = audio_data["audio"]

    # Ensure the sampling rate is within a valid range
    if not (0 <= sampling_rate <= 0x7fff * 2 + 1):
        raise ValueError("Invalid sampling rate")

    # Save the audio data as a WAV file
    scipy.io.wavfile.write("../data/audio_out.wav", rate=sampling_rate, data=audio)
    audio_path = "../data/audio_out.wav"
    return audio_path
