#Sum of Consecutive Numbers


#find the sum of the first N numbers.
#Take a number N as input and output the sum of all numbers from 1 to N (including N).
#Sample Input
#100
#Sample Output
#5050

#code :

N = int(input("which number are you going to sum up to?"))
#using gaussian sum method
sum = (N*(N+1)/2)
#print the result
print (int (sum))
