# a programm to calculate the multiplication summation and substraction of two 2*2 matrix without numpy
# without numpy


#taking matrixes from user 
a=[[],
   []]

b=[[],
   []]

c=[[0,0],
   [0,0]]

# taking matrix a
for i in range (2):
   for j in range(2):
      a[i].append(int(input(f"please give me index({i+1},{j+1}) of matrix A\t")))

print("\n\n")

#taking matrix b
for i in range (2):
   for j in range(2):
      b[i].append(int(input(f"please five me index({i+1},{j+1}) of matrix B\t")))



# calculation algorithms 


# multipulication  algorithm 
for i in range(2):
   for j in range(2):
      for k in range(2):
            c[i][j] += a[i][k] * b[k][j]
print (f"A . B is: {c}\n\n")

# summation algorithm
for i in range(2):
   for j in range(2):
      c[i][j] = a[i][j] + b[i][j]
print (f"A + B is: {c}\n\n")

# substraction algorithm 
for i in range(2):
   for j in range(2):
      c[i][j] = a[i][j] - b[i][j]
print (f"A - B is: {c}\n\n")


print("new)")
print(a+b)