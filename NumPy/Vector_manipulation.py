# Vector manipulation program with numpy
import numpy as np

# taking input for 2, 2D vectors
# we cant creat empty np array so we creat lists and then we cast them to np.array
vec1 = []
vec2 = []
for i in range (2):
    for j in range (2):
        if i == 0 : 
            vec1.append(int(input(f"give me vector {i+1} index {j+1} \t")))
        if i == 1:
            vec2.append(int(input(f"give me vector {i+1} index {j+1} \t")))

# casting to np.array

vec1 = np.array(vec1)
vec2 = np.array(vec2)

#summation 
sum = np.add(vec1,vec2)

#substraction
sub = np.subtract(vec1,vec2)

#result
print(sum)
print(sub)