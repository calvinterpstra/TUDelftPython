"Python 10.2"

"Standaardfuncties"
import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt
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

"Constanten"
mtot=1.8
g=2
r=0.75
d=2.5
theta0=np.deg2rad(5)
omega0=0
k=20

"Dimensies"
a=d/np.sqrt(2)
Avierkant=a**2
Acirkel=np.pi*(r)**2
Atot=Avierkant-Acirkel

"Massas"
dichtheid=mtot/Atot
mvierkant=dichtheid*Avierkant
mcirkel=dichtheid*Acirkel

"Massa-traagheidsmoment I"
Ivierkant=(1/12)*mvierkant*(a**2+a**2)
Icirkel=(1/2)*mcirkel*r**2
Ig=Ivierkant-Icirkel
Io=Ig+mtot*0.25*d**2

"Integreren"
dt=0.01; t=np.linspace(0, 10, 10/dt+1)
s0=[theta0, omega0]

def derivatives(state,t):
    theta, omega = state
    M=-k*theta
    alfa=(M-0.5*d*np.sin(theta)*mtot*g)/Io
    return[omega, alfa]
state=integrate.odeint(derivatives, s0, t)

omegavector=lineintersect(t,state[:,0],0)
omegan=(2*np.pi)/(omegavector[2]-omegavector[0])
print("omega =",omegan,"rad/s")

fn=omegan/(2*np.pi)
print("fn =",fn,"Hz")

"Grafiek"
plt.figure(num=1)
plt.plot(t,state[:,0])
plt.xlabel('t [m]')
plt.ylabel('theta [m]')
plt.title('Massa-veer systeem')






