# -*- coding: utf-8 -*-
"""
Fit arctan model 

@author: Bart Gerritsen
"""

# for string matching ...
import re
import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt


def getSamples(nrSamples,modelName,modelparms,xrange,yrange,noiseLevel):
    data = np.empty(nrSamples*2, dtype=float).reshape(nrSamples,2)
    # residual R = 0
    R = 0
    # generate and scale ... and add noise
    x = np.linspace(xrange[0],xrange[1],nrSamples,endpoint=True,dtype=float)
    r = np.random.rand(nrSamples)
    # does model name start with 'atan' or 'ATAN' or something?
    # feel free to implement more models below ...
    model = re.compile(modelName[:len('atan')], re.IGNORECASE)
    if model.match('atan'):
        # invoke the arctan model ...
        # .. start computing the noise ...
        R = noiseLevel*(yrange[0] + (yrange[1]-yrange[0])*r)
        # ... then compute a NO NOISE y ...
        y = atanModel(x,modelparms)
        # ... and compose all elements ...
        data[:,0] = x
        data[:,1] = y + R 
    else:
        # hmm, we have not (yet) implement the mode requested ...
        print('model {:s} not yet implemented'.format(modelName))
        data = None
    return data, R
    
def atanModel(x,C):
    # use an atan model on the noisy data ...
    return C[0] + C[1]*np.arctan(C[2]*(x-C[3]))

def plotSamples(D):
    assert not D is None, 'we don''t have valid data. Nodel not implented? '
    N,M = D.shape
    
    fig, ax = plt.subplots(1, figsize=(10,4))
    
    ax.plot(D[:,0],D[:,1],'ro')
    ax.grid(which='major', axis='both')
    return ax
    
def plotModelFit(ax,mData,colorStr,dataLabel=''):
    # find the optimal coefficients ...
    
    # ... plot the model fit ...
    ax.plot(mData[:,0],mData[:,1],colorStr,linewidth=3.0,label=dataLabel)
    ax.set_title('Least-squares model fit')
    ax.legend(loc='best')

def runMain():

    MODELNAME  = 'AtanModel'
    MODELPARMS = [0.0,0.55,1.0,0]
    NOISE      =  0.15
    
    # generate noise-endowed points using the above model ...
    N = 64
    XMIN,XMAX = (-20,20)
    YMIN,YMAX = ( -1, 1)
    data, noise = getSamples(N,MODELNAME,MODELPARMS, \
                             [XMIN,XMAX],[YMIN,YMAX],NOISE)
    # plot all the sample data ...
    axis = plotSamples(data)
    
    # let's fit a atan model and see the best fit ...
    # ... we reduce the model to a linear combination: 
    #     y = C0 + C1*atan(x) so that:
    #     the model parameters are [C0,C1,1,0], of which:
    #     we let Least Squares compute [C0,C1]
    #     Define y = Ap, so that: A = [[1 atan(C2*(x-C3))]
    A = np.zeros(N*2, dtype=float).reshape(N,2)
    A[:,0] = [1] # use NumPy's broadcast to create a 1-column ...
    # Define the linear components in matrix A for the model to fit ...
    A[:,1] = np.arctan(MODELPARMS[2]*(data[:,0]-MODELPARMS[3]))
    # Now let least squares find out the best C0 and C1 ...
    # of course we expect these to be close to the model we used
    # to generate the samples ...
    coeffs, resid, rank, sigma = la.lstsq(A,data[:,1])
    
    print('least squares Atan model fitting results;')
    print('coefficients model {:<10s}: {:s}'.format(MODELNAME,str(coeffs)))
    print('residuals                    : {:s}'.format(str(resid)))
    print('sigma                        : {:s}'.format(str(sigma)))
    print('rank                         : {:s}'.format(str(rank)))
    print('Euclidean norm noise vector  : {:.6f};'.format(la.norm(noise,2)))
    
    # now that we have the optimized parameters for [C0,C1],
    # update the model parms and generate the model data ..
    newParms = MODELPARMS
    newParms[0] = coeffs[0]
    newParms[1] = coeffs[1]
    
    modelData = np.zeros(N*2, dtype=float).reshape(N,2)
    modelData[:,0] = data[:,0]
    modelData[:,1] = atanModel(modelData[:,0],newParms)
    
    coeffStr = '[C0,C1,C2,C3]=[{:+.3f},{:+.3f},{:+.3f},{:+.3f}]'. \
                    format(newParms[0],newParms[1],newParms[2],newParms[3])
    label = 'Model: {:s}\n\n{:s}\n\nN={:d}'.format(MODELNAME,coeffStr,N)
    plotModelFit(axis,modelData,'b-.',dataLabel=label)

    plt.savefig('AtanModel.pdf')
    
# run it ...
runMain()
    