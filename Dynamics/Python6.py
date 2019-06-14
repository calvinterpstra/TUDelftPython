"""
Created:    Mon March 5 2018
Author:    Calvin Terpstra (Python 3.5.2)
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

theta = 45
e = 0.75
v_x0 = 3
v_y0 = 0
x0 = 0
y0 = 0
g = -10
vxImpact = 0.375
vyImpact = 2.625
state0 = [1,0, 0.375, 2.625] # [x, y, v_x, v_y]
dt = 0.001
t_end = 21
t = np.linspace(0,t_end,round(t_end/dt+1))

def impactvelocity(v_x0, v_y0, e):
    vxImpact = 0.5*((v_x0+v_y0) + e*(v_y0-v_x0))
    vyImpact = 0.5*((v_x0+v_y0) - e*(v_y0-v_x0))
    return [vxImpact, vyImpact]

print("impactvelocity", impactvelocity(v_x0, v_y0, e))

def derivative(state, t):    
    x, y, v_x, v_y = state
    a_x = 0
    a_y = g
    return [v_x, v_y, a_x, a_y]

state = odeint(derivative,state0,t)
x, y, v_x, v_y = state.T

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

# t_1 = lineintersect(t, x, 1)[0]
x_20 = lineintersect(x, t, 20-0.333333333)[0] # x[len(t)-1] # 
y_20 = lineintersect(y, t, 20-0.333333333)[0] # y[len(t)-1]
print("x_20:", x_20)
print("y_20:", y_20)
