# -*- coding: utf-8 -*-
"""
Bearings.py   -- lees lager gegevens in uit een file, bepaal minimum, 
                 maximum en gemiddelde, en plot een histogram
                 
                 De data is als volgt georganiseerd, zowel in de 
                 file en in array 'data':
                 
                     nr      Cr-waarde
                  ---------------------------------------------
               0  |  1  |   0.00099
                  ---------------------------------------------
               1  |  2  |   0.00191
                  ---------------------------------------------
               j  | ... |     ...
                  ---------------------------------------------
              N-1 |  N  |   0.00328
                  _____________________________________________
                
                
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

# alle onderdelen die we gebruiken ...
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt


def loadBearingDataFromFile(flname,delim=','):
    """
    lees de data van de lagers (2 kolommen) in vanuit de file 'flname'
    
    input : flname, string, naam van de file met lager-gegevens die moeten
                            worden ingelezen
            delim , string, teken (string) waarmee in de file de kolommen
                            van elkaar gescheiden zijn
    return: N, data
    """
    nr, cr = np.loadtxt(flname, \
                      delimiter=delim, comments='#', \
                      usecols=(0,1), unpack=True)
    N = len(nr)
    print('{:d} data records gelezen van file: {:s}'.format(N,flname))
    # organiseer deze data in data array 'data', op een zelfde wijze; zie
    # ook de header van deze file ...
    data = np.empty(N*2, dtype=float).reshape(N,2)
    data[...,0] = nr
    data[...,1] = cr
    # geef het aantal lagers en het data array 'data' terug ...
    return N, data

def printAnalysis(data,domain):
    """
    Analyseer de lager data en druk de statistics af: min, max, avg. Druk
    ook het aantal lagers af. Geef aan welk lager(s) de laagste en hoogste
    Cr hebben (druk hun Nr af). 
    
    input : data, 2darray(float), tabel met [Nr, Cr]-rijen waarin de 
                                  lager-gegevens van een enkel lager staan
          : domain, 2-tuple(float),open interval waarin de Cr-waardes liggen
          
    return: min, max, avg
    """
    # index data record layout ...
    NR,CR = (0,1)
    # constanten voor initiele waarden CRMIN en CRMAX ...
    CRMIN,CRMAX  = (domain[1],domain[0])
    
    # hoeveel data item in data array ?
    N = len(data)
    
    # wijs initiele waarden toe bij begin loop ...
    crmin,crmax,crsum =(CRMIN,CRMAX,0.0)
    # welke Nr horen bij deze waarden?
    nrmin, nrmax = (None,None)
    
    for d in range(N):
        if data[d][CR] < crmin:
            crmin = data[d][CR] # leg het nieuwe min vast 
            nrmin = data[d][NR] # onthoud welke dat is
        if data[d][CR] > crmax:
            crmax = data[d][CR] # idem, maar nu maximum
            nrmax = data[d][NR]
        crsum += data[d][CR]    # tel alle Cr's op voor cravg later
    cravg = crsum/N             # deel door aantal lager voor average
    
    # druk lager resultaten af ...
    hdr='... ... ... ... ... ... ... ... ... ... ...'   
    print(hdr)
    print('... ... .. Count  : {:d} data values'.    format(N))
    print('... ... .. Cr min : {:15.10e} [nr {:d}]'. format(crmin,int(nrmin)))
    print('... ... .. Cr max : {:15.10e} [nr {:d}]'. format(crmax,int(nrmax)))
    print('... ... .  Cr avg : {:15.10e}'.           format(cravg))
    # geef de gevonden statistics terug ...
    return (crmin,crmax,cravg)

def plotStats(data,domain,mma):
    """ 
    plot de data en de statistische analyse resultaten in een histogram
    
    input : data, 2darray(float), tabel met [Nr, Cr]-rijen waarin de 
                                  lager-gegevens van een enkel lager staan
          : domain, 2-tuple(float),open interval waarin de Cr-waardes liggen
          : mma, 3-tuple(float),  (min Cr, max Cr, avg Cr) waarden
    """
    # definities van de lokale constanten ...
    # ... aantal klassen in histo
    NRCLASSES    = 10
    # ... stapgroottes voor klassengrenzen
    LOW,HGH,STEP = (domain[0],domain[1],(domain[1]-domain[0])/NRCLASSES)
    # ... index in mma met min,max,avg waarde Cr
    MIN,MAX,AVG = (0,1,2)
    
    # stel het histogram samen ....
    plt.subplots(1, figsize=(8,4))
    axis = plt.subplot(111)
    axis.set_title('Verdeling $C_r$ (N={:d})'.format(len(data)))
    axis.set_xlabel('$C_r$')
    axis.set_ylabel('Frequency')
    axis.set_xticks(np.arange(LOW, HGH+STEP, STEP ))
    axis.set_yticks([0,5,10,15,20])
    # ... het eigenlijke histogram ...
    axis.hist(data[...,1], 
              bins=np.arange(LOW, HGH+STEP, STEP), rwidth=.72, \
              color='orange',histtype='bar')
    # ... de waarde min uit de analyse ...
    axis.plot([mma[MIN],mma[MIN]],[0, 5], \
              color='red',linestyle='--',linewidth=3.0,\
              label='minimum $C_r$')
    # ... de waarde avg uit de analyse ...
    axis.plot([mma[AVG],mma[AVG]], [0,20], \
              color='brown',linestyle=':',linewidth=3.0,\
              label='gemiddelde $C_r$')
    axis.grid(which='major',axis='both',alpha=.75)
    # ... de legenda op de best geschikte plaats in de plot ...
    plt.legend(loc='best')


# het main gedeelte van de analyse ...
def runMainProgram():
    """
    Het hoofdprogramma voor de statistische analyse
    """
    # constants ..
    COMMA       = ','
    flname      = 'Bearings.dat'
    # de waarden voor Cr liggen in dit OPEN domein
    CRLOW,CRHGH = (0.000, 0.010)    
    DOMAIN      = (CRLOW,CRHGH) # 2-tuple met domein grenzen

    print('Statistische analyse ... ')    
    # ... lees de lager data in ...
    N, data = loadBearingDataFromFile(flname,COMMA)
    # ... analyseer. print en plot de resultaten ...
    mma = printAnalysis(data,DOMAIN)
    plotStats(data,DOMAIN,mma)
    print('Statistische analyse klaar.')


# start de analyse in het MainProgram  ... 
runMainProgram()