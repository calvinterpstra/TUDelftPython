# originates from Ingeborg Goddijn, adapted PW

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

exti1 = pd.read_excel("exti1.xlsx")
time = np.array(exti1["time"])
rainfall = np.array(exti1["rainfall"])
runoff = np.array(exti1["runoff"])

fig = plt.figure(1)
ax1 = fig.add_subplot(111)
ax1.yaxis.set_label_position("left")
ax1.set_ylim(0,300)
ax1.set_yticks([0,100,200,300])
ax1.grid()
plt.ylabel("runoff")
plt.plot(time,runoff,"o-")

ax2 = ax1.twinx()
ax2.yaxis.set_label_position("right")
ax2.set_ylim(0,20)
ax2.set_yticks([0.0,5.0,10.0,15.0,20.0])
ax2.invert_yaxis()
plt.ylabel("rainfall")
plt.bar(time,rainfall)
plt.show()
