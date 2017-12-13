# -*- coding: utf-8 -*-
"""
Permutations2.py  -- do our own design morpho permutation

@author: Bart Gerritsen
"""

import random as rand
import itertools as itr


def doMain():
    
    # create a set of just even numbers ...    
    body = list(itr.permutations(['chassis', 'door', 'hood', 'top']))
    mat  = list(itr.permutations(['aluminium','wood', 'plastic', 'fabric']))
    
    parts = list(zip(mat,body))
    
    # print('Parts : {:s}'.format(str(parts)))
    
    print('A design ...consider any combniation of ...')
    for n in range(len(parts)):
        for p in range(len(parts[n])):
            print(str(parts[n][p]), end='')
        print()

    # randomly sample from first half of parts list 
    half = int( len(parts)/2 )
    concepts = rand.sample(range(half), 5)
    
    for d in concepts:
        print(parts[d])


# run the program ...
doMain()
