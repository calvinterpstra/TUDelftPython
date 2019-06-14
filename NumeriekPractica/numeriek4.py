# -*- coding: utf-8 -*-

from math import *
import numpy as np
import matplotlib.pyplot as plt

u = 0
v = 0
a = 2
b = 4.5
p = 4

def f(t_n, w_n, t_f):
    du = a(t_n, t_f) - b*w_n[0] + w_n[1]*w_n[0]**2 - w_n[0]
    dv = b*w_n[0] - w_n[1]*w_n[0]**2
    return np.array([du, dv])

def a(t, t_f):
    if(t > t_f):
        return 2*np.e**(t_f - t)
    else:
        return 2

def truncErr(w_n, w_n_2):
    return (w_n - w_n_2)/15.0

def rk4(dt, t_end, t_f):
    w_n = np.array([[u, v]])
    t = 0
    while(t < t_end):
        k1 = dt * f(t, w_n[-1], t_f)
        k2 = dt * f(t + 0.5*dt, w_n[-1] + 0.5*k1, t_f)
        k3 = dt * f(t + 0.5*dt, w_n[-1] + 0.5*k2, t_f)
        k4 = dt * f(t + dt, w_n[-1] + k3, t_f)

        w_n_new = w_n[-1] + (1/6)*(k1 + 2*k2 + 2*k3 + k4)
        w_n = np.append(w_n, np.array([w_n_new]), axis=0)
        t = round(t+dt, 10)

    return w_n

k = 5
dt = 0.2/2**k
t_f = np.linspace(0, 10, 100)
v_eq = np.linspace(0, 0, 100)

for i in range(len(t_f)):
    v_eq[i] = rk4(dt, 60, t_f[i])[-1][1]

v_max_pos = np.argmax(v_eq)
t_f_max = t_f[v_max_pos]
print("t_f_max: ", t_f_max)

plt.plot(t_f, v_eq)
plt.axvline(x=t_f_max, color='r', dashes=[6, 2])
plt.title(r'$t_f$ vs $v_{eq}$')
plt.ylabel(r'$v_{eq}$')
plt.xlabel(r'$t_f$ (s)')
plt.text(3.5, 7, r'$t_f = 3.333$ s')
plt.axis("equal")
plt.grid(True)
plt.show()
