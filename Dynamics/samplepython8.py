# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 16:00:37 2018

@author: bryan
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

m=200
I=100
r=0.75
F=500
dt=0.01
t=np.linspace(0,20,round(20/dt+1))

def derivative(state,t):
    x,y,theta,vx,vy,vtheta=state
    ax=(F)/m
    ay=(F)/m
    atheta=np.cos(theta)*(F*r)/I
    return[vx,vy,vtheta,ax,ay,atheta]

state0=[0,0,0,0,0,0]
state=odeint(derivative,state0,t)
x,y,theta,vx,vy,vtheta=state.T

print(x[2000],y[2000],theta[2000],vx[2000],vy[2000],vtheta[2000])
