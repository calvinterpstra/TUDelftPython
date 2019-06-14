# -*- coding: utf-8 -*-

from math import *
import numpy as np
import matplotlib.pyplot as plt

"""
x1 = [0.1, 1]
y1 = [0.9, 0]
x2 = [1, 1.8]
y2 = [0, 0.6]

plt.plot(x1, y1)
plt.plot(x2, y2)
plt.axis([0, 2, 0, 1])
plt.show()
"""
"""
l = 5
phi = pi/3
lx = l*np.cos(phi)
ly = l*np.sin(phi)

plt.plot([0, lx], [0, ly])
plt.show()
print("lx = ", lx, ", ly = ", ly)
"""
"""
t = np.linspace(0, 10, 101)
y = np.sin(t)
w = np.cos(t)

plt.plot(t, y)
plt.plot(t, w, 'r--')
plt.axis([0, 10, -2, 2])
plt.title("Golven")
plt.legend(["y=sin(t)","y=cos(t)"], loc='upper right')
plt.grid(True)
plt.ylabel('y')
plt.xlabel('t')
plt.show()
"""

t = np.linspace(-2*pi, 2*pi, 300)
x = t + 2*np.sin(2*t)
y = t + 2*np.cos(5*t)

plt.plot(x, y)
plt.title("Skipping-rope after usage by my children")
plt.ylabel('y')
plt.xlabel('x')
plt.axis("equal")
plt.show()












