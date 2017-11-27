# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 10:54:13 2017

@author: Calvin
"""

from math import *;
import numpy as np;
import matplotlib.pyplot as plt;
import numpy.linalg as lg;


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

xs1[:, 0], xs1[:, 1] = h2, h2 + l1*np.cos(alphar);
ys1[:, 0], ys1[:, 1] = h1, h1 + l1*np.sin(alphar);
xs2[:, 0], xs2[:, 1] = xs1[:,1], xs1[:,1] + l2*np.cos(betar);
ys2[:, 0], ys2[:, 1] = ys1[:,1], ys1[:,1] + l2*np.sin(betar);

for i in range(6):
    plt.plot(xs1[i], ys1[i],'-o');
    plt.plot(xs2[i], ys2[i],'-o');

plt.show();


"""
l = 5
phi = np.linspace(0, pi, 21);

xxs = np.zeros((21,2));
yys = np.zeros((21,2));

xxs[:, 0], xxs[:, 1] = np.ones([21]), l*np.cos(phi);
yys[:, 0], yys[:, 1] = 0, l*np.sin(phi)

for j in range(len(xxs[:,0])):
    plt.plot(xxs[j], yys[j])

    
print("xxs: ", xxs)
print("yys: ", yys)
plt.show()
"""

"""
a = np.array([[1, 2, 3],
             [3, 3, 4],
             [2, 3, 3]]);
b = np.array([1, 1, 2]);

s = lg.solve(a, b);
print(s);
"""

"""
p = 1.2;
v = np.linspace(20, 120, 6);
v = v*1000/3600;
fdReal = np.array([11, 45, 109, 182, 298, 419]);
fdPredicted = (1/2)* p * v**2;

cda = 2 * fdReal / (p * v**2);
cdaR = np.polyfit(fdPredicted, fdReal, 1)[0];
print("cda: ",cdaR);

r = fdReal - fdPredicted;
plt.bar(v, r);

plt.plot(v, fdPredicted);
plt.plot(v, fdReal);
plt.show();
"""











