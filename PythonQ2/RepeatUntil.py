# -*- coding: utf-8 -*-
"""
RepeatUntil.py   -- Implement a repeat until loop (discouraged)

@author : Bart Gerritsen
"""

import math

REPEAT = True
UNTIL  = True

PI    = math.pi
delta = 1.0e-06

p    = 0
phi  = 0
dphi = 2*PI/360

# repeat ...
while REPEAT: 
    # print('Point {:d} at angle: {:f} rad'.format(p,phi))
    p = p + 1
    phi = phi + dphi
    print('Point {:d} at angle: {:f} rad'.format(p,phi))
    # ... until ...
    if not UNTIL or abs( phi - PI ) < delta: break 
