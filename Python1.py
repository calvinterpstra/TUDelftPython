"""
Created:    Mon Feb 12 2018
Author:    Calvin Terpstra (Python 3.5.2)
Assignment: Python1
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
'''
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
'''

# Q7
m = 1000
g = 9.81
f1 = 2000
f2 = 1000
t1 = 30
t2 = 18
alpha = 10 * (2*np.pi / 360)
print(np.sin(alpha))

f = np.sin(alpha)*m*g
ax1 = (f1-f)/(m)
v1 = ax1*t1
x1 = 0.5*ax1*t1**2
ax2 = (f2-f)/(m)
v2 = ax2*t2 + v1
x2 = 0.5*ax2*t2*t2 + v1*t2 + x1
x2max = -(v1**2) / (2*ax2) + x1
xtot= 2*x2max-x2
xend= x2

print("xtot = ", xtot)
print("xend = ", xend)
print("ax1 = ", ax1)
print("ax2 = ", ax2)
print("x1 = ", x1)
print("x2 = ", x2)
print("v1 = ", v1)
print("v2 = ", v2)
print("x2max = ", x2max)
print("f = ", f)
print("")

# Q8
# m = 1000
# g = 9.81
# f1 = 2000
# f2 = 1000
dt = 0.0001
t1 = np.linspace(0,30,round(30/dt+1))
t2 = np.linspace(0,18,round(18/dt+1))
ax1 = (f1-f)/(m)
ax2 = (f2-f)/(m)
x1=np.zeros([len(t1)])
vx1=np.zeros([len(t1)])
x2=np.zeros([len(t2)])
vx2=np.zeros([len(t2)])
x1[0]=0
vx1[0]=0

for i in range(len(t1)-1):
    x1[i+1]=x1[i]+vx1[i]*dt
    vx1[i+1]=vx1[i]+ax1*dt

x2[0]=x1[len(t1)-1]
vx2[0]=vx1[len(t1)-1]

for i in range(len(t2)-1):
    x2[i+1]=x2[i]+vx2[i]*dt
    vx2[i+1]=vx2[i]+ax2*dt

Trest = t2[np.argmax(x2)]
Xreverse = x2[np.argmax(x2)]-x2[len(t2)-1]
Xend = x2[len(t2)-1]

print("Trest = ", 30+Trest)
print("Xreverse = ", Xreverse)
print("Xend = ", Xend)
print("dEnd = ", Xend-xend)

plt.plot(t1,x1)
plt.plot(t2,x2)