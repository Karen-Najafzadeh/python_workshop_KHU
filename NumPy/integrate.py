# a program to calculate the answer of an integrate (gives a number)


#input and defining
#from matplotlib import pyplot as plt
import numpy as np


a = float(input("where is the begining of the range? \n"))
b = float(input("where is the end of range? \n"))
n = int(input("how many regions do you want to devide the function into?\n"))
x = a
area = 0
dx = (b-a)/n

#for ploting
x_axis=[]
function_value=[]

#integrating
#we are trying to make a list of floats with very small steps dx
for i in range (n):
    #finding Midpoint Riemann Sum
    x += dx
    x_axis.append(x)
    # area = ∫ 𝑓(𝑥)𝑑𝑥
    F = 4*np.sin(np.pi*x)*np.cos(np.pi*3*x)
    function_value.append(F)
    area += (F)*(dx)
print(area)

# ploting the original f(x)
#plt.plot(x_axis,function_value)
#plt.xlabel("pi")
#plt.title("F(x)")
#plt.show()

# program finished