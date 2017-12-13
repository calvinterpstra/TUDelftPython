# -*- coding: utf-8 -*-
"""
Permutations.py  -- permute a number series from a small set of permitted
                    decimals

@author: Bart Gerritsen
"""

import itertools


def doMain():
    
    # create a set of just even numbers ...
    decimals = set( (x for x in range(0,10,2)) )
    
    print('Decimals : {:s}'.format(str(decimals)))
    
    # generate a big list ...
    decNumbers = list(itertools.permutations(decimals));
    
    print('These increasing numbers that can be made out of these decimals;')
    
    for n in range(len(decNumbers)):
        num = ''
        for d in decNumbers[n]: 
            num += str(d)
        print('Number: {:s}'.format(num))
    print('{:d} permutations (all unique numbers) printed'.format(n))
    print('For all these numbers: the sum of the decimals = {:d}'. \
          format(sum(decNumbers[0])))


# run the program ...
doMain()
