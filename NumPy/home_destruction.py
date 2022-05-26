#there is a neighborhood that we want to destroy the houses saticfying this conditions
#x<5 or x>16
#imports 
import numpy as np

#define
x = np.arange(1,21)

#befor
print(np.reshape(x, newshape=(5,4)))

#check for x<5 or x>16 and replace to 1 or 0 

for i in range(len(x)):
    if (x[i]<6 or x[i]>16) :
        x[i]=0
    else:
        x[i]=1


#after
x = np.reshape(x,newshape=(5,4))

print(x)
