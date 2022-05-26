# a program to calculate sum of 0 to N and the factorial of N!

#getting input
N = int(input("please give me a number\n"))


#Gaussian method
#sum = (N*(N+1)/2)
#print (int (sum))

#for loop method
sum = 0
for i in range(N+1): # because range counts to N-1
    sum += i
print(f"the sum of numbers [0,{N}]is {sum}")

#calculating factorial 
multipul=1
for i in range (N,0,-1):
    multipul *= i
print("the factorial of ",N,"is ",multipul)