from eq.audio_stream import AudioStream
from eq.gui import EqualizerGUI

def main():
    # Create the audio stream and start audio processing
    stream = AudioStream()
    stream.start()

    # Create and run the GUI for controlling the equalizer
    gui = EqualizerGUI(stream)
    gui.run()

if __name__ == "__main__":
    main()
