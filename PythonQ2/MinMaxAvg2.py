# -*- coding: utf-8 -*-
"""
MinMaxAvg2.py

@author: Bart Gerritsen
"""

import numpy as np
import matplotlib.pyplot as plt

def getSamples(N,RANGE):
    """ 
    returns N uniformly distributed samples (floats)
    in range RANGE[0] .. RANGE[1]
    """
    LOW,HIGH = (0,1)
    r = np.random.random(N)
    # scale the samples into the range ...
    samples = RANGE[LOW] + r*(RANGE[HIGH]-RANGE[LOW])
    return samples
    
def plotStats(S,RANGE,save=True):
    """
    Plots the data in S in 4 sublots:
    Samples, xmin, xmax, avg
    The stats are running stats, updated
    sample by sample
    """
    # assign the subplots an identifier ...
    PSAMP,PXMIN,PXMAX,PXAVG = (0,1,2,3)
    # detemrine the boundaries of the range ...
    XMIN,XMAX,XAVG = RANGE[0],RANGE[1],np.sum(RANGE)/2.0

    # EXPERIMENT: set S to one of:
    #S = [XMIN,XMIN,XMIN,XMIN,XMIN]
    #S = [XMAX,XMAX,XMAX,XMAX,XMAX]
    #S = [XAVG,XAVG,XAVG,XAVG,XAVG]
    #S = [8.0, 2.0, 1.0, 9.0]
    
    # find out the sample set size ...
    nrSamples = len(S)
    
    # ... and the expected avg (only for uniform distribution) ....
    midRange = XAVG
    
    # create the figure ...
    fig, ax = plt.subplots(1,4, figsize=(16,4))
    
    for axis in ax:
        axis.set_ylim(RANGE[0],RANGE[1])
        axis.set_xlim(0,nrSamples+1)
        axis.plot([0,nrSamples+1],[midRange,midRange],\
                  'k:',alpha=.9,linewidth=3.0)
        axis.grid(axis='both', which='major')
        axis.set_xlabel('Sample')
    # decorate the plots...
    ax[PSAMP].set_title('Samples (N={:s})'.format(str(nrSamples)))
    ax[PXMIN].set_title('Running min')
    ax[PXMAX].set_title('Running max')
    ax[PXAVG].set_title('Running avg')
    
    # start the plot at initial values settings ...       
    xminp,xmaxp,avgp = XMAX, XMIN, np.sum(RANGE)/2.0
    xmin ,xmax ,avg  = xminp,xmaxp,avgp
    p0,p,asum = 0,1,0.0
    while p <= nrSamples:
        # obtain the next sample 
        s = S[p-1]
        # plot the sample ...
        ax[PSAMP].plot([p],[s],'bo')
        # use NumPy fnctions to find moving stats ...
        xmin = np.amin(S[:p])
        xmax = np.amax(S[:p])
        avg  = np.mean(S[:p])
        # now update the plot ...
        ax[PXMIN].plot([p0,p],[xminp,xmin ],'g-',linewidth=3.0)
        ax[PXMAX].plot([p0,p],[xmaxp,xmax ],'r-',linewidth=3.0)
        ax[PXAVG].plot([p0,p],[avgp ,avg  ],'m-',linewidth=3.0)
        # handover to the next loop cycle ...
        xminp,xmaxp,avgp = xmin,xmax,avg
        p0,p = p,p+1
        
    if save:
        fig.savefig('minmaxavg2.pdf')
        

def runMain():
    N=20
    MIN,MAX = (0,10)
    
    S = getSamples(N,(MIN,MAX))

    plotStats(S,(MIN,MAX))


runMain()