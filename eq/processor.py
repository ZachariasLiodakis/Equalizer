import numpy as np
from .filters import create_bandpass_filter, apply_filter

class Equalizer:
    def __init__(self, fs=44100):
        self.fs = fs  # Sampling rate

        # Συχνοτικές μπάντες (σε Hz)
        self.bands = {
            "bass": (60, 250),
            "mid": (250, 4000),
            "treble": (4000, 16000)
        }

        # Default gains (1.0 = 100%)
        self.gains = {
            "bass": 1.0,
            "mid": 1.0,
            "treble": 1.0
        }

        # Δημιουργία φίλτρων (coefficients)
        self.filters = {
            band: create_bandpass_filter(low, high, fs)
            for band, (low, high) in self.bands.items()
        }

    def update_gain(self, band, gain):
        """
        Ενημερώνει το gain (π.χ. από GUI)
        gain: float (0.0 - 2.0)
        """
        if band in self.gains:
            self.gains[band] = gain

    def process(self, input_buffer):
        """
        Επεξεργάζεται ένα audio buffer με τα φίλτρα και τα gains.

        input_buffer: np.ndarray (mono ή stereo)
        επιστρέφει: np.ndarray (επεξεργασμένο)
        """
        if input_buffer.ndim > 1:
            input_buffer = input_buffer[:, 0]  # μόνο mono προς το παρόν

        output = np.zeros_like(input_buffer)

        for band, (b, a) in self.filters.items():
            filtered = apply_filter(input_buffer, b, a)
            gain = self.gains[band]
            output += filtered * gain

        # Κλιμάκωση / αποφυγή clipping
        output = np.clip(output, -1.0, 1.0)

        return output
