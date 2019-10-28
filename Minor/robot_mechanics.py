# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

# RE 50 24V
nominal_torque = 405 
no_load_r = 5950 
r_m_gradient = 0.668 
operating_range_r = [0, 6000, 12000]
operating_range_m = [nominal_torque, nominal_torque*0.93, nominal_torque*0.80]
electrical_limit_r = [no_load_r, (no_load_r - nominal_torque*r_m_gradient)]
electrical_limit_m = [0, nominal_torque]

# Calculate gearing limits
gear_limit_m = 10200/(nominal_torque*0.985)
gear_limit_r = (no_load_r - (nominal_torque*(4100/10200))*r_m_gradient)/(20*30/np.pi) #/191
for i in range(100):
    gear_limit_r = (no_load_r - (4100/gear_limit_r)*r_m_gradient)/191

gearing = gear_limit_r # using the electrical limit threshold as the gearing limit
# Calculate torques and rotational velocities for each scenario
r1 = (20*30/np.pi) * gearing
m1 = 4100 / gearing
r2 = (20*30/np.pi) * gearing
m2 = 100 / gearing
r3 = (20*30/np.pi) * gearing
m3 = 3900 / gearing
r4 = (2*30/np.pi) * gearing
m4 = 10200 / gearing
r5 = (2*30/np.pi) * gearing
m5 = 10000 / gearing

# Plotting
plt.plot(m1, r1, 'o', label='1')
plt.plot(m2, r2, 'o', label='2')
plt.plot(m3, r3, 'o', label='3')
plt.plot(m4, r4, 'o', label='4')
plt.plot(m5, r5, 'o', label='5')
plt.plot(electrical_limit_m, electrical_limit_r, 'b--', label='Electrical limit')
plt.plot(operating_range_m, operating_range_r, 'r--', label='Continuous operating range limit')

plt.xlabel('M (mNm)')
plt.ylabel('$\omega$ (rpm)')

plt.title("Torque vs rotational velocity with gearing {:.1f}:1".format(gearing))

plt.legend()

# Print gearing limits
print("r limit: {:.1f}:1".format(gear_limit_r))
print("m limit: {:.1f}:1".format(gear_limit_m))

plt.show()

# Calculations for Q6
I = 5.36*10**(-5)
M_m = I*(20*gearing)/0.5
M_r = 4.1/gearing

print("omega: {:.3f} rad/s".format(20*gearing))
print("alpha: {:.3f} rad/s^2".format(40*gearing))
print("M_m: {:.1f} mNm".format(M_m*1000))
print("M_r: {:.1f} mNm".format(M_r*1000))
print("ratio: {:.3f}".format(M_m/M_r))
