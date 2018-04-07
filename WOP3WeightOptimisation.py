"""
Created:    Wed Feb 28 2018
Author:    Calvin Terpstra (Python 3.5.2)
"""

import matplotlib.pyplot as plt
import numpy as np

QUALITY = 1000
M_CONTAINER = 2.5 
M_HANDLER = np.linspace(4,6, QUALITY)
D_CONTAINER = 0.850 # 0.850
D_CONTAINER_1 = 0.370
D_CONTAINER_2 = 0.490
D_CONTAINER_3 = 0.610
D_CONTAINER_4 = 0.730
D_COUNTERWEIGHT = 0.480 # 0.480
D_CM = 0.130 # 0.130
M_COUNTERWEIGHT_CAR = 1

def solveMCounterweight(mContainer, mHandeler, dContainer, dCounterweight, dCM):
    return (mContainer*dContainer - mHandeler*dCM) / dCounterweight

def solveMaxPickupDist(mContainer, mHandeler, mCounterweightCar, dCounterweightCar, dCM):
    return (mHandeler*dCM + mCounterweightCar*dCounterweightCar) / mContainer

def main():
    mCounterweight = solveMCounterweight(M_CONTAINER, M_HANDLER, D_CONTAINER, D_COUNTERWEIGHT, D_CM)
    mCounterweightCar = solveMCounterweight(M_CONTAINER, M_HANDLER, D_CONTAINER_1, D_COUNTERWEIGHT, D_CM)
    mCounterweight2 = solveMCounterweight(M_CONTAINER, M_HANDLER, D_CONTAINER_2, D_COUNTERWEIGHT, D_CM)
    mCounterweight3 = solveMCounterweight(M_CONTAINER, M_HANDLER, D_CONTAINER_3, D_COUNTERWEIGHT, D_CM)
    mCounterweight4 = solveMCounterweight(M_CONTAINER, M_HANDLER, D_CONTAINER_4, D_COUNTERWEIGHT, D_CM)
    maxPickupDist = solveMaxPickupDist(M_CONTAINER, M_HANDLER, M_COUNTERWEIGHT_CAR, D_COUNTERWEIGHT, D_CM)
    mTotal = M_CONTAINER + M_HANDLER + mCounterweight
    print("Counterweight car:", mCounterweightCar[0],"-", mCounterweightCar[QUALITY-1], "kg")
    print("Counterweight 2:", mCounterweight2[0],"-", mCounterweight2[QUALITY-1], "kg")
    print("Counterweight 3:", mCounterweight3[0],"-", mCounterweight3[QUALITY-1], "kg")
    print("Counterweight 4:", mCounterweight4[0],"-", mCounterweight4[QUALITY-1], "kg")
    print("Counterweight:", mCounterweight[0],"-", mCounterweight[QUALITY-1], "kg")
    print("Max pickup dist without conunterweight:", maxPickupDist[0],"-", maxPickupDist[QUALITY-1], "m")
    print("Total:", mTotal[0],"-", mTotal[QUALITY-1], "kg")
    print("Slope:", (mTotal[QUALITY-1]-mTotal[0]) / (M_HANDLER[QUALITY-1]-M_HANDLER[0]))

    plt.plot(M_HANDLER, mTotal)
    # plt.show()

main()

