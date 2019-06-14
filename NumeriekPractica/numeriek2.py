# -*- coding: utf-8 -*-

# Imports
from math import *
import numpy as np
import matplotlib.pyplot as plt

# Initial values
dt = 0.2
t_f = 1
u = 0
v = 0
w_n = np.array([u, v]) # The state: current concentrations of u and v
a = 2
b = 4.5

# Derivative function of u and v
def f(t_n, w_n):
    du = a(t_n) - b*w_n[0] + w_n[1]*w_n[0]**2 - w_n[0]
    dv = b*w_n[0] - w_n[1]*w_n[0]**2
    return np.array([du, dv])

# Function to find value of a
def a(t):
    if(t > t_f):
        return 2*np.e**(t_f - t)
    else:
        return 2

# RK4 time integration
t = 0
while(t < 2): # Run until time is 2 s
    # Calculation of constants
    k1 = dt * f(t, w_n)
    k2 = dt * f(t + 0.5*dt, w_n + 0.5*k1)
    k3 = dt * f(t + 0.5*dt, w_n + 0.5*k2)
    k4 = dt * f(t + dt, w_n + k3)

    # Updating new state
    w_n1 = w_n + (1/6)*(k1 + 2*k2 + 2*k3 + k4)
    w_n = w_n1
    t = round(t+dt, 10)

# Reporting final concentration of v
print("v: ", w_n[1])