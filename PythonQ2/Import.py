# -*- coding: utf-8 -*-
"""
import.py -- experiment with the import location 

@author: Bart Gerritsen
"""

def myFunc():
    import math
    
    # EXPERIMENT: comment the above import
    # and try to do this instead ...
    # from math import *
        
    print('PI={:f}'.format(math.pi))

def main():
    myFunc()
    # EXPERIMENT: uncomment the following line
    # and study the error this produces. How to
    # remedy this?
    
    # print('PI={:f}'.format(math.pi))
    
main()