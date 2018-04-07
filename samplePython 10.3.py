"Python 10.3"

import numpy as np

"Constanten"
m=4
r=0.1
y=np.deg2rad(20)
g=9.81
mu_s=0.25
mu_k=0.11
t=2.8

"Vraag 1"
Fw0=(m*g*np.cos(y)/3)
N=m*g*np.sin(y)

"Fw<mu_s*N geldt niet, dus er zal slip optreden tijdens het rollen"

Fw=mu_k*N
Ig=0.5*m*r**2
alfa=(-r*Fw)/Ig
omega=alfa*t
print("omega =",np.abs(omega),"rad/s")

"Vraag 2"
ax=(Fw-m*g*np.cos(y))/m
vG=ax*t
print("vG =",np.abs(vG),"m/s")

"Vraag 3"
T2=0.5*m*vG**2+0.5*Ig*omega**2
print("Ek",T2,"J")

"Bonusvraag"
s=(ax*t**2)/2
print("s =",np.abs(s),"m")
