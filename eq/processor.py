import numpy as np
from .filters import create_bandpass_filter, apply_filter

class Equalizer:
    def __init__(self, fs=44100):
        """
        Initialize the Equalizer with sampling rate and default settings.

        Parameters:
        fs (int): Sampling rate in Hz (default 44100)
        """
        self.fs = fs  # Sampling rate

        # Define frequency bands in Hz
        self.bands = {
            "bass": (60, 250),
            "mid": (250, 4000),
            "treble": (4000, 16000)
        }

        # Initialize default gain values for each band (1.0 means no change)
        self.gains = {
            "bass": 1.0,
            "mid": 1.0,
            "treble": 1.0
        }

        # Create Butterworth bandpass filters for each frequency band
        self.filters = {
            band: create_bandpass_filter(low, high, fs)
            for band, (low, high) in self.bands.items()
        }

    def update_gain(self, band, gain):
        """
        Update the gain value for a specific frequency band.

        Parameters:
        band (str): One of "bass", "mid", "treble"
        gain (float): Gain factor (0.0 to 2.0, where 1.0 is no change)
        """
        if band in self.gains:
            self.gains[band] = gain

    def process(self, input_buffer):
        """
        Apply the equalizer filters and gains to the input audio buffer.

        Parameters:
        input_buffer (np.ndarray): 1D numpy array of audio samples for one channel

        Returns:
        np.ndarray: Processed audio buffer with applied equalization
        """
        # Initialize output buffer with zeros (same shape as input)
        output = np.zeros_like(input_buffer)

        # Apply each bandpass filter, multiply by gain, and sum results
        for band, (b, a) in self.filters.items():
            filtered = apply_filter(input_buffer, b, a)
            gain = self.gains[band]
            output += filtered * gain

        # Clip the output signal to the [-1.0, 1.0] range to avoid distortion
        output = np.clip(output, -1.0, 1.0)

        return output
