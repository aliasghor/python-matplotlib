# 7. Membuat legend
import matplotlib.pyplot as plt
import numpy as np

# Preparing the data
def sinusoidal(amplitude: int, frequency: int, time: int, theta: int) -> tuple:
    t = np.arange(0, time, 0.1)
    y = amplitude * np.sin(2 * frequency * t + np.deg2rad(theta))
    return t, y

t1, y1 = sinusoidal(1, 1, 4, 0)

# Create the plots

# Tipe pertama
plt.plot()