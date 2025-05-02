# 4. Set Properties

import matplotlib.pyplot as plt
import numpy as np

# Membuat data
def sinusoidal(amplitude: int, frequency: int, time: int, theta: int) -> tuple:
    t = np.arange(0, time, 0.1)
    y = amplitude * np.sin(2 * frequency * t + np.deg2rad(theta))
    return t, y

t1, y1 = sinusoidal(1, 1, 4, 0)
t2, y2 = sinusoidal(1, 1, 4, 90)
t3, y3 = sinusoidal(1, 1, 4, 180)

# Membuat plot
data_plot1 = plt.plot(t1, y1)
data_plot2 = plt.plot(t2, y2)
data_plot3 = plt.plot(t3, y3)

# Set the properties
plt.setp(data_plot1, color="red", linestyle="-", marker="o", linewidth=2)
plt.setp(data_plot2, linestyle="-.", color="yellow", marker="^", linewidth=4)
plt.setp(data_plot3, linestyle=":", color="cyan", marker="D", linewidth=1.75)

# Menampilkan plot
plt.show()