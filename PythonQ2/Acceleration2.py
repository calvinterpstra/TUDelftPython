"""
Acceleration2 -- computer acceleration using NumPy and using
                 a 3-point differentiation
                 
@Author : Bart Gerritsen
"""

import math
import numpy as np
import matplotlib.pyplot as plt


def loadVeloDataFromFile(flname,delim=',',DOPRINT=False):
    """
    load verlocity data from given CSV file, using MunPy load...().
    Specify the delimeter (default: ',') to separate columns
    return: x,v = position resp. velocity measured in that position
    """
    x, v = np.loadtxt(flname, dtype=(float,float), \
                      delimiter=delim, comments='#', \
                      usecols=(0,1), unpack=True)
    print('data loaded: {:s}'.format(flname))
    if DOPRINT:
        ndx = 0
        for j in range(len(x)):
            print('read: (x,v)[{:2d}] = ({:5.2f},{:5.2f})'. \
                  format(ndx,x[j],v[j]))
            ndx += 1
    return x,v

def getAccData(pos,velo, degree=1, step=1):
    """ 
    Numerically compute gradient degree 1 and 2 edge effects ...
    return array acc
    """
    return np.gradient(velo, step, edge_order=degree)

def getCentrals(pos,velo, step=1, to_begin=0, to_end=0):
    """
    return the central point gradient using a 3-point method
    """
    N = len(pos)
    ctrl = np.empty((N), dtype=float)
    xl = to_begin
    j = 0
    while j < N:
        if j+1 < N:
            xr = velo[j+1]
        else:
            xr = to_end
        ctrl[j] = xr-xl
        xl = velo[j]
        j += 1
    # divide by twice the step size ...
    ctrl /= (2*step)     
    return ctrl
 
def printVeloStats(pos,velo):
    """
    print the velocity statistics
    """
    MIN,MAX,AVG = (0,1,2)
    veloStats = [ np.amin(velo), np.amax(velo), np.average(velo) ]
    
    # ... compute distance dist = pos - pos[0]
    dist = pos[len(pos)-1] - pos[0]
    
    print('Statistics: #data points: {:d}'.format(len(pos)) )
    print('  Travetime        [s]    : {:8.5f}'.format( dist/veloStats[AVG] ))
    print('  Distance         [m]    : {:5.2f}'.format( dist ))
    print('  min velocity     [m/s]  : {:8.5f}'.format( veloStats[MIN] ))
    print('  max velocity     [m/s]  : {:8.5f}'.format( veloStats[MAX] ))
    print('  avg velocity     [m/s]  : {:8.5f}'.format( veloStats[AVG] ))
    
def printAccStats(pos,acc,label=''):
    # see what we have obtained
    MIN,MAX,AVG = (0,1,2)
    accStats = [ np.amin(acc), np.amax(acc), np.average(acc) ]
    
    print('Acceleration stats {:s};'.format(label))
    print('  min acceleration [m/s2] : {:8.5f}'.format( accStats[MIN]) )
    print('  max acceleration [m/s2] : {:8.5f}'.format( accStats[MAX]) )
    print('  avg acceleration [m/s2] : {:8.5f}'.format( accStats[AVG]) )

def plotStats(xva,save=False):
    N,M = xva.shape
    
    print('xva dimensions: ({:d},{:d})'.format(N,M))
    
    fig, ax = plt.subplots(1, figsize=(6,4))
    
    # ... define the plot scales ...
    ax.set_xlim(0,20)
    # ax.set_ylim(0,math.ceil(np.amax(v)))
    ax.set_ylim(-1,2)
    
    # ... plot acceleration stats ...
    ax.plot( xva[...,0], xva[...,2], 'g-.', label = '$a(x)$')
    ax.plot( xva[...,0], xva[...,3], 'y--', label = '$a(x)$ (corr.)')
    ax.plot( xva[...,0], xva[...,4], 'r.' , label = '$a(x)$ central')
    ax.plot( xva[...,0], xva[...,5], 'b--', label = '$\Delta v/\Delta x$')
        
    # ... turn on grid ...
    ax.grid(axis='both',which='major')
    # ... decorate graph and axes ...
    ax.set_title('Acceleration plot')
    ax.set_xlabel('Distance $[m]$', ha='center')
    ax.set_ylabel('Acceleration $[m/s^2]$')
                                                                                                          
    ax.legend(loc='best')
    
    if save == True:
        # ... save plot on file ...
        fig.savefig('Run102-3.pdf')
    

def runMain():
    # constants ...
    COMMA = ','
    
    # read velocity data from file ...
    DATPATH = './'
    DATFILE = 'velocity1.dat'
    DOPRINT = False
    
    # read the velocity data ...
    pos,velo = loadVeloDataFromFile(DATPATH+'/'+DATFILE, COMMA, DOPRINT)
    
    # print the velocity plus acceleration statistics ...
    printVeloStats(pos,velo)
    
    # obtain acceleration data ...
    acc1 = getAccData(pos,velo,degree=1,step=1)
    acc2 = getAccData(pos,velo,degree=2,step=1)
    # ... and print it ...
    printAccStats(pos,acc1,'degree 1')
    printAccStats(pos,acc2,'degree 2')

    # pack all data for plotting ...
    N = len(pos)    # nr of data points
    G = 6           # nr of plots
    xvaTable = np.zeros(N*G, dtype=float).reshape(N,G)
    
    xvaTable[...,0] +=  pos  # add position data to first column
    xvaTable[...,1] += velo  # ... velocity data to second column
    xvaTable[...,2] += acc1  # ... acceleration degree 1 to third column
    xvaTable[...,3] += acc2  # ... acceleration degree 2 to fourth column
    
    # now add check data we compute ourselves ...
    ctrl = getCentrals(pos,velo,to_begin=velo[0], to_end=velo[N-1])
    xvaTable[...,4] += ctrl  # ... 3-point calc gradients 
    
    edif = np.ediff1d(velo, to_begin=0)
    xvaTable[...,5] += edif  # ... point to point Delta y
    
    printAccStats(pos,ctrl,'3-points, central')
    printAccStats(pos,edif,'Dv/Dx')
        
    plotStats(xvaTable,save=True)
    
    print('Velocity analysis done.')
 
# run the main function ...
runMain()