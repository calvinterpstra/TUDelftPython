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
m = np.linspace(0.45,0.45, 100000); # np.linspace(0.3,1.5, 100000); #0.4; # Mass
h = 1.7; # Height
s = 5; # Length of slope
phi = np.arcsin(h/s); # Slope
Cr = 0.002; # Rolling resistance rubber wheel
d = 2; # Flat distance to finish
rho = 1.225; # Air density
v = 3.61663 *0.9; # Average velocity
Cw = 0.5; # Air resistance constant
Af = 0.08*0.15*0.5; # Frontal Area
mu = 0.002; # Friction coefficient in bearing
Daxel = 0.004; # Diameter of axel
Dwheel = np.linspace(0.060,0.170, 100000); #0.150 # np.linspace(0.075,0.170, 10000); # Diameter of wheel
Crlager = mu*(Daxel/Dwheel); # Rolling resistance steel bearing
#x = np.linspace(0.1,0.5, 100000); #np.linspace(0.1,0.5, 100000);
x = (s+d)*(Daxel/Dwheel);

def Eg(x):
    return m*g*h; # Grav. potential energy
def Erol(x):
    return Cr*m*g*np.cos(phi)*s + Cr*m*g*d; # Energy loss due to rolling resistance (one way)
def ErolLager(x):
    return Crlager*m*g*np.cos(phi)*s + Crlager*m*g*d;
def Eair(x):
    return 0.5*rho*(v**2)*Cw*Af*(s+d); # Energy loss due to air resistance (one way)
def Ebear(x): 
    return 2*(mu*(m*g*h - Eair(x) - ErolLager(x) - Erol(x))); # Energy loss due to internal forces in bearing (one way)
def Elost(x):
    return (Erol(x) + Eair(x) + Ebear(x) + ErolLager(x)); # Energy lost (one way)
def solveDh(x):
    return Elost(x)/(m*g);

def ErolReturn(x, dh):
    return Cr*m*g*np.cos(phi)*((h-dh)/np.sin(phi)) + Cr*m*g*d; # Energy loss due to rolling resistance (one way)
def ErolLagerReturn(x, dh):
    return Crlager*m*g*np.cos(phi)*((h-dh)/np.sin(phi)) + Crlager*m*g*d;
def EairReturn(x, dh):
    return 0.5*rho*(v**2)*Cw*Af*(((h-dh)/np.sin(phi))+d); # Energy loss due to air resistance (one way)
def EbearReturn(x, dh): 
    return 2*(mu*m*g*(h-dh)); # Energy loss due to internal forces in bearing (one way)
def ElostFull(x):
    return Elost(x) + (ErolReturn(x, solveDh(x)) + EairReturn(x, solveDh(x)) + EbearReturn(x, solveDh(x)) + ErolLagerReturn(x, solveDh(x))); # Energy lost (one way)
def solveK(x):
    return 2*(Eg(x) + Erol(x) + Eair(x) + Ebear(x) + ErolLager(x))/(x**2);
def redement(x):
    return (Eg(x)-ElostFull(x))/Eg(x);

def main():
    print("x:",x);
    k = solveK(x);
    print("k:",k);
    plt.figure(1);
    plt.plot(x, k);
    plt.show();
    print("x vs k");
    plt.figure(2);
    plt.plot(k/x, redement(x));
    plt.show();
    print("k/x vs redement");
    plt.figure(3);
    plt.plot(Dwheel, redement(x));
    plt.show();
    print("Dwheel vs redement");
    print("lost in rol:     ",((Erol(x) + ErolReturn(x, solveDh(x)))/Eg(x))[0]*100,",", ((Erol(x) + ErolReturn(x, solveDh(x)))/Eg(x))[x.size-1]*100);
    print("lost in rol bear:",((ErolLager(x) + ErolLagerReturn(x, solveDh(x)))/Eg(x))[0]*100,",", ((ErolLager(x) + ErolLagerReturn(x, solveDh(x)))/Eg(x))[x.size-1]*100);
    print("lost in air:     ",((Eair(x) + EairReturn(x, solveDh(x)))/Eg(x))[0]*100,",", ((Eair(x) + EairReturn(x, solveDh(x)))/Eg(x))[x.size-1]*100);
    print("lost in bear:    ",((Ebear(x) + EbearReturn(x, solveDh(x)))/Eg(x))[0]*100,",", ((Ebear(x) + EbearReturn(x, solveDh(x)))/Eg(x))[x.size-1]*100);
    print("diff in redement:",((redement(x)[0]-redement(x)[x.size-1])*-100));
    print("redement:", redement(x)[0]*100,",",redement(x)[x.size-1]*100);
    
    
main();