# 5. Set axis

# Import the necessary packages to preparing the data and plotting the data
import numpy as np
import matplotlib.pyplot as plt

# Preparing the data
def sinusoidal(amplitude: int, frequency: int, time: int, theta: int) -> tuple:
    t = np.arange(0, time, 0.1)
    y = amplitude * np.sin(2 * frequency * t + np.deg2rad(theta))
    return t, y

t, y = sinusoidal(1, 1, 4, 0)

# Create the plot
data1 = plt.plot(t, y)
# plt.plot(t, y, 'b-o') # Set the color, linestyle, and marker directly on the plot function.

# Set the properties
plt.setp(data1, color="blue", linestyle="-", marker="o")

# Set the minum and maximum numbers
# plt.axis([xmin, xmax, ymin, ymax])
plt.axis([0, 4.25, -1, 1.25])

# Output the plot
plt.show()