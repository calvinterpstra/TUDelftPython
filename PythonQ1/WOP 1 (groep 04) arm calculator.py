# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 15:04:47 2017

@author: Calvin
"""

from math import *
import numpy as np

wally = 26;
wallx = 0.6;
x = 13 + wallx/2;
platform = 1.6;
gap = 1.5;
apple = 8 /2;

h = (wally + gap)/2 - pow(x,2)/(2*(wally + gap)) + apple + platform; # Height to main axle
l = (wally + gap)/2 + pow(x,2)/(2*(wally + gap)); # Distance between axles

height = 15;
length = 17;

dh = height - h;
dl = length - l;
dx = sqrt(abs(pow(dl, 2) - pow(dh, 2))) * -((pow(dl, 2) - pow(dh, 2))/abs(pow(dl, 2) - pow(dh, 2)));
gap = height + length - wally - apple - platform;

print("h = ", h);
print("l = ", l);
print("dx = ", dx);
print("dh = ", dh);
print("dl = ", dl);
print("gap = ", gap);