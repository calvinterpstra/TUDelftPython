"""
Created:    Sat April 7 2018
Author:    Calvin Terpstra (Python 3.5.2)
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

# Q1:
print("Q1:")
m = 1.2
g = 2
r = 0.42
d = 1.5
r_cm = d/2
theta0 = np.deg2rad(45)
omega0 = 2
k = 20
a = d/np.sqrt(2)
rho = m/(a**2 - np.pi*r**2)
I = (1/6)*rho*(a**2)*a**2 - (1/2)*rho*(np.pi*r**2)*r**2 + m*r_cm**2

dt = 0.01
t = np.linspace(0, 10, 10/dt+1)
state0 = [theta0, omega0]

def derivatives(state,t):
    theta, omega = state
    M = -k*theta
    alpha = (M - 0.5*d*np.sin(theta)*m*g)/I
    return [omega, alpha]
    
state = odeint(derivatives, state0, t)
theta, omega = state.T

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

omega = np.abs(lineintersect(omega, theta, 0)[0])
print("omega:", omega,"rad/s")

# Q2:
print("Q2:")
m = 1.4
g = 2
r = 0.9
d = 3
r_cm = d/2
theta0 = np.deg2rad(5)
omega0 = 0
k = 20
a = d/np.sqrt(2)
rho = m/(a**2 - np.pi*r**2)
I = (1/6)*rho*(a**2)*a**2 - (1/2)*rho*(np.pi*r**2)*r**2 + m*r_cm**2

dt = 0.01
t = np.linspace(0, 10, 10/dt+1)
state0 = [theta0, omega0]

def derivatives(state,t):
    theta, omega = state
    M = -k*theta
    alpha = (M - 0.5*d*np.sin(theta)*m*g)/I
    return [omega, alpha]
    
state = odeint(derivatives, state0, t)
theta, omega = state.T

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

omega_v = lineintersect(t, omega, 0)
omega_n = (2*np.pi)/(omega_v[2]-omega_v[0])
print("omega_n:", omega_n,"rad/s")

f_n = omega_n/(2*np.pi)
print("f_n:", f_n,"Hz")

# Q3:
print("Q3:")
m = 4
r = 0.9
gamma = np.deg2rad(35)
g = 9.81
mu_s = 0.22
mu_k = 0.18
t = 2.2

N = m*g*np.sin(gamma)

Ff = mu_k*N
I = 0.5*m*r**2
alpha = (-r*Ff)/I
omega = alpha*t
print("omega:", np.abs(omega), "rad/s")

ax = (Ff-m*g*np.cos(gamma))/m
vG = ax*t
print("vG:", np.abs(vG), "m/s")

Ek = 0.5*m*vG**2 + 0.5*I*omega**2
print("Ek:", Ek, "J")

s = (ax*t**2)/2
print("s:", np.abs(s), "m")