# -*- coding: utf-8 -*-
"""
myLATask.py        -- Compute angle phi between two vectors

@author : Bart Gerritsen
"""

# importeer math om de acos() functie te 
# kunnen gebruiken ...
from math import *;
# import matplotlib pyplot en noem dat plt
import matplotlib.pyplot as plt;


def dot(u,v):
    """
    return the dot product u.v of two vectors u and v
    
    parameters
    ----------
    u,v  vector, len(u)==len(v)
    
    return
    ------
    f = u.v real sum of the element-by-element product
    """
    if not ( len(u) == len(v) ):
        print("error: u and v must have equal lengths")
    else:
        w = 0.0
        for j in range(len(u)):
            w = w + u[j] * v[j]
    return w    


def getNorm(u):
    """
    return the norm of vector u from the following
    computation: norm = sqrt(dot(u,u))
    """
    norm = None
    # compute the norm here ...
    norm = sqrt(dot(u,u))
    return norm
    

def plotVectors(a,b):
    
    fig = plt.figure(figsize=(6,4))
    
    # origin O = (0.0)
    orig = (0,0)
    plt.plot([orig[0], a[0]], [orig[1], a[1]], 'r-', [a[0]],[a[1]],'r*')
    plt.plot([orig[0], b[0]], [orig[1], b[1]], 'g-', [b[0]],[b[1]],'g*')
    
    plt.plot([orig[0]], [orig[1]],'ko')
    plt.grid(axis='both', which='major')
    plt.axis('equal')
    
def doThisMain():
    
    u = [1, 3]
    v = [3,-1]
    
    # compute the form of u and v ...
    normU = getNorm(u)
    normV = getNorm(v)
    
    # phi = acos( (u.v)/(|u||v|) )
    phi = acos( (dot(u, v)/(normU*normV)) );
 
    # print the dot product 
    print('Dot product w=u.v=' + '{:+8.5f}'.    format(dot(u, v)) )
    print('Angle phi (rad)  =' + '{:+8.5f} pi'. format(phi/pi) )
    
    print('length |u|       = {:8.5f}'.format(normU))
    print('length |v|       = {:8.5f}'.format(normV))
    
    # compute the normUV from the other two vectors u and v
    normUV = sqrt( normU**2 + normV**2 );
    print('length |u-v|)    = {:8.5f}'.format(normUV))
    
    plotVectors(u,v)

# launch your main function ...
doThisMain();