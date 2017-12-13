# -*- coding: utf-8 -*-
"""
Ellipse.py -- plot an ellipse in 2d and experiment with eccentricity

            Verify below that the distances are correct and always
            equal-valued for an ellipse, even in the event the
            ellipse decayes into a circle (which is a special 
            ellipse with a=b=R)
            
@author: Bart Gerritsen
"""


import numpy as np
import matplotlib.pyplot as plt

def genEllipse(C,A,B,N):
    ellData = np.zeros(N*2, dtype=float).reshape(N,2)
    t = np.linspace(0,2*np.pi,num=N,endpoint=True)
    ellData[...,0] = C[0]+A*np.cos(t)   # the x coordinate 
    ellData[...,1] = C[1]+B*np.sin(t)   # and the y-coordinate
    return ellData

def getK(a,b):
    m = (a-b)/(a+b)
    return ( 1 + (35*m**2)/72 + (2*(m**2)**2)/15 ) / (1+m)
    
def plotEllipse(dat,C,a,b,N,save=True):
    # create the figure ...
    fig = plt.subplots(1, figsize=(6,4))
    
    ax = plt.subplot(111)
    
    ax.set_xlim([C[0]-a,C[0]+a])
    ax.set_ylim([C[1]-b,C[1]+b])
    ax.plot(dat[...,0],dat[...,1], color='blue', alpha=.85)
    ax.fill_between(dat[...,0],dat[...,1],-dat[...,1],color='blue',alpha=.15)
    ax.grid(which='major', axis='both')
    
        # rearrange the axis system ...
    for axis in ['right', 'top', 'left', 'bottom']:
        ax.spines[axis].set_color('none')
    for axis in ['left', 'bottom']:
        ax.spines[axis].set_color('black')
        ax.spines[axis].set_linewidth(2.0)
    # make axes system cross the origin
    ax.spines['left'].set_position(('data',C[0]))
    ax.spines['bottom'].set_position(('data',C[1]))
    
    # plot the origin ...
    ax.plot([C[0]],[C[1]],'ko')
    
    # plot the poles ...
    e = np.sqrt(1-(b/a)**2)
    f = [C[0]-e*a,C[0]+e*a]
    ax.plot([f[0],f[1]],[C[1],C[1]],'ro')
    ax.axis('equal')
    
    # take any aritrary val of phi ...
    rpoints = 5
    phi = np.random.random(rpoints) * np.pi
    p   = C[0] + a * np.cos(phi)
    q   = C[1] + b * np.sin(phi)
    
#    print(' points (p,q);')
#    print('p={:s}'.format(str(p)))
#    print('q={:s}'.format(str(q)))

    # draw the point ...
    ax.plot(p, q, 'go')
    # and connect to the poles ...
    for r in range(rpoints):
        ax.plot([f[0],p[r],f[1]],[C[1],q[r],C[1]],'g--')
    
    if save:
        plt.savefig('Ellipse.pdf')
    
    return p,q,f,e

def runMain():
    #
    C   = (0,0)    # center point C holding the ellipse origin
    a,b = 2,1.5   # a,b the major and the minor semiaxis
    N = 90+1        # one point extra to close the ellipse

    # generate the points
    
    E = genEllipse(C,a,b,N)
    
    p,q,f,e = plotEllipse(E,C,a,b,N)
    
    # EXPERIMENT: verify below that the distances are correct and always
    #             equal-valued for an ellipse, even in the event the
    #             ellipse decayes into a circle (which is a special 
    #             ellipse with a=b=R)
    print('Ellipse characteristics;')
    print('semi-major a             :  {:8.5g}'.format(a))
    print('semi-minor b             :  {:8.5g}'.format(b))
    print('eccentricity             :  {:8.5g}'.format(e))
    print('center                   :  ({:+8.3f},{:+8.3f})'.format(C[0],C[1]))
    print('poles: f0                :  ({:+8.3f},{:+8.3f})'.format(f[0],C[1]))
    print('       f1                :  ({:+8.3f},{:+8.3f})'.format(f[1],C[1]))
    print('distance: fo-(p,q)-f1    :  {:8.5f}'.format(2*a))
    print('area                     :  {:8.5g}'.format(np.pi*a*b))
    print('perimeter (approx.)      :  {:8.5g}'.format(2*np.pi*a*getK(a,b)))
    
runMain()

