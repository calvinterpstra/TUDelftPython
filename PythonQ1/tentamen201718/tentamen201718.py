#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 21:35:47 2018

@author: calvint
"""

import numpy as np
import matplotlib.pyplot as plt

#Stap 1
H = 3
B = 3.5
Hb = 0.6
Wb = 1
xb = 2
La = 1.5
Lc = 0.9
Lv = 0.6
Lp = 0.2
Dp = 0.45
beta = 40

#Stap 2
plt.figure(1)

Sx = [0, B, B, 0, 0]
Sy = [0, 0, H, H, 0]

Ax = [xb, xb+Wb, xb+Wb, xb, xb]
Ay = [0, 0, Hb, Hb, 0]

plt.plot(Sx, Sy, "--g")
plt.plot(Ax, Ay, "--k")

#Stap 3
betar = beta/360 * 2*np.pi
Wc = Lc*np.sin(betar)
Hc = Lc*np.cos(betar)
Ap = 2*Wc - Lv

#Stap 4
plt.figure(2)

Rx1 = [xb-Lv, xb-Lv, xb-Lv+Wc, xb+Ap]
Ry1 = [0, La, La+Hc, La]

Rx2 = [Rx1[3], Rx1[3]]
Ry2 = [Ry1[3], Ry1[3] - Lp]

plt.plot(Rx1, Ry1, "-o")
plt.plot(Rx2, Ry2, "-o")

#Stap 5
plt.figure(3)

gam = np.linspace(0, 360, 91)
gamr = gam/360 * 2*np.pi

Dx = (Dp/2)*np.cos(gamr)
Dy = (Dp/2)*np.sin(gamr)

Dxp = Rx2[1] + (Dp/2)*np.cos(gamr)
Dyp = Ry2[1] - (Dp/2) + (Dp/2)*np.sin(gamr)

plt.plot(Dx, Dy, Dxp, Dyp)
plt.axis("scaled")

#Stap 6
plt.figure(4)

plt.plot(Sx, Sy, "--g")
plt.plot(Ax, Ay, "--k")
plt.plot(Rx1, Ry1, "-ob")
plt.plot(Rx2, Ry2, "-or")
plt.plot(Dxp, Dyp, "-r")
plt.axis("scaled")

#Stap 7
plt.figure(5)

n = 5
beta = np.linspace(25, 45, n)
betar = beta/360 * 2*np.pi
Wc = Lc*np.sin(betar)
Hc = Lc*np.cos(betar)
Ap = 2*Wc - Lv

Rx1 = np.zeros((n, 4))
Ry1 = np.zeros((n, 4))
Rx2 = np.zeros((n, 2))
Ry2 = np.zeros((n, 2))

for i in range(n):
    Rx1[i,0], Rx1[i,1], Rx1[i,2], Rx1[i,3] = xb-Lv, xb-Lv, xb-Lv+Wc[i], xb+Ap[i]
    Ry1[i,0], Ry1[i,1], Ry1[i,2], Ry1[i,3] = 0, La, La+Hc[i], La
    
    Rx2[i,0], Rx2[i,1] = Rx1[i,3], Rx1[i,3]
    Ry2[i,0], Ry2[i,1] = Ry1[i,3], Ry1[i,3] - Lp
    
for i in range(n):
    plt.plot(Sx, Sy, "--g")
    plt.plot(Ax, Ay, "--k")
    plt.plot(Rx1[i], Ry1[i], "-ob")
    plt.plot(Rx2[i], Ry2[i], "-or")
    plt.axis("scaled")
    
    
#Stap 8
plt.figure(6)

n = 5
beta = np.linspace(25, 45, n)
betar = beta/360 * 2*np.pi

Hm = 1
Lm = 0.65
Dm = 0.3
Mp = 80
Mm = 50

Wc = Lc*np.sin(betar)
Hc = Lc*np.cos(betar)
Ap = 2*Wc - Lv
Am = Ap*Mp / Mm
dxm = Am - Lv
dym = np.sqrt(Lm**2 - dxm**2)

Rx1 = np.zeros((n, 4))
Ry1 = np.zeros((n, 4))
Rx2 = np.zeros((n, 2))
Ry2 = np.zeros((n, 2))
Emx = np.zeros((n, 2))
Emy = np.zeros((n, 2))

for i in range(n):
    Rx1[i,0], Rx1[i,1], Rx1[i,2], Rx1[i,3] = xb-Lv, xb-Lv, xb-Lv+Wc[i], xb+Ap[i]
    Ry1[i,0], Ry1[i,1], Ry1[i,2], Ry1[i,3] = 0, La, La+Hc[i], La
    
    Rx2[i,0], Rx2[i,1] = Rx1[i,3], Rx1[i,3]
    Ry2[i,0], Ry2[i,1] = Ry1[i,3], Ry1[i,3] - Lp
    
    Emx[i,0], Emx[i,1] = xb-Lv, xb-Lv-dxm[i]
    Emy[i,0], Emy[i,1] = Hm, Hm+dym[i]
    
for i in range(n):
    plt.plot(Sx, Sy, "--g")
    plt.plot(Ax, Ay, "--k")
    plt.plot(Rx1[i], Ry1[i], "-ob")
    plt.plot(Rx2[i], Ry2[i], "-or")
    plt.plot(Emx[i], Emy[i], "-oy")
    plt.axis("scaled")









