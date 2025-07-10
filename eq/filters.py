import numpy as np
from scipy.signal import butter, lfilter


def create_bandpass_filter(lowcut, highcut, fs, order=4):
    """
    Δημιουργεί τα coefficients ενός bandpass φίλτρου Butterworth.

    Parameters:
        lowcut (float): Κάτω συχνότητα (Hz)
        highcut (float): Πάνω συχνότητα (Hz)
        fs (int): Συχνότητα δειγματοληψίας
        order (int): Τάξη φίλτρου (default: 4)

    Returns:
        b, a (np.ndarray): coefficients για χρήση με lfilter
    """
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    return b, a


def apply_filter(data, b, a):
    """
    Εφαρμόζει το φίλτρο σε ηχητικό σήμα.

    Parameters:
        data (np.ndarray): Σήμα ήχου (1D)
        b, a: Συντελεστές φίλτρου από την butter()

    Returns:
        filtered (np.ndarray): Φιλτραρισμένο σήμα
    """
    return lfilter(b, a, data)
