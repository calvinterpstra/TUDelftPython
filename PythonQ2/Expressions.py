# -*- coding: utf-8 -*-
"""
Expressions.py  -- evaluate and print expression results. Expressions 
                   can be modified for experimenting, new expressions 
                   can be inserted anywhere seen convenient.

@author:  Bart Gerritsen
"""

# math and cmath may be needed for experiments 
# Spyder will complain: you re not really using math and cmath
# that is because here, their use is expressed IN A STRING FORMAT,
# which is being evaluated inside the eval() function, out of sight 
# for the static code analysis (don't worry about it)
import math
import cmath
import numpy as np

def myFunc(p,q,flag=False):
    # assert not (p==0 or q==0), 'myFunc: provide non zero values'
    if not (p==0 or q==0):
        return p,q

# global constant and variables ...
EPS        = float('1.0e-06')

a,b,c      = (-1.0, 0.0, 1.0)
i,j,k      = (-1,0,1)
b1,b2,b3   = (True, False, False)
intTriplet = (i,j,k)
fltTriplet = (a,b,c)
blnTriplet = (b1,b2,b3)
nilTriplet = ()

u = [-1, 1, 1, 0, 0 , 1]
v = [-0.2, -7.4, 8.2, 8,1, 4.0, 0.0]
w = [ 2+1j, 4-1j, 0-j, 2+2j]

A = np.ones(25, dtype=np.float64).reshape(5,5)
B = np.eye ( 5, dtype=np.float64).reshape(5,5)
# inject a single zeroe in the center ...
A[2][2] = 0
# print(A)

z = None

T = [False, True, True, False, not True]
ATT = '!'
QST = '?'
NON = ' '
WNG = 'X'

# list (NOTE: Nr will be set automagically)
expression = [ \
# NR   EXPR                                                           REMARK
 [ 0, 'not a',                                                          ATT],
 [ 0, 'bool(a)',                                                        ATT],
 [ 0, 'b==0.0',                                                         QST],
 [ 0, 'fltTriplet is tuple',                                            NON],
 [ 0, 'fltTriplet is None',                                             NON],
 [ 0, 'type(fltTriplet) is tuple',                                      NON],
 [ 0, 'type(fltTriplet) == tuple',                                      NON],
 [ 0, 'type(fltTriplet) == "tuple"',                                    NON],
 [ 0, 'any(intTriplet) <  0',                                           ATT],
 [ 0, 'any(intTriplet) == 0',                                           ATT],
 [ 0, 'any(intTriplet) >  0',                                           ATT],
 [ 0, 'any(fltTriplet) <  0.0',                                         ATT],
 [ 0, 'any(fltTriplet) == 0.0',                                         ATT],
 [ 0, 'any(fltTriplet)  > 0.0',                                         ATT],
 [ 0, 'all(fltTriplet) >  0.0',                                         NON],
 [ 0, 'any(blnTriplet) == True',                                        ATT],
 [ 0, 'any(blnTriplet)',                                                ATT],
 [ 0, 'not any(blnTriplet)',                                            NON],
 [ 0, 'not all(blnTriplet)',                                            ATT],
 [ 0, 'all(blnTriplet)',                                                NON],
 [ 0, 'nilTriplet',                                                     ATT],
 [ 0, 'not nilTriplet',                                                 NON],
 [ 0, 'any(nilTriplet)',                                                ATT],
 [ 0, '0 in intTriplet',                                                NON],
 [ 0, 'k in intTriplet',                                                ATT],
 [ 0, 'any(intTriplet) < 0 and any(intTriplet) > 0',                    NON],
 [ 0, 'any(intTriplet) < k',                                            ATT],
 [ 0, 'max(v) > max(u) and min(v) < min(u)',                            NON],
 [ 0, 'z is None',                                                      NON],
 [ 9, 'bool(z)',                                                        NON],
 [ 0, 'not z or not j or not all(T)',                                   ATT],
 [ 0, 'not( z and j and all(T) )',                                      ATT],
 [ 0, 'not z and not j and not any(T)',                                 NON],
 [ 0, 'not any(T)',                                                     ATT],
 [ 0, 'not any(T) == True',                                             ATT],
 [ 0, 'not any(T) == False',                                            ATT],
 [ 0, 'not all(T)',                                                     NON],
 [ 0, 'all(T) and any(T)',                                              WNG],
 [ 0, 'all(T) or  any(T)',                                              WNG],
 [ 0, 'not (any(T) == True)',                                           ATT],
 [ 0, '~(any(T) == False)',                                             ATT],
 [ 0, 'A.dtype == "float64" and A.ndim == 2 and A.shape == (5,5)',      NON],
 [ 0, 'np.all(A) == 1',                                                 ATT],
 [ 0, 'np.all(A == 1)',                                                 ATT],
 [ 0, '(A == 1).all()',                                                 NON],
 [ 0, 'np.any(A) == 1',                                                 ATT],
 [ 0, 'np.any(A == 1)',                                                 ATT],
 [ 0, '(A == 1).any()',                                                 NON],
 [ 0, 'np.any(A) < 1.0 or np.any(A) > 1.0',                             QST],
 [ 0, 'np.any(A < 1.0) or np.any(A < 1.0)',                             NON],
 [ 0, '(A < 1.0).any() or (A > 1.0).any()',                             NON],
 [ 0, 'np.any(A[0,:]) > 0 and np.array(A[:,3]) > 0',                    NON],
 [ 0, 'np.any(A[2,:] < 1)',                                             NON],
 [ 0, 'np.any(A[:,2] < 1)',                                             NON],
 [ 0, 'np.any(A[2,...] < 1) and np.any(A[...,2] < 1)',                  ATT],
 [ 0, '(A==B).any()',                                                   ATT],
 [ 0, '(A==B).all()',                                                   ATT],
 [ 0, 'np.array_equal(A,A)',                                            ATT],
 [ 0, 'np.array_equiv(A,A)',                                            ATT],
 [ 0, 'np.allclose(A,A)',                                               ATT],
 [ 0, 'np.array_equal(A,B)',                                            ATT],
 [ 0, 'np.array_equiv(A,B)',                                            ATT],
 [ 0, 'np.equal(A.dtype,np.float) and np.equal(B.dtype,np.float)',      NON],
 [ 0, 'np.allclose(A,B)',                                               ATT],
 [ 0, 'np.allclose([b],[0])',                                           ATT],
 [ 0, '(True and not False) and (False and not True)',                  ATT],
 [ 0, 'i <= i & k >= k',                                                ATT],
 [ 0, 'j <= j & k >= k',                                                ATT],
 [ 0, 'a <= a and b >= b',                                              NON],
 [ 0, 'sum(v) > sum(u)',                                                NON],
 [ 0, 'math.isnan(any(fltTriplet))',                                    NON],
 [ 0, 'abs(max((max(u),max(v)))-max((max(v),max(u)))) < EPS',           NON],
 [ 0, 'np.isinf( sum(v) + sum(u) )',                                    NON],
 [ 0, '(w[0].real > w[1].real) and (w[0].imag > w[1].imag)',            ATT],
 [ 0, 'abs(w[2]) - abs(u[2]) < 0',                                      NON],
 [ 0, 'cmath.phase(w[1]) - cmath.phase(w[2]) > 0',                      NON],
 [ 0, 'abs(w[1]) - abs(w[1].conjugate()) < EPS',                        ATT],
 [ 0, '"keyword" in "I do not understand this keyword"',                NON],
 [ 0, '"KeyWord" in "I do not understand this keyword"',                NON],
 [ 0, 'len(\'this_is_a_super_slim_string\') in range(1,25)',            NON],
 [ 0, 'str(2+2+3*2)==str(10)==str(1)+str(0)==str("1"+"0")==str("10")',  ATT],
 [ 0, 'myFunc(i,k) == (i,k)',                                           NON],
 [ 0, 'myFunc(i,j) is None',                                            ATT],
 [ 0, 'myFunc(10,10) is (10,10)',                                       NON],
 [ 0, 'myFunc(5,5) == (5,5)',                                           ATT],
 [ 0, 'myFunc(j,k) == (0,0)',                                           ATT],
 [ 0, 'myFunc(float("nan"),1) is None',                                 ATT],
 [ 0, 'np.pi - math.pi < EPS',                                          NON],
 [ 0, 'np.pi-math.pi+cmath.pi-math.pi == 0.000000000000000000000',      ATT],
 [ 0, 'math.isnan(myFunc(float("nan"),float("nan"))[0])',               ATT],
 [ 0, 'float("nan") in myFunc(float("nan"),float("nan"))',              ATT],
 [ 0, 'myFunc(float("nan"),float("nan"))==(float("nan"),float("nan"))', ATT],
 [ 0, 'np.isnan(myFunc(np.float("nan"),np.float("nan"))).any()',        ATT],
 [ 0, 'np.isnan(myFunc(np.float("nan"),np.float("nan"))).all()',        ATT]
]


def printEvalListHeader(hdr):
    print('{:s}'.format(str(hdr)))
    printListHRuler()
    print( \
    'NR Expression (! = attention, ? = doubtful, X = DON\'t do)         Result        !')
    printListHRuler()

def printListHRuler():
    print( \
    '---------------------------------------------------------------------------------')

def printEvalResult(expr):
    print('{:2d} {:<62s} {:12s} {:^3s}'. \
          format(expr[0],expr[1],str(eval(expr[1])),expr[2])) 

def runMain():
    # fill out the expression list ....
    
    # start printing the list ...
    header = 'Expression evaluations;'
    
    printEvalListHeader( header )
    
    # now evaluate and print them ...
    exprNr = 0
    for expr in expression:
        exprNr += 1
        expr[0] = exprNr
        printEvalResult( expr )

if __name__=="__main__": 
    runMain()
else:
    print('either import this py script or execute it directly')
       
