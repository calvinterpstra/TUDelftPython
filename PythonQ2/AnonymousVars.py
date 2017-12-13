# -*- coding: utf-8 -*-
"""
AnonymousVars.py -- On the use of anonymous versus names variables

@author: Bart Gerritsen
"""

import numpy as np
import matplotlib.pyplot as plt


def doMain():
    # EXPERIMENT: anonymous versus named variables ...
    #             separate all the information determining 
    #             your plots from the logic in the loop 
    
    # put a reference to the module pyplot in my variable p ...
    p = plt
    
    # define a domain ...
    myDomain = np.linspace(0,2,21,dtype=np.float,endpoint=True)*np.pi

    # these are the plots I would like to make ..
    myPlots  = ( p.figure(num=1,figsize=(6,4)), \
                 p.figure(num=2,figsize=(6,4)), \
                 p.figure(num=3,figsize=(6,4))  )
    
    # specify a phase shift and apply broadcasting ...
    myShifts = ( 0.0, 0.0, -1.0 )
    myFuncs  = ( np.sin, np.cos, np.tanh )
    myLegends= ('$\sin(\phi)$', '$\cos(\phi)$', '$tanh(\phi-\pi)$' )
    myStyles = ( 'r-*', 'g-o', 'b-+')
    
    
    # you don't need to change anything below to plot different 
    # functions, phase shift, or domains ...
    
    plot = 0
    for f in myPlots:
        p.figure(f.get_figure())
        p.plot(myDomain, \
                   # use broadcasting to apply the phase shift ...
                   myFuncs[plot](myDomain + [ myShifts[plot]*np.pi ]), \
                   myStyles[plot])
        p.grid(axis='both',which='major')
        p.xlabel('$\phi$ [rad]')
        p.title( 'my plot #{:d}'.format(plot+1) )
        p.text(0.05*np.pi,-0.6,'$f(\phi)_{:s}=${:s}'. \
               format(str(plot+1), str(myLegends[plot])))
        fname = 'my-plot-#{:s}.pdf'.format(str(plot+1))
        p.savefig(fname,dpi=1200,orientation='landscape')
        plot += 1

    
if __name__=='__main__': doMain()