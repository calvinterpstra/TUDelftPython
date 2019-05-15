# -*- coding: utf-8 -*-

from math import *
import numpy as np
import matplotlib.pyplot as plt

dt = 0.2
t_f = 1
u = 0
v = 0
w_n = np.array([u, v])
a = 2
b = 4.5

def f(t_n, w_n):
    print("a: ", a)
    du = a - b*w_n[0] + w_n[1]*w_n[0]**2 - w_n[0]
    dv = b*w_n[0] - w_n[1]*w_n[0]**2
    return np.array([du, dv])


t = 0
while(t < 2):
    if(t > t_f):
        a = 2*np.e**(t_f - t)
    
    k1 = dt * f(t, w_n)
    k2 = dt * f(t + 0.5*dt, w_n + 0.5*k1)
    k3 = dt * f(t + 0.5*dt, w_n + 0.5*k2)
    k4 = dt * f(t + dt, w_n + k3)

    w_n1 = w_n + (1/6)*(k1 + 2*k2 + 2*k3 + k4)
    print("t: ", t, "u: ", w_n[0], "v: ", w_n[1])
    w_n = w_n1
    t += dt