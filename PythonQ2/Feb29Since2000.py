# -*- coding: utf-8 -*-
"""
Feb29Since2000.py -- count the number of Feb 29's since the millenium change 
                     using ranges

@author: Bart Gerritsen
"""

import datetime as dt

# constants ...
millenium = dt.date(2000,1,1)   # EXPERIMENT: change as you see fit
today     = dt.date(2017,11,28) #             change as you see fit

feb29s = 0
for y in range( millenium.year, today.year, 4):
    feb29s += 1

# print results ...

print('Millenium   : ', millenium)
print('Today:      : ', today)
print('Elapsed     : ', today.year - millenium.year, ' years')
print('This era    :  ', feb29s, ' times a Feb 29.')
print('Next Feb 29.: ', int(today.year - (today.year % 4) + 4) )

# EXPERIMENT: compute the next Feb 29 by extending the range by 4 years
extFebList = range(millenium.year, today.year+4, 4)
for y in extFebList:
    # to hold the last in the extended list
    nextFeb29 = y
    
print('Check       : ', nextFeb29)

