"""
Acceleration2 -- computer acceleration using NumPy and using
                 a 3-point differentiation
                 
@Author : Bart Gerritsen
"""

import numpy as np
import scipy.linalg as la
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

def exportAccStats(fname,xvaTable,dd,delim=' '):
    OK = 0
    print('saving data to export file: {:s} ...'.format(fname))   
    np.savetxt(fname, xvaTable, \
               fmt = '%+12.9e', delimiter=delim, newline='\n', \
               header='# Run 102 Acceleration data\n{:s}'. \
               format(str(dd)), \
               footer='', comments='# ')
    print('...export done')
    return OK

def getPolyModel(x,y,degree):
    """
    compute the model polynomial given its coefficients ...
    """
    # find the coefficients first using least square ...
    coeffs = np.polyfit(x,y,degree)
    poly   = np.poly1d(coeffs)
    print('coefficients: {:s}'.format(str(coeffs)))
    
    N = len(x)
    model = np.zeros(N, dtype=float)
    # for each position ...
    for p in range(N):
        # for each term of the polynomial
        model=poly(x)
    return model

def getPolyModelEXCEL(pos,coeffs):
    """
    compute the model polynomial given its coefficients ...
    """    
    N = len(pos)
    model = np.zeros(N, dtype=float)
    # which degree, i.e. how many coefficients?
    PMAX = len(coeffs)
    # for each position ...
    for p in range(N):
        # for each term of the polynomial
        for k in range(PMAX):
            model[p] += coeffs[PMAX-k-1] * np.power(p,k)
    return model
    
    
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

    
def plotStats(xva,dd,save=False):
    SUBROWS = 1
    SUBCOLS = 3
    
    N,M = xva.shape
    
    print('xva dimensions: ({:d},{:d})'.format(N,M))
    
    # set the subplot layout and sizes ...
    fig, ax = plt.subplots(SUBROWS,SUBCOLS, figsize=(10,4))  
    # ... make the plots nicely fit together ...
    fig.tight_layout(pad=2.0,w_pad=4.5,h_pad=0.0)
    
    # plot the Velocity measured ...
    
    # ... define the plot scales ...
    ax[0].set_xlim(0,20)
    ax[0].set_ylim(0,np.ceil(np.amax(xva[...,dd['VELO']])))
    # ... add the plots one by one ...
    ax[0].plot(xva[...,dd['POS']],xva[...,dd['VELO']],'r-o',label='$x(x)$')
    ax[0].plot(xva[...,dd['POS']],xva[...,dd['CTRL']],'r-.',label='$a(x)$ central')
    # ... turn on grid ...
    ax[0].grid(axis='both',which='major')
    # ... decorate graph and axes ...
    ax[0].set_title('Velocity plot NumPy')
    ax[0].set_xlabel('Distance $[m]$', ha='center')
    ax[0].set_ylabel('Velocity $[m/s]$')

    # plot the polynomial velocity models ...
    ax[0].plot(xva[...,dd['POS']],xva[...,dd['PLY1']],'k:', label='poly 1')
    ax[0].plot(xva[...,dd['POS']],xva[...,dd['PLY2']],'k-.',label='poly 2')
    ax[0].plot(xva[...,dd['POS']],xva[...,dd['PLY3']],'k-', label='poly 3')

    # ... compare to the trendlines EXCEL computes ...
    
    ax[1].set_xlim(ax[0].get_xlim())
    ax[1].set_ylim(ax[0].get_ylim())
    # ... add the plots one by one ...
    ax[1].plot(xva[...,dd['POS']],xva[...,dd['VELO']],'r-o',label='$x(x)$')
    ax[1].plot(xva[...,dd['POS']],xva[...,dd['CTRL']],'r-.',label='$a(x)$ central')
    # plot the EXCEL trendlines for verification ...
    ax[1].plot(xva[...,dd['POS']],xva[...,dd['PLX1']],'k:', label='EXCEL 1')
    ax[1].plot(xva[...,dd['POS']],xva[...,dd['PLX2']],'k-.',label='EXCEL 2')
    ax[1].plot(xva[...,dd['POS']],xva[...,dd['PLX3']],'k-', label='EXCEL 3')
    # ... turn on grid ...
    ax[1].grid(axis='both',which='major')
    # ... decorate graph and axes ...
    ax[1].set_title('Velocity trendlines EXCEL')
    ax[1].set_xlabel('Distance $[m]$', ha='center')
    ax[1].set_ylabel('Velocity $[m/s]$')

    # Acceleration subplot ...
    
    ax[2].set_xlim(ax[0].get_xlim())
    ax[2].set_ylim(np.floor(np.amin(xva[...,dd['DIFF']])), \
                   np.ceil( np.amax(xva[...,dd['DIFF']])))
    # ... plot acceleration stats ...
    ax[2].plot(xva[...,dd['POS']],xva[...,dd['ACC1']],'g-.',label='$a(x)$')
    ax[2].plot(xva[...,dd['POS']],xva[...,dd['ACC2']],'y--',label='$a(x)$ corr')
    ax[2].plot(xva[...,dd['POS']],xva[...,dd['CTRL']],'r.' ,label='$a(x)$ central')
    ax[2].plot(xva[...,dd['POS']],xva[...,dd['DIFF']],'b--',label='$\Delta v/\Delta x$')
    # plot the polyline fit to the ACC2 data ...
    ax[2].plot(xva[...,dd['POS']],xva[...,dd['ACCP']],'k-', label='poly 3 corr')
    
    # ... turn on grid ...
    ax[2].grid(axis='both',which='major')
    # ... decorate graph and axes ...
    ax[2].set_title('Acceleration plot')
    ax[2].set_xlabel('Distance $[m]$', ha='center')
    ax[2].set_ylabel('Acceleration $[m/s^2]$')

    # draw legends ...
    for s in range(len(ax)):
        ax[s].legend(loc='best')
    
    # Save all the subplots?
    if save == True:
        # ... save plot on file ...
        fig.savefig('Run102-4.pdf')

def runMain():
    # constants ...
    COMMA = ','
    
    OK    =  0
    NotOK = -1
    
    # the layout for the xvaTable ...
    dataDict = {
    'POS' :  0,    # positiona vector along x-axis
    'VELO':  1,    # velocity data, measured in pos[]
    'PLY1':  2,    # polynomial model, degree 1
    'PLY2':  3,    # polynomial model, degree 2
    'PLY3':  4,    # polynomial model, degree 3
    'PLX1':  5,    # trendline degree 1 imported from EXCEL
    'PLX2':  6,    # trendline degree 2 EXCEL
    'PLX3':  7,    # trendline degree 3 EXCEL
    'ACC1':  8,    # acceleration, degree=1 data
    'ACC2':  9,    # acceleration, degree=2 data
    'CTRL': 10,    # central model difference
    'DIFF': 11,    # Dx/Dy stepwise difference
    'ACCP': 12     # model poly 3 for acceleration  
    }
    
    # read velocity data from file ...
    DATPATH  = './'
    DATFILE  = 'velocity1.dat'
    DOPRINT  = False
    # export acceleration data to ...
    EXPPATH  = DATPATH
    EXPACCL  = 'acceleration.dat'
    
    # read the velocity data ...
    pos,velo = loadVeloDataFromFile(DATPATH+'/'+DATFILE,COMMA,DOPRINT)
      
    # print the velocity plus acceleration statistics ...
    printVeloStats(pos,velo)

    # prepare one big table and pack all data for plotting ...
    N = len(pos)    # nr of data points
    nrPlots = len(dataDict)
    xvaTable = np.zeros(N*nrPlots, dtype=float).reshape(N,nrPlots)
    
    # ... and start packing data array into a central xvaTable one-by-one ...
    xvaTable[...,dataDict['POS' ]] +=  pos  # add positions to first column
    xvaTable[...,dataDict['VELO']] += velo  # ... velocity to second column
    
    # fit polynomails to the data up to degree 3 ...
    model = getPolyModel(pos,velo,1)
    xvaTable[...,dataDict['PLY1']] += model  # ... add next poly model
    
    model = getPolyModel(pos,velo,2)
    xvaTable[...,dataDict['PLY2']] += model  # ... next polynomial model
    
    model = getPolyModel(pos,velo,3)
    xvaTable[...,dataDict['PLY3']] += model  # ... next polynomial model    

    # let's compare this with what Excel says ...
    
    # add polynomial models to velocity AS CREATED by EXCEL ...
    # ... polynomial degree 1: y = 0.7148*x+0.3825
    model = getPolyModelEXCEL(pos, [0.3825,0.7148])
    xvaTable[...,dataDict['PLX1']] += model  # ... add poly model 
    # ... poly, degree 2: velo = -0.0313*x^2+0.8789*x -0.5132
    model = getPolyModelEXCEL(pos, [-0.0313,0.8789,-0.5132])
    xvaTable[...,dataDict['PLX2']] += model  # ... add poly model
    # ... poly, degree 3: velo = -0.0013*x^3-0.0015*x^2+0.6971*x-0.3122
    model = getPolyModelEXCEL(pos, [-0.0013,-0.0015,0.6971,-0.3122])
    xvaTable[...,dataDict['PLX3']] += model  # ... add poly model
 

    # obtain acceleration data ...
    
    acc1 = getAccData(pos,velo,degree=1,step=1)
    acc2 = getAccData(pos,velo,degree=2,step=1)
    # ... and print it ...
    printAccStats(pos,acc1,'degree 1')
    printAccStats(pos,acc2,'degree 2')
    
    # ... pack it ...
    xvaTable[...,dataDict['ACC1']] += acc1  # ... acceleration to third column
    xvaTable[...,dataDict['ACC2']] += acc2  # ... acc. 2 to fourth column
    
    # now add check data we compute ourselves ...
    ctrl = getCentrals(pos,velo,to_begin=velo[0], to_end=velo[N-1])
    xvaTable[...,dataDict['CTRL']] += ctrl  # ... 3-point calc gradients 
    
    # add difference data ...
    edif = np.ediff1d(velo, to_begin=0)
    xvaTable[...,dataDict['DIFF']] += edif  # ... point to point Delta y
    
    printAccStats(pos,ctrl,'3-points, central')
    printAccStats(pos,edif,'Dv/Dx')
    
    model =  model = getPolyModel(pos,acc2,3)
    xvaTable[...,dataDict['ACCP']] += model # ... add poly model
    
    exportfile = EXPPATH + '/' + EXPACCL
    result = exportAccStats(exportfile,xvaTable,dataDict)
    if not result==OK:
        print('export acceleration statistics failed.')

    # now plot all the data ...    
    plotStats(xvaTable,dataDict,save=True)
    
    print('Velocity analysis done.')



# run the main function ...
runMain()