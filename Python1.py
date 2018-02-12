"""
Created:    Mon Feb 12 2018
Author:    Martijn Wisse (Python 3.5.2)
Assignment: Python0
"""

## Resetting the console, to erase old parameter values
## Uncomment the following two lines if you use Spyder. 
#from IPython import get_ipython
#get_ipython().magic('reset -sf')

# Importing the useful Matlab libraries
import matplotlib.pyplot as plt
import numpy as np

# Q2
'''
x0 = 0.1
v0 = 1.5
m = 2

dt  = 0.05
t = np.linspace(0, 1, round(1/dt+1))
x = np.linspace(x0, x0, round(1/dt+1))
v = np.linspace(v0, v0, round(1/dt+1))
a = 0
for i in range(1,len(t)):
    x[i] = x[i-1]+v[i-1]*dt
    v[i] = v[i-1]+a*dt

print(t[10])
print(v[10])
    
plt.figure(num=1)
plt.plot(t,x)
plt.xlabel('t [s]')
plt.ylabel('x [m]')
plt.title('plot of function x(t)')
plt.show()
'''
# Q4
'''
y0 = 2
v0 = -0.2
a = -9.81
m = 1

dt  = 0.01
t = np.linspace(0, 1, round(1/dt+1))
y = np.linspace(y0, y0, round(1/dt+1))
v = np.linspace(v0, v0, round(1/dt+1))

for i in range(1,len(t)):
    y[i] = y[i-1]+v[i-1]*dt
    v[i] = v[i-1]+a*dt
    
print(t[80])
print(v[80])
    
plt.figure(num=1)
plt.plot(t,y)
plt.xlabel('t [s]')
plt.ylabel('y [m]')
plt.title('plot of function x(t)')
plt.show()
'''
# Q6

y0 = 0
x0 = 0
v_y0 = 2
v_x0 = 2
a_y = -9.81
a_x = 0
m = 1

dt  = 0.01
t = np.linspace(0, 1, round(1/dt+1))
y = np.linspace(y0, y0, round(1/dt+1))
x = np.linspace(x0, x0, round(1/dt+1))
v_y = np.linspace(v_y0, v_y0, round(1/dt+1))
v_x = np.linspace(v_y0, v_y0, round(1/dt+1))
t_top = 0
x_top = 0

for i in range(1,len(t)):
    y[i] = y[i-1]+v_y[i-1]*dt
    v_y[i] = v_y[i-1]+a_y*dt
    x[i] = x[i-1]+v_x[i-1]*dt
    v_x[i] = v_x[i-1]+a_x*dt
    if(np.abs(v_y[i]) < 0.1):
        print(v_y[i])
        t_top = t[i]
        x_top = x[i]
        print("max y:", y[i])
        print("")
print("max y:", np.max(y))
print(x_top)
print(t_top)

print(t[len(t)-1])
print(2.905+y[len(t)-1])
    
plt.figure(num=1)
plt.plot(t,y)
plt.xlabel('t [s]')
plt.ylabel('y [m]')
plt.title('plot of function x(t)')
plt.show()

