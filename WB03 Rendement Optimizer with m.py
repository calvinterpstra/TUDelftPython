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
m = np.linspace(0.35,1.5, 100000); # np.linspace(0.3,1.5, 100000); #0.4; # Mass
h = 1.5; # Height
s = 5; # Length of slope
phi = np.arcsin(h/s); # Slope
Cr = 0.002; # Rolling resistance rubber wheel
d = 2; # Flat distance to finish
rho = 1.225; # Air density
v = 3.61663 *0.9; # Average velocity
Cw = 0.5; # Air resistance constant
Af = 0.08*0.05; # Frontal Area
mu = 0.002; # Friction coefficient in bearing
Daxel = 0.004; # Diameter of axel
Dwheel = np.linspace(0.072,0.072, 100000); #0.150 # np.linspace(0.075,0.170, 10000); # Diameter of wheel
Crlager = mu*(Daxel/Dwheel); # Rolling resistance steel bearing
#x = np.linspace(0.1,0.5, 100000); #np.linspace(0.1,0.5, 100000);
x = (s+d)*(Daxel/Dwheel);
alpha = 170;
alpha = (alpha/360)*2*np.pi;

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
    return 2*(Eg(x) - Erol(x) - Eair(x) - Ebear(x) - ErolLager(x))/(x**2);
def rendement(x):
    return (Eg(x)-ElostFull(x))/Eg(x);

def main():
    print("x:",x[0]);
    print("m:",m);
    k = solveK(x);
    print("k:",k);
    plt.figure(1);
    plt.plot(m, k);
    plt.title("m vs k");
    plt.show();
    plt.figure(2);
    plt.plot(m, rendement(x));
    plt.title("m vs rendement");
    plt.show();
    print("lost in rol:     ",((Erol(x) + ErolReturn(x, solveDh(x)))/Eg(x))[0]*100,",", ((Erol(x) + ErolReturn(x, solveDh(x)))/Eg(x))[x.size-1]*100);
    print("lost in rol bear:",((ErolLager(x) + ErolLagerReturn(x, solveDh(x)))/Eg(x))[0]*100,",", ((ErolLager(x) + ErolLagerReturn(x, solveDh(x)))/Eg(x))[x.size-1]*100);
    print("lost in air:     ",((Eair(x) + EairReturn(x, solveDh(x)))/Eg(x))[0]*100,",", ((Eair(x) + EairReturn(x, solveDh(x)))/Eg(x))[x.size-1]*100);
    print("lost in bear:    ",((Ebear(x) + EbearReturn(x, solveDh(x)))/Eg(x))[0]*100,",", ((Ebear(x) + EbearReturn(x, solveDh(x)))/Eg(x))[x.size-1]*100);
    print("diff in rendement:",((rendement(x)[0]-rendement(x)[x.size-1])*-100));
    print("rendement:", rendement(x)[0]*100,",",rendement(x)[x.size-1]*100);
    
    
    
    l = np.sqrt((x**2)/(2*(1-np.cos(alpha))));
    e = 0.5*k*(x**2);
    kTors = (2*e)/(alpha**2);
    beta = np.linspace(alpha, 0, x.size);
    xval = 0;
    dx = np.linspace(0, x[xval], x.size);
    r = l[xval]*np.cos(beta/2);
    f = ((alpha-beta)*kTors[xval])/r;
    muWheel = f*(Daxel/Dwheel);
    f2 = k[xval]*dx;
    fMax = (alpha*kTors)/l;
    fMax2 = k*x;
    MPeak = (alpha*kTors);
    fPeakTorsionAttatchment = (alpha*kTors)/0.01;
    muWheel = (fMax*(Daxel/Dwheel)/(m*g*0.6));
    muWheel2 = (fMax2*(Daxel/Dwheel)/(m*g*0.6));
    
    print("M/2 peak:", MPeak[0]*1000/2, "Nmm");
    print("M/2 per rad:", kTors[0]*1000/2, "Nmm/rad");
    print("M/2 per deg: {:5.3f} Nmm/deg". format(((kTors[0]*(2*np.pi))/360)*1000/2))

    plt.figure(3);
    plt.plot(m, l*100);
    plt.title("m vs l (cm)");
    plt.show();
    print("l:", l[0]*100 ,"cm,", l[l.size-1]*100,"cm");
    
    plt.figure(4);
    plt.plot(m, kTors);
    plt.title("m vs kTors (N/rad)");
    plt.show();
    print("kTors:", kTors[0] ,"N/rad,", kTors[kTors.size-1], "N/rad");
    
    plt.figure(5);
    plt.plot(dx, f);
    plt.plot(dx, f2);
    plt.title("x vs f");
    plt.show();
    print("fmax for min m:                  ", f[beta.size-1], "N");
    print("fmax if reg. spring for min m:   ", f2[beta.size-1], "N");
    
    plt.figure(6);
    plt.plot(m, fMax);
    plt.title("m vs fMax (axel)");
    plt.show();
    print("f peak (axel):               ", fMax[0] ,"N,", fMax[fMax.size-1], "N");
    print("f peak (torsion attatment):  ", fPeakTorsionAttatchment[0] ,"N,", fPeakTorsionAttatchment[fPeakTorsionAttatchment.size-1], "N");
    
    plt.figure(7);
    plt.plot(m, muWheel);
    plt.title("m vs mu (wheel)");
    plt.show();
    print("mu (wheel):                  ", muWheel[0] ,",", muWheel[muWheel.size-1]);
    print("mu (wheel) if reg. spring:   ", muWheel2[0] ,",", muWheel2[muWheel2.size-1]);
    
    
main();