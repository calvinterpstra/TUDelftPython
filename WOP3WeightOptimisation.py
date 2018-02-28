"""
Created:    Wed Feb 28 2018
Author:    Calvin Terpstra (Python 3.5.2)
"""

import matplotlib.pyplot as plt
import numpy as np

QUALITY = 1000
M_CONTAINER = 2.5
M_HANDLER = np.linspace(3,7, QUALITY)
D_CONTAINER = 0.850
D_COUNTERWEIGHT = 0.480
D_CM = 0.130

def solveMCounterweight(mContainer, mHandeler, dContainer, dCounterweight, dCM):
    return (mContainer*dContainer - mHandeler*dCM) / dCounterweight

def main():
    mCounterweight = solveMCounterweight(M_CONTAINER, M_HANDLER, D_CONTAINER, D_COUNTERWEIGHT, D_CM)
    mTotal = M_CONTAINER + M_HANDLER + mCounterweight
    print("Counterweight:", mCounterweight[0],"-", mCounterweight[QUALITY-1], "kg")
    print("Total:", mTotal[0],"-", mTotal[QUALITY-1], "kg")
    print("Slope:", (mTotal[QUALITY-1]-mTotal[0]) / (M_HANDLER[QUALITY-1]-M_HANDLER[0]))

    plt.plot(M_HANDLER, mTotal)
    # plt.show()

main()

