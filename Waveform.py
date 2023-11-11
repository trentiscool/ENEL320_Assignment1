import numpy as np
import matplotlib.pyplot as plt
import scipy
"""
Assignment 1 ENEL320
"""

import numpy as np
import matplotlib.pyplot as plt

# Parameters of the sawtooth wave
T = 1
A = 1  # Amplitude

# Create time values for one period
time = np.linspace(0, 5, 500)

def Waveform(cutoff):
    signal = []
    for t in time:
        if t % 1 < cutoff:
            signal.append(0)
        else:
            signal.append(abs(np.sin(np.pi*t)))
    return signal

output = Waveform(0.1)

"""
# Plot the sawtooth wave
plt.plot(time, output)
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude (Volts)')
plt.title('Single Phase Rectifier W/ Commutation')
plt.grid(True)
plt.show()
"""

fast = scipy.fft.fft(output)
magnitude = np.abs(fast)
phase = np.angle(fast)
plt.plot(np.fft.fftfreq(time.size), magnitude)
plt.xlabel('Frequnecy (Hz)')
plt.ylabel('Amplitude (dB)')
#plt.ylim(-1,1)
plt.title('Single Phase Rectifier W/ Commutation Fourier Transform')
plt.grid(True)
plt.show()



