# -*- coding: utf-8 -*-
"""
datatypes.py  -- experiment with standard data types 
                 (Py3k/NumPy data types, and str() formatting)

@author: Bart Gerritsen
"""

import sys, math, cmath
import numpy as np

def doIntegers():
    # integers ....a mix of definitions
    zero, a,b,c,d,e = ( int('0',10), int('1'), int('2'), int(3), 4, 5 )
    maxint = int(sys.maxsize)
    
    print('Experiment with standard data types')
    print('-----------------------------------')
    print('Integers;')
    print('Value integer {1:s}           : {0:d}'.format(zero,str(zero)))
    print('maxsize                   : {:d}'.format(sys.maxsize))
    print('integer \"inf\"             : {:d}'.format(maxint))
    print('Integers lie in range     : [{:d} ... {:d}]'. \
          format(-maxint,maxint-1))
    print('Big stuff: 10^100         : {:s}'.format('(see next line)'))
    print('{:s}'.format(str(pow(10,100))))
    print('(should be equal to: {:2.0e})'.format(pow(10,100)))
    
    print('integers: (a,b,c,d,e) = {:s} is composed of;'. \
          format(str((a,b,c,d,e))))
    for i in (a,b,c,d,e):
        # first, print the class (the type,say) ...
        print('  {:s} variabele'.format(str(type(i))), end='')
        # check if indeed we are dealing with an integer ...
        if isinstance(i, int):
            intCheck = 'int'
        else:
            intCheck = 'NOT an int!'
        print(' (instance: {:s})'.format(intCheck), end='')
        print(' heeft waarde : {:s}'.format(str(i)), end='\n')
    print('Note:')
    print('  Python3 has no long type anymore.')
    print('  Python3 ints can grow to arbitrary value')
    print('  In practice, int have a max given by \"sys.maxsize\"')
    
    # EXPERIMENT: simulate integer overflow and underflow ...
    MAXINT = sys.maxsize
    print('MAXINT for this implementation is set to: {:+d}'.format(MAXINT))
    overflown = False
    for i in range(10):
        if MAXINT+i < MAXINT:
            print('   ... integer OVERFLOW!                : {:+d}'. \
                  format(MAXINT+i))
            overflown = True
        else:
            print('   ... no integer overflow; continue ...: {:+d}'. \
                  format(MAXINT+i))
    if overflown:
        print('Overflow at MAXINT did occur.')
    # ... now the MININT boundary value ...
    MININT = -sys.maxsize
    print('MININT for this implementation is set to: {:+d}'.format(MININT))
    underflown = False
    for i in range(10):
        if MININT-i > MININT:
            print('   ... integer UNDERFLOW!               : {:+d}'. \
                  format(MININT-i))
            underflown = True
        else:
            print('   ... no integer underflow; continue...: {:+d}'. \
                  format(MININT-i))
    if underflown:
        print('Underflow at MAXINT did occur.')
        

def doFloats():
    # floats ... also a mix of definitions and initialisations
    EPS = float(1.0E-03)   # a constant
    zero, x,y = ( float('0.00'), float('3.9999'), float(1) )
    PI = math.pi
    
    INF = float('inf')
    NAN = float('nan')
    BIGFLOAT = float('1.0E000') # EXPERIMENT with E000 .. E999
    eps1 = y / INF
    eps2 = y / BIGFLOAT
    
    print('Floats;')
    print('Value float {1:s}             : {0:+12.9f}'.format(zero,str(zero)))
    print('maxsize                     : {:f}'.format(sys.maxsize))
    print('Variable y in default format: {:f}'.format(y))
    
    # EXPERIMENT: gebruik ook een andere afdrukformaten, zoals E en G
    z = NAN
    print('Variable z in default format: {:f}'.format(z))
    z = INF
    print('Variable z is nu oneindig   : {:G} (String: {:s})'. \
          format(z,str(z)))
        
    print('PI = {:53.52f}'.format(PI))
    print('PI = {:<70s}'.format(str(math.pi)))
    # EXPERIMENT: see how small an eps you can generate ...
    print('eps={:+64.62e}'.format(eps1))
    # EXPERIMENT: and a non-zero 
    print('eps={:+64.62e}'.format(eps2))
    if pow(x,2) - 16 == 0:
        print('Hey, the value of x^2-16 is exact 0!')
    else:
        # EXPERIMENT: check for which x, we hit +/- EPS.
        #             Is that x+EPS or x-EPS?
        if abs( pow(x,2) - 16 ) <= EPS:
            print('x^2-16 = {:f} in range [-EPS,+EPS]=[{:f},{:f}]'. \
                  format(pow(x,2)-16,-EPS,EPS))
        else:
            print('x^2-16={:+12.10f} (is not 0)'. \
                  format(pow(x,2)-16))
    
def doNumPyFloats():
    # Numpy floats ... also a mix of definitions and initialisations
    zero, u, v = ( np.float('0.00'), np.float('1'), \
                  np.float( 1.0*1.0*100**0/0.001) )
    PI16 = np.float16(math.pi)
    PI32 = np.float32(math.pi)
    PI64 = np.float64(math.pi)
    PI_  = np.float_(math.pi)
    BIGFLOAT = np.float('1.0E000') # EXPERIMENT with E0000 .. E9999
    eps1 = u / BIGFLOAT - zero
    eps2 = v / BIGFLOAT - zero
    
    print('NumPy floats;')
    print('Variable u in default format: {:f}'.format(u))
    print('Variable v in default format: {:f}'.format(v))
    # EXPERIMENT: see how small an eps you can generate ...
    print('eps1={:+64.62e}'.format(eps1))
    # EXPERIMENT: and a non-zero 
    print('eps2={:+64.62e}'.format(eps2))
    print('Check my numpy PI values;')
    for f in (PI16, PI32, PI64, PI_):
        print('PIxx={:+64.62e}'.format(f))
        print('PIxx= ', repr(f), sep='', end='\n')
    # EXPERIMENT: check out different representations of PI when
    #             using standard functions, including round() ...
    n = 2 # how many digits after decimal point in round(number,n) ?
    print('PI16          = {:+36.34e}'.format(PI16))
    print('round(PI16,{:d}) =  {:e}'.format(n,round(PI16,n)))
    print('round(PI16,{:d}) =  {:g}'.format(n,round(PI16,n)))
    print('eval(PI16))   = {:+36.34e}'.format(eval('PI16')))
    print('repr(PI16))   =  {:36s}'.format(repr(PI16)))
    print('PI32          = {:+36.34e}'.format(PI32))
    print('round(PI32,{:d}) =  {:e}'.format(n,round(PI32,n)))
    print('round(PI32,{:d}) =  {:g}'.format(n,round(PI32,n)))
    print('eval(PI32))   = {:+36.34e}'.format(eval('PI32')))
    print('repr(PI32))   =  {:36s}'.format(repr(PI32)))
    same = True
    digits = 1
    while same:
        if round(PI32,digits) - round(PI16,digits) > 0:
            same = False
        else:
            digits += 1
    print('PI16 and PI32 differ in fraction decimal {:d}'.format(digits))
    
    # EXPERIMENT: lets do the same experiment with float32 en float64
    print('PI32          = {:+36.34e}'.format(PI32))
    print('round(PI32,{:d}) =  {:e}'.format(n,round(PI32,n)))
    print('round(PI32,{:d}) =  {:g}'.format(n,round(PI32,n)))
    print('eval(PI32))   = {:+36.34e}'.format(eval('PI32')))
    print('repr(PI32))   =  {:36s}'.format(repr(PI32)))
    print('PI64          = {:+36.34e}'.format(PI64))
    print('round(PI64,{:d}) =  {:e}'.format(n,round(PI64,n)))
    print('round(PI64,{:d}) =  {:g}'.format(n,round(PI64,n)))
    print('eval(PI64))   = {:+36.34e}'.format(eval('PI64')))
    print('repr(PI64))   =  {:36s}'.format(repr(PI64)))
    same = True
    digits = 1
    while same:
        # EXPERIMENTEER: probeer hieronder ook eens: if ...... > 0.1:
        #                Werkt dat wel?
        if round(PI64,digits) - round(PI32,digits) > 0:
            same = False
        else:
            digits +=1
    print('PI32 and PI64 differ in fraction decimal {:d}'.format(digits))
    print('PI32 and PI64 actually differ: {:+30.28f}'. \
              format(round(PI64,digits) - round(PI32,digits)))
    # EXPERIMENTEER met float in expressions in de volende 'predicates' 
    print('round(PI64,digits) - round(PI32,digits) == 0       : {:s}'. \
          format(str(round(PI64,digits) - round(PI32,digits) == 0)))
    print('round(PI64,digits) - round(PI32,digits) > 0        : {:s}'. \
          format(str(round(PI64,digits) - round(PI32,digits) > 0)))
    
    # EXPERIMENTEER: with float itemsize (nr of bytes)
    U = np.empty(36,dtype=np.float16).reshape(6,6)
    print(U); print('Matrix U has item sizes: {:d} bytes'. \
         format(U.itemsize))
    

def doComplexs():
    z1,z2,z3,z4 = ( complex(1.0,1.0), complex(1j),
                       complex(2.0),complex('-4.5+3j') )
    z5 = -9.1-2.7j
    
    print('Complexs;')
    print('Complex numbers z1 thru z5={:s}'.format(str((z1,z2,z3,z4,z5))))
    for z in (z1,z2,z3,z4,z5):
        print('  z = {0:<12s}'. \
              format(str(z)), end='')
        print(' ordered pair (Re z,Im z)=({:+5.3f},{:+5.3f}) '. \
              format(z.real,z.imag))
    # EXPERIMENT: printing complex numbers in different formats
    Z = []
    for z in (z1,z2,z3,z4,z5): Z.append(z)
    print('Complex {1:d}-vector Z={0:s}'.format(str(Z),len(Z)))
    print('Conjugates z* of Z[k], using \'i\' i.s.o \'j\';')
    for z in Z:
        # pretty ptring using 'i' instead of 'j'
        print("  z= {c.real:+0.05f} {c.imag:+0.05f}i". \
              format( c=z ), end='')
        print("  z*= {c.real:+0.05f} {c.imag:+0.05f}i". \
              format( c=z.conjugate() ), end='' )
        # EPERIMENT: calculate |z.conjugate()| and show that
        #            |z|==|z.jonguate()|
        print('  |Z[i]|={:g}'.format(abs(z)))
    for z in Z:
        print('  z= {c.real:+0.05f} {c.imag:+0.05f}i'. \
              format( c=z ), end='')
        r, phi = cmath.polar(z)
        print('  polar (r,phi)=({:+8.5f},{:+8.5f})'. \
              format( r, phi ) )
    for z in Z:
        # EXPERIMENT: r and phi can be obtained in different ways.
        #             Experiment with the calulcation scheme for r,phi
        r, phi = ( abs(z), cmath.phase(z) )
        print('  polar (r,phi)=({:+8.5f},{:+8.5f})'. \
              format( r, phi ), end='')
        print(' z=|z|exp(i*phi)={:+8.5f}*exp({:+8.5f}i)'. \
              format(r,phi) )

def doNone():
    a,b,c = (None, int('0'), complex(0,0))
    desc  = '(unknown)'
    print('None objects;')
    print('Variables: a,b,c={:s}'.format(str((a,b,c))))
    b = a
    # EXPERIMENT: try to set: c = complex(a,a). What happens? Why?
    # EXPERIMENT: try to set: c = complex(0,a). What happens? Why?
    # EXPERIMENT: try to set: c = complex(1,1*a). What happens? Why?
    c = a  # we can asign a None to a complex! 
    # EXPERIMENT: check b being equal to the None object
    #             experiment with a NAN solution versus is None.
    #             What is the difference?
    if b is None:
        desc = 'a None object'
    else:
        if isinstance(b, int):
            desc = 'still an int'
        else:
            desc = '(cannot determine)' 
    print('  b has now become: {:s} with value: {:s}'. \
          format( desc, str(b) ) )
    if c is None:
        desc = 'a None object'
    else:
        if isinstance(c, complex):
            desc = 'still a complex'
        else:
            desc = '(cannot determine)' 
    print('  c has now become: {:s} with value: {:s}'. \
          format( desc, str(c) ) )
    # ... and back: make a complex out of a None type!
    c = complex(0,0)
    if c is None:
        desc = 'a None object'
    else:
        if isinstance(c, complex):
            desc = 'again a complex'
        else:
            desc = '(cannot determine)' 
    print('  c has now become: {:s} with value: {:s}'. \
          format( desc, str(c) ) )

def doTuples():
    # tuples ... also a mix of definitions and initialisations
    (x1,x2,x3) = (-1.0,1.0,2.0) # a tuple
    w1,w2,w3  = ( 0.0,2.0,1.0) # 3 named float variables 
    t = (x1,x2,x3) # a tuple 
    # a tuple of tuples of floats ...
    s = ( (float('1.0'), float('0.0'), float('1.0')), 
             (float('-1.0'), float('-1.0')) )
    
    # EXPERIMENT: see the differences and similarities in tuples 
    #             with and without brackets ( ... )
    print('Tuples;')
    print('tuple (x1,x2,x3)     : {:s}'.format(str((x1,x2,x3))))
    print('tuple  x1,x2,x3      : ({:f},{:f},{:f})'.format(x1,x2,x3))
    print('tuple  w1,w2,w3      : {:s}'.format(str((w1,w2,w3))))
    print('tuple  w1,w2,w3      : ({:f},{:f},{:f})'.format(w1,w2,w3))
    print('tuple t=(x1,x2,x3)   : {:s}'.format(str(t)))
    print('t enhanced precision : ({:+8.5e},{:+8.5e},{:+8.5e})'. \
          format( t[0], t[1], t[2] ))
    # remember tuples are immutable ...
    p = 8.0
    # EXPERIMENT: try to do this ...
    # t[2] = p
    t = (t[0],t[1],p)
    print('t with modified x3=p : {:s}'.format(str(t)) )
    t = (t[0],t[1],x3)
    print('t with original x3   : {:s}'.format(str(t)) )
    # EXPERIMENT: with the indexing of this tuple ...
    # EXPERIMENT: try to change the value of the floats...
    print('composite tuple s    : {:s}'.format(str(s)) )
    # now swap signs of the floats ...
    for i in range(len(s)):
        # print('tuple: ', end='')
        for j in range(len(s[i])):  # observe: different lengths!
            # print('{:>4s}   '.format(str( s[i][j] )), end='')
            # s[i][j] = -1.0 * s[i][j]
            pass
        # print()
    sSwp=[[-s[i][j] for j in range(len(s[i]))] for i in range(len(s))]
    print('\'tuple\' s sign swap  : {:s}'.format(str(sSwp)) )
    
def doLists():
    # lists ... a mix of definitions and initialisations
    L1,L2 = [11,12,13,14], [21,22,23,24]
    L3,L4 = [31,32,33,34], [41,42,43,44]
    S3,S4 = ['these','items'], ['are','valid']
    M1,M2 = [L1, L2], [[31,32,33,34], [41,42,43,44]]
    M     = [M1,M2]
    MAT   = [L1,L2,L3,L4]
    MAT0  = [] # empty 0x0 matrix
    # EXPERIMENT: with the composition of matrices as lists-of-lists
    print('Lists (vectors and matrices);')
    print('L1       : {:s}'.format(str(L1)))
    print('L2       : {:s}'.format(str(L2)))
    print('S3+S4    : {:s} {:s}'.format(str(S3),str(S4)))
    print('Rows in M1;')
    for row in range(len(M1)):
        print('           {:s}'.format(str(M1[row])))
    print('Rows in M2;')
    for row in range(len(M2)):
        print('           {:s}'.format(str(M2[row])))
    print('Rows in M;')
    for row in range(len(M)):
        print('           {:s}'.format(str(M[row])))
    print('Rows in MAT;')
    for row in range(len(MAT)):
        print('           {:s}'.format(str(MAT[row])))
    # are lists mutable ? Recall that MAT is square ...
    for diagElem in range(len(MAT)):
        MAT[diagElem][diagElem] = 2*MAT[diagElem][diagElem]
    print('Modified MAT (mutable);')
    for row in range(len(MAT)):
        print('           {:s}'.format(str(MAT[row])))
    # EXPERIMENT: make a 0x0 matrix and inquire its dimensions
    N, M = len(MAT0),0
    if N>0: M=len(MAT0[0])
    print('MAT0 is a {:d}x{:d} matrix'.format(N,M))

def doRanges():
    print('For experiments with ranges, load and run files;')
    print('   loop-in-range.py   (simpel, start here)')
    print('   loop-in-range2.py  (focus on matrices and vectors)')
    print('   Feb29Since2000.py  (range, time, date)')
    # print all even numbers in range ...
    # EXPERIMENT: try to amend the range(1,100+1,2)
    # EXPERIMENT: use enumerate( range(0,100+1,2) ) and see what you get
    for val in range(0,100+1,2):
        print('{:s} '.format(str(val)), end='')
    print()

def doNumPyLinspaces():
    print('linspace;')
    print('...slice a 90 degree quadrant in 6 15 degrees segments...')
    segments = np.linspace( 0, 90, num=6, endpoint=False, dtype=int)
    for j,angle in enumerate(segments, start=1):
        print('segment {:2d} starts at angle: {:2g} degrees ({:6.4g} rad)'. \
              format(j,angle, (angle/180)*math.pi))
    print()
    print('... 0.1 step wide x-subdomain from 10.0 to 12.0 ...')
    dStart, dStop, deltaX =(10.0,12.0,0.1)
    xDomain = np.arange( dStart, dStop+deltaX, step=deltaX, dtype=float)
    for i,x in enumerate(xDomain):
        print('x[{:2d}] at position x={:5.2f}'.format(i,x))
    print()

def doStrings():
    print('Strings;')
    
    aString = \
        'This is the cannonical string' + \
        ' ' + \
        'everyone is so familiar with'
    
    # you would normally print this way ...
    print( aString )
    
    print( aString, '(length: {:d})'.format(len(aString)))

    # print a string array enumeration ...  
    for i in enumerate( aString ):
        print('{:s}'.format(str(i)), end='')
    print()
    
    # print a string character for character ...  
    for i in aString:
        print('{:s}'.format(i), end='')
    print()
    
    # print string character for character, backwards ...  
    for i in reversed(aString):
        print('{:s}'.format(i), end='')
    print()
    
    # print the sorted characters of the string ...
    for i in sorted(aString):
        print('{:s}'.format(i), end='')
    print()
    
    # print sorted characters of the string ...
    for i in sorted(aString, key=str.lower):
        print('{:s}'.format(i), end='')
    print()
    
    # split in words, and sort, ignore case ...
    print( sorted(aString.split(), key=str.lower) )

    # split in words, and sort, ignore case, backwards ...
    print( sorted(aString.split(), key=str.lower, reverse=True) )
    
    # count characters in the string ...
    for char in ['a','c','i','o','y']:
        count = 0; 
        for i in aString:
            if i == char:
                count += 1
        print('"', aString,'"', ' contains: ', count, char, '\'s')
        
    # print my encoded word ...
    print('my encoded word in the string is;')
    for l in [45, 46, 47, 48, 49, 34]:
        print(aString[l], end='')
    print()
    
    # print substrings ...
    print('substring "aString[12:22]", start=12, end=22:', aString[12:22])
    print(aString[:7], aString[30:38],end='!! ')
    print(aString[0:8], aString[41:53], sep='*', end=' :-)\n')
    print(aString[30:], aString[12:29], sep=' (well) ', end=' !!\n')
    
def printEpilogue(dtype):
    """
    print general NumPy implementation environment info...
    """
    print('About your Python and Numpy, for floats;')
    print(np.finfo(dtype))
    
def main():
    # EXPERIMENT: try group-bygroup to run the 
    #             experiments by uncommenting a
    #             function down here, one at a time
    # NOT elegant, but easy to (un)comment by hand
    #              or using CTRL+1 (Edit menu)
    print('main program started')    
#    doIntegers()      ; print()
#    doFloats()        ; print()
#    doNumPyFloats()   ; printEpilogue(np.float); print()
#    doComplexs()      ; print()
#    doNone()          ; print()
#    doTuples()        ; print()
#    doRanges()        ; print()
#    doLists()         ; print()
#    doNumPyLinspaces(); print()
#    doStrings()       ; print()
    print('main program done.')
    
# run main program ...
main()