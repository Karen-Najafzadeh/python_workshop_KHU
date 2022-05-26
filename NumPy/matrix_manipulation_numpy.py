# a programm to calculate the multiplication summation and substraction of two 2*2 matrix with numpy library

import numpy as np 
#taking matrixes from user 
a=[[],
   []]
b=[[],
   []]
# taking matrix a
for i in range (2):
   for j in range(2):
      a[i].append(int(input(f"please give me index({i+1},{j+1}) of matrix A\t")))
print("\n")
#taking matrix b
for i in range (2):
   for j in range(2):
      b[i].append(int(input(f"please five me index({i+1},{j+1}) of matrix B\t")))


#casting lists to np array
a = np.array(a)
b = np.array(b)


#calculations:
#multipulication
mul = np.dot(a,b)
#summation 
sum = a+b
#substraction
sub = a-b
#results
print (f"A . B is:\n {mul}\n\n")
print (f"A + B is:\n {sum}\n\n")
print (f"A - B is:\n {sub}\n\n")

# note
# we can use + and - in this way but + and -  will not work without numpy