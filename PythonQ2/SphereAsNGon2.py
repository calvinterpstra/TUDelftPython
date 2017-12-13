# -*- coding: utf-8 -*-
"""
SphereAsNGon2.py   -- approach a sphere by using the limit of 
N->infty for an n-gon. Enhanced version, using NumPy arrays.
Generating n-gon data using a function. Plotting has moved to
a function, too.

Reference
---------
Needham, T. Visual Complex Analysis, pp. 26

@author: Bart Gerritsen
"""

import math, numpy as np, matplotlib.pyplot as plt

def getNGonData(Center,N,R,doPrint=False):
    # check the input data first;
    # assert this condition, 'give this warning if violated'
    assert N >= 3,          'Start at n=4 minimum'
    assert R >= 0,          'Need positive radius for n-gon circle'
    assert len(Center) == 2,'Give center coordinates pair C=(c1,c2)'
    # compute angle step ...
    dPHI = 2*math.pi/N
    # n-gon data first ...
    # arrays to hold N-gon approximation data ...
    X = np.zeros(N+1).reshape(N+1,1)
    Y = np.zeros(N+1).reshape(N+1,1)
    
    for k in range(N+1):
        if k == N:
            X[k] = X[0]
            Y[k] = Y[0]
        else:
            X[k] = Center[0] + R*math.cos(k*dPHI)
            Y[k] = Center[1] + R*math.sin(k*dPHI)
        if doPrint: 
            print('z=(x,y)=({:+5.3f},{:+5.3f})'. \
                  format(float(X[k][0]),float(Y[k][0])))
    # return two arrays of data ..
    return X,Y

def plotNGon(Size,P,Q,colString,SX,SY,withRef=True):
    # check input data first;
    assert len(Size) == 2 and Size[0] > 0 and Size[1] > 0, 'Wrong size figure'
    assert withRef and len(SX) > 0 and len(SY) == len(SX), 'Missing ref data'
    
    # set figure size ...
    fig = plt.figure(figsize=Size)
    # ... prepare the plot axes ...
    axis = plt.subplot(111)
    scale =  ( math.ceil( max(P) )/10.0 ) * 10.0
    axis.set_xlim(-round(scale,1),round(scale,1)); 
    axis.set_ylim( axis.get_xlim() )
    axis.axis('equal')
    
    # ... plot graph with data points ...
    axis.plot(P, Q, 'b-')
    # ... and reference circle ??
    if withRef: 
        axis.plot(SX,SY,'r--')
    # ... turn on grid ...
    axis.grid(axis='both',which='major')
    # ... decorate graph and axes ...
    myTitle = 'Circle as a {:s}-gon'.format(str(len(Q)-1))
    myPDFFileName='CircleNGon{:s}.pdf'.format(str(len(Q)-1))
    axis.set_title(myTitle)
    
    fig.savefig(myPDFFileName)

def runMain():
    # Constant definition --------------------------------------------------
    # midpoint; if to change, also change the xlim and ylim plot
    C = [0,0]   
    # unit circle
    R = 1.0;
    # use this for a high precision circle ...
    P=360
    # use cases: N=4 .. N=P=360 (equiv of segment 90 .. 1 degree)
    N=15
    # want values printed ?
    DOPRINT = False
    # figure size
    SIZE = (6,4)
    # ----------------------------------------------------------------------

    # n-gon data and reference data ...
    DX,DY = getNGonData(C,N,R,doPrint=DOPRINT)  # check this out
    SX,SY = getNGonData(C,P,R)

    # and plot figure ...
    plotNGon(SIZE,DX,DY,'b-',SX,SY,True)

# run the application ...
runMain()