"Python 9"

import numpy as np

xA = 4
yA = 0
zA = 0
L = 1.4
theta = 140*np.pi/180
vA_x = 11
vA_y = 0
vA_z = 0
aA_x = 0.3
aA_y = 0
aA_z = 0
omega = [0, 0, 2.4] #dit is je fluxi theta(vraag 1 en 2)
alfa = [0, 0, 0.05] #dit is je dubbel fluxi theta(vraag2)

"Q1"
"1:"
rA = [xA, yA, zA]

print("1 = ", rA)

"2:"
rBA = [0.5*L*np.cos(theta), 0.5*L*np.sin(theta), 0]

print("2 = ", rBA)

"3:"
rB = [rA[0] + rBA[0], rA[1] + rBA[1], rA[2] + rBA[2]]

print("3 = ", rB)

"4:"
vA = [vA_x, vA_y, vA_z]
3
print("4 = ", vA)

"5:"
cross = np.cross(omega, rBA)

print("5 = ", cross)

"6:"
vB = vA + np.cross(omega, rBA)

print("6 = ", vB)

"Q2"
"1: "
aA = [aA_x, aA_y, aA_z]
print("1aA = ", aA)

"2: "
cross_2 = np.cross(alfa, rBA)
print("2cross_2 = ", cross_2)

"3: "
scalar_omega = np.dot(omega, omega)
scalar_multiplication = np.dot(scalar_omega, rBA)
print("3scalar multi = ", scalar_multiplication)

"4: "
vBA = np.cross(omega, rBA)
aB = aA + np.cross(alfa, rBA) + np.cross(omega, vBA)
print("4aB = ", aB)

"Q3"
"SomFx=0"
"SomFy=Fy-m*g"
"SomMB=-(0.5*L*cos(THETA))*Fy"
        