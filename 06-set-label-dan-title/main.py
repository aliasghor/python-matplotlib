# 6. Set label dan title

# Import the necessary packages to prepare and plot the data
import matplotlib.pyplot as plt
import numpy as np

# Preparing the data
def sinusoidal(amplitude: int, frequency: int, time: int, theta: int) -> tuple:
    t = np.arange(0, time, 0.1)
    y = amplitude * np.sin(2 * frequency * t + np.deg2rad(theta))
    return t, y

t, y = sinusoidal(1, 1, 4, 0)
amplitude = 1
frequency = 1
time = 4
theta = 0

# Create the plot
judul = "Grafik Sinusoidal\n"
rumus = r'$ \mathcal{Y} = A.sin(2 \omega t + \theta) $'
# parameter1 = r'$ A =  $' + str(amplitude) + 'cm, '
# parmeter2 = r'$ \omega =  $' + str(frequency) + r'$ \mathit{Hz} $' + ', '
# parameter3 = r'$ \theta = $' + str(theta) + r'$ ^{o} $'

plt.plot(t, y, 'b-o')

# plt.title(judul + rumus + parameter1 + parmeter2 + parameter3)
plt.title(judul + rumus)
plt.xlabel('Waktu (detik)')
plt.ylabel('Magnituda (cm)')

# Output the plot
plt.show()
