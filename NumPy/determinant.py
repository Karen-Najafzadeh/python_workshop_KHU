# a program to calculate the Determinant of a 2*2 and 3*3 matrix
import numpy as np 


#asking user which kind of matrix they have? 2*2 or 3*3
dimention = int (input("if your matrix is 2*2 enter \"2\" and if it's 3*3 enter \"3\" \n"))
# taking matrix
# yo can also import this as a function from matrix_manipulation_numpy.py
# setting the matrix "a" dimention
# a is a list we use as our matrix
if dimention == 3:
    a=[[],[],[]]
else:
    a=[[],[]]

for i in range (dimention):
    for j in range(dimention):
        a[i].append(int(input(f"please give me index({i+1},{j+1}) of matrix A\t")))

#casting list to np array
a = np.array(a)

#algorithm

#I don't know :)
# probably ther is a general mathematical solution for this but currantly i dont have access to internet to find it out
#so we're just gonna leave the shit here for later.
#save and quit.
print(a)

