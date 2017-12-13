# -*- coding: utf-8 -*-
"""
NumPyMatrixAddressing.py     -- Experiment with matrix indexing
                                Py3 and Numpy specific!

@author: Bart Gerritsen
"""

import numpy as np

def matrixPrettyPrint(A,label=''):
    hdr='The {:d} by {:d} matrix {:s}'.format(len(A),len(A[0]),label)
    print(hdr)
    for r in range(len(A)):
        print('[ ', end='')
        for c in range(len(A[0])):
            print(A[r][c],'', sep=' ', end='')
        print(' ]')    
            
A = np.array([
     [ 'a00', 'a01', 'a02', 'a03', 'a04' ],
     [ 'a10', 'a11', 'a12', 'a13', 'a14' ],
     [ 'a20', 'a21', 'a22', 'a23', 'a24' ],
     [ 'a30', 'a31', 'a32', 'a33', 'a34' ],
     [ 'a40', 'a41', 'a42', 'a43', 'a44' ]
     ])

V1 = np.array([  'v0' , 'v1' , 'v2'  ])   # 1d row vector
V2 = np.array([ ['v0'],['v1'],['v2'] ])   # dx1 2d column vector

matrixPrettyPrint(A,label='numpy.ndarray A')

print('NumPy pretty print matrix A;')     
print(A)

# EXPERIMENT: adrressing, rows, columns, elements
#             including slicing

print('(1) Ways to address the 3rd row...')
print('    ------------------------------')
print(A[2])
print(A[2],)    # not nice ...
print(A[2][:])
print(A[len(A)-3]) # yes, scroll backwards through indices! 
print('Numpy specific;')
print(A[2,:])
print(A[2,...])

print('(2) Ways to address 2nd through 3rd rows ...')
print('    ----------------------------------------')
print(A[1:3])
print(A[1:3:1])
print(A[1:3][:])
print('Numpy specific;')
print(A[1:3,:])
print(A[1:3:1,:])
print(A[1:3,...])

print('(3) Ways to address the first 2 rows ...')
print('    ------------------------------------')
print(A[0:2])
print(A[:2])
print(A[:2],)    # not nice ...
print(A[:2][:])
print('Numpy specific;')
print(A[:2,:])
print(A[0:2,:])
print(A[:2,...])
print(A[0:2,...])

print('(4) Ways to address the 3rd through 5th row...')
print('    ------------------------------------------')
print(A[2:])
print(A[2:],)    # not nice ...
print(A[2:][:])
print('Numpy specific;')
print(A[2:,:])
print(A[2:,...])

# EXPERIMENT:   indexing of columns is not always what you expect
print('(5) Ways to address the 3rd column...')
print('    ---------------------------------')
print(A,[2])     # not nice ...
print(A[:][2])    
print(A[:][len(A)-3]) # yes, scroll backwards through indices! 

print('Correct ways to address the 3rd column...')
print([r[2] for r in A])
print('Numpy specific;')
print(A[:,2])
print(A[...,2])

print('(6) ways to address the 3rd and 4th column...')
print('    -----------------------------------------')
print([r[2:4] for r in A])

print('Numpy specific;')
print(A[:,2:4])
print(A[...,2:4])

print('(7) Correct ways to address columns in reversed order ...')
print('    -----------------------------------------------------')
print([r[::-1] for r in A])
print('Numpy specific;')
print(A[:,::-1])
print(A[...,::-1])

print('The {:d} by {:d} reversed matrix A;'.format(len(A),len(A[0])))
print([r[::-1] for r in reversed(A)])
matrixPrettyPrint([r[::-1] for r in reversed(A)],'reversed A;')
print('Numpy specific;')
print(A[::-1,::-1])

print('Numpy specific;')
print('mixed elements: ',A[0,-1],A[0][3],A[0,-3],A[0][1], sep=' ')

print('Numpy vectors V1 and V2')
print('The {:d}-row-vector V1: {:s}'.format(len(V1),str(V1)))
print('The {:d}-by-{:d}-column-vector (matrix) V2: {:s}'.\
      format(len(V2),len(V2[0]), str(V2)))

# EXPERIMENT: adrressing, rows, columns, elements
#             including slicing
print('(8) addressing V1;')
print('    --------------')
print(V1[2])
print(V1[2][0])
print(V1[2][0:2])   # indxing and substring
print(V1[::-1])
print(V1[::])
print(V1[:])
print('Numpy specific;')
print(V1[1,...])
print(V1[...])
print(V1[...,0])
print(V1[...,1])
print(V1[...,1][...][...][...][...][...]) # don't do this at home ...

print('(9) addressing V2;')
print('    --------------')
print(V2[2])
print(V2[2],)   # not nice
print(V2[2][:])
print(V2[2][0])
print(V2[2][0][0:2])

print('Numpy specific;')
print(V2[1,...])  # not very consistent; compare V2
print(V2[1,:])
print(V2[...])
print(V2[...,0])
print(V2[:,0])
print(V2[:,0][1][:])
print(V2[:,0][1][1:])
print(V2[:,0][1][:1])
print(V2[:,0][::-1][::-1][::-1][::-1][::-1])
print(V2[:,0][:][::-1])
print(V2[...,0][::-1])

print('(10) using asarray();')
print('    -----------------')
print('V1 as np.anarry(V1)')
print(np.asarray(V1))
print('V2 as np.anarry(V2)')
print(np.asarray(V2))
print('merging arrays;')
print(np.asarray([ V2[::] ] + ['v3', 'v4']))



print('test')
print('======================================================================')
print('rij 1:', A[1,...])
print('rij 1:', A[1,:])
print('rij 2-3:', A[2:4,...])
print('rij 2-3:', A[2:4,:])
print('element:',A[1,3])
print('linksonder submatrix: ', A[3:,:2])
print('column 3: ', A[:,3])
print('column 3: ', A[...,3])
print('column 3: ', A[:,3:])
print('column 3: ', A[...,3:])
print('column 3: ', [r[3] for r in A])

