"""
Created:    Wed April 4 2018
Author:    Calvin Terpstra (Python 3.5.2)
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

# Q1:
print("Q1:")
m = 1.6
r = 0.5
g = -2
theta0 = np.pi * 0.5
I = m*r**2
print("I (cm):", 0, "kg*m^2")
dt = 0.1
T = 2*np.pi * np.sqrt(r/-g)
t_end = 100
t = np.linspace(0,t_end,round(t_end/dt+1))

def derivative(state, t):
    theta, omega = state
    alpha = np.sin(theta)*r*m*g/I # theta*r*m*g/I
    return [omega, alpha]

state0 = [theta0, 0]
state = odeint(derivative, state0, t)
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

T_0s = lineintersect(t,theta,0)
print("T:", (T_0s[21]-T_0s[1])/10, "s")

def derivative(state, t):
    theta, omega = state
    alpha = theta*r*m*g/I
    return [omega, alpha]

state0 = [theta0, 0]
state = odeint(derivative, state0, t)
theta, omega = state.T

T_0s = lineintersect(t,theta,0)
print("T (linearized):", (T_0s[21]-T_0s[1])/10, "s")

# Q2:
print("Q2:")
m1 = 1.6/2
m2 = 1.6/2
r1 = 0.25
r2 = 0.75
g = -2
theta0 = np.pi * 0.5
I = m1*r1**2 + m2*r2**2
print("I (cm):", (m1+m2)*((r2-r1)/2)**2, "kg*m^2")
dt = 0.1
T = 2*np.pi * np.sqrt(r/-g)
t_end = 100
t = np.linspace(0,t_end,round(t_end/dt+1))

def derivative(state, t):
    theta, omega = state
    alpha = np.sin(theta)*r*(m1+m2)*g/I # (theta)*r*m*g/I
    return [omega, alpha]

state0 = [theta0, 0]
state = odeint(derivative, state0, t)
theta, omega = state.T

T_0s = lineintersect(t,theta,0)
print("T:", (T_0s[21]-T_0s[1])/10, "s")

def derivative(state, t):
    theta, omega = state
    alpha = theta*r*(m1+m2)*g/I
    return [omega, alpha]

state0 = [theta0, 0]
state = odeint(derivative, state0, t)
theta, omega = state.T

T_0s = lineintersect(t,theta,0)
print("T (linearized):", (T_0s[21]-T_0s[1])/10, "s")

# Q3:
print("Q3:")
m = 1.6
r_cm = 0.5
l = 1
g = -2
theta0 = np.pi * 0.5
I = (1/6)*m*l**2 + m*r_cm**2
print("I (cm):", I - m*r_cm**2, "kg*m^2")
dt = 0.1
T = 2*np.pi * np.sqrt(r_cm/-g)
t_end = 100
t = np.linspace(0,t_end,round(t_end/dt+1))

def derivative(state, t):
    theta, omega = state
    alpha = np.sin(theta)*r_cm*m*g/I # (theta)*r*m*g/I
    return [omega, alpha]

state0 = [theta0, 0]
state = odeint(derivative, state0, t)
theta, omega = state.T

T_0s = lineintersect(t,theta,0)
print("T:", (T_0s[21]-T_0s[1])/10, "s")

def derivative(state, t):
    theta, omega = state
    alpha = theta*r_cm*m*g/I
    return [omega, alpha]

state0 = [theta0, 0]
state = odeint(derivative, state0, t)
theta, omega = state.T

T_0s = lineintersect(t,theta,0)
print("T (linearized):", (T_0s[21]-T_0s[1])/10, "s")

# Q4:
print("Q4:")
m = 1.6
r_cm = 0.5
r = 0.25
g = -2
theta0 = np.pi * 0.5
I = (1/2)*m*r**2 + m*r_cm**2
print("I (cm):", I - m*r_cm**2, "kg*m^2")
dt = 0.1
T = 2*np.pi * np.sqrt(r_cm/-g)
t_end = 100
t = np.linspace(0,t_end,round(t_end/dt+1))

def derivative(state, t):
    theta, omega = state
    alpha = np.sin(theta)*r_cm*m*g/I # (theta)*r*m*g/I
    return [omega, alpha]

state0 = [theta0, 0]
state = odeint(derivative, state0, t)
theta, omega = state.T

T_0s = lineintersect(t,theta,0)
print("T:", (T_0s[21]-T_0s[1])/10, "s")

def derivative(state, t):
    theta, omega = state
    alpha = theta*r_cm*m*g/I
    return [omega, alpha]

state0 = [theta0, 0]
state = odeint(derivative, state0, t)
theta, omega = state.T

T_0s = lineintersect(t,theta,0)
print("T (linearized):", (T_0s[21]-T_0s[1])/10, "s")

# Q5:
print("Q5:")
m = 1.6
d = 1
a = d/np.sqrt(2)
r = 0.25
r_cm = d/2
rho = m/(a**2 - np.pi*r**2)
g = -2
theta0 = np.pi * 0.5
I = (1/6)*rho*(a**2)*a**2 - (1/2)*rho*(np.pi*r**2)*r**2 + m*r_cm**2
print("I (cm):", I - m*r_cm**2, "kg*m^2")
dt = 0.1
T = 2*np.pi * np.sqrt(r_cm/-g)
t_end = 100
t = np.linspace(0,t_end,round(t_end/dt+1))

def derivative(state, t):
    theta, omega = state
    alpha = np.sin(theta)*r_cm*m*g/I # (theta)*r*m*g/I
    return [omega, alpha]

state0 = [theta0, 0]
state = odeint(derivative, state0, t)
theta, omega = state.T

T_0s = lineintersect(t,theta,0)
print("T:", (T_0s[21]-T_0s[1])/10, "s")

def derivative(state, t):
    theta, omega = state
    alpha = theta*r_cm*m*g/I
    return [omega, alpha]

state0 = [theta0, 0]
state = odeint(derivative, state0, t)
theta, omega = state.T

T_0s = lineintersect(t,theta,0)
print("T (linearized):", (T_0s[21]-T_0s[1])/10, "s")
