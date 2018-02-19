"""
Created:    Mon Feb 15 2018
Author:    Calvin Terpstra (Python 3.5.2)
"""

import matplotlib.pyplot as plt
import numpy as np

# Q1
# v0 = 5
# v1 = 23
# Dx = 1000

# dt = 0.1
# T = 135
# t = np.linspace(0,T, round(T/dt + 1))
# x = np.zeros(len(t))
# v = np.zeros(len(t))
# x[0] = 0
# v[0] = v0
# a = (v1**2-v0**2) / (2*Dx)

# for i in range(len(t)-1):
#     x[i+1] = x[i] + v[i]*dt
#     v[i+1] = v[i] + a*dt

# v3 = np.sqrt(v0**2 + 2*a*3000)
# print(v3)
# t3 = (v3-v0)/a
# print(t3)

# print(x)

# plt.plot(t, v)
# plt.plot(t, x)
# plt.show()

# Q2
# x0 = 0
# v0 = 7
# Dx = 1000
# P = 12
# m = 1000

# dt = 0.001
# T = 700
# t = np.linspace(0,T, round(T/dt + 1))
# x = np.zeros(len(t))
# v = np.zeros(len(t))
# x[0] = x0
# v[0] = v0
# a = P/m
# print("a", a)

# for i in range(len(t)-1):
#     x[i+1] = x[i] + v[i]*dt
#     v[i+1] = v[i] + a*dt

# v1 = np.sqrt(v0**2 + 2*a*6000)
# print("v: ", v1)
# t1 = (v1-v0)/a
# print("t1: ", t1)

# v1n = np.interp(6000, x, v)
# print("v1n: ", v1n)
# t1n = np.interp(4000, x, t)
# print("t1n: ", t1n)

# print("error: ", v1 - v1n)

# plt.plot(t, v)
# plt.plot(t, x)
# plt.show()

# Q3:
x0 = 0
v0 = 10
m = 200

dt = 0.01
T = 15
t = np.linspace(0,T, round(T/dt + 1))
x = np.zeros(len(t))
v = np.zeros(len(t))
a = np.zeros(len(t))
x[0] = x0
v[0] = v0

for i in range(len(t)-1):
    a[i+1] = -(10*v[i]**3)/m
    x[i+1] = x[i] + v[i]*dt
    v[i+1] = v[i] + a[i]*dt

v1 = ((20*10 / m)+v0**(-2))**(-1/2)
print("v: ", v1)
x1 = (m/10)*((20*8 / m)+v0**(-2))**(1/2) - 2
print("x: ", x1)

v1n = np.interp(10, t, v)
print("v1n: ", v1n)
x1n = np.interp(8, t, x)
print("x1n: ", x1n)

print("v error: ", v1 - v1n)
print("x error: ", x1 - x1n)

plt.plot(t, a)
plt.plot(t, v)
plt.plot(t, x)


# Q5:
# Fy = T - ma*g
# Fy = T - mb*g
# l = sa + sb
# aa = -ab
# aa = (2*g*mb) / (ma+mb) - g

# Q6:
#Fy=2*T-ma*g
#Fy=T-mb*g
#l=2*sa+sb
#aa=-ab/2
#aa=(6*g*mb)/(ma+4*mb)-g