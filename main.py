from eq.audio_stream import AudioStream
from eq.gui import EqualizerGUI

def main():
    # Δημιουργούμε το audio stream και ξεκινάμε τον ήχο
    stream = AudioStream()
    stream.start()

    # Δημιουργούμε το GUI και το τρέχουμε
    gui = EqualizerGUI(stream)
    gui.run()

if __name__ == "__main__":
    main()
