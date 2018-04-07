"Python 9.4"
import scipy.integrate as integrate
import numpy as np
import matplotlib.pyplot as plt

"Constanten"
m=2
L=3
g=9.81

vA0=[0.25, 0, 0]
theta0=np.deg2rad(60)
omega0=[0, 0, -0.5]
s0=[0, 0.25, theta0, -0.5]

dt=0.01; t=np.linspace(0, 25, 25/dt+1)

"Vraag 1"
rBA = [0.5*L*np.cos(theta0), 0.5*L*np.sin(theta0), 0]
vB = vA0 + np.cross(omega0, rBA)
print("vB begin=",vB[0], "m/s")


"Vraag 2"
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


"Vraag 3"
vB1 = vA1 - 0.5*L*omega1*np.sin(theta1) 
print("vB eind=", vB1, "m/s")


"Grafiek"
plt.figure(num=1)
plt.plot(t,state[:,0])
plt.xlabel('t [m]')
plt.ylabel('xA [m]')
plt.title('t-xA')






