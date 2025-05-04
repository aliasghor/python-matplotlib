# 7. Membuat legend
import matplotlib.pyplot as plt
import numpy as np

# Preparing the data
def sinusoidal(amplitude: int, frequency: int, tAkhir: int, theta: int) -> tuple:
    t = np.arange(0, tAkhir, 0.1)
    y = amplitude * np.sin(2 * frequency * t + np.deg2rad(theta))
    return t, y

t1, y1 = sinusoidal(1, 1, 4, 0)
t2, y2 = sinusoidal(1, 1, 4, 90)

# Create the plots

# Tipe pertama
# plt.plot(t1, y1, 'b-o', label="sin(0)")
# plt.plot(t2, y2, 'r-o', label="sin(90)")

# Tampilkan legend
# plt.legend()

# Tipe kedua
# plt.plot(t1, y1, 'b-o', label="sin(0)")
# plt.plot(t2, y2, 'r-o', label="sin(90)")

# Tampilkan legend
# plt.legend(loc="upper right")
# plt.legend(loc="upper center")

# Tipe ketiga
# plt.plot(t1, y1, 'b-o', label="sin(0)")
# plt.plot(t2, y2, 'r-o', label="sin(90)")

# Tampilkan legend
# plt.legend(loc="upper center", bbox_to_anchor=(0.5, -0.5))

# Tipe ketiga
plt.figure(1)
ax = plt.subplot(111)

plt.plot(t1, y1, 'b-o', label="sin(0)")
plt.plot(t2, y2, 'r-o', label="sin(90)")

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.7, box.height])

# Tampilkan legend
plt.legend(loc="upper center", bbox_to_anchor=(1.2, 1))

# Tampilkan plot
plt.show()