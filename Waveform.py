import numpy as np
import matplotlib.pyplot as plt

"""
Assignment 1 ENEL320
"""

import numpy as np
import matplotlib.pyplot as plt

# Parameters of the sawtooth wave
T = 1
A = 1  # Amplitude

# Create time values for one period
t = np.linspace(0, 5, 500)

sawtooth = (2*t)%2



# Plot the sawtooth wave
plt.plot(t, sawtooth)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Sawtooth Wave')
plt.grid(True)
plt.show()
