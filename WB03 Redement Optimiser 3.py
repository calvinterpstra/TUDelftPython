# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 14:48:33 2017

@author: Calvin
"""

from math import *;
import numpy as np;
import matplotlib.pyplot as plt;
import numpy.linalg as lg;

k = 0; # Spring constant
x = 0; # Spring dispacement
g = 9.81; # Grav const.
m = 0.4; # Mass
h = 1.7; # Height
s = 5; # Length of slope
phi = np.arcsin(h/s); # Slope
Cr = 0.006; # Rolling resistance
d = 2; # Flat distance to finish
rho = 1.225; # Air density
v = np.sqrt(2*g*h); # Peak velocity
Cw = 0.5; # Air resistance constant
Af = 0.08*0.15*0.5; # Frontal Area
mu = 0.002; # Friction coefficient in bearing

Daxel = 0.004; # Diameter of axel
dx = 0.0001;
Dwheel = np.linspace(0.075,0.170, (s+d)/dx); # Diameter of wheel

def Eg(x):
    return m*g*h; # Grav. potential energy
def Erol(x):
    return Cr*m*g*np.cos(phi)*s + Cr*m*g*d; # Energy loss due to rolling resistance (one way)
def Eair(x):
    return 0.5*rho*(v**2)*Cw*Af*(s+d); # Energy loss due to air resistance (one way)
def Ebear(x): 
    return (mu*m*g*h*(s+d)*Daxel)/(x*Dwheel); # Energy loss due to internal forces in bearing (one way)
def Elost(x):
    return (Erol(x) + Eair(x) + Ebear(x)); # Energy lost (one way)
def solveDh(x):
    return Elost(x)/(m*g);
def ErolReturn(x, dh):
    return Cr*m*g*np.cos(phi)*(((h-dh)/np.sin(phi))+d); # Energy loss due to rolling resistance (one way)
def EairReturn(x, dh):
    return 0.5*rho*(v**2)*Cw*Af*(((h-dh)/np.sin(phi))+d); # Energy loss due to air resistance (one way)
def EbearReturn(x, dh): 
    return (mu*m*g*h*(((h-dh)/np.sin(phi))+d)*Daxel)/(x*Dwheel); # Energy loss due to internal forces in bearing (one way)
def ElostFull(x):
    return Elost(x) + (ErolReturn(x, solveDh(x)) + EairReturn(x, solveDh(x)) + EbearReturn(x, solveDh(x))); # Energy lost (one way)
def solveApproxK(x):
    return 2*(Eg(x) + Erol(x) + Eair(x) + Ebear(x))/(x**2);


def dxs(dx1, dx2):
    return (dx1+dx2)*(Daxel/Dwheel);
def xs(dx1, dx2):
    return np.sum(dx1+dx2)*(Daxel/Dwheel);
def dEs(dx1, dx2, k):
     return 0.5*k*dxs(dx1, dx2)^2;
def dEg(dx1, dx2, k):
    return m*g*dx1*np.sin(phi); # Grav. potential energy
def dErol(dx1, dx2, k):
    return Cr*m*g*np.cos(phi)*dx1 + Cr*m*g*dx2; # Energy loss due to rolling resistance (one way)
def dEbear(dx1, dx2, k): 
    return (mu*m*g*h*(s+d)*Daxel)/(x*Dwheel); # Energy loss due to internal forces in bearing (one way)
def dv(dx1, dx2, k):
    return np.sqrt(2*g*dx1*np.sin(phi)); # - ((k**dxs(dx1,dx2)**2)/m)));
def vx(dx1, dx2, k):
    return np.sqrt(np.abs(2*g*np.sum(dx1)*np.sin(phi))); # np.sqrt(np.abs(2*g*x1*np.sin(phi) - ((k**((x1+x2)*(Daxel/Dwheel))**2)/m)));
def dEair(dx1, dx2, k):
    return 0.5*rho*(np.power(dv(dx1, dx2, k),2))*Cw*Af*(s+d); # Energy loss due to air resistance (one way)

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

# v = sqrt(a^2 k x1^2 + 2 a^2 k x1 x2 + a^2 k x2^2 - 2 g m R w^2 cos(p) (2 x1 + x2) - 2 g m w^2 x1 sin(p) + 2 g m R w^2 x2)/sqrt(w^2 (A P W (x1 + x2) + m))

def main():
    x1 = np.append(np.linspace(0, s, s/dx), np.linspace(0, 0, d/dx));
    dx1 = np.append(np.linspace(dx, dx, s/dx), np.linspace(0, 0, d/dx));
    x2 = np.append(np.linspace(0, 0, s/dx), np.linspace(s, d, d/dx));
    dx2 = np.append(np.linspace(0, 0, s/dx), np.linspace(dx, dx, d/dx));
    
    x = xs(dx1, dx2);
    k = solveApproxK(x);
    v = np.sum(dv(dx1, dx2,k)*dx);
    print("k approx:",k);
    print("v:",v);
    
    print(2*g*dx1*np.sin(phi) - ((k**dxs(dx1,dx2)**2)/m));
        
    
    
    plt.show();
    
    
main();