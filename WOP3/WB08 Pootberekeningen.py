import numpy as np
import matplotlib.pyplot as plt


m = 2.5 #Massa van de last, in dit geval de arm + rails + container
Fa = 2.5 * 9.81 #De zwaartekracht van de last
a = 150 / 1000 # De momentarm tussen de last en de poot
M = Fa * a #Moment dat ontstaat op de poot door de last
L = 0.480 #Totale hoogte van de poot
Ealu = 73.1E9 #Young's modulus aluminium
Est = 210E9 #Young's modulus steel
rhoalu = 2.79E3 #Dichtheid aluminium
rhost = 7.8E3 #Dichtheid steel


d = np.linspace(0.001,0.005,5) #Dikte van het materiaal
c = 0.06 #Lengte van de zijde van het profiel van de poot
h1 = np.cos(np.pi/4)*c #Buitenste hoogte van de poot-doorsnee
h2 = h1 - d #Binnenste hoogte van de poot-doorsnee

b1 = 2 * np.tan(np.pi/4)*h1 #Buitenste breedte van de poot-doorsnee
b2 = 2 * np.tan(np.pi/4)*h2 #Binnenste breedte van de poot-doorsnee

A1 = 0.5*b1*h1 #Buitenste doorsnee oppervlakte van de poot
A2 = 0.5*b2*h2 #Binnenste doorsnee oppervlakte van de poot
A = A1-A2 #Doorsnee oppervlakte van de poot

Ix1 = (1/36)*b1*(h1)**3 #Moment of inertia van de buitenste doorsnede driehoek
Ix2 = (1/36)*b2*(h2)**3 #Moment of inertia van de binnenste doorsnede driehoek

I = Ix1-Ix2 #Totale moment of inertia van de poot

deltaalu = (M*(L)**2)/(2*Ealu*I) #Berekening van de doorsnede van de poot, met het opgelegde moment M. Volgens vergeet-me-nietjes uit Mechanics of materials, Fourteenth Edition in SI Units, R.C. Hibbeler.
deltast = (M*(L)**2)/(2*Est*I)
V = A * L #Totale volume van de poot
mpalu = V * rhoalu #Totale massa van de poot aluminium
mpst=V*rhost #Totale massa van de poot aluminium

print(deltaalu)
print(deltast)
print(mpalu)
print(mpst)
plt.figure(1)
plt.plot(d,deltaalu)
