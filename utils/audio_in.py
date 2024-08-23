import pyaudio
import wave
import keyboard

def record_audio(filename, channels=1, rate=22050, chunk=1024) -> str:
    # Initialize PyAudio
    p = pyaudio.PyAudio()

    # Open a stream with the specified format
    stream = p.open(format=pyaudio.paInt16,
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=chunk)

    print("Recording started... Press 'q' to stop recording.")

    frames = []

    # Record audio until the user presses 'q'
    try:
        while True:
            data = stream.read(chunk, exception_on_overflow=False)
            frames.append(data)

            # Check if 'q' is pressed to stop the recording
            if keyboard.is_pressed('q'):
                print("Recording stopped.")
                break

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Stop the stream and close it
        stream.stop_stream()
        stream.close()

        # Terminate the PyAudio object
        p.terminate()

        # Save the recorded audio to a file
        with wave.open(filename, 'wb') as wf:
            wf.setnchannels(channels)
            wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
            wf.setframerate(rate)
            wf.writeframes(b''.join(frames))

        print(f"Audio saved to {filename}")
        return filename

if __name__ == "__main__":
    filename = "./data/output.wav"  # Output file name

    record_audio(filename)
