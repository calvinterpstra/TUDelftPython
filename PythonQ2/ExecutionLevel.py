# -*- coding: utf-8 -*-
"""
ExecutionLevel.py -- experiment whith execution levels

    Instructions: whenever you insert a function CALL, do this:
        
                  myFunc(lvl+1)
                  
                  whenever you DEFINE a new function, define it like this:
                      
                  def myFunc(lvl):
                      print('myFunc() at level {:d}'. format(lvl))
                      ...
                  
                  This will keep you indentation level tracking consistent

@author: Bart Gerritsen
"""

# this global variabe is recording the execution (stack) level ...
lvl = 0

# we start tracking here ...
print('Starting at level {:d}'. format(lvl))


def myFunc(lvl):
    print('... ... entering myFunc() at level {:d}'. format(lvl))
    my2ndFunc(lvl+1)
    print('... ... returning from  myFunc() level {:d}'. format(lvl))


def my2ndFunc(lvl):
    print('... ... ... entering my2ndFunc() at level {:d}'. format(lvl))
    # ... do some other stuff
    print('... ... ... returning from my2ndFunc() level {:d}'. format(lvl))
    
    
def runMain(lvl):
    print('... entering runMain() at level {:d}'. format(lvl))
    myFunc(lvl+1)
    print('... returning from runMain() level {:d}'. format(lvl))




# invoke main from level 0 
runMain(lvl+1)
print('Terminating at level {:d}'. format(lvl))