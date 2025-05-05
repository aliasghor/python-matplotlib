# 9. Set Ticks

# Import the necessary packages
import numpy as np
import matplotlib.pyplot as plt

# Create the data
sudut = np.arange(0, 360, 1)
y = np.sin(np.deg2rad(sudut))

# Create the plot
plt.plot(sudut, y)
plt.xlabel("Sudut")
plt.ylabel("Magnituda")

plt.yticks([-1, 0, 1])
plt.xticks([0, 90, 180, 270, 360], [r'$ {0}^o $', r'$ {90}^o $', r'$ {180}^o $', r'$ {270}^o $', r'$ {360}^o $'])

# Show the plot
plt.show()