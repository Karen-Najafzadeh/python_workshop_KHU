#a program to plot the movement of a missile
# the equation of motion for a thrown object under gravity is :
# y(x) = ((-g*(x**2))/(2(v**2)(cos(𝜃)**2)))+x*tan(𝜃)


#importing essentials
from matplotlib import pyplot as plt
import numpy as np

# taking inputs 
g = float(input("what is the Gravitational acceleration? (positive) (m/s^2)"))
v = float(input("what is the initial velocity? (m/s) \n"))
𝜃 = np.pi*float(input("what is the angel of throw? (pi radians) \n"))
Range = float(input("how far do you want to track the object? (m) \n"))

# range of plot 
x = np.arange(0,Range,0.1)

# motion of object
y = ((-g*x**2)/(2*(v**2)*np.cos(𝜃)**2))+x*np.tan(𝜃)

#plot

plt.plot(x,y)
plt.grid()
plt.show()


# 14/2/1401
# finished but wrong result
# 16/21401
# fixed the problem and finished :)