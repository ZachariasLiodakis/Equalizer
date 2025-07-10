import tkinter as tk
from tkinter import ttk

class EqualizerGUI:
    def __init__(self, audio_stream):
        self.audio_stream = audio_stream

        self.root = tk.Tk()
        self.root.title("Real-Time Audio Equalizer")

        self.create_sliders()
        # Handle window close event
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def create_sliders(self):
        # Slider configuration
        slider_config = {
            "from_": 0,
            "to": 200,        # 0% to 200% gain
            "orient": tk.HORIZONTAL,
            "length": 300,
        }

        self.sliders = {}

        # Create sliders for bass, mid, treble frequency bands
        for i, band in enumerate(["bass", "mid", "treble"]):
            label = ttk.Label(self.root, text=band.capitalize())
            label.grid(row=i, column=0, padx=10, pady=10, sticky="w")

            slider = tk.Scale(
                self.root,
                **slider_config,
                command=lambda val, b=band: self.on_slider_change(b, val)
            )
            slider.set(100)  # default 100% gain
            slider.grid(row=i, column=1, padx=10, pady=10)

            self.sliders[band] = slider

    def on_slider_change(self, band, val):
        # Convert slider value from 0-200 to 0.0-2.0 gain range
        gain = float(val) / 100.0
        self.audio_stream.set_gain(band, gain)

    def run(self):
        # Start the Tkinter event loop
        self.root.mainloop()

    def on_close(self):
        # Stop audio stream and close the GUI window
        self.audio_stream.stop()
        self.root.destroy()
