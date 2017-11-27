# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 20:10:02 2017

@author: Calvin
"""

from math import *;
import numpy as np;

alpha;
width;
gap;
Larm;
x;

Daxel = 4;
Dwheel = 150;
Lramp = 7000;
theta = 3*np.pi / 2;

x = (Lramp * Daxel / Dwheel) + gap;
width = gap / np.sin(alpha);
Larm =  gap / np.tan(alpha);
def main():
    
    
main();