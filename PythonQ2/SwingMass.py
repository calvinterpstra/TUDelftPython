# -*- coding: utf-8 -*-
"""
SwingMass.py    -- numerically compute a 2-element composed mass

@author: Bart Gerritsen
"""
import numpy as np


# SI unit m, kg etc.
rho =  8.0e+03  # specific mass bronze
h   =  1.0e-02  # height of ellipse
a   = 20.0e-02  # ellipse semi-major
b   = 10.0e-02  # ball radius=ellipse semi-minor


# how many steps form x=0 to x=b
N  = 60  # nr of steps to use, increase if not accurate enough
dx = b/N # the higher N, the smaller the step size dx from 0 to b
A14 = 0

step = np.arange(0,b,dx)
Y2 = (a/b)*np.sqrt(b**2 - step**2)
Y1 = (b/b)*np.sqrt(b**2 - step**2)

dA = (Y2-Y1)*dx
A14 = np.sum(dA)

A44=4*A14      # area of ALL 4 quadrants
M44=A44*h*rho  # volume x rho = mass

# print results
print('Results (numeric);')
print('  A14: {:12.9e} [m^2]'.  format(A14))
print('  A44: {:12.9e} [m^2]'.  format(A44))
print('  M44: {:12.9e} [ kg]'.  format(M44))

# analytic results for verification
A14a = np.pi*a*b/4 - np.pi*b*b/4
A44a = 4*A14a
M44a = np.pi*b*(a-b)*h*rho
print('Verification (analytic);')
print('  A14: {:12.9e} [m^2]'.  format(A14a))
print('  A44: {:12.9e} [m^2]'.  format(A44a))
print('  M44: {:12.9e} [ kg]'.  format(M44a))

err=(A14-A14a)/A14a  # percent of analytic result

if err <= 0.01:
    print('Error relative to analytic less than 1%. OK.')
    
else:
    print('Not accurate enough (err={:+5.3%}); increase steps N !'.\
          format(err))