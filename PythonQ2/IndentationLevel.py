# -*- coding: utf-8 -*-
"""
IndentationLevel.py -- experiment whith source code indentation levels

@author: Bart Gerritsen
"""

# EXPERIMENT: try shifting any line at this level (including def's) one to
#             position to the right
# EXPERIMENT: try shifting all lines at this level (consistently) to the right
print('Starting')


# comment at indentation level 0 ...
 # for comments, the indentation level is irrelevant
                # put them anywhere you see fit
                
a,b = 1,2

 # EXPERIMENT: break the indentation consistency
 # this would cause an error because we breach indentation consistency
 # we might observe the orange triangle in Spyder, signalling this as 
 # soon as we uncomment the next line
 #c = 3
 
 
 
# EXPERIMENT: try replacing a single TAB by 2 TABs
# define a function with an indentation composed of 1 TAB character
# (Spyder may instantly replace this by a consistent number of spaces)
def myFunc():
    print('... ... entering myFunc()')
        # my2ndFunc()
    my2ndFunc()
    print('... ... returning from  myFunc()')



# EXPERIMENT: let try another (consistent!) indentation format
# define a function with an indentation composed of just a single space
def my2ndFunc():
 print('... ... ... entering my2ndFunc()')
 # ... do some other stuff
 print('... ... ... returning from my2ndFunc()')
 
 
 
 
# EXPERIMENT: and yet another ...   
def runMain():
                                         print('... entering runMain()')
                                         myFunc()
                                         print('... returning from runMain()')
                       



# invoke main from level 0 
runMain()
print('Terminating')