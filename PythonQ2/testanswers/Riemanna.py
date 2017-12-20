# -*- coding: utf-8 -*-
"""
RiemannSum.py  - bepaal de midpoint Riemann Sum van een gegeven functie en
                 vergelijk de verkregen waarde met de waarde die je vindt
                 met de trapezium regel, gebruik makend van Numpy.trapz() 

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
import matplotlib.pyplot as plt


def F(x):
    """
    bereken de functiewaarde van x
    """
    return 0.85*x+0.6*(1-np.exp(1/4*x))
    
def getFuncTable(domain, doPrint=False):
    """
    Bepaal de N waarden x, f(x) gegeven een domein
    
    input : domain, 3-tuple, (x0,xN,N), voorstellend domein [x0,xN] waaruit
                    N lineair verdeelde punten moeten worden bepaald
            doPrint, bool, flag waarmee waarden al dan niet afgedrukt worden
    return: x,f, numpy.ndarray, float,float, van punten xi uit het domein en 
                 hun functiewaarden F(xi)
    """
    (x0,xN,N) = domain
    x = np.linspace(x0,xN,num=N,endpoint=True)
    f = F(x)
    if doPrint:
        printFuncTable(x,f)
    return x,f

def mid(fa,fb):
    """
    functie waarmee midpoint-waarde=ggemiddelde van fa en fb bepaald worden
    
    input : a,b, float, functiewaarden in x=xa en x=xb=xa+h, resp.
    return: g, float, gemiddelde waarde van fa en fb
    """
    g =(fa+fb)/2
    return g
    
def calcRSum(x,f,func):
    """
    bepaal Riemann Sum, door toepassing van functie 'func' op x en f(x):
    RSum = Sum func(x_j), j=x0..xN
    
    input : x,f, ndarray, float, punten x en waarden F(x) van N lineair
                 verdeelde punten in domein [x0,xN]
            func,function, de functie waarde de Riemann sum moet worden 
                 berekend.
    return: sm, float, Riemann Sum op basis van 'func'
    """
    sm = 0.0
    for r in range(1,len(x),1):
        fm = f[r]
        fm = func(f[r],f[r-1])  # hiet worden func min(),max(),mid() aange-
        sm += (x[r]-x[r-1])*fm  # roepen, bv:  fm = func(f[r],f[r-1])
    return sm

def printFuncTable(x,f):
    """
    druk de lineair verdeelde punten x en functiewaarden F(x) af in tabel-
    vorm
    
    input : x,f, ndarray, float, de af te drukken N punten uit het domein
                 [x0,xN] en hun functiewaarden F(x)
    """
    print('Mijn datapunten;')
    print('    x           f(x)')
    print('----------------------------')
    for p in range(len(x)):
        print(' {:6.3f}     {:+8.3f}'. format(x[p],f[p]))
        
def plotFunc(axis,x,f,colString='k-'):
    """
    plot de functie waarvoor de Riemann Sum moet worden bepaald. De functie
    u representeert deze functie. Functie u benadert de 'exacte' functie
    door heel veel punten in het domein te gebruiken. De N waardes van F(x)
    die zijn gekozen op het domein, vormen per interval een trapezium, dat
    ten grondslag ligt aan de trapezium regel. Elk trapezium wordt ook 
    geplot.
    
    input : axis, AxisSubplot, de subplot axis te gebruiken voor het plotten
            x,f, ndarray, float, waarvoor de functie u op het domein moet 
                 worden geplot
            colString,string, specificatie van lijnkleur en -type dat
                 MatplotLib moet gebruiken bij het plotten
    """
    axis.grid(which='major', axis='both')
    axis.plot(x,f,colString,label='trapezium')
    # print een nauwkeurige versie met veel meer punten als ref
    u = np.linspace(0,10,2001)
    axis.plot(u,F(u),'r--', label='u=f(x)')
    
def plotRSum(axis,x,f,colString='k-'):
    """
    plot de Riemann sum bijdragen per interval [xa,xa+h], bepaald door
    de functiewaarde F(x) berekend met mid(F(xa),F(xb=xa+h))
    
    input : axis, AxisSubplot, de subplot axis om op te plotten
            x,f, ndarray, float, waarvoor de Riemann sum intervallen 
                 op basis van de midpoint berekening voor de 
                 hoogte moeten worden geplot
            colString,string, specificatie van lijnkleur en -type dat
                 MatplotLib moet gebruiken bij het plotten
    """
    for r in range(1,len(x),1):
        f0 = (f[r]+f[r-1])/2
        axis.plot([x[r-1],x[r],x[r],x[r-1],x[r-1]], \
                  [   0  ,  0,  f0,   f0,     0  ],colString)
        
def main():
    """ hoofdfunctie voor het bepalen en plotten van de Riemann Sum
    """
    N = 21  # neem N=4, N=6, N=11, N=21, N=51,N=101,N=201,N=501,N=1001
    fPARMS = (0,10,N)
    # N erg hoog? Zet dan DOPRINT=False
    DOPRINT= False

    # get function data ...  
    x,F = getFuncTable(fPARMS,DOPRINT)
    
    # vier verschilldende Riemann sums, die
    # we met elkaar willen vergelijken ...
    
    # 1. met de trapezium regel == identiek aan  mid point 
    npRSum = np.trapz(F,x)
    # 2. onze mid point methode (functie mid(a,b))
    RSum   = calcRSum(x,F,mid)
    
    # 3 en 4: onze methode, met resp funcies max en min ...
    mxRSum = calcRSum(x,F,max)
    mnRSum = calcRSum(x,F,min)
    
    # druk ze af ...
    print('Riemann sum: {:12.9e} (NumPy: {:12.9e})'. format(RSum,npRSum))
    
    # laat zien dat voor elke N: RSum_max >= R >= 
    print('Max Riemann : {:s}'. format(str( mxRSum )))
    print('Mid Riemann : {:s}'. format(str(   RSum )))
    print('Min Riemann : {:s}'. format(str( mnRSum )))
    
    # verschil als percentage van RSum_min ...
    print('Max verschil: {:s} %'. format(str( 100*(mxRSum-mnRSum)/mnRSum )) )

    # create the figure ...    
    plt.subplots(1,1, figsize=(12,4))
    # ... plot the data table ...
    plotFunc(plt.subplot(111),x,F,'g-')
    # ... plot the midpoint Riemann sum ...
    plotRSum(plt.subplot(111),x,F,'b-')
    # decoreer de plot ...
    plt.title('Midpoint Riemann Sum benadering (N={:d})'.format(N))
    plt.legend(loc='best')

main()
