import numpy as np
import matplotlib.pyplot as plt
import time

# Three fundamental steps to create plots:
# 1. Create the data
# 2. Create the plot
# 3. Visualize the plot

# 1. Create the data
# The formula: sin(2wt + theta)
def sinus_generator(amplitue: int, frequency: int, time: int, theta: int) -> tuple:
    t = np.arange(0, time, 0.1)
    y = amplitue * np.sin(2 * frequency * t + np.deg2rad(theta))
    return t, y

# 2. Create the plot
t1, y1 = sinus_generator(1, 1, 4, 0)
plt.plot(t1, y1)

t2, y2 = sinus_generator(1, 1, 4, 30)
plt.plot(t2, y2, 'r')

t3, y3 = sinus_generator(1, 1, 4, 90)
plt.plot(t3, y3, 'c-o')

t4, y4 = sinus_generator(1, 1, 4, 60)
plt.plot(t4, y4, 'y-D')

# 3. Visualize the plot
plt.show()

# List of markers to customize the looks of the plots:
# "."	point
# ","	pixel
# "o"	circle
# "v"	triangle_down
# "^"	triangle_up
# "<"	triangle_left
# ">"	triangle_right
# "1"	tri_down
# "2"	tri_up
# "3"	tri_left
# "4"	tri_right
# "8"	octagon
# "s"	square
# "p"	pentagon
# "P"	plus (filled)
# "*"	star
# "h"	hexagon1
# "H"	hexagon2
# "+"	plus
# "x"	x
# "X"	x (filled)
# "D"	diamond
# "d"	thin_diamond
# "|"	vline
# "_"	hline