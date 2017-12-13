# -*- coding: utf-8 -*-
"""
Oefening1.py  -- compute and plot spring load diagram

@author: Bart Gerritsen
"""

import matplotlib.pyplot as plt

def plotLoadDiag(ax,path,k,s,F,colString='k--'):
    ax.plot([path[0],path[0]], [F[0],F[1]], colString)
    ax.plot([path[1],path[1]], [F[0],F[1]], colString)
    f = getForces(path,k,F[0])
    ax.plot([s[0], s[1]],[f[0],f[0]], colString)
    ax.plot([s[0], s[1]],[f[1],f[1]], colString)
    return ax

def getForces(path,k,F0):
    """
    return f for a given path
    """
    s0 = 0
    f = []
    for s in path:
        f.append(F0+k*(s-s0))
    return f

def doMyMain():
    # my subplot numbers ...
    PLT1,PLT2,PLT3,PLT4 = (141,142,143,144)
    PLTS = (PLT1,PLT2,PLT3, PLT4)
    
    # spring constant ...
    c = 5 # N/m
    
    # force range ...
    F0 = 100 # N ...
    F = range(F0,F0+25,5)
    s = range(5)
    
    plt.subplots(1,len(PLTS), figsize=(16,4))
    
    for k in F:
        print('Force F: {:d} N'.format(k))
        
    for p in PLTS:
        ax = plt.subplot( p )
        ax.plot(s,F,'r-')
        ax.grid(which='major', axis='both')
        
    # plot a load-displacement diagram 1
    path = [ 0, 1.5 ]
    color = 'b--'
    ax = plt.subplot( PLT1 )
    plotLoadDiag(ax,path,c,(0,4),(F0,max(F)),colString=color)
    
    # plot a load-displacement diagram 2
    path = [ 2, 3 ]
    color = 'g--'
    ax = plt.subplot( PLT2 )
    plotLoadDiag(ax,path,c,(0,4),(F0,max(F)),colString=color)
    
    # plot a load-displacement diagram 3
    path = [ 2.5, 3.5 ]
    color = 'c--'
    ax = plt.subplot( PLT3 )
    plotLoadDiag(ax,path,c,(0,4),(F0,max(F)),colString=color)
    
    # plot a load-displacement diagram 2
    path4 = [ 3, 4 ]
    color = 'k--'
    ax = plt.subplot( PLT4 )
    plotLoadDiag(ax,path,c,(0,4),(F0,max(F)),colString=color)
    
doMyMain()
