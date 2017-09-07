# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from math import *
import numpy as np
import pylab as pl

'''
x = 0.357
y = (pow(e, x) + sin(pi * x) + pow(x, 10))/(10)
print ("y = " , y)
'''

t = np.linspace(0, 12.5, 300)
x = t + 2*np.sin(2*t)
y = t + 2*np.cos(5*t)

pl.plot(x,y,color = 'k') 

