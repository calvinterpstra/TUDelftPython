# -*- coding: utf-8 -*-
"""
Determinant.py -- compute determinant of a d x d matrix, by recursively
                  developing determinants by its last column until the
                  determinant reaches a 2x2 size, with terminates the 
                  recursion

@author: Bart Gerritsen
"""

import numpy as np

def getMinor(A,r,c):
    """
    return the minor from matrix X associated with A[r][c]
    """
    Am = np.delete(A, (r), axis=0)
    Am = np.delete(Am,(c), axis=1)
    return Am

def getCFSign(r,c):
    return (-1) ** (r+c)

def det(A):
    """ 
    return det matrix A, whatever size 
    """
    N,M = A.shape
    assert N == M, 'non-square matrix found. abandoning'
    # square by here ...
    if N==1: 
        detA = A[0][0]
    elif N==2:
        detA = A[0][0]*A[1][1] - A[1][0]*A[0][1]
    else:
        # develop along the last column 
        detA = 0.0; c = M-1
        for r in range(N):
            detA += A[r][c]*getCFSign(r,c)*det(getMinor(A,r,c))
    return detA

def cdet2(A):
    """
    return a determinant of complex matrix A
    """
    N,M = A.shape
    assert N==M, 'non-square matrix for cdeterminant'
    # split in real and imaginary part     
    A1 = np.real(A) # real matrix
    A2 = np.imag(A) # real matrix
    # compose Z = [ [A1 , -A2], [A2 , A1] ]
    Z = np.zeros((2*N,2*M), dtype=float)
    Z[:N,:M] = A1 ; Z[:N,M:] =-A2
    Z[N:,:M] = A2 ; Z[N:,M:] = A1
    # det(Z) = |det(A)|^2 
    return det(Z)
   
def runTests():
    
    print('\n... DETERMINANTS MAY TAKE SEVERAL MINUTES TO COMPUTE ...\n')
        
    print('\nTest case 1;')
    D = np.ones(1, dtype=np.float64).reshape(1,1)
    for i in range(D.shape[0]):
        for j in range (D.shape[1]):
            D[i][j] = np.random.random(1) * 10
    print(D)
    
    # compute determinant and compare to NumPy's result ...
    print('Computed  determinant  D: {:+12.5f}'.format(det(D)))
    print('Numpy says determinant D: {:+12.5f}'.format(np.linalg.det(D)))
    
    print('\nTest case 2;')
    D = np.zeros(4, dtype=np.float64).reshape(2,2)
    print(D)
    
    # compute determinant and compare to NumPy's result ...
    print('Computed  determinant  D: {:+12.5f}'.format(det(D)))
    print('Numpy says determinant D: {:+12.5f}'.format(np.linalg.det(D)))
    
    print('\nTest case 3;')
    D = np.eye(3, dtype=np.float64).reshape(3,3)
    for i in range(D.shape[0]):
        for j in range (D.shape[1]):
            D[i][j] *= -1.0
    print(D)
    
    # compute determinant and compare to NumPy's result ...
    print('Computed  determinant  D: {:+12.5f}'.format(det(D)))
    print('Numpy says determinant D: {:+12.5f}'.format(np.linalg.det(D)))

    for dim in range(3,6,1):
        print('\nTest case 4-{0:s}: (dim={0:s});'.format(str(dim)))
        D = np.zeros(dim*dim, dtype=np.float64).reshape(dim,dim)
        for i in range(D.shape[0]):
            for j in range (D.shape[1]):
                D[i][j] = -10.0 + np.random.random(1)*10.0
        print(D)
        # compute determinant and compare to NumPy's result ...
        print('Computed  determinant  D: {:+12.9e}'.format(det(D)))
        print('Numpy says determinant D: {:+12.9e}'.format(np.linalg.det(D)))
    
    print('\nTest case 4;')
    D = np.ones(10*10, dtype=np.float64).reshape(10,10)
    for i in range(D.shape[0]):
        for j in range (D.shape[1]):
            D[i][j] = np.random.random(1) * 10
    print(D)
    
    # compute determinant and compare to NumPy's result ...
    print('Computed  determinant  D: {:+12.5f}'.format(det(D)))
    print('Numpy says determinant D: {:+12.5f}'.format(np.linalg.det(D)))
    
    print('\nTest case 5;')
    A1 = np.array([[2, 0], [0, 1]])
    A2 = np.array([[0,-1], [1, 0]])
    A  = np.asmatrix(A1) + 1j*np.asmatrix(A2)
    print(A)
    # compute determinant and compare to NumPy's result ...
    print('Computed determinant D^2: {:+12.5f}'.format(cdet2(A)))
    print('Numpy says determinant D: {:+12.5f}'.format(np.linalg.det(A)))

if __name__=="__main__": runTests()
