"""
Created:    Mon Feb 19 2018
Author:    Calvin Terpstra (Python 3.5.2)
"""

import matplotlib.pyplot as plt
import numpy as np

x0 = 0
v0 = 0
m = 1 * 10**7
c = 5000
F = 4 * 10**5
dF = F/60

dt = 1
T1 = 60
t1 = np.linspace(0,T1, round(T1/dt + 1))
x1 = np.zeros(len(t1))
v1 = np.zeros(len(t1))
a1 = np.zeros(len(t1))
x1[0] = x0
v1[0] = v0


for i in range(len(t1)-1):
    a1[i+1] = (dF*t1[i] - (c*v1[i]**2)) / m
    x1[i+1] = x1[i] + v1[i]*dt
    v1[i+1] = v1[i] + a1[i]*dt

T2 = 600
t2 = np.linspace(T1,T2, round((T2-T1)/dt + 1))
x2 = np.zeros(len(t2))
v2 = np.zeros(len(t2))
a2 = np.zeros(len(t2))
x2[0] = x1[len(t1)-1]
v2[0] = v1[len(t1)-1]
a2[0] = a1[len(t1)-1]

for j in range(len(t2)-1):
    a2[j+1] = (F - (c*v2[j]**2)) / m
    x2[j+1] = x2[j] + v2[j]*dt
    v2[j+1] = v2[j] + a2[j]*dt

print("a2[0]: ", a2[0])

t = np.append(t1, t2)
x = np.append(x1, x2)
v = np.append(v1, v2)
a = np.append(a1, a2)

a_ = np.interp(0, t, a)
print("a: ", a_)
v_ = np.interp(10, t, v)
print("v: ", v_)
v_ = np.interp(600, t, v)
print("v: ", v_)

plt.plot(t, a)
plt.plot(t, v)
plt.show()