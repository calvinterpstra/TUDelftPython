# -*- coding: utf-8 -*-

from math import *
import numpy as np
import matplotlib.pyplot as plt

dt = 0.00625
t_f = 10
u = 0
v = 0
w_n = np.array([u, v])
a = 2
b = 4.5
p = 4

def f(t_n, w_n):
    du = a(t_n) - b*w_n[0] + w_n[1]*w_n[0]**2 - w_n[0]
    dv = b*w_n[0] - w_n[1]*w_n[0]**2
    return np.array([du, dv])

def a(t):
    if(t > t_f):
        return 2*np.e**(t_f - t)
    else:
        return 2

def truncErr(w_n, w_n_2):
    return np.divide((w_n - w_n_2), 15)

t = 0
while(t <= 10):
    k1 = dt * f(t, w_n)
    k2 = dt * f(t + 0.5*dt, w_n + 0.5*k1)
    k3 = dt * f(t + 0.5*dt, w_n + 0.5*k2)
    k4 = dt * f(t + dt, w_n + k3)

    w_n1 = w_n + (1/6)*(k1 + 2*k2 + 2*k3 + k4)

    w_n = w_n1
    if(t>9.999):
        print("t: ", t, "v = ", w_n[1])
    t = round(t+dt, 10)

t = 0
w_n_2 = np.array([u, v])
dt = 2*dt
while(t <= 10):
    k1 = dt * f(t, w_n_2)
    k2 = dt * f(t + 0.5*dt, w_n_2 + 0.5*k1)
    k3 = dt * f(t + 0.5*dt, w_n_2 + 0.5*k2)
    k4 = dt * f(t + dt, w_n_2 + k3)

    w_n_21 = w_n_2 + (1/6)*(k1 + 2*k2 + 2*k3 + k4)


    w_n_2 = w_n_21
    if(t>9.999):
        print("t: ", t, "v_2 = ", w_n_2[1])
    t = round(t+dt, 10)

print(dt/2, "error: ", truncErr(w_n[1], w_n_2[1]))