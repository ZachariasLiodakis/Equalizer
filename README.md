# Real-Time Audio Equalizer (Python)

A simple real-time audio equalizer written in Python that processes audio input from your microphone and outputs the equalized sound to your speakers. It allows you to adjust bass, mid, and treble bands live through a GUI with sliders.

---

## Features

- Real-time audio processing (microphone input)  
- 3-band equalizer: bass, mid, treble  
- GUI with sliders for live gain adjustment (0% - 200%)  
- Uses Python libraries: `numpy`, `scipy`, `sounddevice`, `tkinter`  
- Modular and easy to extend codebase  

---

## Requirements

- Python 3.7 or higher  
- Python packages:  
  ```bash
  pip install numpy scipy sounddevice

## Installation & Running
1. Clone or download the repository
2. Install required packages (see above)
3. Run the main script:

bash 
```
cd /path/to/repo-folder
python main.py
```
## Usage

A window with sliders will open for adjusting the equalizer
Speak into your microphone and hear the processed audio live

## How it works

The program captures audio from your microphone in real-time
Applies three bandpass filters to separate bass, mid, and treble frequency bands
Each band is multiplied by a gain factor set by the sliders
The combined signal is output to your speakers with applied equalization
