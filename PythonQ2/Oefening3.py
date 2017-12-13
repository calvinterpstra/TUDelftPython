# -*- coding: utf-8 -*-
"""
Oefening3 -- draw a ellipse

@author: Bart Gerritsen
"""

import numpy as np
import matplotlib.pyplot as myPlt; 

def myMainPart():
    A,e = (1.0, 0.24); B= e*A
    N=18
    x=np.zeros((N+1), dtype=float)
    y=np.zeros((N+1), dtype=float)
    
    fig, ax = myPlt.subplots(1, figsize=(6,4))
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    ax.spines['bottom'].set_bounds(-A, A)
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_visible(True)

    dphi = 2*np.pi/N
    phi  = 0; 
    # compute it in a loop ...
    for j in range(0,N+1):
        if j == N+1:
            x[j] = x[0]
            y[j] = y[0]
        else:
            x[j] = A*np.cos(phi)
            y[j] = B*np.sin(phi)
        ax.plot([0,x[j]], [0,y[j]], 'k:', linewidth=1)
        phi += dphi

    ax.plot(x, y,'r-')
    ax.grid(which='major',axis='both')
    ax.axis('equal')


myMainPart()