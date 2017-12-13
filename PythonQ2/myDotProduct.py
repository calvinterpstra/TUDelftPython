# -*- coding: utf-8 -*-
"""
myDotProduct.py -- script computing a dot product of two vectors 

@author: Bart Gerritsen
"""

# This is dot product 

u = [1, 4, -2, 3]
v = [-1, 2, 2, 1]

# Compute the dot product w = u.v
w = u[0]*v[0] + u[1]*v[1] + u[2]*v[2] + u[3]*v[3]

# print the dot product 
print('dot product w=u.v=' + '{:d}'.format(w) )

print('dot product computation completed.')