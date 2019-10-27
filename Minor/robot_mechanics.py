# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

# r1 = 191
# m1 = 4100
# r2 = 191
# m2 = 100
# r3 = 191
# m3 = 3900
# r4 = 19.1
# m4 = 10200
# r5 = 19.1
# m5 = 10000

nominal_torque = 405 
no_load_r = 5950 
r_m_gradient = 0.668 
operating_range_r = [0, 6000, 12000]
operating_range_m = [nominal_torque, nominal_torque*0.95, nominal_torque*0.87]
electrical_limit_r = [no_load_r, (no_load_r - nominal_torque*r_m_gradient)]
electrical_limit_m = [0, nominal_torque]

gear_limit_m = 10200/(nominal_torque*0.98)
gear_limit_r = (no_load_r - (nominal_torque*(4100/10200))*r_m_gradient)/191
for i in range(100):
    gear_limit_r = (no_load_r - (4100/gear_limit_r)*r_m_gradient)/191

gearing = gear_limit_m
r1 = 191 * gearing
m1 = 4100 / gearing
r2 = 191 * gearing
m2 = 100 / gearing
r3 = 191 * gearing
m3 = 3900 / gearing
r4 = 19.1 * gearing
m4 = 10200 / gearing
r5 = 19.1 * gearing
m5 = 10000 / gearing


# plt.plot(r1, m1, 'o', label='1')
# plt.plot(r2, m2, 'o', label='2')
# plt.plot(r3, m3, 'o', label='3')
# plt.plot(r4, m4, 'o', label='4')
# plt.plot(r5, m5, 'o', label='5')
plt.plot(m1, r1, 'o', label='1')
plt.plot(m2, r2, 'o', label='2')
plt.plot(m3, r3, 'o', label='3')
plt.plot(m4, r4, 'o', label='4')
plt.plot(m5, r5, 'o', label='5')
plt.plot(electrical_limit_m, electrical_limit_r, 'b--', label='Electrical limit')
plt.plot(operating_range_m, operating_range_r, 'r--', label='Continuous operating range limit')

plt.xlabel('M (mNm)')
plt.ylabel('$\omega$ (rpm)')

plt.title("Torque vs rotational velocity with gearing 100:1")

plt.legend()

print("r limit:", gear_limit_r)
print("m limit:", gear_limit_m)

plt.show()