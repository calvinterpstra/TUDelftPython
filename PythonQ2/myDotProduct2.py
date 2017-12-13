# -*- coding: utf-8 -*-
"""
myDotProduct2 -- compute dot poduct using a function dot()

author: Bart Gerritsen
"""

# This is myDotProduct (version 2)

# we need this module for function isnan()
import math

u = [1, 4, -2, 3]
v = [-1, 2, 2, 1]

z = math.pi

def dot(u,v):
    w = float('nan')
    if not ( len(u) == len(v) ):
        print("error: u and v must have equal lengths")
    else:
        w = 0.0
        for j in range(len(u)):
            w = w + u[j] * v[j]
    return w    

# Compute the dot product w = u.v
w = dot(u,v)

# print the dot product 
if math.isnan(w):
    print('Dot product could not be computed.')
else:
    print('Dot product w=u.v=' + '{:+8.5f}'.format(w) )

print('myDotProduct2 completed.')
