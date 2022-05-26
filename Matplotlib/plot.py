# a program to draw a simple plot
# importing essentials 
import matplotlib.pyplot as plt
import numpy as np

#setting data
x = np.array([0,1,2,3,4,5])
y = np.array([0,3,6,9,12,15])


#showing the result
plt.plot(x,y)
#reverse
#plt.plot(y,x)
plt.show()