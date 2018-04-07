"""
Created on Sat Mar  3 21:41:27 2018

@author: kenricktrip
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

#vraag 5, deel 1:
m=2
k=50
g=10
t0=0.0
t_end=5
s0=[1,-1]

def derivatives(s, t):    
    y, v = s
    a=-k/m*y -g
    return [v, a]
    
    #Potential Energy
def Energy(vector):    
    [y,v]=vector 
    return 1/2*k*y**2 + m*g*y + 1/2*m*v**2
 
dt=0.01 #stepsize
vector = np.empty((round(t_end/dt+1), 2)) #maak een vector = [y,v] 2 kollommen en round(t_end/h+1) rijen
vector[0,:]=s0
t = np.linspace(t0, t_end, round(t_end/dt+1))

for i in range(len(t)-1):    
    vector[i+1,:]=vector[i,:]+np.multiply(dt,derivatives(vector[i,:],t[i]))

y, v = vector.T


DeltaE  = np.abs(Energy(vector[0])-Energy(vector[-1]))
print('Energieverschil E = {:1.6f} J'.format(DeltaE))

plt.figure(1)
plt.plot(t,vector[:,0])
plt.xlabel('t in seconds')
plt.ylabel('y in meters')
plt.figure(2)
plt.plot(t,vector[:,1])
plt.xlabel('t in seconds')
plt.ylabel('v in m/s')

#vraag 5, deel 2:
    
dt=0.001 #stepsize
vector = np.empty((round(t_end/dt+1), 2)) #maak een matrix van vectoren = [y,v] 2 kollommen en round(t_end/dt+1) rijen
vector[0,:]=s0
t = np.linspace(t0, t_end, round(t_end/dt+1))

for i in range(len(t)-1):    
    vector[i+1,:]=vector[i,:]+np.multiply(dt,derivatives(vector[i,:],t[i]))

y, v = vector.T

DeltaE  = np.abs(Energy(vector[0])-Energy(vector[-1]))
print('Energieverschil E = {:1.6f} J'.format(DeltaE))

#vraag 5, deel 3:
cstate=integrate.odeint(derivatives, s0, t) #Dit is ook een matrix = [y,v] 2 kollommen en round(t_end/dt+1) rijen
y, v = cstate.T

cstate_end=cstate[5000] 
s_end=cstate_end[0]
print('s na 5 seconden = {:1.6} m'.format(s_end))

DeltaE  = np.abs(Energy(cstate[0])-Energy(cstate[-1]))
print('Energieverschil E = {:1.6e} J'.format(DeltaE))


# vraag 8:
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

plt.figure(3)
plt.plot(t,y)
plt.xlabel('t in seconds')
plt.ylabel('y in m/s')

def lineintersect(x, y, c):
    n = len(x)-1
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

xint=lineintersect(np.linspace(0,T,int(T/dt+1)), y,0)+tau/4 #Ze willen de minimale waarden voor y
print('Vraag 8:')
print('Starttijd oscillatie t = {:1.6f} s'.format(xint[0]))
print('Eindtijd 5 oscillaties t = {:1.6f} s'.format(xint[10]))
tsum=xint[10]-xint[0]
print('Tijdperiode T nummeriek = {:1.6f} s'.format(tsum/5))
print('Tijdperiode T = {:1.6f} s'.format(tau))
w=(2*np.pi)/tau
print('w nummeriek = {:1.6f} s'.format(w))
w=(10*np.pi)/tsum
print('w nummeriek = {:1.6f} s'.format(w))
