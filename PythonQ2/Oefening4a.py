# -*- coding: utf-8 -*-
"""
Oefening4.py -- print variables of different kinds

@author: Bart Gerritsen
"""

def printList(v,hdr='',lbl=''):
    if len(hdr) > 0:
        print(hdr)
    print('{0:s} {1:s}'. format(lbl,str(v)))
    
def printNumber(v,hdr='',lbl=''):
    if len(hdr) > 0:
        print(hdr)
    print('{0:s} {1:+12.9e}'. format(lbl,v))
    
def printNothing(v,hdr='',lbl=''):
    pass

def printDiag(A,hdr='',lbl=''):
    assert len(A)==len(A[0]),'for diag(A), A must be square'
    if len(hdr) > 0:
        print(hdr)
    for k in range(len(A)):
        print('', A[k][k], sep=' ', end='\n')

def printMatrix(A,hdr='',lbl=''):
    N = len(A)
    if len(hdr) > 0:
        print(hdr)
    for r in range(N):
        print(' {:s}'.format(str(A[r])))

def myMain():
    A =[ ['a00', 'a01', 'a02'],
         ['a10', 'a11', 'a12'],
         ['a20', 'a21', 'a22'],
         ['a30', 'a31', 'a32']
         ]    
    B = [ A[0], A[1], A[2] ]
    V = [0,1,2]
    C = [complex(1,2), complex(0,-1), complex(-1,3)]
    D = float('1.0e-6')
        
    for var in (A, B, V, C, D):
        if   type(var) is list: 
            printList(var,'','list')
        elif type(var) is float: 
            printNumber(var,'','number')
        else: 
            printNothing(var)
            
    for var in (A, B):
        printMatrix(var,'matrix;','mat ')

    printDiag(B,'diagonal matrix B;')
    
myMain()