"""
testmatrices.py -- load a test matrix and compute row, col sum and trace
                 
@Author : Bart Gerritsen
"""

import numpy as np

# ========================================================================
#
# OEFENING: 'vectorize' al deze functie, d.w.z., neem de for-loops weg
#           en vervang ze door NumPy matrix bewerkingen
#
# ========================================================================
def matrixRowSum(A,r):
    """
    return the sum of A[r]
    """
    assert A.shape > (0,0), 'cannot determine row sum of empty matrix'
    rsm = 0
    for row in range(A.shape[0]):
        for col in range(A.shape[1]):
            if row==r:
                rsm += A[row,col]
    return rsm

def matrixColSum(A,c):
    """
    return the sum of column vector A^c
    """
    assert A.shape > (0,0), 'cannot determine column sum of empty matrix'
    csm = 0
    for row in range(A.shape[0]):
        for col in range(A.shape[1]):
            if col==c:
                csm += A[row,col]
    return csm

def matrixTrace(A):
    """
    return trace of matrix A
    """
    assert A.shape > (0,0), 'cannot determine column sum of empty matrix'
    assert A.shape[0]==A.shape[1], 'matrix for trace must be square'
    trace = 0
    for row in range(A.shape[0]):
        for col in range(A.shape[1]):
            if col==row:
                trace += A[row,col]
    return trace

# ========================================================================
#
# EINDE: 'vectorize' oefening
#
# ========================================================================

def loadTestMatrixFromFile(flname,delim=',',DOPRINT=False):
    """
    load testmatrix from given CSV file, using MunPy load...().
    Specify the delimeter (default: ',') to separate columns
    return: x,v = position resp. velocity measured in that position
    """
    mat = np.loadtxt(flname, dtype=int, delimiter=delim)
    print('matrix loaded: {:s}'.format(flname))
    if DOPRINT: 
        print(mat)
    return mat

def printSums(A):
    """
    print the testmatrix sums
    """
    N = A.shape[0]
    print('Test matrix: rank {:d};'. format(N))
    for r in range(N):
        print('|',end='')
        for c in range(N):
            print(' {:3d}'. format(A[r,c]), end='')
        print(' | sum={:d}'. format(matrixRowSum(A,r)))
    lines = int(A.shape[0]/3)
    for line in range( lines ): 
        print(' -------------', end='')
    print()
    print('col sum={:d}'. format(matrixColSum(A,0)), end='')
    for line in range( lines ):
        print('         ', end='')
    print(' trace={:d}'. format(matrixTrace(A)))
    print()

def checkUniques(A,s):
    """
    return trace of matrix A
    """
    assert A.shape > (0,0), 'cannot determine column sum of empty matrix'
    FND = np.zeros(A.shape, dtype=bool)
    # brute force ...
    for e in s:
        for r in range(A.shape[0]):
            for c in range(A.shape[1]):
                if e==A[r,c]:
                    FND[r,c] = True
    return np.all(FND)
    
    
def runMain():
    # constants ...
    COMMA = ','
    
    OK    =  0
    NotOK = -1
    
    # read velocity data from file ...
    DATPATH  = './'
    DATFILE3 =  'magic3.csv'
    DATFILE10= 'magic10.csv'
    DOPRINT  = False
    
        
    # -------------- rank 3 ----------------------------------------------
    
    # read the velocity data ...
    mat3 = loadTestMatrixFromFile(DATPATH+'/'+DATFILE3,COMMA,DOPRINT)
      
    # print the velocity plus acceleration statistics ...
    printSums(mat3)
    # check if all number are unique ...    
    set3  = set( range(1,10) )  # covers set={1..9}
    if checkUniques(mat3,set3):
        print('Uniques checked OK', end='\n\n')
    else:
        print('Uniques not verified OK!', end='\n\n')
    
    # -------------- rank 10 ---------------------------------------------
    
    mat10 = loadTestMatrixFromFile(DATPATH+'/'+DATFILE10,COMMA,DOPRINT)
    
    # print the velocity plus acceleration statistics ...
    printSums(mat10)
    # check if all number are unique ...    
    set10  = set( range(1,100+1) )  # covers set={1..9}
    if checkUniques(mat10,set10):
        print('Uniques checked OK')
    else:
        print('Uniques not verified OK!')
    
    
# run the main function ...
runMain()