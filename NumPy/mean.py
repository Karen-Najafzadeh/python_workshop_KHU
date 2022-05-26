# a programm to calculate mean of a given array


import numpy as np

numbers = input(("how many numbers do you want to insert? \n"))

numbers = int(numbers)

print ("please give me your numbers\n")

x=np.array([])


for n in range(0,numbers):
	m =str(input ("give me number "))
	x = np.append(x,m)
	
	
print ("your array of numbers is :",x)

summation =0
for i in range (0,numbers):
	summation =int(x[i])+ summation 
	
mean = summation/numbers
print ("the mean of your array is : \t " , mean)