# -*- coding: utf-8 -*-
"""
Py3MatrixAddressing.py  -- Experiment with matrix indexing and slicing
                           STANDARD PY3 ONLY!

@author: Bart Gerritsen

Description
-----------

See: http://www.pythoncentral.io/how-to-slice-listsarrays-and-tuples-in-python/

"""



# Observe there is no NumPy or ScipY import here.





def matrixPrettyPrint(A,label=''):
    hdr='The {:d} by {:d} matrix {:s}'.format(len(A),len(A[0]),label)
    print(hdr)
    for r in range(len(A)):
        print('[ ', end='')
        for c in range(len(A[0])):
            print(A[r][c],'', sep=' ', end='')
        print(' ]')    

A = [
     [ 'a00', 'a01', 'a02', 'a03', 'a04' ],
     [ 'a10', 'a11', 'a12', 'a13', 'a14' ],
     [ 'a20', 'a21', 'a22', 'a23', 'a24' ],
     [ 'a30', 'a31', 'a32', 'a33', 'a34' ],
     [ 'a40', 'a41', 'a42', 'a43', 'a44' ]
     ]

V0 = [    0  ,  1   ,   2   ]
V1 = [  'v0' , 'v1' , 'v2'  ]   # 1d row vector
V2 = [ ['v0'],['v1'],['v2'] ]   # dx1 2d column vector

matrixPrettyPrint(A,label='A;')
# EXPERIMENT: adrressing, rows, columns, elements
#             including slicing

print('(1) Ways to address the 3rd row...')
print('    ------------------------------')
print(A[2])
print(A[2],)    # not nice ...
print(A[2][:])
print(A[len(A)-3]) # yes, scroll backwards through indices! 

print('(2) Ways to address 2nd through 3rd rows ...')
print('    ----------------------------------------')
print(A[1:3])
print(A[1:3][:])

print('(3) Ways to address the first 2 rows ...')
print('    ------------------------------------')
print(A[0:2])
print(A[:2])
print(A[:2],)    # not nice ...
print(A[:2][:])

print('(4) Ways to address even rows only ...')
print('    ----------------------------------')
print(A[0:5:2])
evenRows = slice(0,5,2)
print(A[evenRows])

print('(5) Ways to address even rows in reversed order ...')
print('    -----------------------------------------------')
print(A[::-2])
evenRows = slice(4,0,-2)
print(A[evenRows])

print('(6) Ways to address the 3rd through 5th row...')
print('    ------------------------------------------')
print(A[2:])
print(A[2:],)    # not nice ...
print(A[2:][:])
print('(7) rows in reverse order ...')
print('    -------------------------')
print(A[-1])    # last rows
print(A[-2:])   # last two rows 
print(A[:-2])   # everything except the last two rows
print(A[::-1])  # all rows in inverse order
print('slicing ....: ', A[slice( 0)])
print('slicing ....: ', A[slice( 1)])
print('slicing ....: ', A[slice( 2)])
print('slicing ....: ', A[slice( 3)])
print('slicing ....: ', A[slice( 4)])
print('slicing ....: ', A[slice(-1)])
print('slicing ....: ', A[slice(-2)])
print('slicing ....: ', A[slice(-3)])
print('slicing ....: ', A[slice(-4)])
print('slicing ....: ', A[slice(-5)])

# EXPERIMENTL   indexing of columns is not always what you expect
print('(8) Ways to address the 3rd column...')
print('    ---------------------------------')
print(A,[2])     # not nice ...
print(A[:][2])    
print(A[:][len(A)-3]) # yes, scroll backwards through indices! 

print('Correct ways to address the 3rd column...')
print([r[2] for r in A])

print('ways to address the 3rd and 4th column...')
print('    -------------------------------------')
print([r[2:4] for r in A])

print('ways to address columns in reversed order ...')
print('    -----------------------------------------')
print([r[::-1] for r in A])

print('The {:d} by {:d} reversed matrix A;'.format(len(A),len(A[0])))
print([r[::-1] for r in reversed(A)])
matrixPrettyPrint([r[::-1] for r in reversed(A)],'reversed A;')
        
print('Vectors V1 and V2')
print('The {:d}-row-vector V1: {:s}'.format(len(V1),str(V1)))
print('The {:d}-by-{:d}-column-vector (matrix) V2: {:s}'.\
      format(len(V2),len(V2[0]), str(V2)))

# EXPERIMENT: adrressing, rows, columns, elements
#             including slicing
print('(9) addressing V1;')
print('    --------------')
print(V1[2])
print(V1[2][0])
print(V1[2][0:2])   # indxing and substring
print(V1[::-1])
print(V1[::])
print(V1[:])

print(V1[:])  # [0][1][:])


print('(10) addressing V2;')
print('     --------------')
print(V2[2])
print(V2[2],)   # not nice
print(V2[2][:])
print(V2[2][0])
print(V2[2][0][0:2])
