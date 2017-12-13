# -*- coding: utf-8 -*-
"""
Type.py   -- Experiment with variable types 

@author : Bart Gerritsen
"""

# global constants 
VOID      =''
SPACE     = ' '
TAB       = '\t'
NEWLINE   = '\n'
SEPARATOR = SPACE

def myFunc(message):
    mess = message
    # EXPERIMENT: comment out the return value and see
    # how it interacts with the type of the function myFunc()
    return mess


# define a sequence of sequences of a mix of data item types ...
    
S = [    ['gravitatie constante', 9.81, '[m/s^2]', 'maar alleen op aarde!'],
         ['a',0b1101,0xA10,None,__name__,"__main__",myFunc(VOID)],
         [0.1, 0.2, 0.3, 1, 2, 3, 11, 12, 13, 21, 22, 23], 
         [1+2j, complex(-1,2), -1j, complex(0,1), 0+0j] 
    ]

# ... and use the standard iterators to print the elements ...
for seq in S:
    print('Sequence: {:s}'.format(str(seq)))

print('Element type and value;')
print('========================================================')

for seq in S:
    for elem in seq:
        # EXPERIMENT: also comment out the current print statement
        # and try the other one. Study how the printing of the various
        # types change ...
        
        # print( str(type(elem)), str(elem), sep=TAB+TAB, end=NEWLINE )
        print('{:>18s}: {:^30s}'.format(str(type(elem)), str(elem) ))
