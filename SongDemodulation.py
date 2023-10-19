# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 14:22:20 2023

@author: trent
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal
import sounddevice as sd

t = np.linspace(0, 107768, 107768)
fs = 44100

#song_signal = np.loadtxt('mystery_song.txt')

message_freq = 4
Ac = 1
u = 0.5
tone_signal = (u*Ac) * np.cos(2*np.pi*message_freq*t)

carrier_freq = 300e3
carrier_signal = np.cos(2 * np.pi * carrier_freq * t)

modulated_signal = (Ac + tone_signal) * carrier_signal
demodulated_signal = modulated_signal * 2 * carrier_signal

#analytic_signal = scipy.signal.hilbert(song_signal*2*carrier_signal)
#envelope = np.abs(analytic_signal)

cutoff_frequency = 3800  # Adjust this cutoff frequency as needed
filter_order = 6
nyquist_frequency = 0.5 * fs
normalized_cutoff = cutoff_frequency / nyquist_frequency
b, a = scipy.signal.butter(filter_order, normalized_cutoff, btype='low', analog=False)
output = scipy.signal.lfilter(b, a, demodulated_signal)


"""
Graphs
"""

start_value = 0
end_value = 1000
fitted_t = t[(t >= start_value) & (t <= end_value)]

#plt.plot(fitted_t, [:len(fitted_t)], label='signal')
plt.plot(fitted_t, demodulated_signal[:len(fitted_t)], color='red')
plt.plot(fitted_t, tone_signal[:len(fitted_t)])
plt.plot(fitted_t, output[:len(fitted_t)], color='black')

sd.play(output, fs) 