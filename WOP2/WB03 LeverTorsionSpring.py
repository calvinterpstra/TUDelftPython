# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 19:37:34 2017

@author: Calvin
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

quality = 1000

def fAttatch(fEnd, l, r):
    return (l*fEnd)/r

def I(f, l, d, E):
    return (f*l**3)/(3*E*d)

def H(I, w):
    return np.cbrt(12*I/w)

def Itheta(m, l, t, E):
    itheta = np.array([])
    for i in range(quality):
        if(t[i] == 0):
            itheta = np.append(itheta, [0])
        else:
            itheta = np.append(itheta, [(m[i]*l[i]**2)/(E*t[i])]) 
    return itheta

def main():
    fEnd = 18
    r = 0.01
    l = 0.196
    w = 0.002
    delta = 0.001
    E = 68.9 * 10**9
    
    x = np.linspace(0, l, quality)
    mx = lambda x: fEnd*(l-x)
    thetax = np.array([])
    for j in range(quality):
        thetax = np.append(thetax, [sp.integrate.quad(mx, 0, x[j])[0]])
    plt.figure(1);
    plt.plot(x, mx(x));
    plt.title("mx vs x");
    plt.show();
    
    plt.figure(2);
    plt.plot(x, thetax);
    plt.title("thetax vs x");
    plt.show();
    
    i = Itheta(mx(x), x, thetax, E)
    h = H(i, w)
    
    plt.figure(3);
    plt.plot(x, h);
    plt.title("h vs x");
    plt.show();
    
    
main();