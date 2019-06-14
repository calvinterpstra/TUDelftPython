# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 09:03:32 2017

@author: Calvin
"""

from math import *;
import numpy as np;
import matplotlib.pyplot as plt;
import scipy as sp;

quality = 100;
g = 9.81; # Grav const.
m = 0.35; # Mass
h = np.linspace(1.45, 1.5, quality); # Height
phi = np.arcsin(1.5/5); # Slope
s = h/np.sin(phi); # Length of slope
Cr = 0.0025; # Rolling resistance rubber wheel
d = 2.1; # Flat distance to finish
rho = 1.225; # Air density
Cw = 0.5; # Air resistance constant
Af = 0.05*0.03; # Frontal Area
mu = 0.06; # Friction coefficient in bearing
Daxel = 0.004; # Diameter of axel
Dwheel = 0.072; # Diameter of wheel
CrBear = mu*(Daxel/Dwheel); # Rolling resistance steel bearing
alpha = 170;
alpha = (alpha/360)*2*np.pi;
rTSpring = 0.01;
hysteresisCoef = 0.98;
x = (s+d)*(Daxel/Dwheel); # Spring dispacement

def avgVelocity(k):
    a = 0;
    b = h;
    avgVel = np.array([])
    for i in range(b.size):
        f = lambda h: np.sqrt(np.abs(2*g*h - (k[i]*x[i]**2)/m));
        avgVel = np.append(avgVel, [sp.integrate.quad(f, a, b[i])[0] / (b[i]-a)]);
    return avgVel;

def avgF(k):
    a = 0;
    b = x;
    avgF = np.array([])
    for i in range(b.size):
        f = lambda x: k[i]*x;
        avgF = np.append(avgF, [sp.integrate.quad(f, a, b[i])[0] / (b[i]-a)]);
    return avgF;

def avgFpeak(k):
    a = 0;
    b = x;
    avgF = np.array([])
    for i in range(b.size):
        f = lambda x: ((2*(0.5*k[i]*(x**2)))/(alpha))/rTSpring;
        avgF = np.append(avgF, [sp.integrate.quad(f, a, b[i])[0] / (b[i]-a)]);
    return avgF;

def Eg():
    return m*g*h; # Grav. potential energy
def Erol():
    return Cr*m*g*np.cos(phi)*s + Cr*m*g*d; # Energy loss due to rolling resistance (one way)
def ErolBear():
    return CrBear*m*g*np.cos(phi)*s + CrBear*m*g*d;
def Eair(k):
    return 0.5*rho*(avgVelocity(k)**2)*Cw*Af*(s+d); # Energy loss due to air resistance (one way)
def Ebear(k): 
    return mu*(avgF(k)*x) + avgFpeak(k)*Daxel*0.5*alpha*mu; # Energy loss due to internal forces in bearing (one way)
def Elost(k):
    return (Erol() + Eair(k) + Ebear(k) + ErolBear()); # Energy lost (one way)
def solveDh(k):
    return Elost(k)/(m*g);

def ErolReturn(dh):
    return Cr*m*g*np.cos(phi)*((h-dh)/np.sin(phi)) + Cr*m*g*d; # Energy loss due to rolling resistance (one way)
def ErolBearReturn(dh):
    return CrBear*m*g*np.cos(phi)*((h-dh)/np.sin(phi)) + CrBear*m*g*d;
def EairReturn(k, dh):
    return 0.5*rho*(avgVelocity(k)**2)*Cw*Af*(((h-dh)/np.sin(phi))+d); # Energy loss due to air resistance (one way)
def EbearReturn(k, dh): 
    return mu*(avgF(k)*x)*(dh/h) + avgFpeak(k)*Daxel*alpha*mu*(dh/h); # Energy loss due to internal forces in bearing (one way)
def ElostFull(k):
    return (Elost(k) + (ErolReturn(solveDh(k)) + EairReturn(k, solveDh(k)) + EbearReturn(k, solveDh(k)) + ErolBearReturn(solveDh(k)))); # Energy lost (one way)
def solveK(k):
    return 2*((Eg() - Elost(k))*hysteresisCoef)/(x**2);
def rendement(k):
    return ((Eg()-ElostFull(k))*(hysteresisCoef**2))/Eg();

def solveX(k):
    return np.sqrt(2*((Eg() - Elost(k))*hysteresisCoef)/k) * (Dwheel/Daxel);

def main():
    k = np.linspace(1, 1, quality); # Spring constant
    
    
    errorPower = 10;
    print("Loading <", end=' ');
    error1, error2 = 1, 1;
    while(not(np.abs(error1) < (10**-errorPower) and np.abs(error2) < (10**-errorPower))): 
        kOld = k;
        k = solveK(k);
        error1, error2 = (kOld[0]-k[0])/k[0], (kOld[quality-1]-k[quality-1])/k[quality-1];
        #print("(",error1,error2,")", end=' ');
        print("-", end=' ');
    print(">");
    
    print("v:", avgVelocity(k)[0],",", avgVelocity(k)[quality-1]);
    print("x:", x[0],",", x[quality-1]);
    print("X:", (s+d)[0],",", (s+d)[quality-1]);
    print("m:", m);
    print("k:",k[0],",", k[quality-1]);
    
    print("lost in rol:     ",((Erol() + ErolReturn(solveDh(k)))/Eg())[0]*100,",", ((Erol() + ErolReturn(solveDh(k)))/Eg())[quality-1]*100);
    print("lost in rol bear:",((ErolBear() + ErolBearReturn(solveDh(k)))/Eg())[0]*100,",", ((ErolBear() + ErolBearReturn(solveDh(k)))/Eg())[quality-1]*100);
    print("lost in air:     ",((Eair(k) + EairReturn(k, solveDh(k)))/Eg())[0]*100,",", ((Eair(k) + EairReturn(k, solveDh(k)))/Eg())[quality-1]*100);
    print("lost in bear:    ",((Ebear(k) + EbearReturn(k, solveDh(k)))/Eg())[0]*100,",", ((Ebear(k) + EbearReturn(k, solveDh(k)))/Eg())[quality-1]*100);
    print("diff in rendement:",((rendement(k)[0]-rendement(k)[quality-1])*-100));
    print("rendement:", rendement(k)[0]*100,",",rendement(k)[quality-1]*100);
    
    l = np.sqrt((x**2)/(2*(1-np.cos(alpha))));
    e = 0.5*k*(x**2);
    kTors = (2*e)/(alpha**2);
    beta = np.linspace(alpha, 0, quality);
    xval = 0;
    dx = np.linspace(0, x[xval], quality);
    r = l[xval]*np.cos(beta/2);
    f = ((alpha-beta)*kTors[xval])/r;
    muWheel = f*(Daxel/Dwheel);
    f2 = k[xval]*dx;
    fMax = (alpha*kTors)/l;
    fMax2 = k*x;
    MPeak = (alpha*kTors);
    fPeakTorsionAttatchment = ((2*e)/(alpha))/rTSpring;
    muWheel = (fMax*(Daxel/Dwheel)/(m*g*0.6));
    muWheel2 = (fMax2*(Daxel/Dwheel)/(m*g*0.6));
    
    print("M/2 peak:", MPeak[0]*1000/2, "Nmm,", MPeak[quality-1]*1000/2, "Nmm/rad");
    print("M/2 per rad:", kTors[0]/2, "Nm/rad,", kTors[quality-1]/2, "Nm/rad");
    print("M/2 per deg:",(((kTors[0]*(2*np.pi))/360)*1000/2), "Nmm/deg,", (((kTors[quality-1]*(2*np.pi))/360)*1000/2), "Nmm/deg");

    plt.figure(3);
    plt.plot(h, l*100);
    plt.title("height vs l (cm)");
    plt.show();
    print("l:", l[0]*100 ,"cm,", l[quality-1]*100,"cm");
    
    plt.figure(4);
    plt.plot(h, kTors);
    plt.title("height vs kTors (N/rad)");
    plt.show();
    print("kTors:", kTors[0] ,"N/rad,", kTors[quality-1], "N/rad");
    print("kTors/%rendement:", (kTors[quality-1]-kTors[0])/(rendement(k)[quality-1]-rendement(k)[0]));
    
    plt.figure(5);
    plt.plot(dx, f);
    plt.plot(dx, f2);
    plt.title("x vs f");
    plt.show();
    print("fmax for min m:                  ", f[quality-1], "N");
    print("fmax if reg. spring for min m:   ", f2[quality-1], "N");
    
    plt.figure(6);
    plt.plot(h, fMax);
    plt.title("height vs fMax (axel)");
    plt.show();
    print("f peak (axel):               ", fMax[0] ,"N,", fMax[quality-1], "N");
    print("f peak (torsion attatment):  ", fPeakTorsionAttatchment[0] ,"N,", fPeakTorsionAttatchment[quality-1], "N");
    
    plt.figure(7);
    plt.plot(h, muWheel);
    plt.title("height vs mu (wheel)");
    plt.show();
    print("mu (wheel):                  ", muWheel[0] ,",", muWheel[quality-1]);
    print("mu (wheel) if reg. spring:   ", muWheel2[0] ,",", muWheel2[quality-1]);
    
    print("");
    callibrationPos = quality//2;
    print("If callibrated to h =", h[callibrationPos], ":");
    calibK = np.linspace(k[callibrationPos], k[callibrationPos], quality);
    plt.figure(8);
    plt.plot(h, (solveX(calibK)-(s+d))*100);
    plt.title("placed height (m) vs dX (cm)");
    plt.show();
    print("If callibrated to", 5-s[quality-1], "from he top, and placed at", 5-s[0], "from the top");
    calibK = np.linspace(k[quality-1], k[quality-1], quality);
    print("then X:", solveX(calibK)[0], " vs", (s+d)[0]);
    print("then dX:", (solveX(calibK)[0]-(s+d)[0])*100, "cm");
    
main();