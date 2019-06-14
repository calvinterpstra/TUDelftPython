"""
Created on Mon Feb 26 14:48:18 2018

@author: kenricktrip
"""

import numpy as np
import matplotlib.pyplot as plt

#vraag 1:
    
print('Vraag 1:')
print('Fs=45 deg')
print('N=135 deg')
print('G=270 deg')
    
print('Fr=m*g*cos(THETA)-N')
print('F0=(pi/2-THETA)*r*k-m*g*sin(THETA)')
    
#vraag 2:
k=2
m=0.5
g=9.81
h=0.01
r=1
t=np.linspace(0,3,round(3/h+1))

F0=np.zeros(len(t))
s=np.zeros(len(t))
v=np.zeros(len(t))
a=np.zeros(len(t))

for i in range(len(t)-1):
    F0[i]=s[i]*k-np.sin(np.pi/2-s[i]/r)*m*g
    a[i]=-F0[i]/m
    v[i+1]=v[i]+a[i]*h
    s[i+1]=s[i]+v[i]*h
print('Vraag 2:')
print('r = 1 m')
theta=s[300]/r
print('theta = {:1.15f} rad'.format(-theta+np.pi/2))
plt.plot(t,v)
plt.plot(t,s)
#vraag 3:
print('Vraag 3:')
print('T=0.5*m*r^2*DTHETA^2')
print('Vg=-m*g*r*cos(THETA)')
print('Ve=0.5*k*((pi/2-THETA)*r)^2')
    
#vraag 4:

T=0.5*m*(0)**2
Vg=-m*g*r*np.cos(np.pi/2)
Ve=0.5*k*((np.pi/2-np.pi/2)*r)**2
    
print('Vraag 4:')
print('Etotal = {:1.0f} J'.format(-(T+Vg+Ve)))

#motion reverses, Vg=Ve
theta=-np.pi/3
Vg=-m*g*r*np.cos(theta)
Ve=0.5*k*((np.pi/2-theta)*r)**2
k=(-m*g*r*np.cos(theta))/(0.5*((np.pi/2-theta)*r)**2)
print('k = {:1.15f} N/m'.format(-k))

#vraag 5:
k=2
m=0.5
g=9.81
h=0.01
r=1
c=0.1
t=np.linspace(0,3,round(3/h+1))

F0=np.zeros(len(t))
s=np.zeros(len(t))
v=np.zeros(len(t))
a=np.zeros(len(t))
Ffriction=np.zeros(len(t))

for i in range(len(t)-1):
    F0[i]=s[i]*k-np.sin(np.pi/2-s[i]/r)*m*g
    Ffriction[i]=c*np.sign(v[i])
    a[i]=-(F0[i]+Ffriction[i])/m
    v[i+1]=v[i]+a[i]*h
    s[i+1]=s[i]+v[i]*h

U=np.trapz(np.absolute(v),x=None,dx=0.01)*c
print('Vraag 5:') 
print('U = {:1.15f} J'.format(-U))
plt.plot(t,v)
plt.plot(t,s)


#motion reverses, Vg=Ve
theta=-np.pi/3
Vg=-m*g*r*np.cos(theta)
Ve=0.5*k*((np.pi/2-theta)*r)**2
k=(m*g*r*np.cos(theta)-c*(np.pi/2+np.pi/3))/(0.5*((np.pi/2-theta)*r)**2)
print('k = {:1.15f} N/m'.format(k))
