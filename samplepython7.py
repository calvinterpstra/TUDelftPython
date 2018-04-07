# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

m=1.6
r=0.5
g=-2
a=1
dt=0.1
theta0=-0.5*np.pi
t=np.linspace(0,15,round(15/dt+1))
I=0.187213+m*(r**2)
print("I:", I)

def derivative(state,t):
    theta,omega=state
    alpha=r*(theta)*m*g/I
    return[omega,alpha]

state0=[theta0,0]
state=odeint(derivative,state0,t)
theta,omega=state.T

def lineintersect(x, y, c):
    n = len(x)
    xinter = [] 
    for i in range(n-1):
        amountInter = len(xinter)
        lastEntry = xinter[-1] if amountInter>0 else None
        if x[i+1]!=x[i]:     
            a =(y[i+1]-y[i])/(x[i+1]-x[i])
            b =(y[i]-a*x[i])
            if a==0:
                if b==c and lastEntry!=x[i]:
                    xinter.append(x[i])
            else:
                r = (c-b)/a
                if x[i+1] > x[i]:
                    if (x[i] <= r <= x[i+1] and lastEntry!=r):
                        xinter.append(r)   
                elif x[i+1] < x[i]:
                    if (x[i] >= r >= x[i+1] and lastEntry!=r):
                        xinter.append(r)
        else:
            if y[i]<=c<=y[i+1] and lastEntry!=x[i]:
                xinter.append(x[i])
    return sorted(xinter)
tim=lineintersect(t,omega,0)
print(tim)

plt.plot(t,omega)
plt.plot(t,theta)