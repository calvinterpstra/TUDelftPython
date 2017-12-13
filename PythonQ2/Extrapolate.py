# -*- coding: utf-8 -*-
"""
Extrapolate.py -- extrapolation with and without a model

@author: Bart Gerritsen
"""

import re
import numpy as np
import scipy.optimize as sp
import matplotlib.pyplot as plt


def getSamples(nrSamples,modelName,modelparms,xrange,yrange,noiseLevel):
    data = np.zeros(nrSamples*2, dtype=float).reshape(nrSamples,2)
    # residual R = 0
    R = 0
    # generate and scale ... and add noise
    x = np.linspace(xrange[0],xrange[1],nrSamples,endpoint=True,dtype=float)
    data[:,0] = x
    # .. start computing the noise ...   
    r = np.random.rand(nrSamples)
    R = noiseLevel*(yrange[0] + (yrange[1]-yrange[0])*r)
    # ... preload it ...
    data[:,1] += R
 
    # does model name start with 'atan' or 'ATAN' or something?
    # feel free to implement more models below ...
    model = re.compile(modelName[:len('atan')], re.IGNORECASE)
    if model.match('poly'):
        # invoke the linear model ...
        data[:,1] += polyModel(x,modelparms)
    elif model.match('atan'):
        # invoke the arctan model ...
        data[:,1] += atanModel(x,modelparms)
    elif model.match('expo'):
        # invoke an exponential model ...
        data[:,1] += expoModel(x,modelparms)
    else:
        # hmm, we have not (yet) implement the mode requested ...
        print('model {:s} not yet implemented'.format(modelName))
        data = None
    return data, R

def polyModel(x,C):
    return C[0] + C[1]*x + C[2]*x**2

def expoModel(x,C):
    return C[0] + C[1]*np.exp(C[2]*x)

def atanModel(x,C):
    return C[0] + C[1]*np.arctan(C[2]*(x-C[3]))

def runMain():
    MODELNAME  = 'polyModel'
    MODELPARMS = [-1.2,0.49,0.34]
    NOISELEVEL = 2.58
    N=24
    XMIN,XMAX  = ( -5, 15)
    YMIN,YMAX  = ( -5, 10)
    data, R = getSamples(N,MODELNAME,MODELPARMS, \
                         [XMIN,XMAX],[YMIN,YMAX],NOISELEVEL)
    coeffs = np.polyfit(data[:,0],data[:,1],2)
    print(coeffs)
    
    plt.plot(data[...,0],data[...,1],'ro')
    
    x = data[...,0]
    y = coeffs[2] + coeffs[1]*x + coeffs[0]*x**2
    
    # extrapolate ...
    plt.plot(x,y,'k-',linewidth=3.0,label='model')
    plt.grid(which='major',axis='both')
        
    # extrapolate to the point: x=20 ...
    
    # ... method 1: use last gradient and extrapolate ...
    NEWX = 20
    NEWY = data[-2][1] + (data[-1][1]-data[-2][1])* (NEWX-data[-1][0])
    plt.plot(NEWX,NEWY,'ko')
    plt.plot([data[-2][0],NEWX] , [data[-2][1],NEWY],'k:',label='last gradient')
    
    # ... method 2: use a model and analytically extrapolate ... 

    NEWY = coeffs[2] + coeffs[1]*NEWX + coeffs[0]*NEWX**2
    
    plt.plot(NEWX,NEWY,'bo')
    plt.plot(np.append(x,[ NEWX ]),np.append(y,[ NEWY ]), \
             'b:', linewidth=3.0, label='model exttension' )
    
    plt.legend(loc='best')
    plt.savefig('Extrapolate.pdf')
    
runMain()