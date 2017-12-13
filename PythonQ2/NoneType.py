# -*- coding: utf-8 -*-
"""
NoneType -- experiment with the NoneType

@author: Bart Gerritsen
"""


def myFunc(a,b):
    rStart,rStop=(a,b)
    mySum = 0
    for k in range(rStart,rStop):
        mySum += k
    print('myFunc() done. mySum={:s}'.format( str(mySum)) )
    # EXPERIMENT: return mySum as int and or float ... and 
    #             check the changes
    # return int(mySum)
    # return float(mySum)
    # return complex(mySum)

def myOwnNoneFunc(L,v):
    val = None
    for x in L:
        if abs( x-v ) < 1.0E-03:
            # close enough ...
            val = x
    return val


def main():
    a,b = (1,11)
    val=myFunc(a,b)
    # EXPERIMENT: try this also
    # if not val:  of: if val==None:
    #   print('myFunc() returns a {:s} {:s}'.format(str(type(val)),str(val)))
    print('myFunc() returns a {:s} {:s}'.format( str(type(val)), str(val) ) )
    print('Done.')
    
    print('Test myOwnNoneFunc(L);')
    L = [-0.10, 0.16, 5.10, -2.45, 0.00 , -0.15, 2.10, 6.78]
    for item in [-0.10, 2.10, 0.16, -0.16, -0.21, 0.10, -0.15]:
        val = myOwnNoneFunc(L,item)
        if val is None:
            print('Item: {:+4.2f} NOT found.'.format( item) )
        else:
            print('Found item: {:+4.2f}'.format( item) )

# run the main function ...
main()
