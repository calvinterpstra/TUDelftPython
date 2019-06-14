"""
Created:    Thurs March 1 2018
Author:    Calvin Terpstra (Python 3.5.2)
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate

# Q1-2:
# Fy = -k*y-m*g

# Q3:
# y = -m*g/k

# Q4:
# V = m*g*y + 0.5*k*y^2

# Q5:
m = 2
k = 50
g = 10
t0 = 0.0
t_end = 5
s0 = [1,-1]

def derivatives(s, t):    
    y, v = s
    a = -k/m*y -g
    return [v, a]
    
def Energy(vector):    
    [y,v] = vector 
    return 1/2*k*y**2 + m*g*y + 1/2*m*v**2
 
dt=0.01
vector = np.empty((round(t_end/dt+1), 2))
vector[0,:] = s0
t = np.linspace(t0, t_end, round(t_end/dt+1))

for i in range(len(t)-1):    
    vector[i+1,:]=vector[i,:]+np.multiply(dt,derivatives(vector[i,:],t[i]))

y, v = vector.T

DeltaE  = np.abs(Energy(vector[0])-Energy(vector[-1]))
print("DeltaE:", DeltaE)

dt=0.001
vector = np.empty((round(t_end/dt+1), 2))
vector[0,:]=s0
t = np.linspace(t0, t_end, round(t_end/dt+1))

for i in range(len(t)-1):    
    vector[i+1,:]=vector[i,:]+np.multiply(dt,derivatives(vector[i,:],t[i]))

y, v = vector.T

DeltaE  = np.abs(Energy(vector[0])-Energy(vector[-1]))
print("DeltaE:", DeltaE)

cstate=integrate.odeint(derivatives, s0, t)
y, v = cstate.T

cstate_end=cstate[5000] 
s_end=cstate_end[0]
print("s:", s_end)

DeltaE  = np.abs(Energy(cstate[0])-Energy(cstate[-1]))
print("DeltaE:", DeltaE)

# Q6:
# m = 0.5
# k = 2
# x0 = 1
# v0 = -1
# Fnet = -kx

# Q7:
# v(t) = A*w*cos(w*t) - B*w*sin(w*t)
# a(t) = -A*w^2*sin(w*t) - B*w^2*cos(w*t)
# A = -1/2 m, B = 1 m, w = 2 1/s
# effect w: m, k

# Q8:
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

m=0.5
k=2
s0=[1,-1]
dt=0.01
w=np.sqrt(k/m)
tau=2*np.pi/w
T=6*tau
t=np.linspace(0,T,int(T/dt+1))

def derivative(s, t):    
    y, v = s
    a=-k/m*y
    return [v, a]

vector = np.empty((int(T/dt+1), 2))
vector[0,:]=s0
for i in range(int(T/dt)):    
    vector[i+1,:]=vector[i,:]+np.multiply(dt,derivative(vector[i,:],t[i]))
y,v=vector.T

xint=lineintersect(np.linspace(0,T,int(T/dt+1)), y,0)+tau/4
print("Starttijd oscillatie t:", xint[0])
print("Eindtijd 5 oscillaties t:", xint[10])
tsum=xint[10]-xint[0]
print("Tijdperiode T nummeriek:", tsum/5)
print("Tijdperiode T:",tau)
w=(2*np.pi)/tau
print("w nummeriek:", w)
w=(10*np.pi)/tsum
print("w nummeriek:", w)