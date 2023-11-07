
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal
from scipy.io import wavfile


"""
Globals
"""

noise = 0.1

"""
# TONE MODULATION
Ac = 2
fcarrier = 30e3
fcutoff = 1
order = 2

fmessage = 1500
Am = 1

# TONE SIGNALS
t = np.arange(0, 3/fmessage, 0.0001/fmessage)
tone_message = Am * np.cos(2*np.pi*fmessage*t) 
"""

# SONG DECODING
fsamp = 44100
fmessage = 44100
Am = 1
fcarrier = 300e3
Ac = 2
fcutoff = 10e3
order = 2

# Mystery Song Signal
song = np.loadtxt('mystery_song.txt')
t = np.arange(0, len(song)) * (1/fmessage)



"""
Signal Functions
"""

def EnvelopeDetector (signal):
    "Takes envelope of AM signal"
    return np.abs(scipy.signal.hilbert(signal))

def LowPassFilter(signal, fmessage, fcutoff, order):
    
    fnyq = 0.5 * fmessage
    normalized_cutoff = fcutoff / fnyq
    b, a = scipy.signal.butter(order, normalized_cutoff)
    return scipy.signal.lfilter(b, a, signal)

def Transmit(signal, t):
    "Creates transmitted signal"
    output = (Ac + signal) * np.cos(2*np.pi*fcarrier*t)
    return output
    
    
def AGWN(signal, noise):
    "Addative Gausian White Noise"
    return signal + np.random.normal(0, noise, len(signal))


def Recieve(signal):
    "Recieves and demodulates signal"
    # Detects envelope
    m = EnvelopeDetector(signal)
    
    # Filters out high frequency components
    m = LowPassFilter(m, fmessage, fcutoff, order)
    
    # Removes DC component
    return [value - Ac for value in m]

def main():
    "Signals"
    
    #Transmit
    transmitted_signal = Transmit(song, t)
    
    #Channel
    noise_signal = AGWN(transmitted_signal, noise)
    
    #Recieve
    Recieved_signal = Recieve(noise_signal)
    
    "Plot"

    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.grid()

    plt.plot(t, transmitted_signal)
    #plt.plot(t, noise_signal, color='grey')
    plt.plot(t, Recieved_signal)
    #plt.plot(t, tone_message)
    plt.show()
    
    scaled_song = np.int16(song / np.max(np.abs(song)) * (2**16))
    wavfile.write('song.wav', fsamp, scaled_song)



main()

