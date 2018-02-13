# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 16:50:43 2018

@author: Calvin
"""

import numpy as np
import matplotlib.pyplot as plt

#Stap 1
A1 = 14
A2 = 12

H1 = 0.5*A1
H2 = 0.5*A2

L1 = 5
L2 = 1.7
L3 = 0.2*L1

alpha = 20
beta = 90
gamma = 60

n = 6

#Stap 2
plt.figure(1)

Ax = [0, 0, A2, A2, 0]
Ay = [0, A1, A1, 0, 0]

plt.plot(Ax, Ay, "g--", linewidth = 2)
plt.axis("scaled")
plt.title('de pick en place robotarm')
plt.xlabel('afstand X richting [m]')
plt.ylabel('afstand Y richting [m]')
plt.axis([-2, A2+2, -1, A1+1])

#Stap 3
plt.figure(2)

alfar = alpha/360 * 2*np.pi
betar = beta/360 * 2*np.pi
gammar = gamma/360 * 2*np.pi

Rx1 = [H2, H2+L1*np.cos(alfar)]
Ry1 = [H1, H1+L1*np.sin(alfar)]

Rx2 = [Rx1[1], Rx1[1]+L2*np.cos(betar)]
Ry2 = [Ry1[1], Ry1[1]+L2*np.sin(betar)]

Rx3 = [Rx2[1]-L3*np.cos(gammar), Rx2[1]+L3*np.cos(gammar)]
Ry3 = [Ry2[1]-L3*np.sin(gammar), Ry2[1]+L3*np.sin(gammar)]

Rx4 = [Rx3[0], Rx3[0]+L3*np.cos(-np.pi/2)]
Ry4 = [Ry3[0], Ry3[0]+L3*np.sin(-np.pi/2)]

Rx5 = [Rx3[1], Rx3[1]+L3*np.cos(-np.pi/2)]
Ry5 = [Ry3[1], Ry3[1]+L3*np.sin(-np.pi/2)]

plt.plot(Rx1, Ry1, "-ok", linewidth = 2)
plt.plot(Rx2, Ry2, "-ok", linewidth = 2)
plt.plot(Rx3, Ry3, "-k", linewidth = 2)
plt.plot(Rx4, Ry4, "--k", linewidth = 2)
plt.plot(Rx5, Ry5, "--k", linewidth = 2)

#Stap 4
plt.figure(3)

gam = np.linspace(0, 360, 91)
Dx = L3*np.cos(gam/360 * 2*np.pi)
Dy = L3*np.sin(gam/360 * 2*np.pi)

Mx3 = Rx2[1] + L3*np.cos(gam/360 * 2*np.pi)
My3 = Ry2[1] + L3*np.sin(gam/360 * 2*np.pi)

plt.plot(Dx, Dy, "-k", linewidth = 2)
plt.plot(Mx3, My3, "-k", linewidth = 2)
plt.axis("scaled")

#Stap 5
plt.figure(4)

plt.plot(Ax, Ay, "g--", linewidth = 2)
plt.axis("scaled")
plt.title('de pick en place robotarm')
plt.xlabel('afstand X richting [m]')
plt.ylabel('afstand Y richting [m]')
plt.plot(Rx1, Ry1, "-ok", linewidth = 2)
plt.plot(Rx2, Ry2, "-ok", linewidth = 2)
plt.plot(Rx3, Ry3, "-k", linewidth = 2)
plt.plot(Mx3, My3, ":r", linewidth = 2)

#Stap 6
plt.figure(5)

alfa = np.linspace(20, 320, n)
beta = np.linspace(90, 430, n)
gamma = np.linspace(60, 310, n)
alfar = alfa/360 * 2*np.pi
betar = beta/360 * 2*np.pi
gammar = gamma/360 * 2*np.pi
print(alfar)

Rx1 = np.zeros((n,2)) 
Ry1 = np.zeros((n,2))
Rx2 = np.zeros((n,2)) 
Ry2 = np.zeros((n,2))
Rx3 = np.zeros((n,2)) 
Ry3 = np.zeros((n,2))

for i in range(n):
    Rx1[i,0], Rx1[i,1] = H2, H2+L1*np.cos(alfar[i])
    Ry1[i,:] = H1+np.array([0,L1*np.sin(alfar[i])])
    Rx2[i,:] = Rx1[i,1]+np.array([0, L2*np.cos(betar[i])])
    Ry2[i,:] = Ry1[i,1]+np.array([0, L2*np.sin(betar[i])])
    Rx3[i,:] = Rx2[i,1]+np.array([-L3*np.cos(gammar[i]),L3*np.cos(gammar[i])])
    Ry3[i,:] = Ry2[i,1]+np.array([-L3*np.sin(gammar[i]),L3*np.sin(gammar[i])])
'''   
Rx1[:, 0], Rx1[:, 1] = H2, H2 + L1*np.cos(alfar)
Ry1[:, 0], Ry1[:, 1] = H1, H1 + L1*np.sin(alfar)
Rx2[:, 0], Rx2[:, 1] = Rx1[:, 1], Rx1[:, 1] + L2*np.cos(betar)
Ry2[:, 0], Ry2[:, 1] = Ry1[:, 1], Ry1[:, 1] + L2*np.sin(betar)
Rx3[:, 0], Rx3[:, 1] = Rx2[:,1]-L3*np.cos(gammar), Rx2[:,1]+L3*np.cos(gammar)
Ry3[:, 0], Ry3[:, 1] = Ry2[:,1]-L3*np.sin(gammar), Ry2[:,1]+L3*np.sin(gammar)
'''
for i in range(n):
    plt.plot(Rx1[i], Ry1[i], "-ok", linewidth = 2)
    plt.plot(Rx2[i], Ry2[i], "-ok", linewidth = 2)
    plt.plot(Rx3[i], Ry3[i], "-k", linewidth = 2)
    plt.axis("scaled")
    
#Stap 7
Mx3 = np.zeros((n,91))
My3 = np.zeros((n,91))

for i in range(n):
    Mx3[i] = Rx2[i,1] + L3*np.cos(gam/360 * 2*np.pi)
    My3[i] = Ry2[i,1] + L3*np.sin(gam/360 * 2*np.pi)

for i in range(n):
    plt.plot(Rx1[i], Ry1[i], "-ok", linewidth = 2)
    plt.plot(Rx2[i], Ry2[i], "-ok", linewidth = 2)
    plt.plot(Rx3[i], Ry3[i], "-k", linewidth = 2)
    plt.plot(Mx3[i], My3[i], ":r", linewidth = 2)
    plt.plot(Ax, Ay, "g--", linewidth = 2)
    plt.axis("scaled")
    plt.axis([-2, A2+2, -1, A1+1])
    
#Stap 8
#plt.text(0.5, 0.5, "L2 = 1.7 [m]")


