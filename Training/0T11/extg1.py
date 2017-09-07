#!py -3

# Assignment   : extg1
# Author       : Ingeborg Goddijn
# Created      : August 29, 2017
# Last modified: August 29, 2017


import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0,2*np.pi,101) # grid of 101 points (100 intervals)
x, y = np.sin(theta), np.cos(theta) # circle as a parametric curve

plt.figure(1)
plt.plot(x,y)
plt.axis([-2,2,-2,2])
plt.show()
           
plt.figure(2)
plt.plot(x,y)
plt.axis([-2,2,-2,2])
plt.axis("equal")
plt.show()
