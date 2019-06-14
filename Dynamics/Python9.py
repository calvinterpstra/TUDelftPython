"""
Created:    Sat April 7 2018
Author:    Calvin Terpstra (Python 3.5.2)
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

# Q1:
print("Q1:")
xA = 6
yA = 0
zA = 0
L = 1.4
theta = np.deg2rad(65)
vA_x = 18
vA_y = 0
vA_z = 0
aA_x = 0
aA_y = 0
aA_z = 0
omega = [0, 0, 0.8]
alpha = [0, 0, 0]

rA = [xA, yA, zA]
print("1:", rA)
rBA = [0.5*L*np.cos(theta), 0.5*L*np.sin(theta), 0]
print("2:", rBA)
rB = [rA[0] + rBA[0], rA[1] + rBA[1], rA[2] + rBA[2]]
print("3:", rB)
vA = [vA_x, vA_y, vA_z]
print("4:", vA)
cross = np.cross(omega, rBA)
print("5:", cross)
vB = vA + np.cross(omega, rBA)
print("6:", vB)

# Q2:
print("Q2:")
xA = 7
yA = 0
zA = 0
L = 1.6
theta = np.deg2rad(120)
vA_x = 7
vA_y = 0
vA_z = 0
aA_x = 0.3
aA_y = 0
aA_z = 0
omega = [0, 0, 2.0]
alpha = [0, 0, 0.35]

rA = [xA, yA, zA]
rBA = [0.5*L*np.cos(theta), 0.5*L*np.sin(theta), 0]
rB = [rA[0] + rBA[0], rA[1] + rBA[1], rA[2] + rBA[2]]
vA = [vA_x, vA_y, vA_z]
cross = np.cross(omega, rBA)
vB = vA + np.cross(omega, rBA)

aA = [aA_x, aA_y, aA_z]
print("1:", aA)

cross_2 = np.cross(alpha, rBA)
print("2:", cross_2)

scalar_omega = np.dot(omega, omega)
scalar_multiplication = np.dot(scalar_omega, rBA)
print("3:", scalar_multiplication)

vBA = np.cross(omega, rBA)
aB = aA + np.cross(alpha, rBA) + np.cross(omega, vBA)
print("4:", aB)

# Q3:
print("Q3:")
print("2: sum_Fx = 0")
print("3: sum_Fy = Fy-m*g")
print("4: sum_MB = -(0.5*L*cos(THETA))*Fy")

# Q4:
print("Q4:")
m = 2
L = 3
g = 9.81
vA0 = [0.25, 0, 0]
theta0 = np.deg2rad(60)
omega0 = [0, 0, -0.5]
state0 = [0, 0.25, theta0, -0.5]
dt = 0.01
t = np.linspace(0, 25, 25/dt+1)

rBA = [0.5*L*np.cos(theta0), 0.5*L*np.sin(theta0), 0]
vB = vA0 + np.cross(omega0, rBA)
print("vB:", vB[0], "m/s")

def derivatives(state,t):
    xA, vA, theta, omega = state
    alpha = (3*omega**2*L**2*(np.sin(theta)*np.cos(theta))-6*g*L*np.cos(theta))/(L**2+3*L**2*(np.cos(theta))**2)
    aA = alpha*L/2*np.sin(theta)+omega**2*L/2*np.cos(theta)
    return [vA, aA, omega, alpha]

state = odeint(derivatives, state0, t)
xA1 = state[-1,0]
vA1 = state[-1,1]
theta1 = state[-1,2]
omega1 = state[-1,3]

print("xA:", xA1, "m")
print("vA:", vA1, "m/s")
print("theta:", theta1, "rad")
print("omega:", omega1, "rad/s")

vB1 = vA1 - 0.5*L*omega1*np.sin(theta1) 
print("vB:", vB1, "m/s")

# Q5:
print("Q5:")
m = 2
L = 3
L2 = 4
g = 9.81
vA0 = [0.25, 0, 0]
theta0 = np.deg2rad(60)
omega0 = [0, 0, -0.4]
s0 = [0, 0.25, theta0, -0.4]
dt = 0.01
t = np.linspace(0, 5, 5/dt+1)

def derivatives(state,t):
    xA, vA, theta, omega = state
    alpha = (3*omega**2*L**2*(np.sin(theta)*np.cos(theta))-6*g*L*np.cos(theta))/(L**2+3*L**2*(np.cos(theta))**2)
    aA = alpha*L/2*np.sin(theta)+omega**2*L/2*np.cos(theta)
    return [vA, aA, omega, alpha]

state = odeint(derivatives, s0, t)
xA1 = state[-1,0]
vA1 = state[-1,1]
theta1 = state[-1,2]
omega1 = state[-1,3]

print("xA:", xA1, "m")
print("vA:", vA1, "m/s")
print("theta:", theta1, "rad")
print("omega:", omega1, "rad/s")

alpha1 = (3*omega1**2*L**2*(np.sin(theta1)*np.cos(theta1))-6*g*L*np.cos(theta1))/(L**2+3*L**2*(np.cos(theta1))**2)
print("alpha:", alpha1, "rad/s^2")

aA1 = alpha1*L/2*np.sin(theta1)+omega1**2*L/2*np.cos(theta1)
print("aA:", aA1, "m/s^2")

phi = np.deg2rad(90)-theta1
alphaC = [0, 0, alpha1]
rCA = [-(L2*np.cos(phi)-L*np.cos(theta1)), (L2*np.sin(phi)+L*np.sin(theta1)), 0]
aC_t = np.cross(alphaC,rCA)
print("alpha x r(C/A):", aC_t,"m/s^2")

omega_2 = -omega1**2
aC_n = np.dot(omega_2, rCA)
print("-omega^2 * r(C/A):", aC_n,"m/s^2")

aCx = aA1+aC_t[0]+aC_n[0]
aCy = aC_t[1]+aC_n[1]
aCz = aC_t[2]+aC_n[2]
aC = [aCx, aCy, aCz]
print("aC:", aC, "m/s^2")

vC1 = vA1 - omega1*(L2*np.sin(phi)+L*np.sin(theta1))
print("vC:", vC1, "m/s")