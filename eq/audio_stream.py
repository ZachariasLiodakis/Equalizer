import sounddevice as sd
from .processor import Equalizer

class AudioStream:
    def __init__(self, fs=44100, blocksize=2048):
        self.fs = fs
        self.blocksize = blocksize
        self.equalizer = Equalizer(fs=self.fs)

        self.stream = sd.Stream(
            samplerate=self.fs,
            blocksize=self.blocksize,
            channels=1,  # mono για αρχή
            dtype='float32',
            callback=self.callback
        )

    def set_gain(self, band, gain):
        """
        Ενημερώνει το gain στο equalizer (π.χ. από GUI).
        """
        self.equalizer.update_gain(band, gain)

    def callback(self, indata, outdata, frames, time, status):
        """
        Real-time audio callback: input -> EQ -> output
        """
        if status:
            print("[AudioStream] Warning:", status)

        input_signal = indata[:, 0]  # mono
        output_signal = self.equalizer.process(input_signal)
        outdata[:, 0] = output_signal

    def start(self):
        print("🔊 Starting audio stream...")
        self.stream.start()

    def stop(self):
        print("⏹️ Stopping audio stream...")
        self.stream.stop()
        self.stream.close()
