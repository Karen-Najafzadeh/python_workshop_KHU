#example for chapter 4 page 12
# making a list of 1s
my_list = []
for i in range(10):
    my_list.append(1)
print(my_list)

#break continue
sum = 0
for i in range(len(my_list)):
    sum += my_list[i]
    if (i==5):
        #break 
        continue
    print(sum)