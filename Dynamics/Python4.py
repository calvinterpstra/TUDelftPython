"""
Created:    Mon Feb 26 2018
Author:    Calvin Terpstra (Python 3.5.2)
"""

import matplotlib.pyplot as plt
import numpy as np

r = 1
k = 2
m = 0.5
g = 9.81

dt = 0.01
tEnd = 3
t = np.linspace(0,tEnd, round(tEnd/dt + 1))
theta = np.zeros(len(t))
x = np.zeros(len(t))
y = np.zeros(len(t))
v_x = np.zeros(len(t))
v_y = np.zeros(len(t))
a_x = np.zeros(len(t))
a_y = np.zeros(len(t))
theta[0] = 0
x[0] = r-0.01
y[0] = r-0.01
v_x[0] = 0
v_y[0] = 0
a_x[0] = 0
a_y[0] = 0

for i in range(len(t)-1):
    theta[i+1] = np.arcsin((r-y[i])/r)
    s = r*theta[i]
    Fnet_x = -m*g*np.sin(theta[i]) + k*s*np.sin(theta[i])
    Fnet_y = -m*g*np.cos(theta[i]) + k*s*np.cos(theta[i])
    a_x[i+1] = Fnet_x/m
    a_y[i+1] = Fnet_y/m
    v_x[i+1] = v_x[i] + a_x[i]*dt
    v_y[i+1] = v_y[i] + a_y[i]*dt
    x[i+1] = x[i] + v_x[i]*dt
    y[i+1] = r - np.sqrt(r**2 - x[i]**2) # y[i] + v_y[i]*dt

# plt.figure(0)
# plt.plot(t, x)
# plt.plot(t, y)
plt.figure(1)
plt.plot(x, y)
# plt.figure(2)
# plt.plot(t, theta)
plt.show()
