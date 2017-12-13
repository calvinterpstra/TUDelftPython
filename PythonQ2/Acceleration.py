"""
Velocity  compute position-velocity statistics, print en plot
@author : Bart Gerritsen
@date   : Aug 2017
@version: 1.0.1
"""

import math
import numpy as np
import matplotlib.pyplot as plt

# global constants
COMMA = ","
LBLROSE = '#ffeeee'
LBLCOLOR= 'darkslategrey'
LBLFONT = {'family': 'serif',
            'color': LBLCOLOR,
           'weight': 'normal',
             'size':  10
        }
LBLBOX  = {'facecolor': LBLROSE,
           'edgecolor': LBLCOLOR, 
           'boxstyle' : 'round',
                'pad' : 1
        }

# maintain status flags that tell us if data is available for 
# printing and plotting ...
VELODATA,ACCDATA = False, False

# read velocity data from file ...
DATPATH = './'
DATFILE = 'velocity1.dat'
  
# read data from file; may throw
# FileNotFoundError exception if file does not exist
fl = DATPATH + '/' + DATFILE
with open( fl ) as f:
    lines = f.readlines()
    # closes file after reading, automagically

print('data loaded: {:s}'.format(fl))

datHdr = 0
pos  = [] # empty array
velo = []
acc  = []
minVelo  =  math.inf
maxVelo  = -math.inf
avgVelo  =  0.00 # average velocity 

# analysze the data read from file ...
for line in lines:
    # if a comment line, just print it for user info
    if line[0] == '#':
        print('{:s}'.format(line), end='') # line already contains '\n'
        datHdr = datHdr + 1  # count comment lines for later 
    else:
        # read data items from the line (skip white space)
        part = line.split(COMMA)
        if len(part) != 2:
            print('hmm ... found an error in the data')
        else:
            p,v = float(part[0]),float(part[1])
            # append it to the data arrays ...
            pos.append(p); velo.append(v)
            # found a new min or max velocity?
            if v < minVelo:
                minVelo = v
            if v > maxVelo:
                maxVelo = v
            # now sum up velocity  ...
            avgVelo = avgVelo + v

# some post processing needed ...
  
# ... how many valid data points found ?
nrDataPoints = len(pos)
  
# ... and don't forget that avg is still just SUM:
#     Divide it by the N, the number of points ...
avgVelo =  avgVelo / nrDataPoints
  
# ... compute distance dist = pos - pos[0]
dist = math.ceil( pos[len(pos)-1] - pos[0] )

# set the status of the veolcity data to True 
VELODATA = True      

# now let's determine the acceleration by numerical differentiation ..
STEP = 1        # skip measurement points or not ?
ZEROGRAD = 0    # the gradient at the start of the velocity data
acc  = np.gradient(velo, STEP, edge_order=1)
acc2 = np.gradient(velo, STEP, edge_order=2)
edif = np.ediff1d( velo, to_begin=ZEROGRAD)


# see what we have obtained 
if not len(acc) == len(velo):
    print('error: computing acceleration')
    c = False
else:
    minAcc = np.amin(acc)
    maxAcc = np.amax(acc)
    avgAcc = np.average(acc)
    # set the status of the acceleration data ...
    ACCDATA = True

# now we print the basic statistics of the data
if not VELODATA:
    print('Error occurred in veolcity data processing; abandoning')
else:
    print('Statistics: #data points: {:d} (step {:d})'. \
          format(nrDataPoints,STEP) )
    print('  min velocity     [m/s]  : {:8.5f}'.format( minVelo ) )
    print('  max velocity     [m/s]  : {:8.5f}'.format( maxVelo ) )
    print('  avg velocity     [m/s]  : {:8.5f}'.format( avgVelo ) )

    # we might have veloity but but not acceleration ...
    if not ACCDATA:
        print('Error occurred in acceleration data processing; skipping')
    else:
        print('  min acceleration [m/s2] : {:8.5f}'.format( minAcc ) )
        print('  max acceleration [m/s2] : {:8.5f}'.format( maxAcc ) )
        print('  avg acceleration [m/s2] : {:8.5f}'.format( avgAcc ) )

    print('  Travetime        [s]    : {:8.5f}'.format( dist/avgVelo ) )
    print('  Distance         [m]    : {:5.2f}'.format( dist ) )


# ... and plot figure ...
if VELODATA:
    
    # ... size ...
    fig = plt.figure(figsize=(6,4))
    
    axis = plt.subplot('111')
    
    # ... prepare the plot label
    # composed of file header ...
    hdrLabel = ''
    for l in range(datHdr): 
        hdrLabel = hdrLabel+lines[l]
    # ... define the plot scales ...
    axis.set_xlim(0,20)
    axis.set_ylim(0,math.ceil(maxVelo))
    # ... plot graph with data points ...
    axis.plot(pos,velo,'r-o', label='velocity v(x)')
    
    if ACCDATA:
        # ... plot acceleration ...
        axis.plot( pos, acc, 'g-.', label = '$a(x)$')
        axis.plot( pos, acc2,'y--', label = '$a(x)$ (corr.)')
        axis.plot( pos, edif,'b--', label = '$\Delta v/\Delta x$')
        
    # ... turn on grid ...
    axis.grid(axis='both',which='major')
    # ... decorate graph and axes ...
    axis.set_title('Velocity and acceleration plot')
    axis.set_xlabel('Distance $[m]$', ha='center')
    axis.set_ylabel('Velocity $[m/s]$, acceleration $[m/s^2]$')
    
    axis.legend(loc='upper left')
    
    # ... plot label ...
    axis.text(5.3,1.2, hdrLabel, fontdict=LBLFONT, bbox=LBLBOX)
    
    # ... save it on file ...
    fig.savefig('Run102-2.pdf')

