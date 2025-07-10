import sounddevice as sd
from .processor import Equalizer
import numpy as np

class AudioStream:
    def __init__(self, fs=44100, blocksize=4096):
        self.fs = fs
        self.blocksize = blocksize
        self.equalizer = Equalizer(fs=self.fs)

        self.stream = sd.Stream(
            samplerate=self.fs,
            blocksize=self.blocksize,
            channels=2,  # stereo
            dtype='float32',
            callback=self.callback
        )

    def set_gain(self, band, gain):
        """
        Update the gain in the equalizer (e.g. from the GUI).
        """
        self.equalizer.update_gain(band, gain)

    def callback(self, indata, outdata, frames, time, status):
        """
        Real-time audio callback: input -> EQ -> output
        """
        if status:
            print("[AudioStream] Warning:", status)

        # Create output buffer with same shape as input
        output_signal = np.zeros_like(indata)

        # Process each channel separately
        for ch in range(indata.shape[1]):
            output_signal[:, ch] = self.equalizer.process(indata[:, ch])

        # Write processed audio to output buffer
        outdata[:] = output_signal

    def start(self):
        print("🔊 Starting audio stream...")
        self.stream.start()

    def stop(self):
        print("⏹️ Stopping audio stream...")
        self.stream.stop()
        self.stream.close()
