# -*- coding: utf-8 -*-
"""
ComplexRandom.py  -- five simple ways of generating arrays 
                     (matrices) of complex random numbers, 
                     using the standard tools. 
                     
                     Note: there are many more ways of
                     accomplishing the same, like using
                     advanced generators and yield, but these 
                     are considered out of scope here.
                     
                     One may experiment with any NumPy matrix 
                     operation also available for real matrices, 
                     on complex matrices. Like (np.) det(Zi), 
                     eigvals(Zi), sum(Zi), trace(Zi)

@author: Bart Gerritsen
"""

# imported here to support complex math
# and general NumPy operations ...
import cmath as cm
import numpy as np


def isNumPyArrayComplex(z):
    """ 
    return z is a complex matrix; true or false
    """
    isComplex = False
    if isinstance(z, (np.ndarray, np.generic) ):
        if np.equal(z.dtype,np.complex): 
            isComplex = True
    return isComplex

def printZPropsHdr():
    print('Complex array initializations;')
    print('------------------------------------------------------------------------------')
    print('| # |Array | Complex | Shape | Elements | Elem. type | Remarks')
    print('------------------------------------------------------------------------------')
    
def printZProps(Z,nr,remark):
    N,M = Z.shape
    name = 'Z{:1s}'.format(str(nr))
    tp   = Z.dtype
    if nr <= 1: printZPropsHdr()
    part1 = '| {:d} |  {:^2s}  |  {:5s}  | ({:d},{:d}) |    {:d}*{:d}   |'. \
        format(nr,name,str(isNumPyArrayComplex(Z)), N,M,N,M)
    part2 = ' {:^10s} | {:<24s}'.format(str(tp), remark)
    print(part1,part2, sep = '')
    
def doMain():
    # Below are five simple strategies to create a 5 x 5
    # matrix of complex numbers. Change sizes as seen fit.
    # Notice that in memory, Python treats complexes simply
    # as an ordered pair of floats.
    

    # generate a couple of simple arrays; ALL real, none
    # of them COMPLEX!
    
    x = np.random.random(5*5).reshape(5,5)
    y = np.random.random(5*5).reshape(5,5)   
    z = np.random.random(5*5*2).reshape(5,5*2)
    
    if not x.shape == y.shape:
        print('error: x and y must be equally-shaped matrices')
        print('aborting')
        exit(-1)
    
    # valid x and y by here ...
    
    # reduce the decmals printed on matrices ...
    np.set_printoptions(precision=2)
    
    
    
    # below are the five strategies ...
    
    
    print('Strategy 1...', end='')
    # create an empty matrix of complex numbers first
    # then assign each element a random complex number
    Z1 = np.empty(5*5, dtype=np.complex).reshape(5,5)
    N,M = Z1.shape
    for n in range(N):
        for m in range(M):
            Z1[n][m] = np.random.random(1) + 1j*np.random.random(1)
    print('complex matrix Z1 looks like this...;')
    print(Z1)
    
    
    print('Strategy 2...', end='')
    # compose complex matrix as a linear combination of a
    # real scalar * real vector + complex scalar * real vector
    Z2 = 1*x + 1j*y
    # EXPERIMENT: introduce SCALE_X and SCALE_Y and do
    #             Z2 = SCALE_X*x + SCALE_Yj* y
    # EXPERIMENT: try the same experiment with COMPLEX
    #             SCALE_X and COMPLEX SCALE_Y ...
    # EXPERIMENT: what if you make SCALE_X =1.0 and
    #             SCALE_Y = -1j ?
    # EXPERIMENT: what if you make SCALE_X =np.nan and/or
    #             SCALE_Y = np.nan?
    # SCALE_X = 3.0; SCALE_Y = 4.0                    
    # Z2 = SCALE_X*x + SCALE_Y*1j*y
    print('complex matrix Z2 looks like this...;')
    print(Z2)

    
    print('Strategy 3...', end='')
    # create a complex array by 
    # 1. assigning a complex scalar * real vector
    # 2. adding a real scalar * real vector to the complex numvers
    Z3  =  1.0j*y  # make complex first (real part will be 0)
    Z3 += 1.0*x    # add the real part in x ...
    # EXPERIMENT: comment our assigning y and check the property
    #             table in the output... (also remove the += in
    #             Z3 += 1.0*x)
    # # Z3 =  1.0j*y  # make complex first (real part will be 0)
    # Z3 = 1.0*x  # assign the real part in x ...
    # EXPERIMENT: try to reverse the order of operations by 
    #             adding x and y in reversed order
    #             i.e., assign real part first and then try to add
    #             the imaginary part...
    # Z3  = 1.0*x
    # Z3 += 1.0j*y
    print('complex matrix Z3 looks like this...;')
    print(Z3)


    print('Strategy 4...', end='')
    # use NumPy's vectorization. Vectorizing a real and 
    # a complex implies creating a complex (in a sense, a 
    # complex is a generalization of a real number; every 
    # float can be written as a complex, not the other way
    # around)
    Z4 = np.vectorize(np.complex)(x,y)
    # EXPERIMENT: What if you leave out ...(np.complex)...
    #             or try to use (np.float). Why is that?
    #             Hint: a float is a SINGLE real number,
    #                   while a complex is a PAIR of reals  
    print('complex matrix Z4 looks like this...;')
    print(Z4)
        
        
    print('Strategy 5...', end='')
    # create a complex out of a double real array
    # specifying that a complex number is created
    # from two reals 
    Z5 = z.view(dtype=np.complex)
    # EXPERIMENT; what if you don't give a dtype
    #             for output? Check the shape!
    # EXPERIMENT; is there any difference in using
    #             complex versus np.complex
    print('complex matrix Z5 looks like this...;')
    print(Z5)
    
    # print properties of all complex arrays ...
    printZProps(Z1,1,'Only for small Z')
    printZProps(Z2,2,'Simple, scaleable')
    printZProps(Z3,3,'Variant of #2 ')
    printZProps(Z4,4,'Efficient, numpy only')
    printZProps(Z5,5,'Efficient, numpy only')

# launch the program ...   
doMain()