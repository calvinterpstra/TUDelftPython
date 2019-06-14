# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 10:52:26 2017

@author: Calvin
"""

from math import *
import numpy as np
import matplotlib.pyplot as plt

"""
phi = np.linspace(0, pi, 21)
v = phi[::1]
print(v)
"""

"""
a1 = 12
a2 = 14
l1 = 3
l2 = l1
h1 = a1/2
h2 = a2/2
alphar = 120 * (2*pi / 360)
betar = 160 * (2*pi / 360)

wax = np.array([0,a2, a2, 0, 0])
way = np.array([0,0, a1, a1, 0])

x1 = np.array([h2, (h2 + l1*np.cos(alphar))])
y1 = np.array([h1, (h1 + l1*np.sin(alphar))])
x2 = np.array([x1[1], x1[1] + l2*np.cos(betar)])
y2 = np.array([y1[1], y1[1] + l2*np.sin(betar)])

plt.plot(wax, way)
plt.plot(x1, y1)
plt.plot(x2, y2)
plt.show()
"""

"""
a1 = 12
a2 = 14
l1 = 3
l2 = l1
h1 = a1/2
h2 = a2/2
alphar = 120 * (2*pi / 360)
betar = 160 * (2*pi / 360)

x = np.array([h2, (h2 + l1*np.cos(alphar)), x[1] + l2*np.cos(betar)])
y = np.array([h1, (h1 + l1*np.sin(alphar)), y[1] + l2*np.sin(betar)])

plt.plot(x, y)
plt.show()
"""

"""
a = np.array([[1, 2],
              [3, 4],
              [5, 6]]);

l = a.shape;
q = a[2, 0:2];
a2 = np.zeros((2,21))
print(a2);
"""

"""
l = 5
phi = np.linspace(0, pi, 21);

xs = np.zeros((21,2));
ys = np.zeros((21,2));

c = 0;
for i in range(len(xs[:,0])):
    xs[i] = [0, l*np.cos(phi[i])];
    ys[i] = [0, l*np.sin(phi[i])];

for j in range(len(xs[:,0])):
    plt.plot(xs[j], ys[j])

    
print("xs: ", xs)
print("ys: ", ys)
plt.show()
"""

a1 = 12;
a2 = 14;
l1 = 3;
l2 = l1;
h1 = a1/2;
h2 = a2/2;
alpha = np.linspace(20, 340, 6);
beta = np.linspace(60, 240, 6);

alphar = alpha * (2*pi / 360);
betar = beta * (2*pi / 360);

xs1 = np.zeros((6,2));
ys1 = np.zeros((6,2));
xs2 = np.zeros((6,2));
ys2 = np.zeros((6,2));

for i in range(6):
    xs1[i] = np.array([h2, (h2 + l1*np.cos(alphar[i]))]);
    ys1[i] = np.array([h1, (h1 + l1*np.sin(alphar[i]))]);
    xs2[i] = np.array([xs1[i,1], xs1[i,1] + l2*np.cos(betar[i])]);
    ys2[i] = np.array([ys1[i,1], ys1[i,1] + l2*np.sin(betar[i])]);

for i in range(6):
    plt.plot(xs1[i], ys1[i],'-o')
    plt.plot(xs2[i], ys2[i],'-o')

plt.show()














