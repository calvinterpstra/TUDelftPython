# -*- coding: utf-8 -*-
"""
SphereAsNGon.py   -- approach a sphere by using the limit of 
N->infty for an n-gon defined as conjugate pairs of roots of the 
the complex equation z^n -1 = 0, where: C_k+1 = 1.exp(k*2pi/N)
implemeneted here as a iteration k=1..N+1 giving C_1, C_2, 
C_3 ... each an angle 2pi/N apart. Note that:

          complex          ==      real
  -----------------------------------------------
  real(R*exp((k-1)*dphi*%i)) == R*cos((k-1)*dphi)
  imag(R*exp((k-1)*dphi*%i)) == R*sin((k-1)*dphi)

Reference
---------
Needham, T. Visual Complex Analysis, pp. 26

@author: Bart Gerritsen
"""

import math
import matplotlib.pyplot as plt


# Constant definition --------------------------------------------------
# midpoint; if to change, also change the xlim and ylim plot
C = [0,0]   
# unit circle
R = 1.0;
# use this for a high precision circle ...
P=360
# use cases: N=4 .. N=P=360 (equiv of segment 90 .. 1 degree)
N=12
# ... angle increments per segment ...
dPHI = 2*math.pi/N
dPSI = 2*math.pi/P
# want values printed ?
DOPRINT = True
# ----------------------------------------------------------------------

# arrays to hold N-gon approximation data ...
X = [ float(0.0) for k in range(N+1) ]
Y = [ float(0.0) for k in range(N+1) ]
# and array to hols an accurate high precision 
# reference circle ...
SX= [ float(0.0) for s in range(P+1) ]
SY= [ float(0.0) for s in range(P+1) ]

# n-gon data first ...
for k in range(N+1):
    if k == N:
        X[k] = X[0]
        Y[k] = Y[0]
    else:
        X[k] = C[0] + R*math.cos(k*dPHI)
        Y[k] = C[1] + R*math.sin(k*dPHI)
    if DOPRINT: print('z=(x,y)=({:+5.3f},{:+5.3f})'.format(X[k],Y[k]) )

# ... then the reference circle ...
for s in range(P+1):
    if s == P:
        SX[s] = SX[0]
        SY[s] = SY[0]
    else:
        SX[s] = C[0] + R*math.cos(s*dPSI)
        SY[s] = C[1] + R*math.sin(s*dPSI)

# and plot figure ...
# ... size ...
plt.figure(figsize=(6,4))

# subplot(nrows, ncols, plot_number)

# ... prepare the plot label
plt.xlim(-1.5,1.5)
plt.ylim(-1.5,1.5)
plt.axis('equal')
# ... plot graph with data points ...
plt.plot(X, Y, 'b-', SX, SY, 'r--')
# ... turn on grid ...
plt.grid(axis='both',which='major')
# ... decorate graph and axes ...
myTitle = 'Circle as a {:s}-gon'.format(str(N))
plt.title(myTitle)
myPDFFileName='CircleNGon{:s}.pdf'.format(str(N))
plt.savefig(myPDFFileName)
# ... show the plt prepared ...
plt.show()