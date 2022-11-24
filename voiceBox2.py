import pyaudio
import RPi.GPIO as GPIO
import time
import wave

buttons = [24,23,18]
recordButon = 25


GPIO.setmode(GPIO.BCM)

for i in buttons:
    GPIO.setup(i, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(recordButon, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

frames = []
#audio_filename = "item_audio.wav"
chunk = 2048  # data is broken into chunks (buffers) of audio. In this case, each chunk contains 1024 frames (a frame is the total number of samples which occur at the same moment in time. If the audio is mono, then each frame contains 1 sample. If the audio is stereo, then each frame contains 2 samples (one from each channnel)
channels = 2  # stero format. This means there are 2 samples in each frame.
# As there are 2 bytes in each sample and 2 samples in each frame, there are 4 bytes in each frame. Therefore, there are 4096 bytes in each chunk (1024 frames*4 bytes).
sample_rate = 44100  # Sampling rate (number of frames per second). In this case, 44100 frames per second
record = pyaudio.PyAudio()  # initialise PyAudio object
Format = pyaudio.paInt16  # 'paInt16' is the sampling format. In this case, each sample contains 16 bits (2 bytes).
stream = record.open(format=Format,
                               channels=channels,
                               rate=sample_rate,
                               input=True,
                               output=True,
                               frames_per_buffer=chunk)
stream.start_stream()



while True:

    while not GPIO.input(recordButon):
        pass
    time.sleep(0.1)

    while GPIO.input(recordButon):
        for b in buttons:
            while GPIO.input(b):
                for i in range(0, int((sample_rate) / chunk)):  # (sample_rate * record_seconds) is the total number of frames recorded. As the for loop iterates through each chunk of frames and appends each chunk to the list 'frames', the total number of frames must be divided by the chunk size 'chunk'.
                    data = stream.read(chunk)
                     frames.append(data)
            stream.stop_stream()  # stops the stream (recording)
            stream.close()
            record.terminate()
            wf = wave.open(str(b)+".wav", "wb")
            # set the channels
            wf.setnchannels(2)
            # set the sample format
            wf.setsampwidth(record.get_sample_size(pyaudio.paInt16))
            # set the sample rate
            wf.setframerate(sample_rate)
            # write the frames as bytes
            wf.writeframes(b"".join(frames))
            # close the file
            wf.close()
