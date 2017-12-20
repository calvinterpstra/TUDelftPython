# -*- coding: utf-8 -*-
"""
Signals.py -- Een electronicaonderdeel heeft 2 ingangssignalen:
                  
                  1. een sinusvorming ingangssignaal f(phi)
                  2. de afgeleide daarvan g(phi)=cos(phi+omega), waarin 
                     de faseverdraaing (hoekverdraaing) omega kan worden
                     ingesteld door onszelf
              
              We bestuderen het samengestelde complexe signaal: 
                  
                      h(phi)=g(phi)+j.f(phi)  =
                      
                      h(phi)=cos(phi+omega) + j.f(phi)
              
              We willen weten bij welke door ons gekozen omega er wel
              en wanneer er geen hoekverdraaing (faseverdraaing) optreedt
              in het samengestelde signaal. We bestuderen h op het 
              interval: 
                  
                  [-1.5*np.pi .. 1.5*np.pi] en
                  
              bestuderen het effect van omega = k.pi/2, k=1,2,3
              
              OPDRACHT
              --------
              Zie OPDRACHTENBLAD Oefentoets
              
              TEMPLATE
              --------
              Gebruik deze template voor je programma en introduceer
              zelf GEEN NIEUWE VARIABELEN. Houd je aan de bestaande
              namen voor variabelen, functies e.d. Wijzig die niet.
                 
@author: Bart Gerritsen
"""

import numpy as np
import matplotlib.ticker as tck
import matplotlib.pyplot as plt


def f(phi):
    """
    functie voor sinusvormig ingangsignaal f
    
    input : phi, float, ingangshoek sinusvorming signaal, phi in domein
                 [-1.5 pi,+1.5 pi], phi in rad
    return: sin(phi)
    """
    return np.sin(phi)

def g(phi,omega):
    """ 
    functie voor agfeleide ingangssignaal g
    
    input : phi, float, ingangshoek signaal, phi in rad, phi in domein, 
                 [-1.5 pi,+1.5 pi]
    return: cos(phi+omega)
    """
    return np.cos(phi+omega)


def plotSignals(angle,omega):
    """
    plot samengesteld signaal h, en de ingangssignalen f en g.
    Plot een polair diagram om de faseverdraaing in het resulterende 
    singaal te bestuderen
    """
    # maak drie subplots aan (resp. 131,132, en 133)
    fig = plt.subplots(1,3,figsize=(16,4))
    
    # ... plot functies f(x), g(x) ----------------------------------
    axis = plt.subplot('131')
    axis.set_xlim([-1.5,1.5])
    axis.set_ylim([-1.0,1.0])
    axis.xaxis.set_major_formatter(tck.FormatStrFormatter('%g $\pi$'))
    axis.xaxis.set_major_locator(tck.MultipleLocator(base=1.0))
    axis.set_xticks([-1.5, -1.0, -0.5, 0, 0.5, 1.0, 1.5])
    axis.set_xlabel('$\phi$')
    axis.set_title(\
              '$f(\phi),g(\phi+\omega)$')
    axis.plot(angle/np.pi, f(angle), 'r-',\
               label='$f(\phi)=sin(\phi)$')
    axis.plot(angle/np.pi, g(angle,omega), 'b-', \
               label='$g(\phi)=cos(\phi + \omega)$')
    axis.grid(which='major', axis='both', alpha=.75)
    axis.legend(loc='best')
    
    # ... plot polar diagram omega=0 (referentie) --------------------
    axis = plt.subplot('132', projection='polar')
    axis.plot(np.real(g(angle,0)+1j*f(angle)), 
               np.imag(g(angle,0)+1j*f(angle)), \
               color='cyan',linestyle='-')
    axis.set_xlabel('$h(\phi)$')
    
    # ... plot polar omega =/= 0 --------------------------------------
    axis = plt.subplot('133', projection='polar')
    axis.plot(np.real(g(angle,omega)+1j*f(angle)),
               np.imag(g(angle,omega)+1j*f(angle)),  \
               color='orange',linestyle='-')
    axis.set_xlabel('$h(\phi+{:3.1f}\pi)$'. format(omega/np.pi))
    
    
def main():
    """
    main function voor analyse faseverdraaing
    """
    
    # te onderzoeken fase-verschuiving ...
    OMEGA = (1,2,3)
    
    # fase-domein ...
    angle = np.arange(-1.5*np.pi,1.5*np.pi,step=np.pi/90)
    
    # plot the functions ...
    for m in range(len(OMEGA)):
        plotSignals(angle,OMEGA[m]*np.pi/2)

    # print de waarden voor omega waarbij er WEL faseverdraaing optreedt ...
    # pas de string OMEGAS aan voor de juiste melding.
    OMEGAS='omega: k*pi/2, WEL bij k=1 of 3 en NIET bij k=2'
    print('Faseverdraaing treedt op bij omega={:s}'.format(OMEGAS))
    
if __name__=='__main__': main()