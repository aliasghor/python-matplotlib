# 10. Set Spines

# Import the necessary packages
import numpy as np
import matplotlib.pyplot as plt

# Create the data
degree = np.arange(0, 360, 1)
y = np.sin(np.deg2rad(degree))

# Create the plot
plt.plot(degree, y)

plt.title("Grafik Sinusodial")
plt.text(360, -1, "Sudut")
plt.text(360, 1, "Magnituda")

plt.xticks([0, 90, 180, 270, 360], [r'$ {0}^o $', r'$ {90}^o $', r'$ {180}^o $', r'$ {270}^o $', r'$ {360}^o $'])
plt.yticks([-1, -0.5, 0, 0.5, 1])

ax = plt.gca()

ax.spines['left'].set_position(('data', 180))
ax.spines['bottom'].set_position(('data', 0))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Output the plot
plt.show()