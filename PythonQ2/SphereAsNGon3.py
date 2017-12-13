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
            print('N={:2d}: z=(x,y)=({:+5.3f},{:+5.3f})'. \
                  format(int(N),float(X[k][0]),float(Y[k][0])))
    # return two arrays of data ..
    return X,Y

def getDiff(X,Y,R,doPrint=False):
    """
    Returns the perimeter difference betwween exact circle and n-gon
    """
    n = len(X)
    pExact  = 2*np.pi*R
    # we are going to walk X but actually for a REGULAR n-gon
    # this is a waste of tesources ...
    
    # we need two points, so start wuth k=1
    # we query the length, so n == len(X) == N+1, (N from main program)
    pApprox = 0
    for k in range(1,n):
        pApprox += np.sqrt( (X[k]-X[k-1])**2 + (Y[k]-Y[k-1])**2 )
    # compute the fraction (do not mult by 100)
    diff = (pApprox-pExact)/pExact
    if doPrint:
        print('For n={:>2s} the difference is: {:+12.5%}'. \
              format(str(n-1),float(diff)))
    return diff

def subPlotNGon(SubPlotNr,n,U,V,SX,SY,colorStr,grid=True,withRef=True):
    # check input data first;
    assert n >=3, 'Start n-gon form n=3 onward'
    assert len(SubPlotNr) == 3, 'Invalid subplor number'
    if withRef:
        assert len(SX) > 0 and len(SY) == len(SX), 'Missing ref data'

    # point to the right subplot 
    r,c,pn = SubPlotNr          # 3-tuple (#rows, #cols, plot number)
    p = plt.subplot(r,c,pn)
    
    # ... plot graph with data points ...
    p.plot(U, V, colorStr)
    # ... and reference circle ??
    if withRef: p.plot(SX,SY,'r--')
    
    # ... set grid ?
    if grid: plt.grid(axis='both',which='major')
        
    # ... set title this n-gon ...
    ttlOffset = 1.0
    nLabel = 'n={:d} ({:+7.2%})'.format(n,float(getDiff(U,V,1)))
    if pn > SubPlotNr[1]:
        yPos = -ttlOffset+0.6
    else:
        yPos = ttlOffset
    plt.title(nLabel,y=yPos)

def getColorStr(J):
    """
    Return a color string; if J odd, return green color, otherwise
    return blue color string for pyplot line
    """
    solid = '-'
    dash  = '--'
    if J%2==0: 
        color = 'b' 
    else: 
        color = 'g'
    return color + solid

def plotDivs(Size,N,divs):
    """
    plot the divergences (%) of the n-gon compared to circle
    Note: R is of nu influence, take R=1 (unit circle)
    """
    assert len(N) == len(divs), 'Wrong data size divergence array'
    
    # compute reference data from analytic
    plt.figure(figsize=Size)
    # percentages ...
    plt.xlim = (0,50)
    plt.ylim = (0,30)
    plt.ylabel('%')
    plt.xlabel('n')
    
    plt.plot(N, divs,'b-')
    
    plt.grid(which='major',axis='both')
    plt.title('Percentual divergence perimeter n-gon - circle' )
    
def runMain():
    # Constant definition --------------------------------------------------
    # midpoint; if to change, also change the xlim and ylim plot
    C = [0,0]   
    # unit circle (do not change, or change and also change xlim,ylim
    R = 1.0;
    # use this for a high precision circle ...
    P=360
    # use cases: N=4 .. N=P=360 (equiv of segment 90 .. 1 degree)
    N=[3,4,5,6,8,10,12,16,24,48]
    
    # How to layout the subplot? 
    # You may have to change the FIGSIZE too
    NRPLOTS = len(N)
    ROWS = 2
    COLS = int(NRPLOTS/ROWS)

    # figure size
    FIGSIZE = (10,4)
    
    # set grid?
    doGRID = True
    
    # also plot a reference circle?
    refCIRCLE = True
    # ----------------------------------------------------------------------

    # make a vector to store the data of multiple n-gons
    dataX,dataY = ([],[]) # two empty data vectors ...
    # to hold the differences with circle, as a fraction ...
    divergence = [] 
    
    for n in N:
        # n-gon data and reference data ...
        X,Y = getNGonData(C,n,R)         # default: doPrint=False
        div = getDiff(X,Y,R)*100.0       # [%]
        dataX.append(X); dataY.append(Y)
        divergence.append(div)
        
    # single set of reference data ...
    SX,SY = getNGonData(C,P,R)
   
    # let's make a subplot ...
    
    # ... first, some shared settings ...
    plt.figure(figsize=FIGSIZE)
    plt.xlim = (-1.5,1.5); plt.ylim=plt.xlim
    plt.axis('equal')
    
    for n in range(len(N)):
        # which subplot to plot?
        plotNr = (ROWS,COLS,n+1)
        # what are we going to plot?
        subPlotNGon(plotNr,N[n],
                    dataX[n],dataY[n],SX,SY,
                        getColorStr(N[n]),doGRID,refCIRCLE)

    # save this great achievement 
    plt.savefig("CircleNGonPlots.pdf")
    
    # now plot the divergences of the n-gon compared to circle
    plotDivs((6,4),N,divergence)
    
    # save this divergence plot
    plt.savefig("CircleNGonDivs.pdf")

    
# run the application ...
runMain()