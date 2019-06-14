"""
Created:    Thurs March 15 2018
Author:    Calvin Terpstra (Python 3.5.2)
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate

QUALITY = 3
g = 9.81
M_CONTAINER_MAGNET = 2.5
D_CONTAINER = 0.850
SF = 15
SIGMA_MAX = 470 * 10**6
SHEET_THINKNESS = 0.001
E = 69 * 10**9
DENSITY = 2.7

def I(h):
    return (1/12)*SHEET_THINKNESS*h**3
def w(h):
    return h*SHEET_THINKNESS*DENSITY
def v(h):
    vh = np.array([])
    for i in range(QUALITY):
        f = lambda x: w(h)[i]
        vh = np.append(vh, [integrate.quad(f, 0, D_CONTAINER)])
    return vh
def m(h):
    mh = np.array([])
    for i in range(QUALITY):
        f = lambda x: v(h)[i]
        mh = np.append(mh, [integrate.quad(f, 0, D_CONTAINER)])
    return mh
def theta(h):
    thetah = np.array([])
    for i in range(QUALITY):
        f = lambda x: (1 / (E/I(h)[i])) * m(h)[i]
        thetah = np.append(thetah, [integrate.quad(f, 0, D_CONTAINER)])
    return thetah
def delta(h):
    deltah = np.array([])
    for i in range(QUALITY):
        f = lambda x: theta(h)[i]
        deltah = np.append(deltah, [integrate.quad(f, 0, D_CONTAINER)])
    return deltah
def s(h):
    return m(h)/SIGMA_MAX
def solveh(h):
    return np.sqrt(6*s(h) / SHEET_THINKNESS)

def main():
    x = np.linspace(0, D_CONTAINER, QUALITY)
    # M_0 = M_CONTAINER_MAGNET*g*D_CONTAINER
    # s = S(x, M_0, SIGMA_MAX/SF, D_CONTAINER)
    # h = hs(s)
    # h_max = h[0]
    # i = I(h)
    # d = delta(i, D_CONTAINER, E, M_CONTAINER_MAGNET*g)

    h = np.linspace(0.01, 0.01, QUALITY)
    d = delta(h)
    print("d:", d)
    print("h size:", h.size)
    print("solveh(h) size:", solveh(h).size)

    errorPower = 1
    print("Loading <", end=' ')
    error1, error2 = 1, 1
    while(not(np.abs(error1) < (10**-errorPower) and np.abs(error2) < (10**-errorPower))): 
        dOld = d
        d = delta(h)
        h = solveh(h)
        error1, error2 = (dOld[0]-d[0])/d[0], (dOld[QUALITY-1]-d[QUALITY-1])/d[QUALITY-1]
        print("-", end=' ')
    print(">")

    h_max = h[0]
    print("x:", x)
    print("h:", h)
    print("h_max:", h_max)
    print("delta:", d)

    plt.plot(x, h)
    # plt.axis('equal')
    # plt.show()

main()
