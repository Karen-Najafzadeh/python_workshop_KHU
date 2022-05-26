# a program to predict the position of a beam after pasing throgh a glass_air surface 
# postulates:
# glass  is placed under the laser and the wall is placed behind of the glass so y3 < y2 < y1 hence alpha1 < 0
#inputs and imports
import math as m
from matplotlib import pyplot as plt
x1 = float(input("what is the position of laser? (x1)\n"))
y1 = float(input("what is the position of laser? (y1)\n"))
y2 = float(input("where is the glass surface? (y2)\n"))
y3 = float(input("where is the position of the wall? (y3)\n"))
alpha1 =float(input("what is the angel of emmited beam? (degrees)\n")) 
n1 = float(input("what is the index (n1) of the first medium?\n"))
n2 = float(input("what is the index (n2) of the second medium?\n"))

x2 = ((y2-y1)/m.tan(m.pi*alpha1/180))+x1  # casting alpha 1 to radians so we can work with tan function
theta1 = 90-abs(alpha1)                   # finding the amount of theta 1 (abs)
theta1 = theta1*m.pi/180                  # casting theta 1 to radians so we can work with tan function
theta2 = m.asin((n1/n2)*m.sin(theta1))    # finding theta 2 in radians
if (y3 < y2 and y2 < y1 and alpha1<0):    # if the laser is upper than the glass and observer then the slope of its path should be negative
    x3 = -((y3-y2)*m.tan(theta2))+x2
else:                                     ## if the laser is lower than the glass and observer then the slope of its path should be positive
    x3 = ((y3-y2)*m.tan(theta2))+x2

print(f"theta 1 is {theta1*180/m.pi} and theta 2 is {180*theta2/m.pi}  ")

x_axis = []
y_axis = []

#prepering to plot
x_axis.append(x1)
x_axis.append(x2)
x_axis.append(x3)
y_axis.append(y1)
y_axis.append(y2)
y_axis.append(y3)

#plot
plt.plot(x_axis,y_axis,color="red")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("snell's law")

#laser position
plt.scatter(x1,y1,c="red",s=150)

#glass
x_glass = [m.floor(x1),m.ceil(x3)]
plt.plot(x_glass,[y2,y2])
#wall 
x_wall = [m.floor(x1),m.ceil(x3)]
plt.plot(x_glass,[y3,y3])

plt.legend(["beam","laser","glass","wall"])
plt.show()
plt.show()
