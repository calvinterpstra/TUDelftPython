"Python 9.5"

import scipy.integrate as integrate
import numpy as np
import matplotlib.pyplot as plt

"Constanten"
m=2
L=3
L2=4
g=9.81

vA0=[0.25, 0, 0]
theta0=np.deg2rad(60)
omega0=[0, 0, -0.4]
s0=[0, 0.25, theta0, -0.4]

dt=0.01; t=np.linspace(0, 5, 5/dt+1)

"Vraag 1"
def derivatives(state,t):
    xA, vA, theta, omega = state
    alfa=(3*omega**2*L**2*(np.sin(theta)*np.cos(theta))-6*g*L*np.cos(theta))/(L**2+3*L**2*(np.cos(theta))**2)
    aA=alfa*L/2*np.sin(theta)+omega**2*L/2*np.cos(theta)
    return[vA, aA, omega, alfa]
state=integrate.odeint(derivatives, s0, t)

xA1 = state[-1,0]
vA1 = state[-1,1]
theta1 = state[-1,2]
omega1 = state[-1,3]

print("xA eind=", xA1, "m")
print("vA eind=", vA1, "m/s")
print("theta eind=", theta1, "rad")
print("omega eind=", omega1, "rad/s")


"Vraag 2"
alfa1=(3*omega1**2*L**2*(np.sin(theta1)*np.cos(theta1))-6*g*L*np.cos(theta1))/(L**2+3*L**2*(np.cos(theta1))**2)
print("alfa eind=", alfa1, "rad/s^2")


"Vraag 3"
aA1=alfa1*L/2*np.sin(theta1)+omega1**2*L/2*np.cos(theta1)
print("aA eind=", aA1, "m/s^2")


"Vraag 4"
fi=np.deg2rad(90)-theta1
alfaC=[0, 0, alfa1]
rCA=[-(L2*np.cos(fi)-L*np.cos(theta1)), (L2*np.sin(fi)+L*np.sin(theta1)), 0]
aC_tangential = np.cross(alfaC,rCA)
print("alfa x r(C/A)=", aC_tangential,"m/s^2")


"Vraag 5"
omega_kwadraat = -omega1**2
aC_normal = np.dot(omega_kwadraat, rCA)
print("-omega^2 * r(C/A)=", aC_normal,"m/s^2")


"Vraag 6"
aCx=aA1+aC_tangential[0]+aC_normal[0]
aCy=aC_tangential[1]+aC_normal[1]
aCz=aC_tangential[2]+aC_normal[2]
aC=[aCx, aCy, aCz]
print("aC eind=", aC, "m/s^2")


"Vraag 7"
vC1 = vA1 - omega1*(L2*np.sin(fi)+L*np.sin(theta1))
print("vC eind=", vC1, "m/s")

"Grafiek"
plt.figure(num=1)
plt.plot(t,state[:,0])
plt.xlabel('t [m]')
plt.ylabel('xA [m]')
plt.title('X-verplaatsing van A t.o.v. de tijd')






