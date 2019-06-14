"""
Created:    Sat April 7 2018
Author:    Calvin Terpstra (Python 3.5.2)
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

# Q1:
print("Q1:")
m = 200
I = 100
r = 0.75
F = 500
dt = 0.01
t = np.linspace(0, 20, round(20/dt+1))

m_20deg= np.cos(np.deg2rad(20))*(F*r)
print("m_20deg:", m_20deg, "N*m")
alpha_40deg = np.cos(np.deg2rad(40))*(F*r)/I
print("alpha_40deg:", alpha_40deg, "rad/s^2")
ax_30deg = F/m
print("ax_30deg:", ax_30deg, "m/s^2")
ay_30deg = 0
print("ay_30deg:", ay_30deg, "m/s^2")

def derivative(state,t):
    x, y, theta, vx, vy, omega = state
    ax = (F)/m
    ay = 0
    alpha = np.cos(theta)*(F*r)/I
    return[vx, vy, omega, ax, ay, alpha]

state0 = [0, 0, 0, 0, 0, 0]
state = odeint(derivative, state0, t)
x, y, theta, vx, vy, omega = state.T

print("x:", x[len(t)-1], "m")
print("y:", y[len(t)-1], "m")
print("theta:", theta[len(t)-1], "rad", np.rad2deg(theta[len(t)-1]), "deg")
print("vx:", vx[len(t)-1], "m/s")
print("vy:", vy[len(t)-1], "m/s")
print("omega:", omega[len(t)-1], "rad/s")

# Q2:
print("Q2:")
m = 200
I = 100
r = 0.75
F = 500
dt = 0.01
t = np.linspace(0, 20, round(20/dt+1))

m_20deg= (F*r)
print("m_20deg:", m_20deg, "N*m")
alpha_40deg = (F*r)/I
print("alpha_40deg:", alpha_40deg, "rad/s^2")
ax_30deg = (F*np.cos(np.deg2rad(30)))/m
print("ax_30deg:", ax_30deg, "m/s^2")
ay_30deg = (F*np.sin(np.deg2rad(30)))/m
print("ay_30deg:", ay_30deg, "m/s^2")

def derivative(state,t):
    x, y, theta, vx, vy, omega = state
    ax = (F*np.cos(theta))/m
    ay = (F*np.sin(theta))/m
    alpha = (F*r)/I
    return[vx, vy, omega, ax, ay, alpha]

state0 = [0, 0, 0, 0, 0, 0]
state = odeint(derivative, state0, t)
x, y, theta, vx, vy, omega = state.T

print("x:", x[len(t)-1], "m")
print("y:", y[len(t)-1], "m")
print("theta:", theta[len(t)-1], "rad", np.rad2deg(theta[len(t)-1]), "deg")
print("vx:", vx[len(t)-1], "m/s")
print("vy:", vy[len(t)-1], "m/s")
print("omega:", omega[len(t)-1], "rad/s")