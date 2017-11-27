# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 17:39:44 2017

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
#v = np.sqrt(2*g*h); # Peak velocity
Cw = 0.5; # Air resistance constant
Af = 0.08*0.15*0.5; # Frontal Area
mu = 0.002; # Friction coefficient in bearing
Daxel = 0.004; # Diameter of axel
#Dwheel = 0.150; # Diameter of wheel

def v(x):
    return np.sqrt(2*g*h-(k*s*(Daxel/Dwheel))/m);
def Eg(x):
    return m*g*h; # Grav. potential energy
def Ek(x):
    return 0.5*m*v(x)**2; # Kinetic energy
def Erol(x):
    return Cr*m*g*np.cos(phi)*(s+d); # Energy loss due to rolling resistance (one way)
def Eair(x):
    return 0.5*rho*(v(x)**2)*Cw*Af*(s+d); # Energy loss due to air resistance (one way)
def Ebear(x): 
    return (mu*m*g*h*(s+d)*Daxel)/(x*Dwheel); # Energy loss due to internal forces in bearing (one way)
def solveK(x):
    return 2*(Eg(x) + Erol(x) + Eair(x) + Ebear(x))/(x**2);
def Elost(x):
    return (Erol(x) + Eair(x) + Ebear(x)); # Energy lost (one way)
def solveDh(x):
    return Elost(x)/(m*g);
def ErolReturn(x, dh):
    return Cr*m*g*np.cos(phi)*(((h-dh)/np.sin(phi))+d); # Energy loss due to rolling resistance (one way)
def EairReturn(x, dh):
    return 0.5*rho*(v(x)**2)*Cw*Af*(((h-dh)/np.sin(phi))+d); # Energy loss due to air resistance (one way)
def EbearReturn(x, dh): 
    return (mu*m*g*h*(((h-dh)/np.sin(phi))+d)*Daxel)/(x*Dwheel); # Energy loss due to internal forces in bearing (one way)
def ElostFull(x):
    return Elost(x) + (ErolReturn(x, solveDh(x)) + EairReturn(x, solveDh(x)) + EbearReturn(x, solveDh(x))); # Energy lost (one way)
def redement(x):
    return (Eg(x)-ElostFull(x))/Eg(x);

def main():
    #x = 0.025;
    #x = np.linspace(0.1,0.5, 100000);
    Dwheel = np.linspace(0.075,0.170, 100000);
    x = (s+d)*(Daxel/Dwheel)
    print(x);
    print(solveDh(x));
    k = solveK(x);
    plt.figure(1);
    plt.plot(x, k);
    plt.figure(2);
    plt.plot(k/x, redement(x));
    print(v(x));
    print("lost in rol",((Erol(x) + ErolReturn(x, solveDh(x)))/Eg(x))[0],",", ((Erol(x) + ErolReturn(x, solveDh(x)))/Eg(x))[x.size-1]);
    print("lost in air",((Eair(x) + EairReturn(x, solveDh(x)))/Eg(x))[0],",", ((Eair(x) + EairReturn(x, solveDh(x)))/Eg(x))[x.size-1]);
    print("lost in bear",((Ebear(x) + EbearReturn(x, solveDh(x)))/Eg(x))[0],",", ((Ebear(x) + EbearReturn(x, solveDh(x)))/Eg(x))[x.size-1]);
    print("diff in redement",redement(x[0])-redement(x[1]));
    
    plt.show();
    
    
main();