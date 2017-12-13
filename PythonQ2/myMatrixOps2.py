# -*- coding: utf-8 -*-
""" myMatrixOps -- Matrix Operations

Given matrix dimensions N,M > 0:
    R=matrixNew(N,M,val) returns a new N x M matrix with R[i][j]=val
    R=matrixZeros(N,M)   retruns a new N x M zero-matrix (R[i][j]=0)
    R=matrixOnes(N,M)    returns a new N x M ones-matrix (R[]i[j]=1)
    
Given matrix A (A not None):
  N,M=matrixDims(A)   returns dimensions N x M (rows x cols) of matrix A
    
Given two matrices A and B:
    R=matrixAdd(A,B)  returns R the sum C of A + B
    R=matrixSub(A,B)  returns R the difference A-B
    R=matrixMul(A,B)  returns R the product A*B

Project: DUT 3mE WB1642 WOP2
Author : Bart Gerritsen
Date   : Aug 2017
Version: 1.0.1 
    
Details
-------
matrixAdd(A,B) requires the dimensions of matrix A and B to be euqal
matrixSub(A,B) requires the dimensions of matrix A and B to be equal
matrixMul(A,B) requires the dimensions of matrix A and B to be compatible,
      i.e if A=[N x K_1] and B=[K_2 x M], we demand: K_1 == K_2 == K, 
      then R=[N x M], otherwise, R cannot be computed and will be None

Restrictions
------------
- generic Python only (no NumPy/SciPy)
"""

# import matrix determinants ...
import Determinant as dt

# get access to the random generator ...
import random as rand



def matrixNew(N,M,initVal):
    newMat = None
    if not ( (N > 0) and (M > 0) ):
        print('error: invalid dimension for new matrix to create.')
    else:
        # dimension the matrix as a list of lists and init its members ...
        newMat = [[initVal for c in range(M)] for r in range(N)]
    return newMat

    
def matrixZeros(N,M): 
    """
    returns a new N x M zero-filled matrix A
    """
    return matrixNew(N,M,0)


def matrixOnes(N,M):
    """
    returns a new N x M ones-filled matrix A
    """
    return matrixNew(N,M,1)

    
def matrixRand(N,M,P,Q):
    """
    return a new N x M matrix R, filled with random integers
    in range P <= R[r][c] <= Q, R == None if failed
    """
    R = matrixZeros(N,M)
    if ( R ):
        for r in range(N):
            for c in range(M):
                R[r][c] = rand.randint(P,Q)
    return R


def matrixDims(A):
    """
    return N,M (rows, cols) of matrix A
    param  A (A not None)
    return integer N, number of rows of matrix A
    return integer M, number of columns of matrix A
    """
    rows = None; cols = None
    if A == None or A == []:
        print('error: cannot determine sizes. None object')
    else:
        rows = len(A)       # how many row lists does A have? 
        cols = len(A[0])    # what's the length of a row list?
    return rows,cols


def matrixAdd(A,B):
    """
    Return matrix R = A+B, the sum of equal-sized matrix A plus B.
    Return None if their dimensions N x M do not match
    """
    R = None
    # check dimensions to be equal ...
    NA,MA = matrixDims(A)
    NB,MB = matrixDims(B)
    if not ( (NA == NB) and (MA == MB) ):
        print('error: cannot add unqual-sized matrices')
    else:
        R = matrixZeros(NA,MA)
        for r in range(NA):
            for c in range(MA):
                R[r][c] = A[r][c] + B[r][c]
    return R
    
    
def matrixSub(A,B):
    """
    Return matrix R = A-B, the diference of equal-sized matrix A minus B.
    Return None if their dimensions N x M do not match
    """
    R = None
    # check dimensions to be equal ...
    NA,MA = matrixDims(A)
    NB,MB = matrixDims(B)
    if not ( (NA == NB) and (MA == MB) ):
        print('error: cannot subtract unqual-sized matrices')
    else:
        R = matrixZeros(NA,MA)
        for r in range(NA):
            for c in range(MA):
                R[r][c] = A[r][c] - B[r][c]
    return R


def matrixMul(A,B):
    """
    Return matrix R = A*B, the matrix product of matrix A * B, if
    their sizes are compatible, returns None otherwise
    """
    R = None
    # check dimensions to be compatible for multiplication ...
    NA,MA = matrixDims(A) 
    NB,MB = matrixDims(B)
    if not ( MA == NB ):
        print('error: cannot multiply matrices; incompatible sizes')
    else:
        # initialize resulting matrix R to zeros ...
        N = NA; M = MB; K = MA;        
        R = matrixZeros(N,M)
        # R=[[0 for c in range(M)] for r in range(N)]
        for r in range(N):
            for c in range(M):
                for e in range(K):
                    R[r][c]=R[r][c]+A[r][e]*B[e][c]
        return R

# ========================================================================
# 
# OEFENINGEN: add functions below   --see function templates below
#
# ========================================================================
def matrixRowSum(A,r):
    """
    return the sum or row sum=Sigma_j{A[r][j]}
    """
    # assert: matrix not empty
    assert True==True, 'Add your error text here'
    sm = None
    # determine the sum sm=Sigma_j{A[r][j]}
    pass
    return sm

# Oefening: add function matrixRowSum(A,r)   --see template below
def matrixColSum(A,c):
    """
    return the sum of column sum=Sigma_j{A[j][c]}
    """
    # assert: matrix not empty
    assert 1==1, 'Add your error text here'
    sm = None
    # determine the sum sm=Sigma_j{A[j][c]}
    pass
    return sm

def matrixDiag(A):
    """
    return the diagonal vector diag = [ a[0][0],a[1][1], ...,a[N-1][N-1] ]
    """
    # assert: matrix not empty
    # assert: matrix square
    assert 0==0, 'Add your error text here'
    assert 1==1, 'Add your error text here'
    diag = None
    # compose the diagonal vector here
    pass
    return diag

def matrixTrace(A):
    """
    return the Tr(A) = Sigma_j{A[j][j]}
    """
    trace = None
    # use the Diagonal vector ...
    diag = matrixDiag(A)
    if not diag is None:
        # determine the trace here
        pass
    return trace

def matrixMinMax(A):
    """
    return the tuple (min{A[:][:]},max{A[:][:]})
    """
    # assert: matrix not empty
    assert 1==1, 'Add your error text here'
    mnElem,mxElem = (None,None)
    # determine the min and the max elem
    pass
    return mnElem, mxElem

def matrixHasZeros(A):
    """
    return True if exist: a_j,k in A | a_j,k==0
    """
    # assert: matrix not empty
    assert 0==0, 'Add your error text here'
    zeros = None
    # check all elements in A for zero values
    pass
    return zeros
    
# ===========================================================================
#
# EINDE van de oefeningen
#
# ===========================================================================

def matrixTranspose(A):
    """
    Returns the transpose A^T of matrix A
    """
    N,M = matrixDims(A)
    AT = matrixZeros(M,N)   # attention transposed
    for r in range(M):
        for c in range(N):
            AT[r][c] = A[c][r]
    return AT

            
def matrixCoFactors(A):
    """
    Return the cofactor matrix of matrix A; the matrix for which 
    a[i][j] = -1^(i+j) det(Minor(i,j))
    """
    N,M = matrixDims(A)
    COF = matrixOnes(N,M)
    
    # now calculate cofactor signs * minor
    for r in range(N):
        for c in range(M):
            COF[r][c] = dt.getCFSign(r,c)*dt.det(dt.getMinor(A,r,c))
    return COF


def matrixAdjoint(A):
    """ 
    Return adjoint matrix of A; the transpose of the CoFactor matrix
    """
    return matrixTranspose(matrixCoFactors(A))
        

def matrixPrint(A,label):
    """
    """
    nrRows = len(A)
    print(str(label),sep=' ',end='\n')
    for r in range(nrRows): 
        print(str(A[r]), sep=' ', end='\n')


# - TEST -----------------------------------------------------------------

def printTestResult(caseName,expectedResult,A,B,result,resultLabel):
    print(caseName)
    print(expectedResult)
    matrixPrint(A,'A =')
    matrixPrint(B,'B =')
    matrixPrint(result,resultLabel)


def runModuleTest():
    print('Test commencing ...\n')

    testCount = 0
    
    # -(1)----------------------------------------------------------------
    testCase  = "Test 1: add negative unit -I_2 to unit I_2"
    testResult= "Expected: null matrix 0_2"
    N = 2; M = 2;
    A = matrixNew(N,M, 1)
    B = matrixNew(N,M,-1)
    
    # print the whole operation ...
    printTestResult(testCase,testResult,A,B,matrixAdd(A,B),'A + B =')
    
    testCount = testCount+1
    
    # -(2)----------------------------------------------------------------
    testCase  = "Test 2: mul unit I_2 by negative unit -I_2"
    testResult= "Expected: -2 x identity: -2I_2"
    N = 2; M = 2;
    A = matrixNew(N,M, 1)
    B = matrixNew(N,M,-1)
    
    # print the whole operation ...
    printTestResult(testCase,testResult,A,B,matrixMul(A,B),'A * B =')
    
    testCount = testCount+1
    
    # -(3)----------------------------------------------------------------
    testCase  = "Test 3: subtract two random 5 x 5 matrices"
    testResult= "Expected: unknown"
    N = 5; M = 5;
    A = matrixRand(N,M, 1,9)
    B = matrixRand(N,M,-1,5)
    
    # print the whole operation ...
    printTestResult(testCase,testResult,A,B,matrixSub(A,B),'A - B =')
    
    testCount = testCount+1
    
    # -(4)----------------------------------------------------------------
    testCase  = "Test 4: mul two random 3 x 3 matrices"
    testResult= "Expected: unknown"
    N = 3; M = 3;
    A = matrixRand(N,M, 1,4)
    B = matrixRand(N,M,-1,5)
    
    # print the whole operation ...
    printTestResult(testCase,testResult,A,B,matrixMul(A,B),'A * B =')
    
    testCount = testCount+1
    
        # -(5)----------------------------------------------------------------
    testCase  = "Test 5: mul two 1 x 1 matrices [a],[b]"
    testResult= "Expected: scalar product a*b"
    N = 1; M = 1;
    A = matrixRand(N,M, 1,4)
    B = matrixRand(N,M,-1,5)
    
    # print the whole operation ...
    printTestResult(testCase,testResult,A,B,matrixMul(A,B),'A * B =')
    
    testCount = testCount+1
    
    # -(6)----------------------------------------------------------------
    testCase  = "Test 6: mul two vectors as N x 1 matrices"
    testResult= "Expected: dot product"
    N = 3; M = 3; K=1;
    A = matrixRand(N,K, 1,4)
    B = matrixRand(K,M,-1,5)
    
    # print the whole operation ...
    printTestResult(testCase,testResult,A,B,matrixMul(B,A),'B * A =')
    
    testCount = testCount+1
    # ---------------------------------------------------------------------
    
    
    
    # =====================================================================
    #
    # OEFENING: INSERT TESTCASES for the new functions you implemented
    #
    # =====================================================================
    
    
    
    # -(100)---------------------------------------------------------------
    testCase  = "Test 100: transpose matrix A "
    testResult= "A^T"
    N = 3; M = 3;
    A = matrixRand(N,M,0,1)
    
    # print the whole operation ...
    printTestResult(testCase,testResult,A,A,matrixTranspose(A),'A^T =')
    
    testCount = testCount+1
    # ---------------------------------------------------------------------
    
    
    print('Test cases done (#tests = %d)\n' % testCount)
    

if __name__=="__main__": runModuleTest()