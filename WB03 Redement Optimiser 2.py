# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 08:31:13 2017

@author: Calvin
"""

from math import *;
import numpy as np;
import matplotlib.pyplot as plt;
import numpy.linalg as lg;

k = 0; # Spring constant
xs = 0; # Spring dispacement
g = 9.81; # Grav const.
m = 0.4; # Mass
h = 1.7; # Height
s = 5; # Length of slope
phi = np.arcsin(h/s); # Slope
Cr = 0.006; # Rolling resistance
d = 2; # Flat distance to finish
rho = 1.225; # Air density
#v = np.sqrt(2*g*h); # Peak velocity
Cw = 0.5; # Air resistance constant
Af = 0.08*0.15*0.5; # Frontal Area
mu = 0.002; # Friction coefficient in bearing
Daxel = 0.004; # Diameter of axel
#Dwheel = 0.150; # Diameter of wheel
def dxs(dx1, dx2):
    return (dx1+dx2)*(Daxel/Dwheel);
 def dEs(dx1, dx2):
     return 0.5*k*dxs(dx1, dx2)^2;
def dEg(dx1, dx2):
    return m*g*dx1*np.sin(phi); # Grav. potential energy
def dEk(dx1, dx2):
    return 0.5*m*v(dx1, dx2)**2; # Kinetic energy
def dErol(dx1, dx2):
    return Cr*m*g*np.cos(phi)*(s+d); # Energy loss due to rolling resistance (one way)
def dEbear(dx1, dx2): 
    return (mu*m*g*h*(s+d)*Daxel)/(x*Dwheel); # Energy loss due to internal forces in bearing (one way)
def dv(dx1, dx2):
    return np.sqrt((2*())/(m-))
def dEair(dx1, dx2):
    return 0.5*rho*(v(dx)**2)*Cw*Af*(s+d); # Energy loss due to air resistance (one way)

def solveK(dx1, dx2):
    return 2*(Eg(dx) + Erol(dx) + Eair(dx) + Ebear(dx))/(dx**2);
def dElost(dx1, dx2):
    return (Erol(dx) + Eair(dx) + Ebear(dx)); # Energy lost (one way)
def solveDh(dx1, dx2):
    return Elost(dx)/(m*g);

def dErolReturn(dx1, dx2, dh):
    return Cr*m*g*np.cos(phi)*(((h-dh)/np.sin(phi))+d); # Energy loss due to rolling resistance (one way)
def dEairReturn(dx1, dx2, dh):
    return 0.5*rho*(v(dx)**2)*Cw*Af*(((h-dh)/np.sin(phi))+d); # Energy loss due to air resistance (one way)
def dEbearReturn(dx1, dx2, dh): 
    return (mu*m*g*h*(((h-dh)/np.sin(phi))+d)*Daxel)/(dx*Dwheel); # Energy loss due to internal forces in bearing (one way)
def dElostFull(dx1, dx2):
    return Elost(dx) + (ErolReturn(dx, solveDh(dx)) + EairReturn(dx, solveDh(dx)) + EbearReturn(dx, solveDh(dx))); # Energy lost (one way)

def dredement(dx1, dx2):
    return (Eg(dx)-ElostFull(dx))/Eg(dx);

def main():
    dx = 0.00001
    x1 = np.append(np.linspace(0, s, s/dx), np.linspace(0, 0, d/dx));
    dx1 = np.append(np.linspace(dx, dx, s/dx), np.linspace(0, 0, d/dx));
    x2 = np.append(np.linspace(0, 0, s/dx), np.linspace(s, d, d/dx));
    dx2 = np.append(np.linspace(0, 0, s/dx), np.linspace(dx, dx, d/dx));
    
    
    plt.show();
    
    
main();
