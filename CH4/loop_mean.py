# a program to calculate the mean of 5 numbers in a list

my_list=[2,5,4,7,8]
sum = 0
i=0
#while loop way
#while (i<len(my_list)):
#    sum += my_list[i]
#    i+=1

#for loop way
for i in range (len(my_list)):
    sum += my_list[i]

#result
mean = sum / len(my_list)
print (f"the mean of [2,5,4,7,8] is {mean}")