from faster_whisper import WhisperModel

def textgen(audio_path: str) -> list:
    model_size = "large-v3"
    # Run on GPU with FP16
    # model = WhisperModel(model_size, device="cpu", compute_type="float16")

    # or run on GPU with INT8
    # model = WhisperModel(model_size, device="cuda", compute_type="int8_float16")
    # or run on CPU with INT8
    model = WhisperModel(model_size, device="cpu", compute_type="int8")

    segments, info = model.transcribe(audio_path, beam_size=5, vad_filter=True)

    print("Detected language '%s' with probability %f" % (info.language, info.language_probability))
    out = []
    for segment in segments:
        print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
        out.append[segment.text]
    return out

if __name__ == "__main__":
    textgen("/home/ayush/Desktop/voice-assistance/data/output.wav")