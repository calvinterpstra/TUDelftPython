# -*- coding: utf-8 -*-
"""
ConfinedImport.py -- confine your import experiment to what's really 
                     needed

                     (occasionally, packages lack a good structure, and
                      trouble may result if you try to confine imports)

@author: Bart Gerritsen
"""

# EXPERIMENT: different forms of import ...
# import numpy as np
from numpy import pi as myPI



# EXPERIMENT: different forms of import ...
# myPIVal =  float( np.pi )
myPIVal = float( myPI )

print('NumPy\'s PI (often denoted as np.pi) has value: {:20.18f}'. \
      format(myPIVal))