# 8. Menambah text

import matplotlib.pyplot as plt
import numpy as np

# Membuat data
def sinusoidal(amplitude: int, frequency: int, time: int, theta: int) -> tuple:
    t = np.arange(0, time, 0.1)
    y = amplitude * np.sin(2 * frequency * t + np.deg2rad(theta))
    return t, y

t1, y1 = sinusoidal(1, 1, 4, 0)

# Membuat plot
rumus1 = r'$ \mathcal{A}.sin(2 \omega t) $'
plt.plot(t1, y1, 'c-D', label=rumus1)

plt.title("Grafik Sinusodial")
plt.xlabel("Waktu (detik)")
plt.ylabel("Magnitue (cm)")
rumus_sinusoidal = r'$ \mathcal{Y} = A.sin(2 \omega t + \theta) $'
plt.text(1.6, 1, rumus_sinusoidal)

# Tampilkan legend
plt.legend()

# Tampilkan plot
plt.show()