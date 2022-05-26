# a program to calculate the mean of three numbers 
# 
# 
# taking inputs
x1 = int(input("please give me your first number \n"))
x2 = int(input("please give me your second number \n"))
x3 = int(input("please give me your third number \n"))

#showing the user their numbers
indexes = list((x1 , x2 , x3))
print (f"your numbers are {indexes[0]} and {indexes[1]} and {indexes[2]}")

#calculations
sumation = indexes[0] + indexes[1] + indexes[2]
mean = sumation/3

# output
print(mean)
