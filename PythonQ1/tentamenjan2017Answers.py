import numpy as np
import matplotlib.pyplot as plt

# Stap 1
# definieer parameters 
A1 = 14 # [m]
A2 = 12 # [m]

H1 = 0.5*A1
H2 = 0.5*A2

L1 = 5 # [m]
L2 = 3 # [m]

L3 = 0.2*L1

alfa = 20  # [graden]
beta = 90  # [graden]
gamma = 60 # [graden]

n = 6

# Stap 2
plt.figure(1)
# Plot de werkomgeving
Ax = np.array([0,A2,A2,0,0])
Ay = np.array([0,0,A1,A1,0])
plt.plot(Ax,Ay,"g--",linewidth = 2)
plt.axis("scaled")
plt.xlabel("Afstand X-richting [m]")
plt.ylabel("Afstand Y-richting [m]")
plt.title("De 'pick and place' robotarm")
l = 1.5
plt.axis([-l,A2+l,-l,A1+l])


# Stap 3
plt.figure(2)
# Plot de robotarm in een vaste positie

alfar = (alfa/180)*np.pi     # conversie naar radialen
betar = (beta/180)*np.pi     # kan ook met np.radians
gammar = (gamma/180)*np.pi
Rx1 = H2+np.array([0,L1*np.cos(alfar)])       # segment 1
Ry1 = H1+np.array([0,L1*np.sin(alfar)])
Rx2 = Rx1[1]+np.array([0, L2*np.cos(betar)])   # segment 2
# Rx2 = Rx1[-1]+np.array([0, L2*np.cos(beta_r)])
Ry2 = Ry1[1]+np.array([0, L2*np.sin(betar)])
#grijper
Rx3 = Rx2[1]+np.array([-L3*np.cos(gammar),L3*np.cos(gammar)])   # basis
Ry3 = Ry2[1]+np.array([-L3*np.sin(gammar),L3*np.sin(gammar)])
Rx4 = Rx3[0]+np.array([0,0])    # vinger    
# Rx4 = np.array([Rx3[0],Rx3[0]]
Ry4 = Ry3[0]+np.array([0,-L3])
Rx5 = Rx3[1]+np.array([0,0])    # vinger 
Ry5 = Ry3[1]+np.array([0,-L3])

plt.plot(Rx1,Ry1,'ko-',Rx2,Ry2,'ko-',Rx3,Ry3,'k-',linewidth=2)
plt.plot(Rx4,Ry4,'k:',Rx5,Ry5,'k:',linewidth=2)

plt.show()


# Stap 4 
plt.figure(3)
# Plot cirkels, weergeven van het bewegingsbereik
gamma3 = np.arange(0,361,4)   # gamma3 = np.linspace(0,360,91)
gamma3r = (gamma3/180)*np.pi
Dx = L3*np.cos(gamma3r)
Dy = L3*np.sin(gamma3r)
plt.plot(Dx,Dy,"k",linewidth = 2)
Mx3 = Rx2[1]+Dx
My3 = Ry2[1]+Dy
plt.plot(Mx3,My3,"k",linewidth = 2)
plt.axis("scaled")   # plt.axis("equal"), however suboptimal

plt.show()

# Stap 5
plt.figure(4) 
# Plot de werkomgeving met de robotarm in vaste positie en met
# een cirkel om het bewegingsbereik van de grijper aan te geven
plt.plot(Ax,Ay,"g--",linewidth = 2)
plt.axis("scaled")
l = 1.5
plt.axis([-l,A2+l,-l,A1+l])

plt.plot(Rx1,Ry1,'ko-',Rx2,Ry2,'ko-',Rx3,Ry3,'k-',linewidth=2)
plt.plot(Mx3,My3,'r:',linewidth = 2)

plt.show()
 
# Stap 6
# Plot de robotarm in n posities in de werkomgeving

plt.figure(5)
# werkomgeving, code uit Stap 2
plt.plot(Ax,Ay,"g--",linewidth = 2)
plt.axis("scaled")
l = 1.5
plt.axis([-l,A2+l,-l,A1+l])
plt.xlabel("Afstand X-richting [m]")
plt.ylabel("Afstand Y-richting [m]")
plt.title("De 'pick and place' robotarm")

# n posities, gaat uit van de basiscode uit Stap 3 
alfa2 = np.linspace(20,320,n)    # hoeken in graden
beta2 = np.linspace(90,430,n)
gamma2 = np.linspace(60,310,n)
RRx1 = np.zeros((n,2))           # initialisation/declaration
RRy1 = np.zeros((n,2))
RRx2 = np.zeros((n,2))
RRy2 = np.zeros((n,2))
RRx3 = np.zeros((n,2))
RRy3 = np.zeros((n,2))
for k in range(n):
    alfa2r = (alfa2[k]/180)*np.pi
    beta2r = (beta2[k]/180)*np.pi
    gamma2r = (gamma2[k]/180)*np.pi
    RRx1[k,:] = H2+np.array([0,L1*np.cos(alfa2r)])
#    RRx1[k,:] = [H2+0,H2+L1*np.cos(alfa2r)] # possible as well
    RRy1[k,:] = H1+np.array([0,L1*np.sin(alfa2r)])
    RRx2[k,:] = RRx1[k,1]+np.array([0, L2*np.cos(beta2r)])
    RRy2[k,:] = RRy1[k,1]+np.array([0, L2*np.sin(beta2r)])
    RRx3[k,:] = RRx2[k,1]+np.array([-L3*np.cos(gamma2r),L3*np.cos(gamma2r)])
    RRy3[k,:] = RRy2[k,1]+np.array([-L3*np.sin(gamma2r),L3*np.sin(gamma2r)])

for k in range(n):
    plt.plot(RRx1[k,:],RRy1[k,:],"k-o",RRx2[k,:],RRy2[k,:],"k-o",
             RRx3[k,:],RRy3[k,:],"k-",linewidth = 2)  

# Stap 7
# Plot voor iedere positie van de robotarm een cirkel die het
# bewegingsbereik van de grijper weergeeft
# Gaat uit van de basiscode uit Stap 5 (en Stap 4)
MMx3 = np.zeros((n,91))
# m = Dx.size, MMx3 = np.zeros((n,m))
MMy3 = np.zeros((n,91))
for i in range(n):
    MMx3[i,:] = RRx2[i,1]+Dx
    MMy3[i,:] = RRy2[i,1]+Dy
for i in range(n):
    plt.plot(MMx3[i,:],MMy3[i,:],"r:",linewidth = 2)

#plt.show()      

# Stap 8
# Done by trial and error with visual check by changing L2 at
# line 13 several times observing the figure(5) resulting
#plt.text(0.5,0.5,'L2 = 1.7 [m]')

plt.show()