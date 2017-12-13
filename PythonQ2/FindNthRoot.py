# -*- coding: utf-8 -*-
"""
FindNthRoot.py -- How to use a while loop

@author: Bart Gerritsen
"""
# for sqrt function
import math

def main():
    # constants ...
    EPS = 1.0E-06
    # start with arbitrary big number ...
    X0 = 9.927558445732E+12
    Y0 = 1/X0
    
    # construct a while loop ...
    iterCount = 0; X=X0
    while abs( X - 1.0) > EPS:
        X = math.sqrt(X)
        iterCount += 1
    print('The {:2d}th root of {:.12e} = 1.0 +/-{:e}'. \
          format(iterCount,X0,EPS))
 

    # redo with small number, close to zero ...
    iterCount = 0; X=Y0
    while abs( X - 1.0) > EPS:
        X = math.sqrt(X)
        iterCount += 1
    print('The {:2d}th root of {:.12e} = 1.0 +/-{:e}'. \
          format(iterCount,Y0,EPS))  
     
# launch main()
main()