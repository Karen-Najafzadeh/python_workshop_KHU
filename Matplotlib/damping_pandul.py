# a program to predict the movement of a simple harmonic oscilation in plot
# the general solution for the vertical (y(t)) underdamped harmonic oscilator is"
# y(t) = A (e**(−Γt/2))*(cos(ωt − θ)
#refrens of the formula : THE PHYSICS OF WAVES, HOWARD GEORGI, Version date - February 15, 2015, page39, eq(2_10) 


#importing essentials
import numpy as np 
import matplotlib.pyplot as plt


#inpuying
Γ = float(input("what is your damping constant? \n"))
ω = float(input("what is system's angular frequency? \n"))
A = float(input("what is system's elastic amplitude? \n"))
time_range = float (input("what is the maximum range you want to show in plot (in π Radian)? \n"))

#time ranging
t = np.arange(0,time_range*np.pi,0.05)   # start,stop,step

# y  ranging (fourmula)
y = A*(np.e**(-Γ*t/2))*(np.cos(ω*t))

#ploting and result
plt.plot(t,y)
plt.title("damping movement")
plt.xlabel("time")
plt.ylabel("hieght")
plt.grid(axis='y')
plt.show()

# 15/2/1401
#program is completed