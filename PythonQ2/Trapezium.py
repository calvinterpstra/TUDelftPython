# -*- coding: utf-8 -*-
"""
Trapezium.py  -- numerical integration using the trapezium rule.

@author: Bart Gerritsen
"""

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

def F(x):
    return np.sqrt(np.exp(x**(6/5))-(9/5)*x+(1/3)*x**(3/2))
    
def doMain():
    # integrate over domain ?
    XMAX = 10.0
    XMIN =  0.0
    YMAX = 3000
    YMIN =    0

    # prepare the figure ...
    fig, axes = plt.subplots(nrows=1,ncols=5, \
                             sharex=True, sharey=True,figsize=(12,4) )
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    
    # prepare a high-precision curve to serve as the 'exact' ...
    hpPoints = int(10000+1)
    S = np.empty(hpPoints*2, dtype=np.float).reshape(hpPoints,2)
    t = np.linspace(XMIN,XMAX,num=hpPoints,endpoint=True)
    S[:,0] = [   s  for s in t ]
    S[:,1] = [ F(s) for s in t ]
    
    # compute the high-precision approximation of the integral ...
    hpIntgrl = sp.integrate.trapz(y=S[:,1],x=S[:,0],dx=1)
    print('Integral y=F(x), x in [0..10] HIGH-PRECISION (N={:d}): {:+.9f}'. \
              format(hpPoints+1,hpIntgrl))
 
    # now do an integrations with varying stepsize, here
    # specified as a fraction of the x-range ....
           
    # specify the fraction of the domain for step size ... 
    fractions = [0.5, 0.1, 0.05, 0.01, 0.005]
    
    sub = 0 # first subplot ...
    for fr in fractions:
        # with this domain fraction, the stepsize is?
        step = fr*(XMAX-XMIN)
        
        # how many data points to expect
        nData = int( (XMAX-XMIN)/step ) + 1
    
        # compute the numerical integration data points ...
        data = np.zeros((nData,2), dtype=np.float)
        #  ... generate data [x,F(x)] ..
        for k in range(data.shape[0]):
            x = XMIN + k * step
            data[k][0] = x
            data[k][1] = F(x)
        
        # ... and plot the curve so obtained ...
        
        # set the subplot ...
        p = axes[sub]
        # ... plot on it the current approximation and the reference curve ...
        p.plot(data[:,0],data[:,1],'r-',S[:,0],S[:,1],'b-.', linewidth=1.)
        # ... set the grid and the title
        # p.title('step = {:s}'.format(str(step)))
        p.grid(which='major', axis='both', alpha=0.5)
        
        # call in NumPy tp do the actual integration with trapizum method ...
        valIntgrl = sp.integrate.trapz(y=data[:,1],x=data[:,0],dx=1)
        # ... compute the deviation from the reference value hpIntgrl ...
        dev = 100*(valIntgrl-hpIntgrl)/hpIntgrl
        print( \
        'I(F(x)), x in [0..10], step={:.2f}: {:+.9f} (dev={:+5.2f}%)'. \
              format(step,valIntgrl,dev)) 
        p.text((XMAX-XMIN)/2, YMAX+1, '$dx={:.2f}, \Delta I={:+5.2f}\%$'. \
               format(step,dev), ha='center')
        
        # prepare for the next subplot ...
        sub += 1
        
    # save my results in a plot ...
    fig.savefig('trapezium.jpg', dpi=600)
    
doMain()