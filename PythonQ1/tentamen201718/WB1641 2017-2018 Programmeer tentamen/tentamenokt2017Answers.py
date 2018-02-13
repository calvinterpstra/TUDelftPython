import numpy as np
import matplotlib.pyplot as plt

# Stap 1
# definieer parameters, eenheden [m], graden
# parameters kamer
H = 3
B = 3.5
# parameters bed
Hb = 0.6
Wb = 1
xb = 2
# parameters steun
La = 1.5
Lc = 0.9
Lv = 0.6
Lp = 0.2
Dp = 0.45
beta = 40

# Stap 2
plt.figure(1)
# Plot de werkomgeving
Sx = np.array([0,B,B,0,0])
Sy = np.array([0,0,H,H,0])
Ax = np.array([xb,xb+Wb,xb+Wb,xb,xb])
Ay = np.array([0,0,Hb,Hb,0])
plt.plot(Sx,Sy,"g--",Ax,Ay,"k--")
plt.axis("scaled")
l = 0.2
plt.axis([-l,B+l,-l,H+l])   # can be left out
plt.show()

# Stap 3
# Afgeleide parameters
betar = beta*np.pi/180     # naar radialen (evt. np.radians)
Wc = Lc*np.sin(betar)
Hc = Lc*np.cos(betar)
Ap = 2*Wc-Lv

# Stap 4
plt.figure(2)
# frame van de tillift en draagkabel in een vaste positie
Rx1 = np.array([xb-Lv,xb-Lv,xb-Lv+Wc,xb-Lv+2*Wc])
Ry1 = np.array([0,La,La+Hc,La])
Rx2 = np.array([Rx1[-1],Rx1[-1]])
Ry2 = np.array([Ry1[-1],Ry1[-1]-Lp])
plt.plot(Rx1,Ry1,'o-',Rx2,Ry2,'o-')   # or two plot commands
plt.show()

# Stap 5 
plt.figure(3)
# Plot cirkels, weergeven van massa's
gam = np.arange(0,361,4)   # gam = np.linspace(0,360,91)
gamr = (gam/180)*np.pi
Dx = Dp/2*np.cos(gamr)
Dy = Dp/2*np.sin(gamr)
Dxp = Rx2[-1]+Dx
Dyp = Ry2[-1]-Dp/2+Dy
plt.plot(Dx,Dy,Dxp,Dyp)
plt.axis("scaled")   # plt.axis("equal"), however suboptimal
plt.show()

# Stap 6
plt.figure(4) 
# Plot de slaapkamer met bed, het frame van de tillift en 
# de draagkabel met massa Mp
plt.plot(Sx,Sy,"g--",Ax,Ay,"k--")
plt.axis("scaled")
plt.axis([-l,B+l,-l,H+l])   # can be left out

plt.plot(Rx1,Ry1,'o-b',Rx2,Ry2,'o-r')  # or two plot commands
plt.plot(Dxp,Dyp,'r')
plt.show()
 
# Stap 7
plt.figure(5)
# Plot het frame van de tillift met draagkabel in n posities in
# slaapkamer met bed, gaat uit van de basiscode uit Stap 4 en Stap 6  
n = 5  
beta = np.linspace(25,45,n)     # hoeken in graden
Rx1 = np.zeros((n,4))           # initialisation/declaration
Ry1 = np.zeros((n,4))
Rx2 = np.zeros((n,2))
Ry2 = np.zeros((n,2))
for k in range(n):
    betar = beta[k]*np.pi/180
    Wc = Lc*np.sin(betar)
    Hc = Lc*np.cos(betar)
    Ap = 2*Wc-Lv
    Rx1[k,:] = np.array([xb-Lv,xb-Lv,xb-Lv+Wc,xb-Lv+2*Wc])
    Ry1[k,:] = np.array([0,La,La+Hc,La])
    Rx2[k,:] = np.array([Rx1[k,-1],Rx1[k,-1]])
    Ry2[k,:] = np.array([Ry1[k,-1],Ry1[k,-1]-Lp])

plt.plot(Sx,Sy,"g--",Ax,Ay,"k--")
plt.axis("scaled")
plt.axis([-l,B+l,-l,H+l])   # can be left out
for k in range(n):
    plt.plot(Rx1[k,:],Ry1[k,:],"b-o",Rx2[k,:],Ry2[k,:],"r-o")
plt.show()

# Stap 8
plt.figure(6)
Mp = 80  # massa patient, [kg]
# parameters contragewicht
Hm = 1
Lm = 0.65
Dm = 0.3
Mm = 50

Dx = Dm/2*np.cos(gamr)   # cirkel met middellijn Dm
Dy = Dm/2*np.sin(gamr)

Rx3 = np.zeros((n,2))           # initialisation/declaration
Ry3 = np.zeros((n,2))
Dxm = np.zeros((n,len(Dx)))
Dym = np.zeros((n,len(Dy)))
for k in range(n):
    betar = beta[k]*np.pi/180
    # afgeleide hoekafhankelijke parameters
    Wc = Lc*np.sin(betar)
    Ap = 2*Wc-Lv
    Am = Ap*Mp/Mm
    dxm = Am-Lv
    dym = np.sqrt(Lm**2-dxm**2)
    #  posities contragewicht
    Rx3[k,:] = np.array([xb-Lv,xb-Lv-dxm])
    Ry3[k,:] = np.array([Hm,Hm+dym])
    Dxm[k,:] = Rx3[k,-1]+Dx
    Dym[k,:] = Ry3[k,-1]+Dy

plt.plot(Sx,Sy,"g--",Ax,Ay,"k--")
plt.axis("scaled")
plt.axis([-l,B+l,-l,H+l])   # can be left out
for k in range(n):
    plt.plot(Rx1[k,:],Ry1[k,:],"b-o",Rx2[k,:],Ry2[k,:],"r-o",
             Rx3[k,:],Ry3[k,:],"g-o",Dxm[k,:],Dym[k,:],"g-")

plt.show()