# -*- coding: utf-8 -*-
"""
Shaker.py  -- a shaker device using a crankshaft mechanism

@author: Bart Gerritsen
"""


import numpy as np
import matplotlib.pyplot as plt



def doMain():
    # subplot numbers
    xvaPLOT = 0 # plot for x(t), v(t) and a(t)
    FPLOT   = 1 # plot for forces 
    
    # chose a parameter domain t ...
    angleStep = np.pi/45.
    t = np.arange(0,2*np.pi,angleStep)
    
    # crank grounding ...
    C = (0,0)
    
    # crank radius ...
    R =  0.1 # [m]
    L =  1.0 # [m]
    m = 10.0 # [kg]
    
    f =  2.0 # [Hz]
    om=  f*2*np.pi # [rad/s] 

    # plot the results ...
    fig, ax = plt.subplots(1,2,figsize=(10,4))
    ax[xvaPLOT].plot(t,C[0]+L+R*np.cos(t),'r-', label = 'position')
    # ax.plot(t,C[0]+np.sqrt(1-(R*np.sin(t))**2) +R*np.cos(t),'k--')
    ax[xvaPLOT].plot(t,  -np.sin(t),'b-', label = 'speed')
    ax[xvaPLOT].plot(t,  -np.cos(t),'g-', label = 'acceleration')
    
    # plot axes, title, grid and a legend ...
    ax[xvaPLOT].set_title('position $x(t)$ [m], speed [m/s] and acc.[m/s^2]')
    ax[xvaPLOT].set_xlabel('Crank angle [rad]')
    ax[xvaPLOT].grid(which='major',axis='both',alpha=.60)    
    ax[xvaPLOT].legend(loc='best', shadow=True)

    # use F = m.a(t)
    ax[FPLOT].plot(f*t, m * -np.cos(f*t),'m-', label='Force on joint')
    ax[FPLOT].set_title('Joint forces, $\omega = 2\pi \cdot{:4.1f}$ [rad/s]'.\
                    format(f))
    ax[FPLOT].set_xlabel('Crank angle $\omega(t)$ [rad]')
    ax[FPLOT].grid(which='major', axis='both', alpha=.60)
    ax[FPLOT].legend(loc='best', shadow=True)

doMain()
