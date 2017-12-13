# -*- coding: utf-8 -*-
"""
CountingTheStars  -- how to terminate an endlees looping program?

    How to execute?
    ---------------
    Run the program
    Select the CONSOLE
    Key in a maximum number of counts (increase gradually)
    When taking to long, press CTRL+C (simultaniously) in the CONSOLE

@author: Bart Gerritsen
"""

# init N to zero ... safe 
N = 0

print('Counting the stars in the Universe;')
print('---------------------------------------------------------------')
print('CAUTION: this program may be caught in an ENDLESS LOOP')
print()
print('STOP the program using: CTRL+C in the CONSOLE, ')
print('should the programs takes too long')
print()
N = int( input('Give me a maximum number of stars: ' ) )
if N > 0:
    count = 0
    while True:
        print('... counting the stars ... {:6d}'.format(count))
        if count == N:
            break
        else:
            count += 1
    print('We counted {:d} stars'.format(count))

    