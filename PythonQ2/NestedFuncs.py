# -*- coding: utf-8 -*-
"""
NestedFuncs.py -- Experiment with functions defined and used inside other
                  functions

@author: Bart Gerritsen
"""
    
def myFunc(lvl):
    print('{:s}, level: ({:d})'. format('myFunc()',lvl))
    
    def myOtherFunc(lvl):
        print('{:s}, level: ({:d})'. format('myOtherFunc()',lvl))
        
        def againAnotherFunc(lvl):
            print('{:s}, level: ({:d})'. format('againAnotherFunc()',lvl))
        
        againAnotherFunc(lvl+1)
    
    myOtherFunc(lvl+1)
    
    # EXPERIMENT: try to use function aginAnotherFunc() here ...
    # againAnotherFunc(lvl+1)



def doMain():
    lvl = 0
    
    myFunc(lvl+1)
    
    # EXPERIMENT: try to use function myOtherFunc() here ...
    # myOtherFunc(lvl+1)
    # againAnotherFunc(lvl+1)



if __name__ == '__main__': doMain()