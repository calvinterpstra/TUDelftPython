"Python 10.1"

"Standaardfuncties"
import numpy as np
import scipy.integrate as integrate
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
mtot=1.2
g=2
r=0.315
d=1.5
theta0=np.deg2rad(45)
omega0=2
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
dt=0.01; t=np.linspace(0, 5, 5/dt+1)
s0=[theta0, omega0]

def derivatives(state,t):
    theta, omega = state
    M=-k*theta
    alfa=(M-0.5*d*np.sin(theta)*mtot*g)/Io
    return[omega, alfa]
state=integrate.odeint(derivatives, s0, t)

omega=lineintersect(state[:,1],state[:,0],0)[0]
print("omega =",np.abs(omega),"rad/s")